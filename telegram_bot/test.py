from langchain_core.messages import HumanMessage
from langchain_mistralai.chat_models import ChatMistralAI

# If mistral_api_key is not passed, default behavior is to use the `MISTRAL_API_KEY` environment variable.
chat = ChatMistralAI(mistral_api_key="")

messages = [HumanMessage(content="knock knock")]
chat.invoke(messages)