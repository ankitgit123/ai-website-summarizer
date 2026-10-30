# AI Website Summarizer 🌐

An AI-powered application that extracts website content and generates concise summaries using Groq LLMs.

## Features

- Summarize any accessible website URL.
- Choose different summary styles:
  - Friendly
  - Professional
  - Snarky
  - Explain Like I'm 5
- Select sample websites.
- Generate summaries using Groq.
- Simple and interactive Gradio interface.

## Tech Stack

- Python
- Gradio
- Groq API
- OpenAI Python SDK
- BeautifulSoup
- Requests

## Project Structure

```text
AI-Website-Summarizer/
├── app.py
├── scraper.py
├── summarizer.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Setup and Installation

Clone the repository:

```bash
git clone https://github.com/ankitgit123/ai-website-summarizer.git
cd ai-website-summarizer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

Run the application:

```bash
python app.py
```

Open `http://127.0.0.1:7860` in your browser.

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Groq API authentication key |
| `GROQ_MODEL` | Groq model used for summarization |

## Deployment

The application can be deployed as a Render Web Service using GitHub integration.

Configure the environment variables in Render rather than uploading the `.env` file.

## Demo
https://github.com/user-attachments/assets/ca840e0c-65fb-41d6-bdac-4af0a6065722

## License

MIT
