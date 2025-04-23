import random
import streamlit as st

st.title("🪨 Rock, 📜 Paper, ✂️ Scissors, Game")
st.write("👊 Choose one option and see if you can beat the computer! 🤖")

# Choices with emojis
options = {
    "Rock": "🪨 Rock",
    "Paper": "📜 Paper",
    "Scissors": "✂️ Scissors"
}

# User selects

choices = ["Rock", "Paper", "Scissors"]
user_choice = st.selectbox("👇 Select your choice:", choices)


# Play button
if st.button("🎮 Play"):
    # Computer randomly picks
    computer_choice = random.choice(list(options.keys()))

    # Show choices
    if user_choice == computer_choice:
        st.write("🤝 It's a Tie!")
        st.write(f"🧍 You chose: **{options[user_choice]}**")
        st.write(f"🤖 Computer also chose: **{options[computer_choice]}**")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            st.success("🎉 You win! Rock crushes Scissors.")
        else:
            st.error("😢 You lose! Paper covers Rock.")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            st.success("🎉 You win! Paper covers Rock.")
        else:
            st.error("😢 You lose! Scissors cuts Paper.")
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            st.success("🎉 You win! Scissors cuts Paper.")
        else:
            st.error("😢 You lose! Rock crushes Scissors.")

    # Show choices
    if user_choice != computer_choice:
        st.write(f"🧍 You chose: **{options[user_choice]}**")
        st.write(f"🤖 Computer chose: **{options[computer_choice]}**")

# Footer
st.markdown("---")
st.markdown("🎮 Made with fun by **Hamza Syed**")
