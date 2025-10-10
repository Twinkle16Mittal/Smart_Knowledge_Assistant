import streamlit as st
from utils import upload_documents, list_documents, query_documents

st.set_page_config(page_title="Smart Knowledge Assistant", layout="wide")
st.title("Smart Knowledge Assistant (FastAPI + Streamlit + Ollama)")

tab1, tab2 = st.tabs(["Upload Docs", "Ask Questions"])

with tab1:
    files = st.file_uploader("Upload PDF/DOCX/TXT", type=["pdf", "docx", "txt"], accept_multiple_files=True)
    if st.button("Upload"):
        for f in files:
            with st.spinner(f"Uploading {f.name}..."):
                res = upload_documents(f)
                if res:
                    st.success(f"Uploaded {f.name}: {res.get('chunks')} chunks")
                else:
                    st.error("Upload failed.")

    st.subheader("Documents")
    docs = list_documents()
    print(docs)
    print(len(docs))
    for d in docs:
        st.markdown(f"- **{d['file_name']} ** uploaded at {d["uploaded_at"]}")

with tab2:
    query = st.text_area("Ask a Question:")
    if st.button("Get Answer"):
        with st.spinner("Thinking..."):
            res = query_documents(query)
            st.markdown("### Answer")
            print(res)
            st.write(res.get("answer", "No answer"))
            if res.get("sources"):
                st.markdown("### Sources")
                for s in res["sources"]:
                    st.caption(f"-{s.get('source')}(chunk {s.get('chunk_index')})")
