from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Receipt Sharing Platform - Week 1 Setup Done"

if __name__ == '__main__':
    app.run()
