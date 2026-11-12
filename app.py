
import os
import streamlit as st
from groq import Groq

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎯",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .title {
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        color: #2563eb;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 17px;
    }

    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        height: 45px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)


# ==========================================
# API KEY CONFIGURATION
# ==========================================

def get_api_key():

    try:
        api_key = st.secrets.get("GROQ_API_KEY", "")

        if api_key:
            return api_key

    except Exception:
        pass

    return os.getenv("GROQ_API_KEY", "")


# ==========================================
# GENERATE LEARNING ROADMAP
# ==========================================

def generate_roadmap(field, level, duration, hours, goal):

    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "Groq API key is missing. Please configure GROQ_API_KEY."
        )

    client = Groq(api_key=api_key)

    prompt = f"""
You are an expert career mentor, technical educator,
and professional learning roadmap designer.

Your task is to create a detailed and personalized
learning roadmap based on the user's information.

USER INFORMATION:

Learning Domain: {field}
Current Skill Level: {level}
Available Learning Time: {duration}
Study Hours Per Week: {hours}
Learning Goal: {goal}

INSTRUCTIONS:

1. Create a realistic and personalized learning roadmap.
2. Divide the roadmap into weekly or monthly phases,
   depending on the total duration.
3. Adjust the complexity according to the user's
   current skill level.
4. Explain what the user should learn in each phase.
5. Include important concepts and topics.
6. Recommend useful learning resources, such as:
   - Official documentation
   - Online courses
   - YouTube channels
   - Tutorials
   - Books
7. Include practical exercises and projects.
8. Mention important tools and technologies.
9. Define clear milestones and learning objectives.
10. Include a final capstone project.
11. Give tips for staying consistent and improving.
12. Ensure the roadmap fits the available learning time.
13. Avoid unnecessary repetition.
14. Recommend genuine resources and provide official
    URLs when known. Never invent links.

OUTPUT FORMAT:

# 🎯 Personalized Learning Roadmap

## 1. Learning Overview
Explain the learning journey and expected outcome.

## 2. Skills to Develop
List the important skills and technologies.

## 3. Complete Learning Roadmap

For every phase include:

- Phase name
- Duration
- Topics to learn
- Concepts to understand
- Learning resources
- Practical exercises
- Mini projects
- Expected outcomes

## 4. Recommended Learning Resources
Provide useful documentation, courses, books,
tutorials, and YouTube channels.

## 5. Practical Projects
Suggest projects from beginner to advanced level.

## 6. Learning Milestones
Explain how the user can measure progress.

## 7. Final Capstone Project
Suggest one comprehensive project with:
- Project idea
- Main features
- Technologies required
- Expected result

## 8. Daily Study Routine
Suggest a realistic daily and weekly study routine.

## 9. Career Opportunities
Explain possible career paths after mastering this domain.

## 10. Final Advice
Give practical advice to complete the roadmap successfully.

IMPORTANT:

Make the roadmap detailed, practical, realistic,
well-structured, and easy to understand.

Use Markdown headings, bullet points, and tables
wherever appropriate.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert learning roadmap generator. "
                    "Create accurate, practical, personalized learning plans."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_completion_tokens=6000
    )

    return response.choices[0].message.content


# ==========================================
# APPLICATION HEADER
# ==========================================

st.markdown(
    '<div class="title">🎯 AI Learning Roadmap Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your personalized AI-powered learning journey starts here!'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

st.info(
    "Enter your learning details below and let AI "
    "create a personalized roadmap for you."
)


# ==========================================
# USER INPUT SECTION
# ==========================================

st.subheader("📚 Enter Your Learning Details")

col1, col2 = st.columns(2)

with col1:

    field = st.text_input(
        "What do you want to learn?",
        placeholder="e.g. Python, Data Science, AI, Web Development"
    )

    level = st.selectbox(
        "Select Your Current Skill Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    duration = st.selectbox(
        "How much time do you have?",
        [
            "1 Month",
            "2 Months",
            "3 Months",
            "6 Months",
            "9 Months",
            "1 Year"
        ]
    )

with col2:

    hours = st.selectbox(
        "How many hours can you study per week?",
        [5, 10, 15, 20, 25, 30, 40]
    )

    goal = st.text_area(
        "What is your learning goal?",
        placeholder="e.g. I want to become a professional data scientist."
    )


# ==========================================
# GENERATE ROADMAP BUTTON
# ==========================================

st.write("")

if st.button("🚀 Generate My Learning Roadmap"):

    if not field.strip():

        st.warning("Please enter a learning domain.")

    elif len(field.strip()) > 100:

        st.warning("Learning domain must be under 100 characters.")

    elif not goal.strip():

        st.warning("Please enter your learning goal.")

    elif len(goal.strip()) > 500:

        st.warning("Learning goal must be under 500 characters.")

    else:

        try:

            with st.spinner(
                "🤖 AI is creating your personalized learning roadmap..."
            ):

                roadmap = generate_roadmap(
                    field.strip(),
                    level,
                    duration,
                    hours,
                    goal.strip()
                )

            if not roadmap or not roadmap.strip():

                st.error(
                    "AI returned an empty response. Please try again."
                )

            else:

                st.success("🎉 Your learning roadmap is ready!")

                st.divider()

                st.markdown("## 📌 Your Personalized Roadmap")

                st.markdown(roadmap)

                st.download_button(
                    label="📥 Download Your Roadmap",
                    data=roadmap,
                    file_name="my_learning_roadmap.md",
                    mime="text/markdown"
                )

        except ValueError as e:

            st.error(str(e))

        except Exception as e:

            error_message = str(e).lower()

            if "authentication" in error_message or "401" in error_message:

                st.error(
                    "Invalid Groq API key. Please check your API key."
                )

            elif "rate limit" in error_message or "429" in error_message:

                st.error(
                    "API rate limit reached. Please wait and try again."
                )

            elif "connection" in error_message or "timeout" in error_message:

                st.error(
                    "Unable to connect to Groq. Check your internet connection."
                )

            else:

                st.error(
                    "Something went wrong while generating the roadmap."
                )

                st.caption(
                    f"Technical details: {type(e).__name__}"
                )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    "<center>Made with ❤️ using Python, Streamlit & Groq AI</center>",
    unsafe_allow_html=True
)
