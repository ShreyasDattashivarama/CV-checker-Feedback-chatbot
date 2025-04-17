import openai
import os

# Set your API key here or use environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT_TEMPLATE = """
You are a helpful assistant that reviews resumes.
Analyze the following resume text and provide feedback in a friendly tone.
Highlight formatting, grammar, keyword usage, and alignment with the job description.

Resume:
\"\"\"{resume}\"\"\"

{job_section}

Response:
"""

def generate_feedback(resume_text, job_description=None):
    job_section = f"Job Description:\n{job_description}" if job_description else ""
    prompt = PROMPT_TEMPLATE.format(resume=resume_text, job_section=job_section)

    response = openai.ChatCompletion.create(
        model="gpt",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800
    )

    return response.choices[0].message.content.strip()
