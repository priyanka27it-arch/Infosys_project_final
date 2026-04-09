# AI Based Document Search and Knowledge Retrieval with Conversational Interface

## Project Overview
This project is an AI-powered application that allows users to upload documents and interact with them through a conversational interface. It uses Retrieval-Augmented Generation (RAG) to provide accurate and context-based answers from the uploaded documents.

Unlike traditional language models that may generate incorrect or unrelated answers, this system retrieves relevant information from the documents and generates responses based only on that data, improving accuracy and reliability.

---

## Features
- Upload documents in PDF or text format
- Ask questions based on uploaded documents
- Context-aware response generation
- Retrieval-Augmented Generation (RAG) implementation
- Maintains chat history
- Efficient search using vector database

---

## Technologies Used
- Python
- Reflex framework
- LangChain
- Vector database (Chroma or FAISS)
- Large Language Model (local or API-based)

---

## How It Works

1. Document Upload  
   Users upload PDF or text files which are stored in the documents folder.

2. Text Processing  
   Documents are divided into smaller chunks to improve retrieval performance.

3. Embedding  
   Each chunk is converted into a vector representation.

4. Vector Storage  
   These embeddings are stored in a vector database for efficient search.

5. User Query  
   The user enters a question through the chat interface.

6. Retrieval  
   Relevant document chunks are retrieved based on similarity.

7. Response Generation  
   The language model generates an answer using only the retrieved content.

---

## How to Run the Project

Step 1: Install dependencies
pip install -r requirements.txt
Step 2: Run the application
reflex run
Step 3: Open in browser
http://localhost:3000


---

## Advantages
- Provides accurate answers based on user documents
- Reduces hallucination in AI responses
- Works with private and custom data
- Modular and scalable design

---

## Limitations
- Performance depends on document quality
- Large documents may increase processing time
- Requires proper embedding model for best results

---

## Future Enhancements
- Support for more file formats
- Improved user interface
- Deployment on cloud platforms
- Multi-user support
- Voice-based interaction

---

## Conclusion
This project demonstrates the practical implementation of Retrieval-Augmented Generation for building intelligent document-based question answering systems. It combines AI, backend processing, and frontend interaction into a unified application.
