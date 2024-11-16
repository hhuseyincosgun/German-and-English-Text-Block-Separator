import os

def separate_german_english_blocks(directory):
    # Create folders for German and English files
    german_folder = os.path.join(directory, 'German')
    english_folder = os.path.join(directory, 'English')
    os.makedirs(german_folder, exist_ok=True)
    os.makedirs(english_folder, exist_ok=True)

    # List all text files in the specified directory
    text_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    for text_file in text_files:
        input_path = os.path.join(directory, text_file)
        
        # Extract the base name without the extension
        base_name = os.path.splitext(text_file)[0]
        
        # Define output file paths
        german_file = os.path.join(german_folder, f"{base_name}_Ger.txt")
        english_file = os.path.join(english_folder, f"{base_name}_Eng.txt")
        
        german_sentences = []
        english_sentences = []

        # Read and process the input file
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        block = []  # Temporary storage for a block
        for line in lines:
            line = line.strip()
            if line == "":  # Tab separator (empty line)
                if block:  # Process the current block
                    german_sentences.append(block[0].strip())
                    english_sentences.append(block[1].strip() if len(block) > 1 else "")
                block = []  # Reset the block
            else:
                block.append(line)
        
        # Process the last block if it exists
        if block:
            german_sentences.append(block[0].strip())
            english_sentences.append(block[1].strip() if len(block) > 1 else "")
        
        # Write the German sentences to the file
        with open(german_file, 'w', encoding='utf-8') as file:
            for sentence in german_sentences:
                file.write(sentence + '\n')
        
        # Write the English sentences to the file
        with open(english_file, 'w', encoding='utf-8') as file:
            for sentence in english_sentences:
                file.write(sentence + '\n')

        print(f"Processed '{text_file}' -> '{german_file}' and '{english_file}'")

# Specify the directory containing the text files
directory_path = '/content'  # Replace with '/content' or your actual directory

# Call the function
separate_german_english_blocks(directory_path)
