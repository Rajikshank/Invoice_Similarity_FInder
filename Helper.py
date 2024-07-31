import PyPDF2

import cv2
import pytesseract
import re
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


#function to load the pdf file and extract text using pypdf2 library
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

#extracting the features from the extracted text from the pdf document using spacy library

nlp = spacy.load('en_core_web_sm')
#function to extract the key features from the extracted text
def extract_features(text):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]
    dates = re.findall(r'\b\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}\b', text)
    invoice_numbers = re.findall(r'\b\d{4,10}\b', text)  # Adjust regex as needed
    amounts = re.findall(r'\b\d+\.\d{2}\b', text)
    
    features = {
        'keywords': keywords,
        'dates': dates,
        'invoice_numbers': invoice_numbers,
        'amounts': amounts
    }
    return features


#function to find the layout/tables from the invoice document
def extract_layout_features(file_path):
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    # Detecting tables and layout
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    layout_features = [cv2.boundingRect(contour) for contour in contours]
    
    return layout_features



#function to vectoring the features
def vectorize_features(features_list):
    vectorizer = TfidfVectorizer()
    keyword_vectors = vectorizer.fit_transform([' '.join(features['keywords']) for features in features_list])
    return keyword_vectors



#function to calculate the cosine similarity for using sklearn library
def calculate_similarity(vector, database_vectors):
    similarities = cosine_similarity(vector, database_vectors)
    return similarities
