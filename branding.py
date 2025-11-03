from langchain_groq import ChatGroq

def branding_agent(analysis):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )
    prompt = f"Create branding output for the following market analysis: {analysis}"
    return llm.invoke(prompt).content
