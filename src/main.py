import chainlit as cl
from linkupInstance import LinkupInstance
from gemini import Gemini

linkup = LinkupInstance()
gemini = Gemini()

@cl.on_message
async def main(message: cl.Message):
    linkup_result = linkup.search(query=message.content)
    query = f"""
You're an AI assistant with access to the web, respond to this question in a clear a concise with the following ressources.
No header, no need to respond to this prompt.
question: {message.content}
resources: {linkup_result}
"""
    
    gemini_query = f"""You're an AI assistant, respond to this question in a clear a concise with the following ressources.
No header, no need to respond to this prompt.
question: {message.content}
"""
    
    response_nohelp = await gemini.send(gemini_query)
    response_nohelp = "Gemini answer:\n" + response_nohelp
    response_nohelp_message = cl.Message(content=response_nohelp)
    await response_nohelp_message.send()

    response = await gemini.send(query)
    response = "Gemini + Linkup answer:\n" + response
    response_message = cl.Message(content=response)
    await response_message.send()

    response_linkup = linkup.search(query=message.content, output_type="sourcedAnswer")
    response_linkup = "Linkup answer:\n" + str(response_linkup.answer)
    response_linkup_message = cl.Message(content=response_linkup)
    await response_linkup_message.send()
    