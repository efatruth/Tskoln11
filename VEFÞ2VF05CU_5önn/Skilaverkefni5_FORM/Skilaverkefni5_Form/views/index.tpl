% rebase('base.tpl', title="Form")

<h1> Form </h1>

<form action="/send" method="post">
  First name:<br>
  <input type="text" name="firstname"> <br>
  Last name:<br>
  <input type="text" name="lastname"> <br>
  <input type="submit" value="Submit">
</form>
