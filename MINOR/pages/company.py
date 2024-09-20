import streamlit as st
import os

# Function to handle PDF upload
def upload_pdf(uploaded_files):
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            if uploaded_file.type == "application/pdf":
                # Read the PDF content (for demonstration purposes)
                num_pages = uploaded_file.size  # Just for feedback, you can use an external library to get actual page count
                st.success(f"Uploaded successfully: {uploaded_file.name} with {num_pages} bytes.")
            else:
                st.error("Please upload PDF files only.")

def main():
    st.title("UPLOAD FINANCIAL STATEMENTS OF YOUR COMPANY")
    
    # Upload files
    uploaded_files = st.file_uploader("Choose PDF files for your financial statements", type="pdf", accept_multiple_files=True)

    # Check if any files are uploaded
    if uploaded_files:
        upload_pdf(uploaded_files)

        # Display uploaded PDFs
        st.subheader("Uploaded Financial Statements \n\n")
        for uploaded_file in uploaded_files:
            st.write(f"- {uploaded_file.name}")

        # Activate button to save files
        if st.button("  SUBMIT  "):
            st.success("All financial statements submitted successfully!")
            
            # Directory to save uploaded files
            upload_dir = "uploaded_statements"
            os.makedirs(upload_dir, exist_ok=True)

            for uploaded_file in uploaded_files:
                file_path = os.path.join(upload_dir, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.write(f"Saved: {uploaded_file.name}.")
            st.switch_page("pages/company_ratio.py")

if __name__ == "__main__":
    main()
