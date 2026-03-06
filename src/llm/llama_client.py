from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from src.config.settings import HF_TOKEN

def get_llm():
    llm = HuggingFaceEndpoint(
        repo_id="meta-llama/Llama-3.1-8B-Instruct",
        huggingfacehub_api_token=HF_TOKEN,
            # streaming=True,
    )
    
    return ChatHuggingFace(llm=llm)