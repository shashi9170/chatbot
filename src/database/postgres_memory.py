from langgraph.checkpoint.postgres import PostgresSaver
from src.config.settings import DATABASE_URL

def get_memory():
    # Returns the context manager (not entered yet)
    return PostgresSaver.from_conn_string(DATABASE_URL)