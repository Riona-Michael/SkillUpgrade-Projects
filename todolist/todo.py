from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) #initalising the app, to help locate resources associated with the application using current module __name__
# Define an empty list to store tasks
tasks = []
# Define route for the home page
@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

# Define route for adding tasks
@app.route('/add', methods=['POST']) #add_task() function should handle POST requests sent to the '/add' URL path
def add_task():
    task = request.form['task'] #retrieves data from the form submitted with the POST request,Specifically, it accesses the value of the 'task' field from the form data
    tasks.append(task)
    return redirect(url_for('home')) #redirects the user to a different URL after the task has been added
#

if __name__ == '__main__':
    app.run(debug=True)
