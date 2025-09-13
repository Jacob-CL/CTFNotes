#!/usr/bin/env python3
"""
Caesar Cipher Decoder
A CLI tool to decode Caesar ciphers by showing all possible shifts (1-26).
"""

import argparse
import sys
import os

def caesar_shift(text, shift):
    """
    Apply Caesar cipher shift to text.
    
    Args:
        text (str): Input text
        shift (int): Number of positions to shift (positive = forward)
    
    Returns:
        str: Shifted text
    """
    result = []
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            
            # Convert to lowercase for processing
            char = char.lower()
            
            # Apply shift with wrap-around
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            # Restore original case
            if is_upper:
                shifted_char = shifted_char.upper()
            
            result.append(shifted_char)
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)
    
    return ''.join(result)

def decode_caesar_all_shifts(text, output_to_files=False, output_dir='caesar_output'):
    """
    Decode Caesar cipher by trying all possible shifts.
    
    Args:
        text (str): Encrypted text
        output_to_files (bool): Whether to save results to files
        output_dir (str): Directory to save output files
    
    Returns:
        list: List of (shift, decoded_text) tuples
    """
    results = []
    
    if output_to_files:
        os.makedirs(output_dir, exist_ok=True)
    
    print("Caesar Cipher Decoder - All Possible Shifts")
    print("=" * 60)
    print("Original text:")
    print(f">>> {text}")
    print("=" * 60)
    
    for shift in range(1, 27):
        decoded = caesar_shift(text, shift)
        results.append((shift, decoded))
        
        # Display to terminal
        print(f"Shift +{shift:2d}: {decoded}")
        
        # Optionally save to file
        if output_to_files:
            filename = f"shift_{shift:02d}.txt"
            filepath = os.path.join(output_dir, filename)
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"Caesar Cipher - Shift +{shift}\n")
                    f.write("=" * 30 + "\n")
                    f.write(f"Original: {text}\n")
                    f.write(f"Decoded:  {decoded}\n")
            except Exception as e:
                print(f"Warning: Could not save shift {shift} to file: {e}")
    
    print("=" * 60)
    
    if output_to_files:
        print(f"Results also saved to files in: {output_dir}/")
    
    return results

def analyze_text(text):
    """
    Provide basic analysis to help identify correct decryption.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        dict: Analysis results
    """
    words = text.lower().split()
    
    # Common English words that might indicate correct decryption
    common_words = {
        'the', 'and', 'a', 'to', 'of', 'in', 'i', 'you', 'it', 'for', 'is', 'on', 'with', 'as', 'was', 'that', 'are', 'this', 'have', 'from', 'or', 'one', 'had', 'by', 'word', 'not', 'what', 'all', 'were', 'they', 'we', 'when', 'your', 'can', 'said', 'there', 'each', 'which', 'she', 'do', 'how', 'their', 'if', 'will', 'up', 'other', 'about', 'out', 'many', 'then', 'them', 'these', 'so', 'some', 'her', 'would', 'make', 'like', 'into', 'him', 'has', 'two', 'more', 'very', 'after', 'words', 'first', 'where', 'much', 'through', 'back', 'years', 'work', 'came', 'right', 'still', 'should', 'because', 'any', 'good', 'woman', 'three', 'also', 'well', 'before', 'must', 'thought', 'never', 'however', 'too', 'does', 'got', 'united', 'left', 'number', 'course', 'war', 'until', 'always', 'away', 'something', 'fact', 'though', 'water', 'less', 'public', 'put', 'think', 'almost', 'hand', 'enough', 'far', 'took', 'head', 'yet', 'government', 'system', 'better', 'set', 'told', 'nothing', 'night', 'end', 'why', 'called', 'didn', 'eyes', 'find', 'going', 'look', 'asked', 'later', 'knew', 'point', 'next', 'week', 'home', 'give', 'use', 'own', 'under', 'last', 'right', 'move', 'thing', 'general', 'school', 'every', 'don', 'world', 'still', 'try', 'around', 'small', 'found', 'those', 'come', 'made', 'while', 'here', 'old', 'see', 'now', 'way', 'could', 'people', 'my', 'than', 'first', 'been', 'call', 'who', 'oil', 'sit', 'now', 'find', 'long', 'down', 'day', 'did', 'get', 'come', 'made', 'may', 'part'
    }
    
    # Count common words
    common_count = sum(1 for word in words if word.strip('.,!?;:"()[]') in common_words)
    
    return {
        'total_words': len(words),
        'common_words': common_count,
        'common_word_ratio': common_count / len(words) if words else 0
    }

