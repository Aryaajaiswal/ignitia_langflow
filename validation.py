from langchain_groq import ChatGroq

def validation_agent(concept):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )
    prompt = f"Validate the market viability for: {concept}"
    return llm.invoke(prompt).content
