from llama_index.core.node_parser import SemanticSplitterNodeParser, SentenceSplitter


# Semantic Node Splitter

def create_node_splitter(embed_model):
    return SemanticSplitterNodeParser(
        buffer_size=4, breakpoint_percentile_threshold=95, embed_model=embed_model
    )