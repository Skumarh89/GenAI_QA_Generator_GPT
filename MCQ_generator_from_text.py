import openai
import csv

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Set up the OpenAI API client
openai.api_key = api_key

def generate_mcq(user_text):
    # Generate a relevant question stem based on user input
    question_prompt = f"Generate a relevant multiple-choice question based on the following text:\n'{user_text}'"
    question_response = openai.Completion.create(
        engine="davinci",
        prompt=question_prompt,
        max_tokens=300,
        temperature=0.6,
    )
    generated_question_stem = question_response.choices[0].text.strip()

    # Generate distractors (incorrect options)
    options_prompt = f"Options:\n- {generated_question_stem}\n"
    options_response = openai.Completion.create(
        engine="davinci",
        prompt=options_prompt,
        max_tokens=150,
        temperature=0.6,
    )
    generated_options = options_response.choices[0].text.strip().split('\n')[1:]

    # Extract the key (correct answer) from the generated question stem
    key = generated_options[0].replace('-', '').strip()

    # Format the MCQ options
    mcq_options = [key] + generated_options[1:]
    mcq_options = [f"{chr(65 + i)}. {option}" for i, option in enumerate(mcq_options)]

    return generated_question_stem, mcq_options

# Read user input text from keyboard
user_input_text = input("Enter the input text: ")

# Generate MCQ from user input
generated_question_stem, mcq_options = generate_mcq(user_input_text)

# Print the generated MCQ
print("\nGenerated Question Stem:")
print(generated_question_stem)

print("\nGenerated Options:")
for option in mcq_options:
    print(option)

# Save results to a CSV file
csv_filename = "generated_mcq.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Generated Question Stem", "MCQ Options"])
    csv_writer.writerow([generated_question_stem] + mcq_options)

print(f"\nResults saved to '{csv_filename}'")
