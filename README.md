# German and English Text Block Separator

## Overview
This Python script is designed to process text files containing German and English sentence pairs, separated by empty lines, and organize them into two distinct files for each text file. The resulting files will be stored in subfolders named `German` and `English`.

## Features
1. **Automatic Directory Setup**: 
   - Creates `German` and `English` subfolders within the specified directory to store the output files.
2. **File Processing**:
   - Reads `.txt` files from the given directory.
   - Separates German and English blocks of sentences based on tab-separated blocks.
   - Writes the sentences into separate files with `_Ger.txt` and `_Eng.txt` suffixes.
3. **Error Handling**:
   - Ensures the program doesn't crash if a file is empty or improperly formatted.

## How It Works
1. The script scans the specified directory for `.txt` files.
2. Each file is read line by line to identify blocks of German and English sentences. A block is considered as text separated by empty lines.
3. German sentences are written to a file in the `German` folder, and English sentences are written to a file in the `English` folder.
4. The filenames of the output files are derived from the input file's name, appended with `_Ger.txt` and `_Eng.txt`.

### Example Input File
`Sample.txt`:

```perl
Hallo, wie geht's?
Hello, how are you?

Ich bin gut.
I am good.

Vielen Dank!
Thank you very much!
```

### Output Files
- **German**:
  - `German/Sample_Ger.txt`:
    ```
    Hallo, wie geht's?
    Ich bin gut.
    Vielen Dank!
    ```
- **English**:
  - `English/Sample_Eng.txt`:
    ```
    Hello, how are you?
    I am good.
    Thank you very much!
    ```

### Directory Structure
#### Before
```
|--Sample.txt
```

#### After
```
|-- Sample.txt
|--
|-- German/
|   |-- Sample_Ger.txt
|-- English/
    |-- Sample_Eng.txt
```
