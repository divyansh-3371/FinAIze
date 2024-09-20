import streamlit as st
import os
import fitz  # PyMuPDF
import pandas as pd
import re

def extract_financial_values(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()

    financial_data = {}

    # Define regex patterns to extract numerical values for different metrics
    patterns = {
        "Total Assets": re.compile(r"Total Assets[:\s]*([\d,\.]+)", re.IGNORECASE),
        "Current Assets": re.compile(r"Current Assets[:\s]*([\d,\.]+)", re.IGNORECASE),
        "Total Liabilities": re.compile(r"Total Liabilities[:\s]*([\d,\.]+)", re.IGNORECASE),
        "Current Liabilities": re.compile(r"Current Liabilities[:\s]*([\d,\.]+)", re.IGNORECASE),
        "Revenue": re.compile(r"Revenue[:\s]*([\d,\.]+)", re.IGNORECASE),
        "Profit": re.compile(r"Profit[:\s]*([\d,\.]+)", re.IGNORECASE)
    }

    for key, pattern in patterns.items():
        match = pattern.search(text)
        if match:
            financial_data[key] = match.group(1).replace(',', '')  # Remove commas for conversion
        else:
            financial_data[key] = None

    return financial_data

# Main function for the company ratio page
def main():
    st.title("Financial Ratios Calculation")

    # Directory where the PDFs were saved
    upload_dir = "uploaded_statements"
    if not os.path.exists(upload_dir):
        st.error("No uploaded files found. Please upload files first.")
        return

    # Load uploaded PDF files
    uploaded_files = os.listdir(upload_dir)
    financial_values = {}
    
    # Extract financial values from each uploaded PDF
    for file_name in uploaded_files:
        file_path = os.path.join(upload_dir, file_name)
        with open(file_path, "rb") as pdf_file:
            values = extract_financial_values(pdf_file)
            financial_values[file_name] = values

    # Use session state to keep track of user inputs
    if 'user_inputs' not in st.session_state:
        st.session_state.user_inputs = {file_name: {} for file_name in uploaded_files}

    # Create a list to store user prompts
    user_prompts = []

    # Input fields for user to fill in missing values
    for file_name in uploaded_files:
        for key in financial_values[file_name]:
            current_value = financial_values[file_name][key]
            if current_value is None:  # Only ask for values that are missing
                user_input = st.text_input(f"Please enter the {key} as it cannot find in pdf:")
                st.session_state.user_inputs[file_name][key] = user_input
                if user_input:  # Add to user prompts if input is provided
                    st.session_state.user_inputs[file_name][key] = user_input
            else:
                st.session_state.user_inputs[file_name][key] = current_value

    # Check if all required values have been filled
    all_values_filled = all(
        all(st.session_state.user_inputs[file_name].get(key) for key in ['Total Assets', 'Total Liabilities'])
        for file_name in st.session_state.user_inputs
    )

    # Display final table if all values are filled
    if all_values_filled:
        df = pd.DataFrame(st.session_state.user_inputs).T  # Transpose to have files as rows
        df.index.name = 'File Name'

        # Display the updated DataFrame
        st.subheader("Extracted and Entered Financial Data:")
        st.dataframe(df)

        # Calculate and display ratios
        try:
            for file_name in st.session_state.user_inputs:
                total_assets = float(st.session_state.user_inputs[file_name]['Total Assets'])
                total_liabilities = float(st.session_state.user_inputs[file_name]['Total Liabilities'])
                debt_to_equity_ratio = total_liabilities / (total_assets - total_liabilities) if (total_assets - total_liabilities) != 0 else None
                
                if debt_to_equity_ratio is not None:
                    st.write(f"**Debt to Equity Ratio:** {debt_to_equity_ratio:.2f}")

        except ValueError:
            st.error("One of the values is not a valid number. Please check your input.")

if __name__ == "__main__":
    main()
