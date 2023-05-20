<!DOCTYPE html>
<html>
<head>
		<title>Nýskráning</title>
		<meta charset="utf-8" />
		<link href="" rel="stylesheet" />
</head>
<body>
   <form action="/process" method="post">
         <fieldset>
         <legend>Upplýsingar um notandann</legend>
         <!-- create four text boxes for user input -->
         <div>
            <label>Nafnið:</label>
            <input type = "text" name = "nafn" required="required">
         </div>
        <!--
         <div>
            <label>Heimilisfang:</label>
            <input type = "text" name = "heimilisfang" required="required">
         </div>
         <div>
            <label>Netfang:</label>
            <input type = "email" name = "netfang" required="required">
         </div>
         <div>
            <label>Símanúmer:</label>
            <input type = "text" name = "simi" pattern="^(\+354 )?\d{3}[ -]?\d{4}$">
         </div>
           <div>
            <label>Notendanafn:</label>
            <input type = "text" name = "notandanafn" >

         </div>
           <div>
            <label>Lykilorð:</label>
            <input type = "password" name = "lykilord">

         </div>
        -->
      </fieldset>


      <fieldset>
         <legend>Nýskráning</legend>
         <input type = "submit" name = "submit" value = "Staðfesta" />
      </fieldset>
	</form>
</body>
</html>
