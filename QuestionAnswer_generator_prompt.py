import openai
import csv

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Set up the OpenAI API client
openai.api_key = api_key

def generate_questions_and_answers(user_text):
    # Generate questions based on user input
    prompt = f"Generate questions based on the following text: '{user_text}'"
    question_response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )
    generated_questions = question_response.choices[0].text.strip()

    # Generate answers to the generated questions
    answer_prompt = f"Answer the following questions:\n{generated_questions}\nUser Text: {user_text}\n"
    answer_response = openai.Completion.create(
        engine="davinci",
        prompt=answer_prompt,
        max_tokens=300,
        temperature=0.7,
    )
    generated_answers = answer_response.choices[0].text.strip()

    return generated_questions, generated_answers

# Read user input text from keyboard
user_input_text = input("Enter the text for generating questions and answers: ")

# Generate relevant questions and answers
generated_questions, generated_answers = generate_questions_and_answers(user_input_text)

# Print the generated questions and answers
print("Generated Questions:")
print(generated_questions)

print("\nGenerated Answers:")
print(generated_answers)

# Save the results to a CSV file
csv_filename = "generated_qa_results.csv"
with open(csv_filename, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Generated Questions", "Generated Answers"])
    csv_writer.writerow([generated_questions, generated_answers])

print(f"Results saved to {csv_filename}")
