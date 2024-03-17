from flask import Flask, render_template, url_for,redirect,request,session
from cryptography.fernet import Fernet

#key generating
key = Fernet.generate_key()
f = Fernet(key)

#encryption function
def encrypt_func(p_text):
    if p_text!="":
        p_text = bytes(p_text,'utf-8')
        e_text = f.encrypt(p_text)
        e_text = e_text.decode('utf-8')
        return e_text
    

#decryption function
def decrypt_func(e_text):
    if e_text!="":
        try:
            e_text = bytes(e_text,'utf-8')
            d_text = f.decrypt(e_text)
            d_text = d_text.decode('utf-8')
            return d_text
        except:
            d_text="*ERROR! INCORRECT DATA GIVEN!*"
            return d_text

app = Flask(__name__)
app.secret_key = 'oscarthedog'


@app.route("/encrypt",methods=["POST","GET"])
def encrypt():
    if request.method == "POST":
        p_text = request.form["ent"]
        enc = encrypt_func(p_text)
        session['text'] = enc
        return redirect(url_for('result',func="Encrypted"))
    else:
        return render_template("encrypt.html")


@app.route("/decrypt", methods=["POST","GET"])
def decrypt():
    if request.method == "POST":
        e_text = request.form["dct"]
        dec = decrypt_func(e_text)
        session['text'] = dec
        return redirect(url_for('result',func="Decrypted"))
    else:
        return render_template("decrypt.html")
 
    
@app.route("/result")
def result():
    text = session.get('text')
    func = request.args.get('func')
    return render_template('result.html',text=text,func=func)


@app.route("/")
def home():
    return render_template('index.html')


if(__name__) == "__main__":
    app.run(debug=True)
