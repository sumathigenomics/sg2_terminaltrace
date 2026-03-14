SG2: TerminalTrace (v1.0.0)
High-speed terminal sequence motif analyzer for FASTQ data.
Developed by DR Saminathan Sivaprakasham Murugesan Sumathi Genomics Co Ltd (Thailand) | Saminathan Industries Pte Ltd (Singapore)

Overview
SG2: TerminalTrace is a specialized bioinformatics engine designed to characterize the fragmentation patterns of DNA. While its predecessor, SG1, focuses on high-performance genetic circuit design via CUDA, SG2 provides a streamlined, memory-efficient approach to analyzing terminal sequence motifs.
Terminal motifs (the sequence of bases at the ends of DNA fragments) are essential biomarkers in liquid biopsy and cell-free DNA (cfDNA) research. These motifs reflect the enzymatic cleavage processes (e.g., DNASE1L3 activity) that occur during apoptosis and necrosis, providing insights into tissue-of-origin and disease states.

Key Features
Streaming Architecture: Uses a generator-based approach to ensure a low memory footprint (<100MB) even when processing multi-gigabyte FASTQ/GZ files.
Dual-End Tracking: Independently analyzes the 5' (Leading) and 3' (Trailing) termini to account for library preparation biases.
Quality Gating: Integrates Phred quality score filtering (default Q20) to ensure that motif calls are derived from high-confidence sequencing data.
Flexible k-mer Analysis: User-definable motif lengths ($k$) to capture everything from single-nucleotide ends to complex 4-mer or 6-mer patterns.

 Technical Specifications
1. The Algorithm
SG2 scans the boundary bases of every valid sequencing read. It converts sequences to a uniform uppercase format and handles ambiguous bases (N), ensuring a complete representation of the raw data.
2. Quality Control
The tool calculates the average Phred quality score ($Q$) for each read. Reads falling below the user-defined threshold are discarded:

$$Q = -10 \log_{10}(P)$$
(Where $P$ is the probability of an incorrect base call).
3. Performance
The script is optimized for I/O efficiency, utilizing buffered reading for compressed Gzip streams. It operates with $O(n)$ time complexity, where $n$ is the total number of reads.

# SG2: TerminalTrace (v1.0.0)

**High-speed terminal sequence motif analyzer for FASTQ data.**

Developed by **DR Saminathan Sivaprakasham Murugesan** **Sumathi Genomics Co Ltd (Thailand)** | **Saminathan Industries Pte Ltd (Singapore)**

---

## Overview

**SG2: TerminalTrace** is a specialized bioinformatics engine designed to characterize the fragmentation patterns of DNA. While its predecessor, **SG1**, focuses on high-performance genetic circuit design via CUDA, **SG2** provides a streamlined, memory-efficient approach to analyzing terminal sequence motifs.

Terminal motifs (the sequence of bases at the ends of DNA fragments) are essential biomarkers in liquid biopsy and cell-free DNA (cfDNA) research. These motifs reflect enzymatic cleavage processes, providing insights into tissue-of-origin and disease states.

---

## Key Features

* **Streaming Architecture:** Low memory footprint (<100MB) even for large datasets.
* **Dual-End Tracking:** Analyzes 5' and 3' termini independently.
* **Quality Gating:** Built-in Phred quality score filtering (Default Q20).
* **Flexible k-mer Analysis:** User-definable motif lengths.

---

## Installation

```bash
# Clone the repository
git clone [https://github.com/sumathigenomics/sg2_terminaltrace.git](https://github.com/sumathigenomics/sg2_terminaltrace.git)
cd sg2_terminaltrace

# Install dependencies
pip install biopython
