import os
import re
import random

def find_first_pzw_file(directory):
    """
    Find the first .pzw file in a directory.

    Args:
    - directory (str): The directory to search for the .pzw file.

    Returns:
    - str: The path to the first .pzw file, or None if no .pzw file is found.
    """
    # List all files in the directory
    files = os.listdir(directory)
    
    # Find the first file with .pzw extension
    for file_name in files:
        if file_name.endswith('.pzw'):
            return os.path.join(directory, file_name)
    
    # If no .pzw file is found, return None
    print("No .pzw file found in the provided directory.")
    return None

def random_number():
    return random.randint(1, 200)

# Function to process the file
def process_file(file_path):
    # Read the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Define the regex pattern to match the strings
    pattern = r'(\.\./\.\./Building_TBX/Kaizokuroof/Residential/Houses/kr_)(\d+)s_nicholls_suburban_w_(\d+)_(\d+)\.tbx'

    # Find all matches
    matches = re.findall(pattern, content)

    # Replace each match with a random number between 1 and 200
    for match in matches:
        print('match')
        original_string = ''.join(match)
        new_second_number = str(int(match[2]) + 1) if int(match[2]) < 10 else match[2]
        new_last_number = str(int(match[3]) + 1) if int(match[3]) < 30 else match[3]
        random_num = str(random_number())
        new_string = match[0] + new_second_number + 's_nicholls_suburban_e_' + new_last_number + '_' + random_num + '.tbx'
        content = content.replace(original_string, new_string)

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

directory_path = "./"
pzw_file_path = find_first_pzw_file(directory_path)
if pzw_file_path:
    print("Path to the first .pzw file:", pzw_file_path)
else:
    print("No .pzw file found.")

process_file(pzw_file_path)
