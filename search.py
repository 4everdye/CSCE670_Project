import cgi
import cgitb
import os

search_page = '''
<!DOCTYPE html>
<html>
<body>
<div style="height:100px"></div>
<div>
<h1 style="font-size:40px"><center><abbr title="An Efficient People Search Engine">Uncover Anyone</abbr><center></center></h1>
<div>
<center>
<form method="post" action="/result.py">
Query: <input type="Query" name="Query" required autocomplete="on" autofocus style="width:200px" value=""/>
<input type="submit" value="Search">
<br>
<p><b>Note</b>: Query should be name, username or Email address</p>
</form>
</center>
</div>
</div>
<div style="height:100px"></div>
<body>
</html>
'''

print search_page
