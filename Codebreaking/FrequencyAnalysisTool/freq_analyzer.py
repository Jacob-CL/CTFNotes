#!/usr/bin/env python3
"""
Character Frequency Analyzer
A CLI tool to analyze letter frequency in text files.
"""

import argparse
import sys
from collections import Counter
import os

def analyze_frequency(file_path, case_sensitive=False, letters_only=True):
    """
    Analyze character frequency in a text file.
    
    Args:
        file_path (str): Path to the text file
        case_sensitive (bool): Whether to treat uppercase/lowercase as different
        letters_only (bool): Whether to count only letters (A-Z, a-z)
    
    Returns:
        Counter: Character frequency counter
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
    
    # Process the content based on options
    if not case_sensitive:
        content = content.lower()
    
    if letters_only:
        # Keep only alphabetic characters
        content = ''.join(char for char in content if char.isalpha())
    
    # Count character frequencies
    frequency = Counter(content)
    
    return frequency

def calculate_index_of_coincidence(frequency):
    """
    Calculate the Index of Coincidence for the given frequency data.
    
    Args:
        frequency (Counter): Character frequency counter
    
    Returns:
        float: Index of Coincidence value
    """
    total_chars = sum(frequency.values())
    
    # Need at least 2 characters to calculate IoC
    if total_chars < 2:
        return 0.0
    
    # Calculate sum of ni * (ni - 1) for each character
    coincidence_sum = sum(count * (count - 1) for count in frequency.values())
    
    # IoC formula: Σ(ni * (ni - 1)) / (N * (N - 1))
    ioc = coincidence_sum / (total_chars * (total_chars - 1))
    
    return ioc

def interpret_ioc(ioc_value):
    """
    Provide interpretation of IoC value.
    
    Args:
        ioc_value (float): Index of Coincidence value
    
    Returns:
        str: Interpretation of the IoC value
    """
    if ioc_value >= 0.060:
        return "English-like text (monoalphabetic substitution or plaintext)"
    elif ioc_value >= 0.045:
        return "Possibly encrypted with pattern preservation"
    elif ioc_value >= 0.035:
        return "Random or well-encrypted text"
    else:
        return "Highly random or short text sample"

def display_results(frequency, sort_by='frequency'):
    """
    Display the frequency analysis results.
    
    Args:
        frequency (Counter): Character frequency counter
        sort_by (str): How to sort results ('frequency', 'alphabetical')
    """
    # Expected English letter frequencies (from standard English text analysis)
    expected_frequencies = {
        'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.23,
        'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15, 'k': 0.77, 'l': 4.03,
        'm': 2.41, 'n': 6.75, 'o': 7.51, 'p': 1.93, 'q': 0.10, 'r': 5.99,
        's': 6.33, 't': 9.06, 'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15,
        'y': 1.97, 'z': 0.07
    }
    
    if not frequency:
        print("No characters found to analyze.")
        return
    
    total_chars = sum(frequency.values())
    
    # Calculate Index of Coincidence
    ioc_value = calculate_index_of_coincidence(frequency)
    ioc_interpretation = interpret_ioc(ioc_value)
    
    print(f"\nCharacter Frequency Analysis")
    print("=" * 70)
    print(f"Total characters analyzed: {total_chars}")
    print(f"Index of Coincidence: {ioc_value:.4f}")
    print(f"Interpretation: {ioc_interpretation}")
    print("-" * 70)
    
    # Sort results
    if sort_by == 'frequency':
        # Sort by frequency (descending), then alphabetically
        sorted_items = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    else:  # alphabetical
        sorted_items = sorted(frequency.items())
    
    # Display results
    print(f"{'Char':<6} {'Count':<8} {'Actual%':<10} {'Expected%':<12} {'Bar'}")
    print("-" * 70)
    
    for char, count in sorted_items:
        percentage = (count / total_chars) * 100
        
        # Improved bar chart - more granular and always shows something for non-zero values
        if percentage > 0:
            # Scale more generously: use percentage directly but cap at reasonable length
            bar_length = max(1, int(percentage * 4))  # Multiply by 4 for better granularity
            bar_length = min(bar_length, 50)  # Cap at 50 characters max
            
            # Use different characters for different ranges for better granularity
            if percentage >= 2.0:
                bar = '█' * bar_length
            elif percentage >= 0.5:
                bar = '▓' * bar_length  # Medium density for medium frequencies
            else:
                bar = '░' * bar_length  # Light density for low frequencies
        else:
            bar = ''
        
        # Handle special characters for display
        display_char = char if char.isprintable() and char != ' ' else repr(char)
        
        # Get expected frequency for this character (if it's a letter)
        expected = expected_frequencies.get(char.lower(), 0.0) if char.isalpha() else 0.0
        expected_str = f"{expected:.2f}%" if expected > 0 else "N/A"
        
        print(f"{display_char:<6} {count:<8} {percentage:<8.2f}%  {expected_str:<12} {bar}")

def main():
    parser = argparse.ArgumentParser(
        description="Analyze character frequency in text files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python freq_analyzer.py document.txt
  python freq_analyzer.py text.txt --case-sensitive
  python freq_analyzer.py file.txt --all-chars --sort alphabetical
        """
    )
    
    parser.add_argument(
        'file',
        help='Path to the text file to analyze'
    )
    
    parser.add_argument(
        '--case-sensitive',
        action='store_true',
        help='Treat uppercase and lowercase letters as different'
    )
    
    parser.add_argument(
        '--all-chars',
        action='store_true',
        help='Count all characters including punctuation and whitespace'
    )
    
    parser.add_argument(
        '--sort',
        choices=['frequency', 'alphabetical'],
        default='alphabetical',
        help='Sort results alphabetically (default) or by frequency'
    )
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.isfile(args.file):
        print(f"Error: '{args.file}' is not a valid file.")
        sys.exit(1)
    
    # Analyze frequency
    frequency = analyze_frequency(
        args.file,
        case_sensitive=args.case_sensitive,
        letters_only=not args.all_chars
    )
    
    # Display results
    display_results(frequency, args.sort)
    
    print(f"\nAnalysis complete for: {args.file}")

if __name__ == "__main__":
    main()