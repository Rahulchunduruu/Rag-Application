import streamlit as st
import tempfile
import os
from main import start_rag_system

st.title("Smart Search & Ask")
# Initialize session state at the very top
if "uploaded_files" not in st.session_state:
    st.session_state.uploaded_files = []
if "file_names" not in st.session_state:
    st.session_state.file_names = set()

with st.sidebar:
    st.header("📁 Upload Documents")
    uploaded_files = st.file_uploader(
        "Choose files",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True
    )
    if uploaded_files:
        current_file_names = {file.name for file in uploaded_files}
        if current_file_names != st.session_state.file_names:
            st.session_state.uploaded_files = uploaded_files
            st.session_state.file_names = current_file_names
            if "rag_chain" in st.session_state:
                del st.session_state.rag_chain
        st.success(f"✅ {len(uploaded_files)} file(s) uploaded")
        for file in uploaded_files:
            st.write(f"• {file.name}")

# Use files in main app
if st.session_state.uploaded_files:
    st.subheader("Uploaded Documents")
    for file in st.session_state.uploaded_files:
        st.write(f"📄 {file.name}")
try:        
            placeholder = st.empty()
            query = st.text_input("Ask a question about your documents:")
            if st.button("🔍 Search"):
                if not query:
                    st.write("⚠️  Please enter a valid query.")
                elif not st.session_state.uploaded_files:
                    st.write("⚠️  Please upload files first.")
                else:
                    temp_dir = tempfile.mkdtemp()
                    for file in st.session_state.uploaded_files:
                        file_path = os.path.join(temp_dir, file.name)
                        with open(file_path, "wb") as f:
                            f.write(file.getbuffer())
                    st.write("🔍 Processing your query...")
                    if "rag_chain" not in st.session_state:
                        st.session_state.rag_chain = start_rag_system(temp_dir)
                    st.write('your response:')
                    response = st.session_state.rag_chain.invoke(query)
                    st.markdown(response)

except Exception as e:
                     st.write(f"❌ Error: {e}")



