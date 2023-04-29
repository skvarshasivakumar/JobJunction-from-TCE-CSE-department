event=input("enter event name:")
link=input("enter form link:")
string=  """<div class="col">
          <div class="card" style="width: 18rem;">
            <img src="css/sem1.jpg" class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">"""+event+"""</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href=" """+link+ """ "class="btn btn-primary">Take test</a>
            </div>
          </div>
        </div>
     """
print(string)
