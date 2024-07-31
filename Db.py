from Helper import *

class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, file_name, invoice_features):
        self.invoices.append({'file_name': file_name, 'features': invoice_features})

    def find_most_similar(self, invoice_features):
        features_list = [invoice['features'] for invoice in self.invoices]
        invoice_vectors = vectorize_features(features_list + [invoice_features])
        similarities = calculate_similarity(invoice_vectors[-1:], invoice_vectors[:-1])
        most_similar_index = similarities.argmax()
        most_similar_invoice = self.invoices[most_similar_index]
        return most_similar_invoice['file_name'], similarities[0, most_similar_index]
    

def process_invoice(file_path, database):
    text = extract_text_from_pdf(file_path)
    features = extract_features(text)
    
    # Add structural analysis 
    layout_features = extract_layout_features(file_path)
    features['layout'] = layout_features

    most_similar_file, similarity_score = database.find_most_similar(features)
    return most_similar_file, similarity_score