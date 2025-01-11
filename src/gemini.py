import google.generativeai as genai
from env import GEMINI_APIKEY

class Gemini:
    genai.configure(api_key=GEMINI_APIKEY)

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])

    async def send(self, message):
        try:
            response = self.chat_session.send_message(message)
            return response._result.candidates[0].content.parts[0].text
        except:
            return "400"