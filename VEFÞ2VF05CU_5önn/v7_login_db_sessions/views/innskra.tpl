% include("./views/header.tpl")
  <h1>Vinsamlegast skráðu þig inn!</h1>
  <form action="/login" method="post">
    Netfang: <input name="username" type="text" /><br>
    Lykilorð: <input name="password" type="password" />
    <input value="Login" type="submit" />
  </form>

% include("./views/footer.tpl")
