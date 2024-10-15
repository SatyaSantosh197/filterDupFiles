# filterDupFiles

`filterDupFiles` is a Python script designed to automate the task of managing duplicate files in a folder. This tool helps you organize files effortlessly by sorting them into distinct directories based on their uniqueness.

## Problem Statement

Managing duplicate files can be a tedious and time-consuming task, especially when dealing with large folders. This script aims to simplify that process by automatically identifying duplicates and organizing them into three separate folders.

## Features

- **Automated Duplication Detection:** Identifies duplicate files based on their content using hashing.
- **Organized Structure:** Creates three folders to manage files effectively:
  - **originals:** Contains the original files and one copy from any duplicate sets.
  - **duplicates:** Stores all detected duplicate files.
  - **non-duplicates:** Includes unique files that are not duplicates.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/YOUR_USERNAME/your-repo-name.git
   cd your-repo-name

2. Run the Python script:
     py filterDupFiles.py  

3. When prompted, enter the path to the folder containing your files. The script will create the necessary directories (originals, duplicates, and non-duplicates) in the current directory.


## Requirements
    Ensure you have Python installed on your machine. No additional libraries are required for this script.


