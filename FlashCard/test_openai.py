import openai

openai.api_key = "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"

subject_text = "This is a sample paragraph about artificial intelligence. It is a field of computer science that aims to create intelligent machines."

response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Generate 2 questions and answers based on this paragraph:\n\n{subject_text}\n\nFormat: Question: <question> Answer: <answer>",
    max_tokens=1000,
    n=1,
    temperature=0.7
)

print(response.choices[0].text.strip())
