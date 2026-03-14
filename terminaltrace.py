#!/usr/bin/env python3
"""
SG2: TerminalTrace (v1.0.0)
High-speed terminal sequence motif analyzer for FASTQ data.
Author: DR Saminathan Sivaprakasham Murugesan
Affiliations: Sumathi Genomics Co Ltd | Saminathan Industries Pte Ltd
Contact: lab@sumathigenomics.com
"""

import gzip
import argparse
import csv
import sys
from collections import Counter
from Bio import SeqIO

def get_args():
    parser = argparse.ArgumentParser(description="SG2: TerminalTrace - End-Motif Analysis")
    parser.add_argument("-i", "--input", required=True, help="Input FASTQ or FASTQ.GZ file")
    parser.add_argument("-k", "--length", type=int, default=4, help="Motif length to extract (default: 4)")
    parser.add_argument("-o", "--output", default="SG2_terminal_motifs.csv", help="Output CSV filename")
    parser.add_argument("-minq", "--min_quality", type=int, default=20, help="Minimum average Phred quality (default: 20)")
    return parser.parse_args()

def run_analysis():
    args = get_args()
    k = args.length
    
    five_prime_counts = Counter()
    three_prime_counts = Counter()
    total_reads = 0
    skipped_reads = 0

    print("\n--- SG2: TerminalTrace ---")
    print(f"Author: DR Saminathan Sivaprakasham Murugesan")
    print(f"Processing: {args.input}")

    open_func = gzip.open if args.input.endswith('.gz') else open
    
    try:
        with open_func(args.input, "rt") as handle:
            for record in SeqIO.parse(handle, "fastq"):
                total_reads += 1
                
                # Quality filtering logic
                avg_q = sum(record.letter_annotations["phred_quality"]) / len(record)
                if avg_q < args.min_quality:
                    skipped_reads += 1
                    continue

                seq = str(record.seq).upper()
                if len(seq) >= k:
                    five_prime_counts[seq[:k]] += 1
                    three_prime_counts[seq[-k:]] += 1

        # Consolidate and sort motifs
        all_motifs = sorted(set(five_prime_counts.keys()) | set(three_prime_counts.keys()))
        
        with open(args.output, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Motif", "Five_Prime_Count", "Three_Prime_Count"])
            for m in all_motifs:
                writer.writerow([m, five_prime_counts.get(m, 0), three_prime_counts.get(m, 0)])

        print("Analysis Complete.")
        print(f"Total Reads: {total_reads} | Skipped (Low Quality): {skipped_reads}")
        print(f"Results saved to: {args.output}\n")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_analysis()
