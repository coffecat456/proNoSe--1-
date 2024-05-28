from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/area')
def area():
    return render_template("area.html")

@app.route('/Calificaciones')
def Calificaciones():
    return render_template("Calificaciones.html")

@app.route('/Viaje')
def Viaje():
    return render_template("Viaje.html")

@app.route('/TablaMult')
def TablaMult():
    return render_template("TablaMult.html")

@app.route('/Grado')
def Grado():
    return render_template("Grados.html")

@app.route('/areaT',methods=['POST'])
def areaT():
    if request.method == 'POST':
        ar= 0
        b=int(request.form['base'])
        a=int(request.form['altura'])
        ar= b*a/2
        return render_template("area.html", res=ar)

@app.route('/Grados',methods=['POST'])
def Grados():
    if request.method == 'POST':
        c=0
        F=int(request.form['grados'])
        c= 5/9*(F-32)
        return render_template("Grados.html", ras=c)

@app.route('/Calificacion',methods=['POST'])
def Gra():
    if request.method == 'POST':
        c=int(request.form['calidicacion'])
        if c<=5:
            return render_template("Calificaciones.html", res="REPROBATORIA")
        if c==6:
            return render_template("Calificaciones.html", res="SUFICIENTE")
        if c==7:
            return render_template("Calificaciones.html", res="REGULAR")
        if c>=8 and c<=9:
            return render_template("Calificaciones.html", res="Notable")
        if c==10:
            return render_template("Calificaciones.html", res="EXELNTE")
        
@app.route('/Viaje',methods=['POST'])
def viaje():
    if request.method == 'POST':
        a=int(request.form['numero'])
        pr=0
        if a>=50  and a<=99:
            au=70
            pr=a*au
            return render_template("Viaje.html", res=pr, al=a)
        if a>=30  and a<=49:
            au=95
            pr=a*au
            return render_template("Viaje.html", res=pr,al=a)
        if a<=29:
            pr=3000
            return render_template("Viaje.html", res=pr, al=a)
        
@app.route('/tabla',methods=['POST'])
def tabla():
    if request.method == 'POST':
        a=int(request.form['numero'])
        list =[]
        for i in range(1,11):
            e=i*a
            p=f"{a} x {i} = {e}"
            list.append([p])
        return render_template("TablaMult.html", res=list )
    
if __name__ == "__main__":
    app.run(debug=True)