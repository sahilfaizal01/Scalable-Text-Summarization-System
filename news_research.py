import os
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from api_config import get_secret


file_path = "faiss_store_openai.pkl"
llm = OpenAI(temperature=0.9, max_tokens=500, openai_api_key = get_secret())

def data_load_split(urls):
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    docs = text_splitter.split_documents(data)
    return docs 

def create_save_embedding(docs):
    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings(openai_api_key = get_secret())
    #vectorstore_openai = FAISS.from_documents(docs, embeddings)
    first_doc = docs[0].page_content
    embedding_size = len(embeddings.embed_documents([first_doc])[0])
    time.sleep(2)
    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        print("opened file")
        pickle.dump(vectorstore_openai, f)


def info_loader(file_path, query):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            sources = result.get("sources", "")
    return result, sources
