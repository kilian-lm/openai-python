# git clone git@github.com:kilian-lm/openai-python.git
# hatch build


from dotenv import load_dotenv
import openai
from openai import OpenAI
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()


assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo-16k-0613"
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

message

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

run = client.beta.threads.runs.retrieve(
  thread_id=thread.id,
  run_id=run.id
)


messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

messages



assistant = client.beta.assistants.create(
  instructions="You are a personal math tutor. When asked a math question, write and run code to answer the question.",
  model="gpt-3.5-turbo-16k-0613",
  tools=[{"type": "code_interpreter"}]
)


run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
  instructions="Please address the user as Jane Doe. The user has a premium account."
)

thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "I need to solve the equation `3x + 11 = 14`. Can you help me?",
    }
  ]
)


run_steps = client.beta.threads.runs.steps.list(
  thread_id=thread.id,
  run_id=run.id
)


assistant = client.Assistant.create(
    name="Math Tutor",
    description="You are a personal math tutor. Write and run code to answer math questions.",
    training_data=[
        {
            "prompt": "What's 2 + 2?",
            "completion": "The answer is 4."
        },
        # Add more training examples if necessary
    ],
    settings={
        "tools": [{"type": "code_interpreter"}]
    },
    model='gpt-3.5-turbo-16k-0613'  # Replace with the actual model you are using
)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)

# Streaming:
print("----- streaming request -----")
stream = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": "How do I output all files in a directory using Python?",
        },
    ],
    stream=True,
)
for chunk in stream:
    if not chunk.choices:
        continue

    print(chunk.choices[0].delta.content, end="")
print()
