import openai
import csv

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Set up the OpenAI API client
openai.api_key = api_key

# Read user input from the keyboard
input_text = input("Enter the text for which you want to generate questions: ")

# Define a prompt to instruct the model to generate questions
prompt = f"Generate questions based on the following text: '{input_text}'"

# Generate questions using the OpenAI GPT-3 API
response = openai.Completion.create(
    engine="davinci",  # You can experiment with different engines
    prompt=prompt,
    max_tokens=50,  # Adjust the max tokens as needed
    temperature=0.7,  # Adjust the temperature for randomness
)

# Extract and print the generated questions
generated_questions = response.choices[0].text.strip()
print("Generated Questions:")
print(generated_questions)

# Save the generated questions to a CSV file
csv_filename = "generated_questions.csv"
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Generated Questions"])
    csv_writer.writerow([generated_questions])

print(f"Generated questions saved to {csv_filename}")
