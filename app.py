import gradio as gr
import vector_database
from vector_database import qdrant,encoder


import os
ollama_base_url = os.getenv("OLLAMA_BASE_URL")

from ollama import Client
client = Client(host=ollama_base_url)

stream = client.chat(
    model='codegemma',
    messages=[{'role': 'user', 'content': 'write a 1 line code?'}],
    stream=True,
    options={
    'temperature': 0
  }  
)

print("Dummy Test Begins")
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
print("Dummy Test Ends")




chat_template = "User Query: {user_query}\nBelow are some examples of previous conversations.\nQuery: {query1} Solution: {solution1}\nQuery: {query2} Solution: {solution2}\nYou may use the above examples for reference only. Create your own solution and provide only the solution"
print(chat_template)

def response_generator(user_prompt, temperature):
    print("Query: ",user_prompt)

    hits = qdrant.search(
        collection_name='conala',
        query_vector=encoder.encode(user_prompt).tolist(),
        limit=3
        )   
    search_results = [hit.payload for hit in hits]

    query1 = search_results[0]['rewritten_intent']
    solution1 = search_results[0]['snippet']
    query2 = search_results[1]['rewritten_intent']
    solution2 = search_results[1]['snippet']
    prompt = f'{chat_template.format(user_query=user_prompt,query1=query1,solution1=solution1,query2=query2,solution2=solution2)}'
    stream = client.chat(
        model='codegemma',
        messages=[{'role': 'user', 'content': prompt}],
        stream=True,
        options={
        'temperature': temperature
        }   
    )

    output = ""
    for chunk in stream:
        output+=chunk['message']['content']
        yield output


with gr.Blocks() as demo:
    
    gr.Markdown(
    """
    # Codegemma 7B

    ## A simple RAG system.

    - ***LLM:*** Codegemma 7B
    - ***VectorDB:*** Qdrant
    - ***Dataset:*** CoNaLa 

    """)

    
    input_box = gr.Textbox(autoscroll=True,visible=True,label='User',info="Enter a query.",value="create a list of n numbers in python.")
    temp = gr.Slider(minimum=0,maximum=1,label='Temperature',value=0)
    output_box = gr.Textbox(autoscroll=True,max_lines=30,value="Output",label='Assistant')
    gr.Interface(fn=response_generator, inputs=[input_box,temp], outputs=[output_box],
                 delete_cache=(20,10),
                 allow_flagging='never')
    
demo.queue()
demo.launch()


