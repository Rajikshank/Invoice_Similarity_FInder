
from Db import *
from Helper import *
import streamlit as st
import os

def main():
    st.title("Invoice Similarity Finder")

    # File upload
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Extract and display text from uploaded file
        text = extract_text_from_pdf(uploaded_file)
        #st.write("Extracted Text:")
        #st.write(text)
        
        # Extract features and find the most similar invoice
        features = extract_features(text)
        
        # Example existing invoices
        database = InvoiceDatabase()
        database.add_invoice('invoice 1 - Bremer Spirituosen Contor GmbH', extract_features(extract_text_from_pdf(open('/train/2024.03.15_0954.pdf', 'rb'))))
        database.add_invoice('invoice 2 - Bremer Spirituosen Contor GmbH', extract_features(extract_text_from_pdf(open('/train/2024.03.15_1145.pdf', 'rb'))))
        database.add_invoice('invoice 3 - Faller', extract_features(extract_text_from_pdf(open('/train/Faller_8.PDF', 'rb'))))
        database.add_invoice('invoice 4 - Süderelbe HAF Catering u. Service GmbH', extract_features(extract_text_from_pdf(open('/train/invoice_77073.pdf', 'rb'))))
        database.add_invoice('invoice 5 - GmbH & Co', extract_features(extract_text_from_pdf(open('/train/invoice_102856.pdf', 'rb'))))
        
        most_similar_file, similarity_score = database.find_most_similar(features)
        st.write(f'The most similar invoice is: {most_similar_file}')
        st.write(f'Similarity score: {similarity_score}')

if __name__ == '__main__':
    main()