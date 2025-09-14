#!/usr/bin/env python3
"""
Simple Numeric Frequency Analyzer
"""

import argparse
from collections import Counter
import re

def analyze_frequency(filename, delimiter, digit_size):
    """Analyze frequency of digit groups in a file."""
    
    # Read the file
    with open(filename, 'r') as f:
        data = f.read().strip()
    
    # Split by delimiter if provided, otherwise treat as continuous digits
    if delimiter:
        parts = data.split(delimiter)
        # Join all parts to create continuous digit stream
        digit_stream = ''.join(parts)
    else:
        # Remove non-digits
        digit_stream = re.sub(r'[^0-9]', '', data)
    
    # Create groups of specified size
    groups = []
    for i in range(0, len(digit_stream), digit_size):
        group = digit_stream[i:i + digit_size]
        if len(group) == digit_size:  # Only complete groups
            groups.append(group)
    
    # Count frequencies
    counter = Counter(groups)
    total = len(groups)
    
    # Print results
    print(f"Total groups analyzed: {total}")
    print(f"Unique groups: {len(counter)}")
    print()
    print(f"{'Group':<10} {'Count':<8} {'Percentage':<10}")
    print("-" * 30)
    
    # Show top 20
    for group, count in counter.most_common(50):
        percentage = (count / total) * 100
        print(f"{group:<10} {count:<8} {percentage:<9.2f}%")

def main():
    parser = argparse.ArgumentParser(description='Analyze frequency of digit groups')
    parser.add_argument('-f', '--file', required=True, help='Input file')
    parser.add_argument('-d', '--delimiter', help='Delimiter (optional)')
    parser.add_argument('-g', '--group-size', type=int, default=1, help='Digit group size')
    
    args = parser.parse_args()
    
    analyze_frequency(args.file, args.delimiter, args.group_size)

if __name__ == "__main__":
    main()