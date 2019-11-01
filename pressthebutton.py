from flask import Flask, render_template, request, Response, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

def gather_stylsheets_for(route):
	# '/' -> 'style/*.css'
	#
	print("Doing stuff...")

def gather_stylesheets():
	stylesheets = []

	stylesheets.append(url_for('static', filename='style/root.css'))
	stylesheets.append(url_for('static', filename='style/zero.css'))
	stylesheets.append(url_for('static', filename='style/box.css'))
	stylesheets.append(url_for('static', filename='style/main.css'))

	return stylesheets

def gather_scripts():
	scripts = []

	scripts.append(url_for('static', filename='script/application.js'))
	scripts.append(url_for('static', filename='script/main.js'))

	return scripts


count = 0

@app.errorhandler(404)
def not_found(err):
	print(err)
	stylesheets = gather_stylesheets()
	scripts = gather_scripts()
	return render_template('404.html', stylesheets=stylesheets, scripts=scripts)

@app.route('/')
def index():
	count = 0
	stylesheets = gather_stylesheets()
	scripts = gather_scripts()
	return render_template('index.html', stylesheets=stylesheets, scripts=scripts, count=count)

# @app.route('/', methods=['GET', 'POST'])
# def index():
# 	global count

# 	print("Index route hit.")

# 	stylesheets = gather_stylesheets()
# 	scripts = gather_scripts()

# 	if request.method == 'POST':
# 		count += 1
# 		data = {
# 			'count': count
# 		}
# 		return data

# 	elif request.method == 'GET':
# 		return render_template('layout.html', stylesheets=stylesheets, scripts=scripts, count=count)

if __name__ == "__main__":
	app.run(host='127.0.0.1', port='5005')