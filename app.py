from flask import Flask, request, render_template_string

app = Flask(__name__)

# Hardcoded mock data
patients = [
    {"id": 1, "name": "Alice Smith", "history": "Allergic to penicillin"},
    {"id": 2, "name": "Bob Jones", "history": "Type 2 Diabetes"}
]

@app.route('/', methods=['GET', 'POST'])
def update_patient():
    message = ""
    if request.method == 'POST':
        patient_id = int(request.form.get('id'))
        new_history = request.form.get('new_history')
        for p in patients:
            if p['id'] == patient_id:
                p['history'] = new_history
                message = f"Updated record for {p['name']}."
                break

    html = '''
        <h2>Patient Records - v3 (Update)</h2>
        <p style="color: green;">{{ message }}</p>
        <table border="1" cellpadding="5">
            <tr><th>ID</th><th>Name</th><th>History</th><th>Action</th></tr>
            {% for p in patients %}
            <tr>
                <td>{{ p.id }}</td>
                <td>{{ p.name }}</td>
                <td>{{ p.history }}</td>
                <td>
                    <form method="POST" style="margin:0;">
                        <input type="hidden" name="id" value="{{ p.id }}">
                        <input type="text" name="new_history" placeholder="New History" required>
                        <input type="submit" value="Update">
                    </form>
                </td>
            </tr>
            {% endfor %}
        </table>
    '''
    return render_template_string(html, patients=patients, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)