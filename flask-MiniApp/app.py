from flask import request, Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
  message = "Message ;)"
  numbers = [1,2,3,4,5,6,7]

  return render_template("index.html", message = message , numbers = numbers)

@app.route("/toplam", methods = ["GET", "POST"])
def toplam():
  if request.method == 'POST':
    number1 = request.form.get("number1")
    number2 = request.form.get("number2")
    return render_template("number.html", total = int(number1) + int(number2))
  else:
    return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(debug = True)
