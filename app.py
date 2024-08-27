import streamlit as st
from news_summarization import prediction_pipeline
from news_research import data_load_split, create_save_embedding, info_loader

file_path = "faiss_store_openai.pkl"

def page_home():
    st.title("NewsLLM")
    st.write("Welcome to the LLM Powered Era!")

def page_news_summarization_tool():
    st.header("News Summarization GPT")
    user_input = st.text_area("Enter Text to Summarize:")
    button = st.button("Generate Summary")

    if user_input and button:
        summary = prediction_pipeline(user_input)
        st.markdown("### Summary:")
        st.write(summary)

def page_news_research_tool():
    st.title("News Research Tool  📈")
    st.markdown("## News Article URLs")
    urls = []
    for i in range(3):
        url = st.text_input(f"URL {i+1}")
        urls.append(url)
    process_url_clicked = st.button("Process URLs")
    main_placeholder = st.empty()
    if process_url_clicked:
        main_placeholder.text("Data Loading and Splitting...Started...✅✅✅")
        docs = data_load_split(urls)
        main_placeholder.text("Embedding Vector Started Building...✅✅✅")
        size = create_save_embedding(docs)
        st.write("Embedding Size",size)
        main_placeholder.text("Vectors Stored Successfully...✅✅✅")
        query = main_placeholder.text_input("Question: ")
        if query:
            result, sources = info_loader(file_path,query)
            st.header("Answer")
            st.write(result["answer"])
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")
                for source in sources_list:
                    st.write(source)





st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to",("Home","News Summarization","News Research"))

if page == "Home":
    page_home()
elif page == "News Summarization":
    page_news_summarization_tool()
elif page == "News Research":
    page_news_research_tool()