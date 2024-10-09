import streamlit as st
from PIL import Image
import random

# Function for setting the dyslexia-friendly theme
def set_dyslexia_friendly_theme():
    st.markdown(
        """
        <style>
        body {
            background-color: #f0f0f5;
        }
        .reportview-container {
            font-family: Arial, sans-serif;
        }
        h1, h2, h3, h4, h5 {
            font-family: Arial, sans-serif;
            color: #333;
        }
        .css-1lcbmhc {
            color: #003366 !important;
        }
        .stButton button {
            background-color: #003366;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True
    )

# Setting the theme
set_dyslexia_friendly_theme()

# App title and description
st.title("DysQuest - Educational App for Dyslexia Students")

# Language selection
language = st.selectbox("Choose your language / Pilih bahasa anda", ("English", "Bahasa Melayu"))

if language == "English":
    st.header("Welcome to DysQuest!")
    st.write("Let's help you learn in a fun way with games and exercises!")
    game_instructions = {
        "Matching Words": "Match the word with the picture!",
        "Spelling Puzzle": "Drag the letters to form the correct word!",
        "Reading Quiz": "Read the paragraph and answer the quiz!"
    }
    start_label = "Start Game"
    progress_label = "Your progress will be displayed here after each game!"
else:
    st.header("Selamat Datang ke DysQuest!")
    st.write("Mari kita belajar dengan cara yang menyeronokkan melalui permainan dan latihan!")
    game_instructions = {
        "Matching Words": "Padankan perkataan dengan gambar!",
        "Spelling Puzzle": "Seret huruf untuk membentuk perkataan yang betul!",
        "Reading Quiz": "Baca perenggan dan jawab kuiz!"
    }
    start_label = "Mula Permainan"
    progress_label = "Kemajuan anda akan dipaparkan di sini selepas setiap permainan!"

# Display an educational image
image = Image.open("DysQuest/dyslexia_friendly_image.png")  # Replace with actual image path
st.image(image, caption="Learning made fun!", use_column_width=True)


# Simple games for learning
st.write("**Start with a simple game:** / **Mulakan dengan permainan mudah:**")
game = st.selectbox("Choose a game / Pilih permainan", 
                    ("Matching Words", "Spelling Puzzle", "Reading Quiz"))

# Matching Words Game
if game == "Matching Words":
    st.write(game_instructions["Matching Words"])
    
    # Sample words and images for matching
    words = ["Cat", "Dog", "Bird", "Fish"]
    images = {
        "Cat": "cat.png",
        "Dog": "dog.png",
        "Bird": "bird.png",
        "Fish": "fish.png"
    }  # Dictionary of word-image pairs (replace with actual image paths)
    
    # Randomize a new image if none exists or after correct submission
    if "correct_word" not in st.session_state or st.session_state.correct_word is None:
        st.session_state.correct_word = random.choice(list(images.keys()))
    
    correct_word = st.session_state.correct_word  # Get the current random word
    selected_image = images[correct_word]  # Get corresponding image file
    
    image = Image.open(selected_image)  # Load the correct image
    st.image(image, caption="Which word matches this image?", use_column_width=True)
    
    # Word choice
    word_choice = st.radio("Choose the correct word for the image:", words)
    
    # Check if the word matches the image
    if st.button("Submit Answer"):
        if word_choice == correct_word:
            st.success("Correct!")
            # Automatically randomize a new image
            st.session_state.correct_word = random.choice(list(images.keys()))  # New word for next round
        else:
            st.error(f"Incorrect, the correct answer is '{correct_word}'.")

# Spelling Puzzle Game
elif game == "Spelling Puzzle":
    st.write(game_instructions["Spelling Puzzle"])
    
    # Simple word to spell
    word = "Streamlit"
    jumbled_word = ''.join(random.sample(word, len(word)))  # Jumble the letters
    st.write(f"Arrange these letters to form the word: {jumbled_word}")
    
    user_input = st.text_input("Enter the correct word:")
    if st.button("Submit Word"):
        if user_input.lower() == word.lower():
            st.success("Correct!")
        else:
            st.error("Incorrect, try again!")

# Reading Quiz Game
else:
    st.write(game_instructions["Reading Quiz"])
    
    # Sample text and questions for the reading quiz
    text = """Dyslexia is a common learning difficulty that can cause problems with reading, writing, and spelling. 
    It does not affect intelligence but makes it harder to learn in the traditional way."""
    
    st.write("Read the passage below:")
    st.write(text)
    
    question = "What does dyslexia affect?"
    options = ["Intelligence", "Learning ability", "Physical health"]
    answer = "Learning ability"
    
    user_answer = st.radio(question, options)
    
    if st.button("Submit Answer"):
        if user_answer == answer:
            st.success("Correct!")
        else:
            st.error("Incorrect, the correct answer is 'Learning ability'.")

# Feedback and performance measurement
st.write(progress_label)
# Placeholder for performance measurement and feedback
progress = 50  # Example of how progress could be tracked
st.progress(progress)

# End of the app
if st.button(start_label):
    st.write("Game Started! / Permainan Bermula!")
