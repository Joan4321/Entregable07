from flask import Flask, render_template
import os, sys
import platform
import socket

app = Flask(__name__)
mensaje=[]


@app.route("/")
def index():
    return render_template('index.html',mensaje=['Menu del equipo por defecto','Entrega unidad 7','Joan Morales Andres'])

@app.route("/<parametro>")
def mostrar(parametro):
    if parametro=="direccion_ip":
        return render_template('index.html', mensaje=['La direccion ip de nuestro equipo es:', socket.gethosbyname(socket.gethostname() + ".local")])
    elif parametro=="hostname":
        return render_template('index.html', mensaje=['Nombre del equipo', platform.node()]) #Puede que no este identificado por lo que dara una cadena vacia, se puede utilizar sino socket.gethostname() o os.environ['COMPUTERNAME']
    elif parametro=="reinicio":
        if os.name=="nt":
            return render_template('index.html', mensaje=['Reinicio de sistema en 5min', subprocess.run("shutdown -r +5, shell=True")])
        elif os.name=="posix":
            return render_template('index.html', mensaje=['Reinicio de sistema inmediatamente', subprocess.run("shutdown -r now, shell=True")])
    else:
        return render_template('index.html',mensaje=['Error','Parámetro no válido, haz clic en el menú superior'])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
