<!DOCTYPE html>
<html>
    <head>
        <title>Frétt</title>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="">
    </head>
    <body>
        <main>
           <div class='blogposts'>
             % for post in posts:
             <div class='post'>
                 <h2>By {{post[1]}} on {{post[0]}}</h2>
                 {{!post[2]}}
             </div>
             % end
         </div>
        </main>
    </body>
</html>
