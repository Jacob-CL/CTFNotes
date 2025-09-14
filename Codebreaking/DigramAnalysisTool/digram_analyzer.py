#!/usr/bin/env python3
"""
Digram Frequency Analyzer
A CLI tool to analyze digram (letter pair) frequency in text files.
"""

import argparse
import sys
from collections import Counter
import os

def analyze_digram_frequency(file_path, case_sensitive=False, letters_only=True, overlapping=True):
    """
    Analyze digram frequency in a text file.
    
    Args:
        file_path (str): Path to the text file
        case_sensitive (bool): Whether to treat uppercase/lowercase as different
        letters_only (bool): Whether to count only letter pairs (A-Z, a-z)
        overlapping (bool): Whether to use overlapping digrams
    
    Returns:
        Counter: Digram frequency counter
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
    
    # Extract digrams
    digrams = []
    
    if overlapping:
        # Overlapping digrams: "hello" -> "he", "el", "ll", "lo"
        for i in range(len(content) - 1):
            digram = content[i:i+2]
            if len(digram) == 2:
                digrams.append(digram)
    else:
        # Non-overlapping digrams: "hello" -> "he", "ll", "o" (skip single char)
        for i in range(0, len(content) - 1, 2):
            digram = content[i:i+2]
            if len(digram) == 2:
                digrams.append(digram)
    
    # Count digram frequencies
    frequency = Counter(digrams)
    
    return frequency

def display_results(frequency, sort_by='frequency'):
    """
    Display the digram frequency analysis results.
    
    Args:
        frequency (Counter): Digram frequency counter
        sort_by (str): How to sort results ('frequency', 'alphabetical')
    """
    if not frequency:
        print("No digrams found to analyze.")
        return
    
    total_digrams = sum(frequency.values())
    
    print(f"\nDigram Frequency Analysis")
    print("=" * 45)
    print(f"Total digrams analyzed: {total_digrams}")
    print("-" * 45)
    
    # Sort results
    if sort_by == 'frequency':
        # Sort by frequency (descending), then alphabetically
        sorted_items = sorted(frequency.items(), key=lambda x: (-x[1], x[0]))
    else:  # alphabetical
        sorted_items = sorted(frequency.items())
    
    # Display results
    print(f"{'Digram':<8} {'Count':<8} {'Percentage':<12} {'Bar'}")
    print("-" * 45)
    
    for digram, count in sorted_items:
        percentage = (count / total_digrams) * 100
        # Create a simple bar chart
        bar_length = int(percentage * 2)  # Scale for display
        bar = '█' * min(bar_length, 30)  # Cap at 30 characters
        
        print(f"{digram:<8} {count:<8} {percentage:<8.2f}%    {bar}")

def print_top_digrams(frequency, n=10):
    """Print the top N most frequent digrams."""
    if not frequency:
        print("No digrams found.")
        return
    
    print(f"\nTop {n} Most Frequent Digrams:")
    print("-" * 30)
    
    sorted_items = sorted(frequency.items(), key=lambda x: -x[1])
    total_digrams = sum(frequency.values())
    
    for i, (digram, count) in enumerate(sorted_items[:n], 1):
        percentage = (count / total_digrams) * 100
        print(f"{i:2d}. {digram} - {count:4d} times ({percentage:.2f}%)")

def main():
    parser = argparse.ArgumentParser(
        description="Analyze digram (letter pair) frequency in text files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python digram_analyzer.py document.txt
  python digram_analyzer.py text.txt --case-sensitive
  python digram_analyzer.py file.txt --no-overlap
  python digram_analyzer.py cipher.txt --top 20 --sort alphabetical
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
        help='Count all character pairs including punctuation and whitespace'
    )
    
    parser.add_argument(
        '--no-overlap',
        action='store_true',
        help='Use non-overlapping digrams (default: overlapping)'
    )
    
    parser.add_argument(
        '--sort',
        choices=['frequency', 'alphabetical'],
        default='frequency',
        help='Sort results by frequency (default) or alphabetically'
    )
    
    parser.add_argument(
        '--top',
        type=int,
        metavar='N',
        help='Show only top N most frequent digrams'
    )
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.isfile(args.file):
        print(f"Error: '{args.file}' is not a valid file.")
        sys.exit(1)
    
    # Analyze digram frequency
    frequency = analyze_digram_frequency(
        args.file,
        case_sensitive=args.case_sensitive,
        letters_only=not args.all_chars,
        overlapping=not args.no_overlap
    )
    
    if not frequency:
        print("No digrams found in the file.")
        sys.exit(0)
    
    # Show top N if requested
    if args.top:
        print_top_digrams(frequency, args.top)
    else:
        # Display full results
        display_results(frequency, args.sort)
    
    print(f"\nAnalysis complete for: {args.file}")
    
    # Show some additional stats
    total_digrams = sum(frequency.values())
    unique_digrams = len(frequency)
    print(f"Unique digrams found: {unique_digrams}")
    print(f"Total digrams analyzed: {total_digrams}")

if __name__ == "__main__":
    main()