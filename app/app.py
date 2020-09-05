from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

# any app has routes

# define our first route


@app.route('/', methods = ['GET'])
# whenever this route gets called, it will execute a function
def index():
	return "Maximus: My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions, loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next! Maximus Maximum"

# finally lets run our app


if __name__ == '__main__':

	

# all the code that is below here, will only be run when the script is run
	app.run(host='0.0.0.0', port=8000)