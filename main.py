import os
import streamlit as st
import time
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from ApiKey import openapi_key

# Set up API Key for OpenAI
os.environ['OPENAI_API_KEY'] = openapi_key

# App Title
st.set_page_config(page_title="News Researcher", layout="centered")
st.title("📰 News Researcher")
st.markdown("Analyze multiple news sources to answer your questions with relevant citations.")

# Sidebar Input
st.sidebar.title("🔗 News URLs")
st.sidebar.markdown("Paste up to 3 news URLs to extract information from:")
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}", key=f"url_{i}")
    if url:
        urls.append(url)

# Button to trigger analysis
analyse_btn = st.sidebar.button("🧠 Analyze Sources")
faiss_index_path = "faiss_index"

# Placeholder for main content
main_placeholder = st.empty()

# Initialize the LLM
llm = OpenAI(temperature=0.9, max_tokens=500)

# User Input for Questions
query = main_placeholder.text_input("💬 Ask a Question about the News Articles", placeholder="Type your question here...")

# Show spinner during analysis
if analyse_btn:
    if len(urls) > 0 and any(urls):
        with st.spinner("Loading and analyzing news articles..."):
            loader = UnstructuredURLLoader(urls=urls)
            data = loader.load()

            # Split the data into smaller chunks for processing
            text_splitter = RecursiveCharacterTextSplitter(
                separators=['\n\n', '\n', '.', ','],
                chunk_size=1000
            )
            docs = text_splitter.split_documents(data)

            # Create embeddings and save them to FAISS index
            embeddings = OpenAIEmbeddings()
            vector_data = FAISS.from_documents(docs, embeddings)

            time.sleep(2)  # Simulating processing time for better UX

            # Save the index to a local directory
            vector_data.save_local(faiss_index_path)

        st.success("News articles analyzed successfully! You can now ask your question.")
    else:
        st.warning("Please provide at least one valid URL for analysis.")

# Handling query and loading saved index
if query:
    if os.path.exists(faiss_index_path):
        with st.spinner("Fetching the answer..."):
            # Reload embeddings object and the FAISS index
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.load_local(faiss_index_path, embeddings, allow_dangerous_deserialization=True)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())

            # Get the answer and sources
            result = chain({"question": query}, return_only_outputs=True)
            answer = result.get("answer", "No answer found.")
            sources = result.get("sources", "")

        # Display the answer
        st.header("🔍 Answer")
        st.write(answer)

        # Display the sources if available
        if sources:
            st.subheader("📄 Sources:")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(f"🔗 {source}")
    else:
        st.warning("Please analyze the URLs first before asking a question.")
