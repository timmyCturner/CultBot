import os

# Define the folder containing the text files
folder_path = '..\\txts'  # Replace with the path to your folder

# Define the output file name
output_file = 'combined.txt'  # Replace with the desired output file name

# Initialize an empty string to store the combined text
combined_text = ''

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Check if the file is a text file
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_text = file.read()
            combined_text += file_text

# Write the combined text to the output file
with open(output_file, 'w', encoding='utf-8') as output:
    output.write(combined_text)

print(f'Combined text saved in {output_file}')
