from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<task>')
def delete_task(task):
    if task in tasks:
        tasks.remove(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8087, debug=False, use_reloader=False)  # <-- debug=False is important
