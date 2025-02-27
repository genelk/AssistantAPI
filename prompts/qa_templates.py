"""
Prompt templates for document question answering.
"""

def get_basic_qa_template() -> str:
    """Get a basic prompt template for document Q&A.
    
    Returns:
        Formatted prompt template
    """
    template = """
    Please answer the following question based only on the information provided in the document:
    
    QUESTION: {question}
    
    DOCUMENT:
    ```
    {document_text}
    ```
    
    Provide a direct answer to the question using only information found in the document.
    If the answer cannot be determined from the document, clearly state this.
    When possible, cite specific sections or quotes from the document to support your answer.
    """
    
    return template


def get_factual_qa_template() -> str:
    """Get a prompt template for factual document Q&A.
    
    Returns:
        Formatted prompt template
    """
    template = """
    Answer the following factual question based exclusively on the information provided in the document:
    
    QUESTION: {question}
    
    DOCUMENT:
    ```
    {document_text}
    ```
    
    Your answer should:
    1. Provide only facts explicitly stated in the document
    2. Quote directly from the document when possible
    3. Include the location (page, paragraph, section) where the information was found
    4. State clearly if the information is not found in the document
    
    Focus on accuracy and precision, avoiding any speculation or information not provided in the document.
    """
    
    return template


def get_multi_document_qa_template() -> str:
    """Get a prompt template for Q&A across multiple documents.
    
    Returns:
        Formatte
