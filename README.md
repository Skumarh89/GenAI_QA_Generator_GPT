# GenAi_QA_Generator_GPT

### Multiple-Choice Question (MCQ) Generator

This Python script generates multiple-choice questions (MCQs) based on user-provided input text using OpenAI's GPT-3 API. It generates a relevant MCQ stem along with distractors (incorrect options) for the question.

### Prerequisites

Before running the script, you need to have the following:

- Python 3.x installed
- OpenAI API key (Sign up for access at https://beta.openai.com/signup/)

### Setup

- Clone this repository or download the script.
  ```bash
  git clone https://github.com/Skumarh89/GenAi_QA_Generator_GPT.git
  cd GenAi_QA_Generator_GPT
  ```


- Install the required libraries:
   ```bash
   pip install openai
   ```
- Install the required packages using the following command:
  ```bash
  pip install -r requirements.txt
  ```

### Usage

- Run the script using the following command:
    ```bash
    python mcq_generator.py
    ```
- Enter the text for which you want to generate questions and answers when prompted.

- The script will generate relevant questions and answers using OpenAI's GPT-3 API and display them on the console.

- The generated questions and answers will also be saved to a CSV file named generated_qa_results.csv in the same directory.
   
