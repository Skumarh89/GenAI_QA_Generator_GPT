# GenAi_QA_Generator_GPT

### Multiple-Choice Question (MCQ) Generator
This repository contains a Python script that utilizes OpenAI's GPT-3 API to generate relevant Questions, Question-Answers from a given text input.
The repository contains a Python script that also generates multiple-choice questions (MCQs) based on input text. It generates a relevant MCQ stem along with distractors (incorrect options) for the question.

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
  pip install -r requirements_QA_Gen.txt
  ```

### Usage

- Run the script using the following command:
   ```bash
    python Question_generator_prompt.py #for Question generator
    ```
    ```bash
    python QuestionAnswer_generator_prompt.py #for Question-Answer generator
    ```
    ```bash
    python MCQ_generator_from_text.py #for MCQs
    ```
    ```bash
    python Multiple-Choice_Question_(MCQ)_geneartor_prompt.py #for MCQs
    ```
- Enter the text for which you want to generate questions and answers when prompted.

- The script will generate relevant Questions, Question-Answers, and MCQs using OpenAI's GPT-3 API and display them on the console.

- The generated QAs will also be saved to a CSV file named generated_qa_results.csv in the same directory.
   