def suggest_best_shifts(results, top_n=3):
    """
    Analyze results and suggest most likely correct shifts.
    
    Args:
        results (list): List of (shift, decoded_text) tuples
        top_n (int): Number of top suggestions to return
    
    Returns:
        list: Top shift suggestions with analysis
    """
    analyzed_results = []
    
    for shift, text in results:
        analysis = analyze_text(text)
        analyzed_results.append((shift, text, analysis))
    
    # Sort by common word ratio (descending)
    analyzed_results.sort(key=lambda x: x[2]['common_word_ratio'], reverse=True)
    
    print(f"\nTop {top_n} Most Likely Decryptions (based on common English words):")
    print("-" * 60)
    
    for i, (shift, text, analysis) in enumerate(analyzed_results[:top_n]):
        ratio = analysis['common_word_ratio'] * 100
        print(f"{i+1}. Shift +{shift:2d} ({ratio:.1f}% common words): {text[:80]}{'...' if len(text) > 80 else ''}")
    
    return analyzed_results[:top_n]

def main():
    parser = argparse.ArgumentParser(
        description="Decode Caesar ciphers by showing all possible shifts (1-26) with automatic analysis",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python caesar_decoder.py encrypted.txt
  python caesar_decoder.py cipher.txt --save-files
  python caesar_decoder.py text.txt --output-dir results/
  python caesar_decoder.py cipher.txt --analyze --top 5
        """
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the encrypted text file'
    )
    
    parser.add_argument(
        '--save-files',
        action='store_true',
        help='Save each shift result to separate files'
    )
    
    parser.add_argument(
        '--output-dir',
        default='caesar_output',
        help='Directory to save output files (default: caesar_output)'
    )
    
    parser.add_argument(
        '--analyze',
        action='store_true',
        help='Analyze results and suggest most likely correct decryptions'
    )
    
    parser.add_argument(
        '--top',
        type=int,
        default=3,
        help='Number of top suggestions to show in analysis (default: 3)'
    )
    
    parser.add_argument(
        '--single-shift',
        type=int,
        metavar='N',
        help='Show only a specific shift (1-26) instead of all shifts'
    )
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.isfile(args.input_file):
        print(f"Error: '{args.input_file}' is not a valid file.")
        sys.exit(1)
    
    # Read input file
    try:
        with open(args.input_file, 'r', encoding='utf-8') as file:
            text = file.read().strip()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    if not text:
        print("Error: Input file is empty.")
        sys.exit(1)
    
    # Handle single shift request
    if args.single_shift:
        if not (1 <= args.single_shift <= 26):
            print("Error: Shift must be between 1 and 26.")
            sys.exit(1)
        
        decoded = caesar_shift(text, args.single_shift)
        print(f"Caesar Cipher Decoder - Shift +{args.single_shift}")
        print("=" * 40)
        print(f"Original: {text}")
        print(f"Decoded:  {decoded}")
        sys.exit(0)
    
    # Decode with all shifts
    results = decode_caesar_all_shifts(text, args.save_files, args.output_dir)
    
    # Analyze and suggest best decryptions
    if args.analyze:
        suggest_best_shifts(results, args.top)
    
    print("\nLook for the shift that produces readable English text!")

if __name__ == "__main__":
    main()