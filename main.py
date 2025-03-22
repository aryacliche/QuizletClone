import pandas as pd
import streamlit as st
import openpyxl

# Load the data from the xlsx file into a pandas dataframe
file_path = 'Question_paper.xlsx'
df = pd.read_excel(file_path)

# Initialize Streamlit app
st.title('CUET 2022 (Partial) Question Paper')

# Create a form for the quiz
with st.form(key='quiz_form'):
    user_answers = []
    for index, row in df.iterrows():
        st.write(f"Q{index + 1}: {row['Question']}")
        options = [row['Option 1'], row['Option 2'], row['Option 3'], row['Option 4']]
        user_answer = st.radio(f"Options", options, key=f"q{index + 1}", index=None)
        user_answers.append(user_answer)
    
    submit_button = st.form_submit_button(label='Submit')

# Grade the quiz once the user submits
if submit_button:
    total_marks = 0
    for index, row in df.iterrows():
        correct_option = row[f'Option {row["Correct option"]}']
        if user_answers[index] == correct_option:
            total_marks += row['Positive']
        elif user_answers[index] == None:
            total_marks += 0
        else:
            total_marks += row['Negative']
    
    st.write(f"Your total marks: {total_marks}")

    # Point out where the user went wrong
    for index, row in df.iterrows():
        correct_option = row[f'Option {row["Correct option"]}']
        if user_answers[index] == correct_option:
            st.write(f"Q{index + 1}: Correct! You earned {row['Positive']} marks.")
        elif user_answers[index] == None:
            st.write(f"Q{index + 1}: You did not answer this question. You lost 0 marks. Correct answer: <span style='color:green'>{correct_option}</span>", unsafe_allow_html=True)
        else:
            st.write(f"Q{index + 1}: You answered {user_answers[index]}, but the correct answer was <span style='color:green'>{correct_option}</span>. You lost {row['Negative']} marks.", unsafe_allow_html=True)