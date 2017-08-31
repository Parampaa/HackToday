from flask import Flask, request, render_template_string, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    person = {'name':"to You", 'secret':"asfvncvcccccc=="}
    
    template = '''<head>
<style>
h1 {
    text-align: center;
}

p {
    text-align: center;
    font-size: 24px;
    color:black;
} 

body {
        text-align: center;
         background: black;
         color: white;
         font-family: Helvetica;
         background-image: url("https://i.stack.imgur.com/8IjyR.gif");
         background-size: cover;
         background-position: center center;
         background-repeat: no-repeat;
         background-attachment: fixed;
}

input {
  border: 1;
  padding: 12px;
  font-size: 18px;
}    

input[type="submit"] {
  background: limegreen;
  color: black;
}
</style>
</head>
<body>
<img src="http://www.sharegif.com/wp-content/uploads/2013/12/01/birthday-cake-gif-39.gif" height="250" width="250">
<p>Happy Birthday %s!</p>
<form action="" method="post">
<input type="text" name="name" placeholder="Your Name">
<input type="submit" value="Celebrate It">
</form>
<br>
<form action="/birthday" method="post">
<input type="hidden" name="id" value="1">
<input type="submit" value="see your present">
</form>

</body>
</html>
''' % person['name']
    return render_template_string(template, person=person)
    

@app.route('/',methods=['POST'])
def home2():
    person = {'name':"to You", 'secret':"asfvncvcccccc=="}
    person['name']= request.form['name']
    template = '''<head>
<style>
h1 {
    text-align: center;
}

p {
    text-align: center;
    font-size: 24px;
    color:black;
} 

body {
        text-align: center;
         background: black;
         color: white;
         font-family: Helvetica;
         background-image: url("https://i.stack.imgur.com/8IjyR.gif");
         background-size: cover;
         background-position: center center;
         background-repeat: no-repeat;
         background-attachment: fixed;
}

input {
  border: 1;
  padding: 12px;
  font-size: 18px;
}    

input[type="submit"] {
  background: limegreen;
  color: black;
}
</style>
</head>
<body>
<img src="http://www.sharegif.com/wp-content/uploads/2013/12/01/birthday-cake-gif-39.gif" height="250" width="250">
<p>Happy Birthday %s!</p>
<form action="" method="post">
<input type="text" name="name" placeholder="Your Name">
<input type="submit" value="Celebrate It">
</form>
<br>
<form action="/birthday" method="post">
<input type="hidden" name="id" value="1">
<input type="submit" value="see your present">
</form>

</body>
</html>
''' % person['name']
    return render_template_string(template, person=person)

@app.route('/birthday',methods=['POST'])
def result():
    id_want = request.form['id']
    if id_want!="1":
        return render_template("birthday.html")
    return "It's Okay if you <b>don\'t</b> like the present"

@app.route('/birthday')
def result2():
    return render_template("birthday.html")
    
####
# Private function if the user has local files.
###
def get_user_file(f_name):
    with open(f_name) as f:
        return f.readlines()

app.jinja_env.globals['get_user_file'] = get_user_file # Allows for use in Jinja2 templates

if __name__ == "__main__":
    app.run(debug=True)
