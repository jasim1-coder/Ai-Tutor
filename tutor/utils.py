from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')


def get_ai_response(prompt):
    response = generator(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']