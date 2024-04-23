# %% [markdown]
# #### Import libraries

# %%
from datasets import load_dataset,load_from_disk
from qdrant_client import models,QdrantClient
from sentence_transformers import SentenceTransformer
from scipy.stats import rv_discrete

# %%
import os
dirname = os.getcwd()
# Construct the path to your dataset file
dataset_path = os.path.join(dirname, r'CoNaLa\content\CoNaLa')

# %% [markdown]
# #### Load Dataset

# %%
raw_datasets = load_from_disk(dataset_path)
raw_datasets = raw_datasets.shuffle(seed=42)


# %%
dataset = raw_datasets['train']



# %% [markdown]
# ##### Coverting hugging-face dataset to pandas

# %%
df_pandas = dataset.to_pandas()

# %%
# dictionary is easy formatting for creating embedding
df_dict = df_pandas.to_dict(orient='records')

# %% [markdown]
# #### Creating Embedding and in-memory vector databse

# %%
encoder = SentenceTransformer('all-MiniLM-L6-v2') # model to create embedding

# %%
# create vector database client
qdrant = QdrantClient(":memory:") # creating in-memory Qdrant instance

# %%
# create collection
qdrant.recreate_collection(
    collection_name = 'conala',
    vectors_config = models.VectorParams(
        size = encoder.get_sentence_embedding_dimension(),
        distance = models.Distance.COSINE
    )
)

# %%
# vectorize
qdrant.upload_points(
    collection_name='conala',
    points=[
        models.PointStruct(
            id=idx,
            vector=encoder.encode(doc['intent']+". code: "+doc['snippet']).tolist(),
            payload=doc
        )for idx,doc in enumerate(df_dict)
    ]
)
