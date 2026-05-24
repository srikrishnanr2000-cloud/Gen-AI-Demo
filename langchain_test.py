import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

os.environ["USER_AGENT"] = "PromptingAIApp/1.0"

# Load File

loader = TextLoader("prompting_notes.txt")

documents = loader.load()

print("Prompting Documents Loaded Successfully")


# Split 
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print(f"Total Prompt Chunks Created: {len(chunks)}")

# Create Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Prompting Embeddings Model Loaded")

# Store in ChromaDB
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./prompting_chroma_db"
)

print("Prompting Data Stored in ChromaDB")

# Search 
query = "What is chain of thought prompting?"

results = db.similarity_search(query, k=2)

print("\nPrompting Search Results:\n")

for i, result in enumerate(results):
    print(f"Result {i+1}:")
    print(result.page_content)
    print("-" * 50)