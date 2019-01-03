#!/usr/bin/python3
# import cgi module
import cgi
# import sqlite3 module
import sqlite3

#import for debugging
import cgitb
cgitb.enable()

# print the header of the website
print("Content-Type: text/html\r\n\r\n")
print('''<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
	<link rel = "stylesheet" type = "text/css" href = "style.css" />
  	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
	<title></title>
</head>
<body>
	<div class = "main-container container">
		<div class = "row navbar header">
			<div class = "col-6">
				<h1> Predicted Infrastructure Damage in Cox's Bazar refugee camps during the 2018 monsoons</h1>
			</div>
		</div>
		<div class = "row navbar header sub">
			By Manesha Ramesh <br>
			Date: 26 October 2018
		</div>
		<div class = "row">
			<div class =" col-12 content text-center" style = "margin-top: 20px;">
				<div class = "title text-center" style = "margin: 30px;"><h3>Building a small website for your SQLite data</h3></div>
					
						<p class = "name"><b>URL of the dataset:</b> https://data.humdata.org/dataset/kutupalong-infrastructure-risk-to-flood-and-landslide-hazards </p>
''')

# call cgi
form = cgi.FieldStorage();
#get value from the hrml form
input_facility = form["facility"].value
input_sort = form["sort"].value
input_order = form["order"].value
input_risk = form["risk"].value

# different queries for exceptional cases in input_facility and input_risk
if input_facility == "ALL" and input_risk == "Both":
	query = '''SELECT camps_unique_id,camps_facility, camps_campname, camps_funding, camps_both_risk FROM camps ORDER BY '''+input_sort+" "+input_order
elif input_facility != "ALL" and input_risk == "Both":
	query = '''SELECT camps_unique_id, camps_facility, camps_campname, camps_funding, camps_both_risk FROM camps WHERE camps_facility_c ="'''+input_facility+'''" ORDER BY '''+input_sort+" "+input_order
elif input_facility == "ALL" and input_risk != "Both":
	query = '''SELECT camps_unique_id,camps_facility, camps_campname, camps_funding, camps_both_risk FROM camps WHERE camps_both_risk = "'''+input_risk+'''" ORDER BY '''+input_sort+" "+input_order
else:
	query = '''SELECT camps_unique_id,camps_facility, camps_campname, camps_funding, camps_both_risk FROM camps WHERE camps_both_risk = "'''+input_risk+'''" AND camps_facility_c ="'''+input_facility+'''" ORDER BY '''+input_sort+" "+input_order

# connect to sqlite3
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute(query)
# Print the table
print ('''
<div class = "row">
<div class = "col-12 center">
<table class = "dataresult">
<tr>
<td>Unique ID</td>
<td>Facility</td>
<td>Camp Name</td>
<td>Source of Funding</td>
<td>Risk of Flood or Landslide</td>
</tr>''')

# this counter is to check is there are zero results
count = 0
#Print the data
for camps_unique_id, camps_facility, camps_campname,camps_funding,camps_both_risk in cur:
    print ('''<tr>
    	\t<td>'''+camps_unique_id+'''</td>
    	\t<td>'''+camps_facility+'''</td>
    	\t<td>'''+camps_campname       +'''</td>
    	\t<td>'''+camps_funding     +'''</td>
   		\t<td>'''+camps_both_risk +'''</td>
  		</tr>''')
    count += 1
print ('''
	</table>
	</div>
	</div>
	''')
# if the provided filters give zero results then print the following
if count == 0:
	print("<h6> There are no facilities that meet your search filters!!</h6>")
	
# close the cursor
cur.close()
						
print( '''			
			</div>	
	</div>

</body>
</html>
''')