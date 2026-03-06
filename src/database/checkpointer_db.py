from pymongo import MongoClient
from copy import deepcopy

from langgraph.checkpoint.base import BaseCheckpointSaver
from langchain_core.messages import messages_to_dict, messages_from_dict


class MongoCheckpointer(BaseCheckpointSaver):

    def __init__(
        self,
        uri="mongodb://localhost:27017",
        db_name="chatbot",
        collection_name="checkpoints"
    ):
        client = MongoClient(uri)
        self.collection = client[db_name][collection_name]

    # Load checkpoint
    def get_tuple(self, config):

        thread_id = config["configurable"]["thread_id"]

        doc = self.collection.find_one(
            {"thread_id": thread_id},
            sort=[("_id", -1)]
        )

        if not doc:
            return None

        checkpoint = doc["checkpoint"]
        metadata = doc["metadata"]

        state = checkpoint.get("channel_values", {})

        if "messages" in state:
            state["messages"] = messages_from_dict(state["messages"])

        return checkpoint, metadata

    # Save checkpoint
    def put(self, config, checkpoint, metadata, new_versions):

        thread_id = config["configurable"]["thread_id"]

        # deep copy so LangGraph state isn't modified
        checkpoint_copy = deepcopy(checkpoint)

        state = checkpoint_copy.get("channel_values", {})

        if "messages" in state:
            state["messages"] = messages_to_dict(state["messages"])

        self.collection.insert_one({
            "thread_id": thread_id,
            "checkpoint": checkpoint_copy,
            "metadata": metadata
        })

    # List checkpoints
    def list(self, config):

        thread_id = config["configurable"]["thread_id"]

        docs = self.collection.find({"thread_id": thread_id})

        results = []

        for doc in docs:

            checkpoint = doc["checkpoint"]
            metadata = doc["metadata"]

            state = checkpoint.get("channel_values", {})

            if "messages" in state:
                state["messages"] = messages_from_dict(state["messages"])

            results.append((checkpoint, metadata))

        return results