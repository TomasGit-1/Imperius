from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/imperius/")
def Home_App():
    return render_template("imperius.html")

@app.route("/cargar_image", methods = ['POST'])
def cargar_image():
    print("Hola mundo")

    return "recibido"






if __name__ == '__main__':
    app.run(debug=True , port=5000)