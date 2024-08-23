# 📄 Invoice Similarity Finder

This project is a prototype system that identifies and matches similar invoices based on their content and structure.

## ✨ Objective

The objective of this assignment is to develop a system that automatically categorizes incoming invoices by matching them to existing templates or previously processed invoices.

## 🪧 Demo 
https://github.com/user-attachments/assets/6b723d81-5e15-4c42-86d6-d1b58d076a43



## 🚀 Features

- **Document Representation**: Extract text content from PDFs using `PyPDF2`.
- **Feature Extraction**: Extract relevant features such as keywords, invoice numbers, dates, amounts, etc., using `spaCy` and regex.
- **Similarity Calculation**: Implement similarity metrics like Cosine Similarity using `scikit-learn`.
- **Database Integration**: Maintain an in-memory database of existing invoices and find the most similar invoice for any new incoming invoice.
- **Streamlit Interface**: A simple and intuitive web interface to upload PDF files and get the most similar existing invoice.


## 📄 Usage


### Steps to Create and Use the Virtual Environment

1. **Create the virtual environment**:
    ```bash
    python -m venv venv
    ```

2. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

### Run the Application

1. Upload a PDF file using the Streamlit file uploader.
2. The app extracts the text and features from the PDF.
3. It compares the uploaded invoice with existing invoices in the database.
4. The most similar invoice and the similarity score are displayed.



