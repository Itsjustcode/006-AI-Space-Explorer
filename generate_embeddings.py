from sentence_transformers import SentenceTransformer
import os

def read_document(file_path):
    """
    Reads the content of the given file and returns it as a string.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def chunk_text(text, max_words=200):
    """
    Splits the given text into chunks of up to max_words.
    """
    words = text.split()
    chunks = [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]
    return chunks

def generate_embeddings(chunks, model_name="sentence-transformers/msmarco-MiniLM-L-6-v3"):
    """
    Generates embeddings for each chunk of text using the specified model.
    """
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, convert_to_tensor=True)
    return embeddings

def main():
    # File path to the document
    file_path = "Selected_Document.txt"

    # Step 1: Read the content of the document
    try:
        document_text = read_document(file_path)
    except FileNotFoundError as e:
        print(e)
        return

    # Step 2: Split the document into manageable chunks
    text_chunks = chunk_text(document_text)

    # Step 3: Generate embeddings for each chunk
    print("Generating embeddings...")
    embeddings = generate_embeddings(text_chunks)

    # Step 4: Store embeddings and their associated text in a dictionary
    embedding_dict = {f"Chunk {i+1}": {"text": chunk, "embedding": embedding}
                      for i, (chunk, embedding) in enumerate(zip(text_chunks, embeddings))}

    # Output a confirmation
    print(f"Processed {len(text_chunks)} text chunks and stored their embeddings.")

    # Example: Print the first chunk and its embedding shape
    print(f"\nExample Chunk: {embedding_dict['Chunk 1']['text'][:100]}...")
    print(f"Embedding Shape: {embedding_dict['Chunk 1']['embedding'].shape}")

    return embedding_dict

if __name__ == "__main__":
    embedding_data = main()
