from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Dummy list to store registered users
registered_users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Add user to the registered_users list
        registered_users.append({'username': username, 'password': password})
        
        return redirect('/login')
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if user exists in the registered_users list
        for user in registered_users:
            if user['username'] == username and user['password'] == password:
                return redirect('/dashboard')
        
        return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
