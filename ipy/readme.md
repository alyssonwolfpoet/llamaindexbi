# LlamaIndex - Private Setup

## Overview

This README provides instructions for setting up a private LlamaIndex environment using GPT4ALL and HuggingFace embeddings to ingest and analyze Chapter 3 of the 2023 IPCC Climate Report on Oceans and Coastal Ecosystems. This setup allows for efficient local querying of the report, leveraging LlamaIndex with local models. Inspired by PrivateGPT, this guide details the use of CPU and GPU setups for optimal performance.

## Prerequisites

1. **Python**: Ensure you have Python installed. Python 3.10 is recommended.
2. **Colab/Local Environment**: You can use Google Colab or a local environment. If using Colab, switch to a GPU instance for better performance.

## Setup Instructions

### 1. Install Dependencies

Install the required Python packages using pip:

```bash
pip install pymupdf pygpt4all sentence_transformers accelerate
pip install -U git+https://github.com/jerryjliu/llama_index.git
```

### 2. Download Models and Data

- **Download GPT4ALL Model**: Follow instructions to download the GPT4ALL model. This will be used for text generation.
- **Download IPCC Climate Report**: Obtain Chapter 3 of the 2023 IPCC Climate Report, which is 172 pages long.
- **Extra Packages**: The installation commands above will handle this.

### 3. Document Setup

Load and prepare the document using PyMuPDFReader:

```python
from llama_index import SimpleDocumentLoader

# Load the climate report PDF
document_loader = SimpleDocumentLoader("path/to/climate_report_chapter3.pdf")
documents = document_loader.load()
```

### 4. Setup LlamaIndex on CPU

Configure LlamaIndex using GPT4ALL with CPU:

```python
from llama_index.llm_predictor import LLMPredictor
from pygpt4all import GPT4ALL

# Initialize GPT4ALL model
gpt4all_model = GPT4ALL(model_name="path/to/gpt4all_model")

# Wrap the model in LLMPredictor
llm_predictor = LLMPredictor(model=gpt4all_model)
```

### 5. Setup Embeddings

Download and use HuggingFace embeddings:

```python
from sentence_transformers import SentenceTransformer

# Load the embeddings model
embed_model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
```

### 6. Setup Service Context

Initialize the service context:

```python
from llama_index import ServiceContext

service_context = ServiceContext.from_defaults(
    chunk_size=512,
    llm_predictor=llm_predictor,
    embed_model=embed_model
)
```

Set the global service context:

```python
from llama_index import set_global_service_context

set_global_service_context(service_context)
```

### 7. Construct Index and Query

Create the index and perform queries:

```python
from llama_index import GPTVectorStoreIndex

# Construct index
index = GPTVectorStoreIndex.from_documents(documents)
index.storage_context.persist(persist_dir="./storage")

# Optional: Load the index if already saved
index.load(persist_dir="./storage")

# Querying the index
response = index.query("What are the key findings on coastal ecosystems?")
print(response)
```

### 8. (Optional) GPU Setup

For improved performance, especially with large models, use a GPU. Follow these steps:

- Ensure CUDA is installed if using a local GPU.
- Modify the LlamaIndex setup to utilize GPU resources.

Example GPU setup with HuggingFace model:

```python
from llama_index.llm_predictor import HuggingFaceLLMPredictor

# Setup HuggingFace model on GPU
hf_predictor = HuggingFaceLLMPredictor(
    max_input_size=2048,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.25, "do_sample": False},
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="Writer/camel-5b-hf",
    model_name="Writer/camel-5b-hf",
    device_map="auto",
    tokenizer_kwargs={"max_length": 2048},
    model_kwargs={"torch_dtype": torch.bfloat16}
)
```

## Resources

- **LlamaIndex Documentation**: [LlamaIndex Documentation](https://docs.llamaindex.ai/en/stable/module_guides/models/llms/local/)
- **HuggingFace Models**: [HuggingFace Model Hub](https://huggingface.co/models)
- **PrivateGPT Inspiration**: Explore how PrivateGPT uses local models for private querying.

## Troubleshooting

If you encounter issues:

1. Verify all dependencies are correctly installed.
2. Check that the paths to models and data are correct.
3. Ensure your environment (CPU/GPU) is properly configured.

Feel free to open an issue or seek support in relevant forums if problems persist.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy querying!