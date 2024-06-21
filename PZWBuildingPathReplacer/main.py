import os

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

def search_string(file_path, search_str):
    """
    Search for a specific string in a file and return the count of matches.

    Args:
    - file_path (str): The path to the file to search.
    - search_str (str): The string to search for.

    Returns:
    - tuple: A tuple containing a boolean value indicating if the string is found,
             and an integer representing the count of matches.
    """
    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    # Count the occurrences of the search string in the file content
    match_count = file_content.count(search_str)
    
    # Check if the search string is present in the file content
    if match_count > 0:
        return True, match_count
    else:
        return False, 0

def find_replace(file_path, find_str, replace_str):
    """
    Find and replace strings in a file.

    Args:
    - file_path (str): The path to the file to modify.
    - find_str (str): The string to find.
    - replace_str (str): The string to replace the found string with.
    """
    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_content = file.read()
    
    # Perform the find and replace operation
    modified_content = file_content.replace(find_str, replace_str)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(modified_content)

# Example usage:
directory_path = "./"
pzw_file_path = find_first_pzw_file(directory_path)
if pzw_file_path:
    print("Path to the first .pzw file:", pzw_file_path)
else:
    print("No .pzw file found.")

search_str = "../../Building_TBX/Kaizokuroof/Residential/Houses/kr_1s_nicholls_suburban_e_2_1.tbx"

found, count = search_string(pzw_file_path, search_str)
if found:
    print(f"The string '{search_str}' is found in the file. Count: {count}")
else:
    print(f"The string '{search_str}' is not found in the file.")