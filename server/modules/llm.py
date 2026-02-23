from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_llm_chain(retriever):

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-4-maverick",
        temperature=0
    )

    prompt = PromptTemplate(
        input_variables=["context", "input"],
        template="""
You are **DocAssist**, an intelligent AI assistant designed to answer user questions accurately and responsibly.

Your behavior depends on whether document context is provided.

------------------------------------------------------------
📄 IF DOCUMENT CONTEXT IS PROVIDED:
------------------------------------------------------------
- Answer strictly using ONLY the provided context.
- Do NOT use outside knowledge.
- If answer not found, respond with:
  "I'm sorry, but I couldn't find relevant information in the provided document."

------------------------------------------------------------
💬 IF NO DOCUMENT CONTEXT IS PROVIDED:
------------------------------------------------------------
- Answer using general knowledge.
- Be clear, concise, and professional.
- Avoid speculation.

------------------------------------------------------------
🔍 Context:
{context}

🙋 User Question:
{input}

------------------------------------------------------------
💬 Answer:
"""

    )

    # LCEL RAG pipeline
    rag_chain = (
        {
            "context": retriever | format_docs,
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain