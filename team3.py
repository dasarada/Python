from bottle import route,run,Bottle,template,request
app=Bottle()
team3={"amit":"amit1@","dasarada":"dasarada","vinay":"vinay1@","shantha":"shantha1@","shilpa":"shilpa1@"}
@app.route('/')
def home():
  return template('log')
@app.post('/msg')
def msg():
  u=request.forms.get('Uname')
  p=request.forms.get('Pswd')
  if team3[u]==p:
    return template('msg')
  else:
    return template('log')
@app.post('/profile')
def profile():
        return template('profile')

@app.post('/regpage')
def regpage():
        return template('regpage')
@app.post('/msg2')
def msg2():
        return template('msg2')
@app.post('/msg3')
def msg3():
        return template('log')
run(app, host='localhost', port=7777, debug=True)
