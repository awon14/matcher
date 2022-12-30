from django.apps import AppConfig
from sentence_transformers import SentenceTransformer
import pandas as pd


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    embedder = SentenceTransformer('all-MiniLM-L6-v2')

    # read the csv file
    df = pd.read_csv("api/NLP.csv", skipinitialspace=True)

    # this must be loaded when the api is up
    corpus = df["NLP Statements"].tolist()
    commands = df["Commands"].tolist()
    corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)
