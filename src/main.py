import chainlit as cl
from linkupInstance import LinkupInstance
from gemini import Gemini

linkup = LinkupInstance()
gemini = Gemini()

chat = None

@cl.on_message
async def main(message: cl.Message):
    linkup_result = linkup.search(query=message.content)
    query = f"""
You're an AI assistant with access to the web, respond to this question in a clear a concise with the following ressources.
No header, no need to respond to this prompt.
Give your sources.
question: {message.content}
resources: {linkup_result}
"""
    response = await gemini.send(query)
    print("user message:", message.content)
    print("linkup result:", linkup_result)
    print("query:", query)
    print("response:", response)
    response = "Gemini + Linkup answer:\n" + response
    response_message = cl.Message(content=response)
    await response_message.send()

    response_nohelp = await gemini.send(message.content)
    response_nohelp = "Gemini answer:\n" + response_nohelp
    response_nohelp_message = cl.Message(content=response_nohelp)
    await response_nohelp_message.send()
    