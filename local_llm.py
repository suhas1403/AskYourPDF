from llama_cpp import Llama

def load_llm():
    return Llama(
        model_path="models/mistral-7b-instruct-v0.1.Q4_K_M.gguf",
        n_ctx=2048,
        n_threads=8,
        n_gpu_layers=20
    )

def generate_answer(llm, query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""[INST] You are a helpful assistant. Use the following context to answer the question.
Context: {context}
Question: {query} [/INST]"""

    output = llm(prompt, max_tokens=512, stop=["</s>"])
    return output["choices"][0]["text"].strip()
