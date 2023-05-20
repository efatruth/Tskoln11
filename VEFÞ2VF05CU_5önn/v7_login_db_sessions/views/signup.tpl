% include("./views/header.tpl")

  <form action="/register" method="post">
    Nafn: <input name="name" type="text" /><br>
    Netfang: <input name="email" type="email" /><br>
    Lykilorð: <input name="password" type="password" />
    <input value="Skráning" type="submit" />
  </form>

% include("./views/footer.tpl")
