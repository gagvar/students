#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
import smtplib
app=Flask(__name__)
@app.route("/")
def aaa():
    return render_template("registration.html") 
@app.route("/basicdetails",methods=['GET','POST'])
def zzz():
    if(request.method=='POST'):
        name=request.form['n1']
        email=request.form['e1']
        phone=request.form['p1']
        course=request.form['c1']
        
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login('gagvar2000@gmail.com','gagvar2000#')
        msg='Hello {0},\nThanks we will call you for {1} course\nThanks'.format(name,course)
        server.sendmail("gagvar2000@gmail.com",email,msg)
        server.quit()
        
        return render_template("registration.html")


if __name__=="__main__":
    app.run()


# In[ ]:




