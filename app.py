from flask import Flask, request, render_template_string

app = Flask(__name__)

# Mock data to test the search functionality
patients = [
    {"name": "Alice Smith", "history": "Allergic to penicillin"},
    {"name": "Bob Jones", "history": "Type 2 Diabetes"},
    {"name": "Charlie Brown", "history": "Asthma"}
]

@app.route('/', methods=['GET', 'POST'])
def search_patient():
    results = []
    if request.method == 'POST':
        search_query = request.form.get('name').lower()
        results = [p for p in patients if search_query in p['name'].lower()]
    
    html = '''
        <h2>Patient Records - v2 (Search)</h2>
        <form method="POST">
            Search by Name: <input type="text" name="name" required>
            <input type="submit" value="Search">
        </form>
        <h3>Search Results:</h3>
        <ul>
        {% for p in results %}
            <li><strong>{{ p.name }}</strong>: {{ p.history }}</li>
        {% else %}
            {% if request.method == 'POST' %}
                <li>No records found.</li>
            {% endif %}
        {% endfor %}
        </ul>
    '''
    return render_template_string(html, results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)