from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        username TEXT,
        password TEXT,
        music_preferences TEXT,
        hobbies TEXT,
        favorite_festivity TEXT
    )
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

# Ruta de la página de inicio
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para elegir el rol
@app.route('/choose_role/<role>')
def choose_role(role):
    return render_template('choose_role.html', role=role)

# Ruta para funciones específicas de VECINOS
@app.route('/neighbor_functions')
def neighbor_functions():
    return render_template('neighbor_functions.html')

# Ruta para funciones específicas de ADMINISTRADORES
@app.route('/admin_functions')
def admin_functions():
    return render_template('admin_functions.html')

# Ruta para la página de inicio de sesión
@app.route('/login')
def login():
    return render_template('login.html')

# Ruta para el registro de usuarios
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Manejar el registro en la base de datos
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        music_preferences = ', '.join(request.form.getlist('music_preferences'))
        hobbies = ', '.join(request.form.getlist('hobbies'))
        favorite_festivity = ', '.join(request.form.getlist('favorite_festivity'))

        # Conectar a la base de datos
        conn = sqlite3.connect('usuarios.db')
        cursor = conn.cursor()

        # Insertar usuario en la base de datos
        cursor.execute('INSERT INTO usuarios (name, username, password, music_preferences, hobbies, favorite_festivity) VALUES (?, ?, ?, ?, ?, ?)',
                       (name, username, password, music_preferences, hobbies, favorite_festivity))

        # Guardar los cambios y cerrar la conexión
        conn.commit()
        conn.close()

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
