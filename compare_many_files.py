import difflib
import os
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Directory containing the files
directory = askdirectory(title='Select Folder')

# Get a list of all files in the directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Create an empty DataFrame to store the results
df = pd.DataFrame(columns=['File1', 'File2', 'Similarity'])

# Compare each file to every other file
for i in range(len(files)):
    for j in range(i+1, len(files)):
        # Read the files
        
        with open(os.path.join(directory, files[i]), 'r') as file1, open(os.path.join(directory, files[j]), 'r') as file2:
            text1 = file1.read()
            text2 = file2.read()

        # Calculate the similarity ratio
        similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()

        # Append the result to the DataFrame
        data =pd.DataFrame([{'File1': files[i], 'File2': files[j], 'Similarity': similarity_ratio}])
        df = pd.concat([df,data], ignore_index=True)
        print(f'{file1} and {file2} similarity = {similarity_ratio}')
        #except Exception as e:
        #    print(f'An error occured for file {file1} and {file2}, hence skipped')
        #    continue

# Print the DataFrame
df.to_csv('Exp5.csv')
