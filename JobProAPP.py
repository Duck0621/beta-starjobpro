from flask import Flask, request ,jsonify, send_file



app = Flask(__name__)
@app.route('/')
def index(): 
    return 'La pagina esta funcionando bien'

if __name__=='__main__':
    app.run()
    
