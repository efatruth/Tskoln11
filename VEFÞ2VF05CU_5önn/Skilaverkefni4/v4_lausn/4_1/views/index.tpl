<!DOCTYPE html>
<html>
<head>
	<title>Verkefni 4.1</title>
</head>
<body>
	<h1>Gengi</h1>
	% for i in range(0,len(gengi['results'])):
	<ul>
	    <li>{{ gengi['results'][i]["longName"] }} | {{ gengi['results'][i]["shortName"] }}  |  {{gengi['results'][i]["value"]}} </li>
	  </ul>
	% end
	</div>
</body>
</html>
