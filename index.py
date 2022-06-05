#import libreria Flask
from flask import Flask, render_template

app = Flask(__name__)

#ruta principal en la que tendremos nuestra pagina de inicio de sesion
@app.route('/')
def helloworld():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)