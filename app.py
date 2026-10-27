from flask import Flask, request, render_template_string

app = Flask(__name__)
patients = []

@app.route('/', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form.get('name')
        history = request.form.get('history')
        patients.append({"name": name, "history": history})
        return f"Patient {name} added. <a href='/'>Go back</a>"
    
    html = '''
        <h2>Patient Records - v1 (Add)</h2>
        <form method="POST">
            Name: <input type="text" name="name" required><br><br>
            Medical History: <textarea name="history" required></textarea><br><br>
            <input type="submit" value="Store Patient History">
        </form>
        <h3>Stored Records (Memory):</h3>
        <ul>
        {% for p in patients %}
            <li><strong>{{ p.name }}</strong>: {{ p.history }}</li>
        {% endfor %}
        </ul>
    '''
    return render_template_string(html, patients=patients)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)