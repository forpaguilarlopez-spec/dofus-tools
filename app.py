from flask import Flask
from modules.checklist.routes import checklist_bp

app = Flask(__name__)

app.register_blueprint(checklist_bp, url_prefix='/checklist')

if __name__ == '__main__':
    app.run(debug=True)