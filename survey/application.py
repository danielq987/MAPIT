from flaskr import app

app = Flask(__name__)

db = SQL("sqlite:///survey.db")

@app.route('/')
def index():
    rows = db.execute("SELECT * FROM survey")
    return render_template("survey.html", rows=rows)