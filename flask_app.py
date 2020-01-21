from flask import Flask
from flask import jsonify
from flask import request
from flask import redirect

app = Flask(__name__)

tasks = []


def get_table_of_tasks():
    str_table = '''
        <table class = "table" style="width:100%">
            <tr>
                <th scope = "col">Name</th>
                <th scope = "col">Time</th>
            </tr>
        '''
    for task in tasks:
        str_table = str_table + "<tr>"
        str_table = str_table + "<td>" + task["name"] + "</td>"
        str_table = str_table + "<td>" + task["time"]["hour"] + ":" + task["time"]["minute"] + "</td>"
        str_table = str_table + "</tr>"
    str_table = str_table + '''
    </table>

    '''
    return str_table


@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html>
        <head>
        <title>Tasks</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
        </head>
        <body>
        <div class = "container">
            <h1>Add Task</h1>
            <form action = "/add_task_with_param">
                <div class="form-group">
                    <label for="name">Task Name</label>
                    <input type="text" class="form-control" id="name" name = "name">
                    </div>
                <div class="form-group">
                    <label for="hour">Time Due (hour)</label>
                    <input type="number" class="form-control" id="hour" name = "hour">
                    </div>
                <div class="form-group">
                    <label for="minute">minute</label>
                    <input type="number" class="form-control" id="minute" name = "minute">
                    </div>
                <input type= "submit" class="btn btn-primary"></input>
            </form>
        </div>
        <div class = container>
        <h1>Tasks</h1>
        ''' + get_table_of_tasks() + '''
        </div>
        </body>
    </html>
    '''


@app.route("/get_task/")
def get_task():
    return jsonify(tasks)


@app.route("/add_task/<name>/<hour>/<minute>")
def add_task(name, hour, minute):
    tasks.append({"name": name, "time": {"hour": hour, "minute": minute}})
    return redirect("/")


@app.route("/add_task_with_param/")
def add_task_with_param():
    name = request.args.get('name')
    hour = request.args.get('hour')
    minute = request.args.get('minute')
    tasks.append({"name": name, "time": {"hour": hour, "minute": minute}})
    return redirect("/")
