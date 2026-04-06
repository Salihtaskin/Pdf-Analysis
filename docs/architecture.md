# Architecture

## Goal
This project performs automated triage analysis of suspicious PDF documents using a modular Python-based workflow.

## Workflow
1. Input PDF is provided through CLI.
2. SHA256 hash is calculated.
3. `file` command inspects the file type.
4. `strings` output is parsed for suspicious indicators.
5. `peepdf` output is parsed when available.
6. Risk score is calculated using weighted indicators.
7. Reports are generated in JSON and Markdown format.

## Components
- `main.py`: entry point
- `src/core/analyzer.py`: main orchestration logic
- `src/core/indicators.py`: scoring and verdict engine
- `src/core/reporter.py`: report generation
- `src/parsers/`: analysis output parsers
- `src/utils/`: shared utility functions

## Outputs
- `summary.json`
- `summary.md`
- `hashes.txt`
- `payload_strings.txt`
- `payload_filetype.txt`
- `peepdf_report.txt`
