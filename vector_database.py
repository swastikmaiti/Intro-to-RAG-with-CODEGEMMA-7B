# %% [markdown]
# #### Import libraries

# %%
from datasets import load_dataset,load_from_disk
from qdrant_client import models,QdrantClient
from sentence_transformers import SentenceTransformer



# %% [markdown]
# #### Load Dataset

# %%
raw_datasets = load_dataset('neulab/conala',trust_remote_code=True)

# %%
dataset = raw_datasets['train']



# %% [markdown]
# ##### Coverting hugging-face dataset to pandas

# %%
df_pandas = dataset.to_pandas()
df_pandas = df_pandas.dropna()   # drop rows null values

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
            vector=encoder.encode(doc['intent']+" "+doc['rewritten_intent']).tolist(),
            payload=doc
        )for idx,doc in enumerate(df_dict)
    ]
)
