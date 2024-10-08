# 📰 News Analyser

**News Analyser** is a Streamlit-based web app that allows users to input multiple news article URLs, process their content, and answer user queries based on the analyzed articles. The app utilizes **OpenAI's GPT model** via LangChain to provide answers with relevant sources.

## Features

- **Analyze Multiple News URLs**: Input up to 3 URLs to extract and process information from articles.
- **Question Answering with Sources**: Ask questions about the content of the news articles and get answers with citations.
- **Persistent Index**: The app saves the processed data into a local FAISS index for faster responses to subsequent queries.
- **Simple and Intuitive UI**: Built using Streamlit, the app offers a clean and user-friendly interface.

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) (for the web interface)
- **Backend**: [LangChain](https://langchain.com/) (for LLM-based question answering)
- **Vector Storage**: [FAISS](https://github.com/facebookresearch/faiss) (for fast document embeddings retrieval)
- **LLM**: [OpenAI GPT](https://openai.com/)
- **Embeddings**: OpenAI Embeddings (for document and query vectorization)

## Requirements

- Python 3.8+
- Streamlit
- LangChain
- FAISS
- OpenAI API Key

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/News_Analyser.git
    cd news-researcher
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Add your OpenAI API key**:

    Create a file called `ApiKey.py` in the project root directory and add your OpenAI API key as follows:

    ```python
    openapi_key = "your-openai-api-key-here"
    ```

## Usage

1. **Run the app**:

    After setting up the environment, run the app locally:

    ```bash
    streamlit run main.py
    ```

2. **Interact with the App**:

    - Open the app in your browser at `http://localhost:8501`.
    - Paste up to 3 news URLs into the sidebar's input fields.
    - Click **"Analyze"** to process the articles.
    - Once the analysis is complete, ask a question in the main input field, and the app will generate an answer along with relevant sources.

## Project Structure

```bash
.
├── app.py              # Main application file
├── ApiKey.py           # Contains OpenAI API key
├── requirements.txt    # Python dependencies
├── faiss_index         # Directory where FAISS index is saved (auto-created)
└── README.md           # Project documentation
