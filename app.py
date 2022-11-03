from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Entry operator',
    'location': 'Bhimtal, India',
    'salary': 'Rs. 10'
  },
  {
    'id': 2,
    'title': 'Software Developer Engineer',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Full Stack Developer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]

@app.route("/")
def hello_boiis():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Bisht Ji Careers')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)