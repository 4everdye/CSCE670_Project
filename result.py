import cgi
import cgitb
import os

form = cgi.FieldStorage()
query = form.getvalue('Query')
res_page = '''
<!DOCTYPE html>
<html>
<body>
<div style="height:100px"></div>
<div>
<h1 align="center" style="font-size:40px"><abbr title="An Efficient People Search Engine">Uncover Anyone</abbr></h1>
</div>
<table align="center">
<tr align="center">
<td><strong><font size="6">The query is %s.</font></strong></td>
</tr>
</table>
<div style="margin-top:30px">
<center><form action="/search.py"><input type="submit" value="back"></form></center>
</div>
<div style="height:100px"></div>
<body>
</html>
''' %query
print res_page
