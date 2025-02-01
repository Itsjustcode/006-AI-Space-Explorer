# Reflection Report: AI-Powered Question Answering with SPHEREx Document

## Document Overview
The document used for querying is NASA's official page on the SPHEREx mission, which is a space telescope designed to map the entire sky in infrared light. The document provides insights into the mission's goals, scientific significance, and technical aspects.

## How the Program Works
This program processes a document, generates embeddings for different text chunks using the **sentence-transformers** library, and retrieves relevant content based on user queries using **cosine similarity**. The retrieved content is then used to generate an answer using **HuggingFace’s text generation model**.

## Five Key Questions to Understand the Program
1. **What is cosine similarity, and why is it used?**
   - Cosine similarity measures how similar two text embeddings are by computing the cosine of the angle between them. It helps find the most relevant text chunks for a user’s query.

2. **What is the role of sentence-transformers in this program?**
   - The **sentence-transformers** library is used to generate vector embeddings of the text chunks and user queries, making it possible to compare them and retrieve the most relevant information.

3. **How does the AI generate responses based on retrieved content?**
   - The program uses a **HuggingFace text generation model** to process the retrieved text and user query, crafting a human-readable response.

4. **Why is document chunking necessary?**
   - Large documents need to be split into smaller segments to ensure efficient searching and retrieval of relevant text.

5. **How does the system handle ambiguity in questions?**
   - The retrieval model selects the most relevant text chunks based on similarity scores, but sometimes multiple chunks may be needed to construct a full response.

## System Performance Analysis
### Retrieval Effectiveness
The system successfully retrieves relevant text chunks based on user queries. However, some responses could be more detailed if larger context windows were allowed.

### Quality of Generated Responses
The responses are mostly accurate but can sometimes be too brief. Improving prompt engineering for the text generation model could enhance the quality.

### Possible Improvements
- Increase the number of retrieved chunks to provide better context.
- Experiment with different text generation models for more detailed responses.
- Implement a ranking mechanism to prioritize the most relevant retrieved text.

## Example Queries and Responses

**Question: What does SPHEREx aim to discover about the universe?**  
**Answer:** The origins of our universe, galaxies within it, and life’s key ingredients in our own galaxy.  

**Question: How does SPHEREx work?**  
**Answer:** It relies on an entirely passive cooling system — no electricity or coolants are used during normal operations.  

**Question: How many infrared colors does SPHEREx map?**  
**Answer:** 102.  

**Question: What is inflation, and how does SPHEREx study it?**  
**Answer:** The universe increased in size by a trillion-trillionfold. Called inflation, this nearly instantaneous event took place almost 14 billion years ago, and its effects can be found today in the large-scale distribution of matter in the universe.  

**Question: How does SPHEREx contribute to our understanding of the Big Bang?**  
**Answer:** By mapping the distribution of more than 450 million galaxies, SPHEREx will help scientists improve our understanding of the physics behind this extreme cosmic event.  

## Conclusion
This project demonstrates how AI-powered retrieval and generation models can efficiently extract relevant information from large text sources. While effective, further refinements can enhance retrieval accuracy and response detail, making the system even more useful for research and exploration.
