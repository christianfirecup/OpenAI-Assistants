from openai import OpenAI
import Createassistants as c
from dotenv import load_dotenv
import os

api_key = os.getenv("OPENAI_API_KEY")
load_dotenv()

client = OpenAI(api_key=api_key)


# assistant = c.createas("PythonGPT", "you are a insanely good python instructor that answers any python problem in the most educational way possible ", [{"type": "code_interpreter"}], "gpt-4-1106-preview")
thread = client.beta.threads.create()
print(thread)
print("asst_Mv3MzfjZUw4pIUT8jvgWwbMP")

received = False
chatthread = True
numofmessage = 0
while chatthread:
    ask = input("what is your question? ")
    chatthread = False
    received = False

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=ask

    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_Mv3MzfjZUw4pIUT8jvgWwbMP",


    )
    while not received:

        # Retrieve the latest run status
        result = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )

        # Check if the run is completed
        if result.status == 'completed':

            messages = client.beta.threads.messages.list(thread_id=thread.id)
            for message in messages.data:
                role = message.role
                content = message.content[numofmessage].text.value
                print(f"{role.capitalize()}: {content}")
                chatthread = True
                received = True
                var = numofmessage + 1
