from flask import Flask, render_template, url_for,redirect,request

from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
def encrypt_func(p_text):
    if p_text!="":
        p_text = bytes(p_text,'utf-8')
        e_text = f.encrypt(p_text)
        e_text = e_text.decode('utf-8')
        return e_text

def decrypt_func(e_text):
    if e_text!="":
        e_text = bytes(e_text,'utf-8')
        d_text = f.decrypt(e_text)
        d_text = d_text.decode('utf-8')
        return d_text

app = Flask(__name__)



@app.route("/encrypt",methods=["POST","GET"])
def encrypt():
    if request.method == "POST":
        p_text = request.form["ent"]
        enc = encrypt_func(p_text)
        #print(enc)
        return redirect(url_for('result',text=enc,func="Encrypted"))
    else:
        return render_template("encrypt.html")

@app.route("/decrypt", methods=["POST","GET"])
def decrypt():
    if request.method == "POST":
        e_text = request.form["dct"]
        dec = decrypt_func(e_text)
        return redirect(url_for('result',text=dec,func="Decrypted"))
    else:
        return render_template("decrypt.html")
    
@app.route("/result")
def result():
    text = request.args.get('text')
    func = request.args.get('func')
    return render_template('result.html',text=text,func=func)

@app.route("/")
def home():
    return render_template('index.html')

if(__name__) == "__main__":
    app.run()