#importar librerias de Flask y tkinter
from tkinter import SW
from flask import Flask, redirect, request,render_template, url_for

#Iniciar variable de aplicacion 
app = Flask(__name__)

#Definición de arreglo para ingresar los datos
usuario = []
citas = []

#ruta principal en la que tendremos nuestra pagina de inicio de sesion
@app.route('/' )
#Función principal que llamará a la página HTML y encapsula la variable de nuestro arreglo
def principal():
    return render_template('Login.html', Usuario_Registrado = usuario)

@app.route('/Home')
def Home():
    return render_template('Home.html')
    
@app.route('/Citas')
def Citas():
    return render_template('Citas.html')

@app.route('/Contacto')
def Contacto():
    return render_template('Contacto.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Departamentos')
def Departamentos():
    return render_template('Departamentos.html')

@app.route('/Consulta')
def Consulta():
    return render_template('Consulta.html')

# Ruta para el login
@app.route('/Login', methods=['GET','POST'])
def Login():
    if(request.method == "POST"):
        correo = request.form['email']          
        contrase = request.form['password']       

        try:
            if (usuario.index(correo) > 0):              
                posicionCorreo = usuario.index(correo)
                if(usuario[posicionCorreo] == correo and usuario[posicionCorreo+1] == contrase):        
                    return redirect(url_for('Home'))              
                else:
                    return redirect(url_for('Login'))
        except:
            return redirect(url_for('Login'))

    return render_template('Login.html')


# Ruta para el registro
@app.route('/Registro' , methods=['GET','POST'])
def Registro():
     #Obtiene los datos del pagina Login por medio del metodo POST
    if(request.method == "POST"):
        nombre = request.form['name']           #Registro datos usuario
        correo = request.form['email']         
        contrase = request.form['password']
        if(nombre == "" or correo  == "" or contrase == ""):             #Si no hay datos no redirecciona
            return redirect(url_for('Registro'))
        else:
            #Ingresa datos en el array del Usuario
            usuario.append(nombre)
            usuario.append(correo)
            usuario.append(contrase)
            return redirect(url_for('Login'))
    return render_template('Registro.html')

if __name__ == "__main__":
    app.run(debug=True)