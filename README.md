
# 🎯 AI Learning Roadmap Generator

An AI-powered application that generates personalized learning roadmaps based on the user's selected domain, current skill level, available learning time, and learning goals.

## 🚀 Features

- Enter any learning domain.
- Select Beginner, Intermediate, or Advanced level.
- Choose available learning duration.
- Specify weekly study hours.
- Enter personalized learning goals.
- Generate AI-powered learning roadmaps.
- Get weekly or monthly learning phases.
- Receive recommended courses and learning resources.
- Get practical exercises and project ideas.
- Track learning milestones.
- Receive a final capstone project.
- Download the generated roadmap as a Markdown file.

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- GPT-OSS 120B LLM
- Google Colab
- GitHub

## 📂 Project Structure

ai-learning-roadmap/
│
├── app.py
├── requirements.txt
└── README.md

## ⚙️ Installation

### Step 1: Clone the repository

git clone https://github.com/YOUR_USERNAME/ai-learning-roadmap.git

### Step 2: Open the project folder

cd ai-learning-roadmap

### Step 3: Install dependencies

pip install -r requirements.txt

### Step 4: Get your Groq API key

Visit:

https://console.groq.com/

Create an account and generate an API key.

### Step 5: Configure your API key

For local development, create:

.streamlit/secrets.toml

Add:

GROQ_API_KEY = "your_actual_groq_api_key"

Alternatively, set the GROQ_API_KEY environment variable.

### Step 6: Run the application

streamlit run app.py

The application will open at:

http://localhost:8501

## ☁️ Google Colab Development

1. Open Google Colab.
2. Create a new notebook.
3. Install dependencies:

   !pip install -r requirements.txt

4. Create app.py using the %%writefile command.
5. Add your Groq API key securely.
6. Check Python syntax:

   !python -m py_compile app.py

7. Download your project files.
8. Run the application locally or deploy it.

Note: Google Colab is used for development. Streamlit Community Cloud is used for hosting.

## 📤 Upload Project to GitHub

Run these commands inside your project directory:

git init

git add .

git commit -m "Initial commit"

git branch -M main

git remote add origin https://github.com/YOUR_USERNAME/ai-learning-roadmap.git

git push -u origin main

Replace YOUR_USERNAME with your GitHub username.

## 🌐 Deploy on Streamlit Community Cloud

1. Visit https://share.streamlit.io/
2. Sign in using GitHub.
3. Click Create App.
4. Select your repository.
5. Select the main branch.
6. Set the main file path to app.py.
7. Open Advanced Settings.
8. Add your Groq API key under Secrets:

   GROQ_API_KEY = "your_actual_groq_api_key"

9. Click Deploy.

Your application will receive a public URL.

## 🧪 Testing

Test the application with different inputs:

| Domain | Skill Level | Duration |
|---|---|---|
| Python | Beginner | 3 Months |
| Data Science | Intermediate | 6 Months |
| Machine Learning | Advanced | 1 Year |
| Web Development | Beginner | 2 Months |
| Artificial Intelligence | Intermediate | 6 Months |

Also test:

- Empty input validation.
- Missing API key.
- Invalid API key.
- API rate limits.
- Roadmap generation.
- Roadmap download.

## 🔐 Security

- Never upload API keys to GitHub.
- Use Streamlit Secrets for deployment.
- Keep API keys in environment variables locally.
- Add secrets.toml and .env to .gitignore.

## 👨‍💻 Author

Your Name

## 📜 License

MIT License
