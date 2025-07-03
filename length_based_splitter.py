from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./sample-report.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0, #10-20% of chunk size for RAG Application
    separator=''
)

result = splitter.split_text(docs)

print(result[0].page_content)