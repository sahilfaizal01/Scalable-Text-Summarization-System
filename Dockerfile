FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  software-properties-common \
  git \
  && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git

COPY ./requirements.txt requirements.txt
COPY ./app.py app.py
COPY ./api_config.py api_config.py
COPY ./news_research.py news_research.py
COPY ./news_summarization.py news_summarization.py

RUN pip install -r requirements.txt 

EXPOSE 8501

ENTRYPOINT ["streamlit","run"]

CMD ["app.py"]