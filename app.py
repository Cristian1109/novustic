from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("https://sites.google.com/view/novusticsas/p%C3%A1gina-principal")

@app.route('/info')
def info():
    return "Servidor Novustic funcionando"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
    
