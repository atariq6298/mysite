from flask import Flask
from flask import jsonify

app = Flask(__name__)

tasks = []


def get_table_of_tasks():
    str_table = '''
        <table style="width:100%">
            <tr>
                <th>Name</th>
                <th>Time</th>
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
        </head>
        <body>
        <h1>Add Task</h1>
        <div>
            <form>
                <label>Task Name:</lable>
                <input name = "task_name">
                </input>
                <label>Time Due:</lable>
                <input name = "time_due">
                </input>
                <input type= "submit"></input>
            </form>
        </div>
        <h1>Tasks</h1>
        ''' + get_table_of_tasks() + '''
        </body>
    </html> 
    '''


@app.route("/get_task/")
def get_task():
    return jsonify(tasks)


@app.route("/add_task/<name>/<hour>/<minute>")
def add_task(name, hour, minute):
    tasks.append({"name": name, "time": {"hour": hour, "minute": minute}})
    return "added " + name + " due at " + hour + ":" + minute


