from langchain_community.document_loaders import TextLoader,PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_google_vertexai import ChatVertexAI
import os 
load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './daring-atrium-448311-p9-bb3f69b98364.json'

llm = ChatVertexAI(model_name='gemini-1.5-flash')

text = """

from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {"id" : 1,"Title" : "Test Book 1"},
    {"id" : 2,"Title" : "Test Book 2"},
    {"id" : 3,"Title" : "Test Book 3"}
]

@app.route('/')
def home():
    return jsonify({"msg" : "Getting Home page"})

@app.route('/api/books',methods=['GET'])
def getBooks():
    return jsonify({"books" : books})

@app.route('/api/books/<int:bookid>',methods=['GET'])
def getBooksById(bookid):
    book = next((book for book in books if book["id"]==bookid),None)
    if book is None:
        return jsonify({"msg" : "Book not available"}),404
    return jsonify({"msg" : "Book Found","book":book}),200

@app.route('/api/book',methods=['POST'])
def addBooksbyID():
    if not request.json or 'title' not in request.json :
        return jsonify({"msg" : "Incomplte Data Cannot be Added\n"}),400
    new_book = {
        "id" : books[-1]["id"] + 1 if books else 1,
        "Title" : request.json["title"]
        
    }
    books.append(new_book)
    return jsonify({"book" : new_book,"msg" : "New BooK Added Succesfully!"}),201

@app.route('/api/book/<int:bookid>',methods=['PUT'])
def updateBooks(bookid):
    book = next((book for book in books if book["id"]==bookid),None)
    if book is None:
        return jsonify({"msg" : "Book not available"}),404
    print(request.json)
    book["title"] = request.json["title"]
    return jsonify({"book" : book,"msg": "Working!"}),200


@app.route('/api/process-query',methods=['POST'])
def process_query():
    print(request.json)
    return jsonify({'body' : request.json}),200

if __name__ == '__main__':
    app.run(debug=True)


"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size=100,
    chunk_overlap=10
)

chunks = splitter.split_text(text)

print(len(chunks))

print(chunks[5])

