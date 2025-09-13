#!/usr/bin/env python3
"""
Word Length Organizer
A CLI tool to organize words from a file into separate files based on word length.
"""

import argparse
import sys
import os
import re
from collections import defaultdict

def clean_word(word, remove_punctuation=True):
    """
    Clean a word by removing punctuation and/or converting case.
    
    Args:
        word (str): The word to clean
        remove_punctuation (bool): Whether to remove punctuation
    
    Returns:
        str: Cleaned word
    """
    if remove_punctuation:
        # Remove all non-alphabetic characters
        word = re.sub(r'[^a-zA-Z]', '', word)
    
    return word

def organize_words_by_length(file_path, delimiter=' ', remove_punctuation=True, case_sensitive=False):
    """
    Read file and organize words by length.
    
    Args:
        file_path (str): Path to input file
        delimiter (str): Delimiter to split words by
        remove_punctuation (bool): Whether to remove punctuation from words
        case_sensitive (bool): Whether to preserve case
    
    Returns:
        dict: Dictionary with lengths as keys and lists of words as values
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied accessing '{file_path}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    # Split content by delimiter
    words = content.split(delimiter)
    
    # Organize words by length
    word_groups = defaultdict(list)
    
    for word in words:
        # Clean the word
        cleaned_word = clean_word(word.strip(), remove_punctuation)
        
        # Skip empty words
        if not cleaned_word:
            continue
        
        # Handle case sensitivity
        if not case_sensitive:
            cleaned_word = cleaned_word.lower()
        
        # Group by length
        length = len(cleaned_word)
        word_groups[length].append(cleaned_word)
    
    return dict(word_groups)

def create_output_files(word_groups, output_dir, base_name, keep_duplicates=False):
    """
    Create output files for each word length group.
    
    Args:
        word_groups (dict): Dictionary of word groups by length
        output_dir (str): Output directory
        base_name (str): Base name for output files
        keep_duplicates (bool): Whether to keep duplicate words
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    files_created = []
    
    for length, words in sorted(word_groups.items()):
        # Remove duplicates if requested
        if not keep_duplicates:
            words = list(dict.fromkeys(words))  # Preserves order while removing duplicates
        
        # Create filename
        filename = f"{base_name}_length_{length}.txt"
        filepath = os.path.join(output_dir, filename)
        
        # Write words to file
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                for word in words:
                    file.write(word + '\n')
            
            files_created.append((filepath, len(words), length))
            
        except Exception as e:
            print(f"Error creating file '{filepath}': {e}")
            continue
    
    return files_created

def print_summary(files_created, total_words):
    """Print a summary of the operation."""
    print(f"\nWord Length Organization Complete!")
    print("=" * 50)
    print(f"Total words processed: {total_words}")
    print(f"Files created: {len(files_created)}")
    print("-" * 50)
    
    for filepath, word_count, length in files_created:
        filename = os.path.basename(filepath)
        print(f"{filename:<25} | {word_count:>3} words ({length} letters each)")
    
    print("-" * 50)
    print("Files saved in:", os.path.dirname(files_created[0][0]) if files_created else "No files created")

def main():
    parser = argparse.ArgumentParser(
        description="Organize words from a file into separate files based on word length",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python word_organizer.py input.txt
  python word_organizer.py text.txt -d "|" -o results/
  python word_organizer.py file.txt --keep-punctuation --case-sensitive
  python word_organizer.py data.txt -d "," --keep-duplicates
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the input text file'
    )
    
    parser.add_argument(
        '-d', '--delimiter',
        default=' ',
        help='Delimiter to split words by (default: space)'
    )
    
    parser.add_argument(
        '-o', '--output-dir',
        default='word_length_output',
        help='Output directory for organized files (default: word_length_output)'
    )
    
    parser.add_argument(
        '--base-name',
        default='words',
        help='Base name for output files (default: words)'
    )
    
    parser.add_argument(
        '--keep-punctuation',
        action='store_true',
        help='Keep punctuation in words (default: remove punctuation)'
    )
    
    parser.add_argument(
        '--case-sensitive',
        action='store_true',
        help='Preserve case in words (default: convert to lowercase)'
    )
    
    parser.add_argument(
        '--keep-duplicates',
        action='store_true',
        help='Keep duplicate words in output files (default: remove duplicates)'
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: '{args.input_file}' is not a valid file.")
        sys.exit(1)
    
    print(f"Processing file: {args.input_file}")
    print(f"Using delimiter: '{args.delimiter}'")
    
    # Organize words by length
    word_groups = organize_words_by_length(
        args.input_file,
        delimiter=args.delimiter,
        remove_punctuation=not args.keep_punctuation,
        case_sensitive=args.case_sensitive
    )
    
    if not word_groups:
        print("No words found in the file.")
        sys.exit(0)
    
    # Calculate total words
    total_words = sum(len(words) for words in word_groups.values())
    
    # Create output files
    files_created = create_output_files(
        word_groups,
        args.output_dir,
        args.base_name,
        args.keep_duplicates
    )
    
    # Print summary
    if files_created:
        print_summary(files_created, total_words)
    else:
        print("No output files were created.")

if __name__ == "__main__":
    main()