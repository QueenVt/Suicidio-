from flask import Flask,render_template

app = Flask("GlitchEstético")

@app.route("/")
def hello_word():
    return render_template("index.html")

@app.route("/example")
def example_route():
    return "¡Bienvenid@ a nuestro rincón estético del internet! ✨"

@app.route("/<name>")
def return_with_dynamic_content(name):
    return render_template("name.html",contenido=name,lorem ="Estetica404")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
    
    
