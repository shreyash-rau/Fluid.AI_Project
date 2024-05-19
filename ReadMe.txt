How to Use
Download the required NLTK packages by running the following commands in your Python environment:
Python

import nltk
nltk.download('punkt')
nltk.download('stopwords')
AI-generated code. Review and use carefully. More info on FAQ.
Define the keywords that you’re interested in. These are the words that the script will look for in the PDF file.
Call the extract_info_from_pdf function with the path to the PDF file you want to analyze. This function will return a dictionary where the keys are the keywords and the values are lists of occurrences of the keywords in the text.
Print the extracted information. For each keyword, the script will print the keyword and the number of its occurrences in the text.
Example
Here’s an example of how to use the script:

Python

file_path = r'C:\Users\Shreyash Raut\OneDrive\Desktop\SJS\SJS Transcript Call.pdf'
info = extract_info_from_pdf(file_path)

for keyword, occurrences in info.items():
    print(f"{keyword}: {len(occurrences)} occurrences")
AI-generated code. Review and use carefully. More info on FAQ.
In this example, the script will read the PDF file at the specified path, extract the keywords, and print the number of occurrences of each keyword.

Output
The output of the script will be a dictionary where the keys are the keywords and the values are lists of occurrences of the keywords in the text. For each keyword, the script will print the keyword and the number of its occurrences in the text.

Please note that the actual output will depend on the content of the PDF file you’re analyzing. If the PDF file doesn’t contain any of the keywords, the lists in the dictionary will be empty.


Please replace `'C:\Users\Shreyash Raut\OneDrive\Desktop\SJS\SJS Transcript Call.pdf'` with the path to the PDF file you want to read.
