from flask import Flask , render_template
from url import api_Imperius
from flask_cors import CORS

app = Flask(__name__ , static_url_path='/static')
app.register_blueprint(api_Imperius)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True , port=5000)