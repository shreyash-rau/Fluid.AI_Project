import PyPDF2
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download the required NLTK packages
nltk.download('punkt')
nltk.download('stopwords')

# Define the keywords that the investor is interested in
keywords = ['growth', 'business', 'triggers', 'earnings', 'prospects', 'changes', 'material effect']

def extract_info_from_pdf(file_path):
    # Open the PDF file in binary mode
    with open(file_path, 'rb') as file:
        # Create a PDF file reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Initialize an empty string to hold the text
        text = ''

        # Loop through each page in the PDF and extract the text
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()

        # Tokenize the text
        tokens = word_tokenize(text)

        # Remove punctuation and convert to lower case
        words = [word.lower() for word in tokens if word.isalpha()]

        # Remove stopwords
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]

        # Initialize a dictionary to hold the keywords and their occurrences
        keyword_dict = {keyword: [] for keyword in keywords}

        # Search for the keywords and extract the sentences that contain them
        for word in words:
            if word in keywords:
                keyword_dict[word].append(word)

        return keyword_dict

# Replace 'path_to_your_file.pdf' with the path to the PDF file you want to read
file_path = r'C:\Users\Shreyash Raut\OneDrive\Desktop\SJS\SJS Transcript Call.pdf'
info = extract_info_from_pdf(file_path)

# Print the extracted information
for keyword, occurrences in info.items():
    print(f"{keyword}: {len(occurrences)} occurrences")
