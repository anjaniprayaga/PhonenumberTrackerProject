f = open('helloworld.html','w')

message = """<html>
<head>Phone number Tracker</head>
<br />
<body><p>Enter a number with country code</p>
<label for="number">Phonenumber:</label>
  <input type="text" id="number" name="number"><br><br>
  <input type="submit" name="search">

</body>
</html>"""
with open('html.py', 'r') as f:
    html_string = f.read()
f.write(message)
f.close()