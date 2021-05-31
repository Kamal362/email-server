from flask import Flask, render_template,request
from flask_mail import Mail, Message

app = Flask(__name__, template_folder="templates")

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="turntabl80@gmail.com"
app.config['MAIL_PASSWORD']='Turntabl@024'
app.config['MAIL_USE_SSL']=True


mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html') 
    
    
@app.route('/send_message', methods = ['POST','GET'])
def massage_server():
    if request.method == 'POST':
       email = request.form['email']
       subject = request.form['subject']
       msg = request.form['message']
       message = Message(subject, sender="turntabl80@gmail.com", recipients=[email])
       message.body = msg
       mail.send(message)
       
       success = "message sent"
       return render_template('result.html', success = success)
   
if __name__ =='__main__':
    app.run(debug=True)