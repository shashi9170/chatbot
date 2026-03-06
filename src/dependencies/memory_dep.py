from src.database.postgres_memory import get_memory

def get_memory_context():
    memory_ctx = get_memory()
    
    with memory_ctx as memory:
        memory.setup()
        yield memory