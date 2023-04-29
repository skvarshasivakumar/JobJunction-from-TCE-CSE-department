title=input("Enter contest title")
first=input("Enter winner one name")
second=input("enter runner name")
third=input("enter 3rd prize winner name")
string="""<body>
    <div style="margin:5%;padding:10%;" class="row" id="sample">
      <div style="margin-bottom:30px;" class="full heading_s5">
        <center>
          <h2 id="welcome">"""+title+"""</h2>
        </center>
      </div>
      <div class="col-md-4 text_align_center">

        <center>
          <h3>"""+first+"""</h3>
          <p>A 3rd year student has won First Prize</p>
        </center>
      </div>
      <div class="col-md-4 text_align_center">
        <center>
          <h3>"""+second+"""</h3>
          <p>A 3rd year student has won Second Prize</p>
        </center>
      </div>
      <div class="col-md-4 text_align_center">

        <center>
          <h3>"""+third+"""</h3>
          <p>A 2nd year student has won Third Prize</p>
        </center>

      </div>

    </div>
    <section>

    </section>"""
print(string)
