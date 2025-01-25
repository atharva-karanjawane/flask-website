from flask import Flask, render_template,jsonify

app = Flask(__name__)

# Simulating data for courses (You can replace this with actual database queries)
COURSES = [
    {'id': 4, 'title': 'Graphic Designing', 'instructor': 'Shruti', 'price': 'Rs.17999'},
    {'id': 5, 'title': 'Web Development', 'instructor': 'Rahul', 'price': 'Rs.12999'},
    {'id': 6, 'title': 'Digital Marketing', 'instructor': 'Priya', 'price': 'Rs.14999'},
    
]

@app.route("/")
def courses():
    return render_template("courses.html", courses=COURSES)

@app.route("/api/courses")
def list_courses():
    return jsonify(COURSES)
if __name__ == "__main__":
    app.run(debug=True)
