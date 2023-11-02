import streamlit as st
import csv

# Load the CSV data
def load_csv_data(csv_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# Define the main function
def main():
    st.title("Chatbot with Mineral Data")

    # Load CSV data
    csv_file = 'mineral.csv'  # Replace 'your_data.csv' with your CSV file
    data = load_csv_data(csv_file)

    # Create a text input for user questions
    user_question = st.text_input("Ask about Mineral:")

    if user_question:
        # Search for answers in the CSV
        results = []
        for row in data:
            if user_question.lower() in row[0].lower():  # Assuming the questions are in the first column of the CSV
                results.append(row)

        if results:
            # Display the results
            st.header("Answers:")
            for result in results:
                st.write(result)
        else:
            st.warning("No matching answers found.")

if __name__ == '__main__':
    main()

