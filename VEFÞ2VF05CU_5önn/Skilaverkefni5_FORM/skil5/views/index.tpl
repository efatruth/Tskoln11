% rebase('base.tpl', title='SkilaVerkefni 5')

<form action="/send" method="POST">
  <fieldset>
    <label>3 Dagar frjálst val á Námskeið</label>
    <input type="checkbox" name="nam" value="1">fyrsti Dagur
    <input type="checkbox" name="nam" value="2">Annan Dagur
    <input type="checkbox" name="nam" value="3">Þiðji Dagur
  </fieldset>

  <fieldset>
    <label>Fyrilestur á fyrsti dag</label>
    <input type="radio" name="dag1" value="Python">Python<br>
    <input type="radio" name="dag1" value="JavaScript">JavaScript<br>
    <input type="radio" name="dag1" value="Gagnasofn">Gagnasofn<br>
  </fieldset>

  <fieldset>
    <label>Fyrilestur á Annan dag</label>
    <input type="radio" name="dag2" value="Python">Python<br>
    <input type="radio" name="dag2" value="JavaScript">JavaScript<br>
    <input type="radio" name="dag2" value="Gagnasofn">Gagnasofn
  </fieldset>

  <fieldset>
    <label>Fyrilestur á þriðji dag</label>
    <input type="radio" name="dag3" value="Python">Python<br>
    <input type="radio" name="dag3" value="JavaScript">JavaScript<br>
    <input type="radio" name="dag3" value="Gagnasofn">Gagnasofn
  </fieldset>

  <h4>upplýsingar um pöntunina:</h4>
  <label>Nafn:</label>
  <fieldset>
    <legend></legend>
      <input type="text" name="nafn" required
      % if err == 1 or err == 3:
        placeholder="VILLA"
      % else:
        placeholder="Nafnið þitt"
      % end
      >

      <label>Heimilisfang:</label>
      <input type="text" name="heim" required
      % if err == 2 or err == 3:
        placeholder="VILLA"
      % else:
        placeholder="Heimilisfangið þitt"
      % end
      >

      <label>Netfang:</label>
      <input type="email" name="email" placeholder="Netfangið þitt" required>

      <label>Símanúmer:</label>
      <input type="text" name="simi" pattern="^(\+354 )?\d{3}[ -]?\d{4}$"/ placeholder="Símanúmerið þitt" required>

      <label>Klára pöntun</label>
      <button type="submit">Panta</button>
  </fieldset>
</form>
