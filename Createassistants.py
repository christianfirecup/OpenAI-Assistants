from openai import OpenAI
from dotenv import load_dotenv
import os

api_key = os.getenv("OPENAI_API_KEY")
load_dotenv()

client = OpenAI(api_key=api_key)
def createas(names, instructions1, tools1, model1 ):
    assistant = client.beta.assistants.create(
        name= names,
        instructions= instructions1,
        tools= tools1,
        model= model1





    )
    return assistant
if __name__ == "__main__":
    createas("ForgeGPT", "You are a Documentation handler for the forge minecraft docs", [{"type": "code_interpreter"}], "gpt-4-1106-preview")

