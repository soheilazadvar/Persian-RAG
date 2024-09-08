from llama_index.core.tools import QueryEngineTool
from llama_index.core.selectors import PydanticSingleSelector
from llama_index.core.query_engine.router_query_engine import RouterQueryEngine

# Initialize Query Engine
def initialize_query_engine(vector_index):
    vector_query_engine = vector_index.as_query_engine(similarity_top_k=5)
    vector_tool = QueryEngineTool.from_defaults(
        query_engine=vector_query_engine,
        description="Useful for retrieving specific context from the Document."
    )
    return RouterQueryEngine(
        selector=PydanticSingleSelector.from_defaults(),
        query_engine_tools=[vector_tool],
        verbose=True,
    )
