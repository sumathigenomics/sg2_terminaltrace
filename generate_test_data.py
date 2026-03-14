#!/usr/bin/env python3
import random

def generate_dummy_fastq(filename="test_data.fastq", num_reads=1000):
    nucleotides = ['A', 'C', 'G', 'T']
    with open(filename, "w") as f:
        for i in range(num_reads):
            seq = ''.join(random.choices(nucleotides, k=50))
            # Inject a common motif for validation (CCCA)
            if random.random() < 0.25:
                seq = "CCCA" + seq[4:]
            
            f.write(f"@READ_{i}\n{seq}\n+\n{'F'*50}\n")
    print(f"Generated {filename} with {num_reads} reads for SG2 testing.")

if __name__ == "__main__":
    generate_dummy_fastq()
