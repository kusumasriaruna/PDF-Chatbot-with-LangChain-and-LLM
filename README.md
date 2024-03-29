# Memory Chat-Bot
## Demo

https://github.com/kusumasriaruna/chatbot/blob/main/Architecture.jpg
https://github.com/kusumasriaruna/chatbot/blob/main/Architecture2.jpg


## Steps
1. Upload a PDF file
2. Ask questions about the PDF
3. Get answers from the PDF

## About
This is an LLM powered chatbot build using:
 - [Streamlit](https://streamlit.io/)
 - [LangChain](https://python.langchain.com/docs/get_started/introduction.html)
 - [OpenAI](https://openai.com/)

## Architecture
![Architecture](https://github.com/kusumasriaruna/chatbot/blob/main/Architecture.jpg)
![Architecture2](https://github.com/kusumasriaruna/chatbot/blob/main/Architecture2.jpg)

## How does it work?
#### Text Extraction: 
 - Extract text content from the provided PDF file.
#### Text Chunking: 
 - Split the extracted text into smaller, overlapping chunks of 1000 characters with a 200-character overlap between chunks.
 - Because OpenAI API has a limit of 2048 tokens per request.
#### Embedding Generation:
 - Generate embeddings (numerical representations) for each text chunk by using OpenAI API.
 - These embeddings capture the semantic meaning of the text.
#### Similarity Search: 
 - Compare the embeddings of text chunks with the user's query using a similarity metric.
 - Rank the text chunks based on their similarity to the query.
#### Output:
 - Utilize a Language Model (LLM) to process the ranked results.
 - Provide the user with relevant and ranked information based on the query and similarity search results.
#   c h a t b o t 
 
 
