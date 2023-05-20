<!DOCTYPE html>
<html>
<head>
	<title>Verkefni 4.2</title>
</head>
<body>
    <h1>Gengi</h1>

	<table>
	  <tr>
	    <th>Land</th>
	    <th>skammst.</th>
	    <th>gengi</th>
	  </tr>
	
	% for i in gengi['results']:
	<tr>
	    <td>{{ i['longName'] }}</td>
	    <td>{{ i['shortName'] }}</td>
	    <td>{{ i['value'] }}</td>
	  </tr>
	% end
	</table>
</body>
</html>
