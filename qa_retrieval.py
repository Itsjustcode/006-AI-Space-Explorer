from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch
import re

# Load the retrieval and generation models
retrieval_model = SentenceTransformer("sentence-transformers/msmarco-MiniLM-L-6-v3")
generation_model = pipeline("text2text-generation", model="google/flan-t5-large", device=0)

# Function to clean and chunk the document
def read_and_chunk_document(file_path, max_words=200):
    """
    Reads the content of the document, cleans unnecessary info, and splits it into manageable chunks.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Clean text: Remove URLs, email addresses, and extra spaces
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)  # Remove URLs
    text = re.sub(r"\S+@\S+\.\S+", "", text)  # Remove email addresses
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces and newlines

    # Split text into word chunks
    words = text.split()
    chunks = [" ".join(words[i:i + max_words]) for i in range(0, len(words), max_words)]
    return chunks

# Main retrieval and generation function
def ask_question(query, document_text, embeddings, top_k=2, max_tokens=512):
    """
    Retrieve relevant content and generate an answer for the user's query.
    """
    # Encode the user query
    query_embedding = retrieval_model.encode(query, convert_to_tensor=True)

    # Compute cosine similarity between the query and document embeddings
    similarities = util.pytorch_cos_sim(query_embedding, embeddings)
    top_indices = torch.topk(similarities, k=top_k).indices[0].tolist()

    # Retrieve the most relevant chunks
    retrieved_chunks = [document_text[i] for i in top_indices]
    combined_context = " ".join(retrieved_chunks)

    # Truncate the context to fit within the model's token limit
    truncated_context = " ".join(combined_context.split()[:max_tokens // 2])

    # Debugging: Print retrieved chunks and input to the generation model
    print(f"\nRetrieved Chunks: {retrieved_chunks}")
    input_text = f"Based on the following context:\n{truncated_context}\n\nQuestion: {query}"
    print(f"\nInput to Generation Model:\n{input_text}")

    # Generate an answer using the retrieved chunks and query
    generated_answer = generation_model(
        input_text,
        max_length=150,
        num_return_sequences=1,
        do_sample=True,
        temperature=0.7
    )

    # Return the generated answer
    return generated_answer[0]['generated_text']


def main():
    # File path to the scraped document
    file_path = "Selected_Document.txt"

    # Step 1: Read and chunk the document
    print("Loading and processing document...")
    document_text = read_and_chunk_document(file_path)

    # Step 2: Generate embeddings for the chunks
    print("Generating embeddings for document chunks...")
    embeddings = retrieval_model.encode(document_text, convert_to_tensor=True)

    # Step 3: Start an interactive loop for user queries
    print("Ask any question related to the document. Type 'exit' to quit.")
    while True:
        query = input("\nYour Question: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break
        
        # Retrieve and generate an answer
        answer = ask_question(query, document_text, embeddings)
        print(f"\nAnswer: {answer}")


if __name__ == "__main__":
    main()
