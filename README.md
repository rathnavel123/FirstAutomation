# DICOM File Synchronization Script

## Overview

This Python script synchronizes DICOM files between a main folder and a source folder. It copies DICOM files from the main folder to a specified destination folder if they match with the JPEG files in the source folder. Additionally, it sends an email notification if any DICOM files from the main folder are not found in the source folder.

## Features

- **File Synchronization**: Copies DICOM files from the main folder to a specified destination folder if they match with JPEG files in the source folder.
- **Email Notification**: Sends an email alert if any DICOM files are missing in the source folder.

## Requirements

- Python 3.x
- `shutil` (for file operations)
- `os` (for directory and file management)
- `re` (for regular expressions)
- `schedule` (for scheduling tasks)
- `time` (for time management)
- `smtplib` (for sending emails)
- `email` (for constructing email messages)

## Acknowledgements

  - **Python Libraries**: `shutil`, `os`, `re`, `schedule`, `time`,`smtplib`, `email`.
