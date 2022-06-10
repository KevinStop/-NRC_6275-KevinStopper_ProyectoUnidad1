#importar librerias de Flask y tkinter
#from flask_wtf import FlaskForm
#from wtforms import StringField
#from wtforms.validators import DataRequired
from tkinter import SW, messagebox
from flask import Flask, redirect, request,render_template, url_for

#Iniciar variable de aplicacion 
app = Flask(__name__)

#Definición de arreglo para ingresar los datos
usuario = []
citas = []

#ruta principal 
@app.route('/' )
#Función principal que llamará a la página HTML y encapsula la variable de nuestro arreglo
def principal():
    #Retorno de la pagina
    return render_template('Home.html', Usuario_Registrado = usuario)

#Ruta pagina de inicio
@app.route('/Home')
#Funcion que llama pagina de Inicio
def Home():
    #Retorno de la pagina
    return render_template('Home.html')

#Ruta pagina de Citas  
@app.route('/Citas', methods=['GET','POST'])
def Citas():
    if(request.method == "POST"):
        #Instanciamiento de datos de nuestra pagina Citas
        nombre = request.form['fname']          
        apellido = request.form['lname'] 
        telefono = request.form['cell']
        sexo = request.form['Sexo']      
        ci = request.form['cedula']
        date = request.form['fecha']
        depa = request.form['departamentos']
        #(Condicional) Si el formulario no tiene ingresado datos no registrara
        if(nombre == "" or apellido  == "" or telefono == "" or ci == ""  or date == ""):
            return redirect(url_for('Citas'))
        else:
            citas.append({'fname': nombre, 'lname': apellido, 'cell': telefono, 'Sexo': sexo,
            'cedula': ci, 'fecha': date, 'departamentos': depa })
            print(citas)
    return render_template('Citas.html')

##Ruta pagina de de consulta
@app.route('/Consulta')
#Funcion que llama pagina de Consulta
def Consulta():
    #Retorno de la pagina
    return render_template('Consulta.html', ocitas = citas)

#Ruta pagina de contacto
@app.route('/Contacto')
def Contacto():
    #Retorno de la pagina
    return render_template('Contacto.html')

#Ruta pagina de Sobre nosotros
@app.route('/About')
#Funcion que llama pagina de Inicio
def About():
    #Retorno de la pagina
    return render_template('About.html')

#Ruta pagina de Departamentos
@app.route('/Departamentos')
#Funcion que llama pagina de Inicio
def Departamentos():
    #Retorno de la pagina
    return render_template('Departamentos.html')

# Ruta para el login
@app.route('/Login', methods=['GET','POST'])
def Login():
    if(request.method == "POST"): 
        #Instanciamiento de deatos de la pagina de Login
        correo = request.form['email']          
        contrasenia = request.form['password']       
        try:
            if (usuario.index(correo) > 0):              
                posicionCorreo = usuario.index(correo)
                if(usuario[posicionCorreo] == correo and usuario[posicionCorreo+1] == contrasenia):        
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


# main del programa 
if __name__ == "__main__":
    #debug = true, para reiniciar automaticamente el servidor, tiempo de desarrollo
    app.run(debug=True)