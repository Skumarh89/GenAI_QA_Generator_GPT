import openai
import csv

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Set up the OpenAI API client
openai.api_key = api_key

def generate_mcq(user_text):
    # Generate relevant questions based on user input
    prompt = f"Generate a multiple-choice question based on the following text:\n'{user_text}'"
    question_response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
    )
    generated_question = question_response.choices[0].text.strip()

    # Generate distractors (incorrect options)
    options_prompt = f"Options:\n- {generated_question}\n"
    options_response = openai.Completion.create(
        engine="davinci",
        prompt=options_prompt,
        max_tokens=100,
        temperature=0.7,
    )
    generated_options = options_response.choices[0].text.strip().split('\n')[1:]

    # Extract the key (correct answer) from the generated question
    key = generated_options[0].replace('-', '').strip()

    # Format the MCQ options
    mcq_options = [key] + generated_options[1:]
    mcq_options = [f"{chr(65 + i)}. {option}" for i, option in enumerate(mcq_options)]

    return generated_question, mcq_options

# Read user input from the keyboard
user_input_text = input("Enter the text for generating MCQ: ")

# Generate MCQ from user input
generated_question, mcq_options = generate_mcq(user_input_text)

# Print the generated MCQ
print("Generated Question:")
print(generated_question)

print("\nGenerated Options:")
for option in mcq_options:
    print(option)

# Save the results in a CSV file
csv_filename = "generated_mcq.csv"
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Generated Question", "Options"])
    csv_writer.writerow([generated_question] + mcq_options)

print(f"Results saved to {csv_filename}")
