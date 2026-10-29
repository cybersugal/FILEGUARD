# FILEGUARD
Python-based cybersecurity tool that identifies file types using magic bytes and detects filename extension mismatches.
# FileGuard — File Signature Analyzer

FileGuard is a beginner-friendly cybersecurity project written in Python. It identifies file types by examining their file signatures (magic bytes) and checks whether the detected type matches the filename extension.

## Features

- Detects PDF, PNG, JPEG, and ZIP file signatures.
- Scans multiple files in a single run.
- Handles missing and empty files.
- Checks whether file extensions match detected file types.
- Displays the first bytes of each file in hexadecimal format.

## Technologies Used

- Python 3
- File handling
- Dictionaries and conditional statements
- Exception handling
- Basic file signature analysis


## How to Run

1. Install Python 3.
2. Open a terminal in the project directory.
3. Run:

```bash
python3 fileguard.py
```

4. Enter filenames separated by commas, for example:

```text
sample.pdf, invoice.jpg, test.png
```

Make sure the files are in the project directory or provide their full paths.

## Test Cases

| Test file | Purpose |
|---|---|
| `sample.pdf` | Tests PDF signature detection |
| `invoice.jpg` | Tests detection of a PDF file with a `.jpg` extension |
| `test.png` | Tests PNG signature detection using a signature-only sample |

Note: `test.png` contains only the PNG signature bytes and is not a complete PNG image.

## Limitations

FileGuard checks file signatures and filename extensions. It does not determine whether a file contains malware, prove that a file is safe, or fully validate the file format.

A matching signature does not guarantee that a file is valid or trustworthy. An extension mismatch is a warning sign, not proof of malicious activity.

## Learning Goals

This project helped me practise Python file handling, binary data, file signatures, dictionaries, conditional logic, exception handling, and basic cybersecurity analysis.

## Future Improvements

- Nedd to Add automated unit tests.
- Support scanning entire directories.
- Export scan results to CSV or text reports.
- Add more file signatures.
- Improve error handling and reporting.

