from flask import Flask , render_template
from url import api_Imperius

app = Flask(__name__)
app.register_blueprint(api_Imperius)


if __name__ == '__main__':
    app.run(debug=True , port=5000)