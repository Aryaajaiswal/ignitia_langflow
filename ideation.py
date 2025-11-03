from langchain_groq import ChatGroq

def ideation_agent(idea):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )
    prompt = f"Generate a refined startup concept for: {idea}"
    return llm.invoke(prompt).content
