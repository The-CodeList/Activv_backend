from Utils.flask_app import app
from dotenv import load_dotenv

if __name__ == "__main__" :
    load_dotenv()
    app.run(debug=True, port=10000)