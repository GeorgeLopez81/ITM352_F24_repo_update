import os


file_path = "/Users/georgelopez/Downloads/survey_1000.csv"

# Check if the file exists and is readable
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    # Get file size in bytes
    file_size = os.path.getsize(file_path)
    
    # Get detailed file information (permissions, size, etc.)
    file_stat = os.stat(file_path)
    
    print(f"File '{file_path}' exists and is readable.")
    print(f"File size: {file_size} bytes")
    print(f"File permissions: {oct(file_stat.st_mode)}")
    
    # Open the file and process it
    with open(file_path, 'r') as file:
        # Process file as needed
        print(f"File contents: {file.read()[:100]}...")  # Print first 100 characters as a preview
else:
    print(f"File '{file_path}' does not exist or is not readable.")
