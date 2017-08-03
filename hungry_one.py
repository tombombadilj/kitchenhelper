import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session


app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_game():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("FoodIntent")

def checking(first, second, third):
    home = [first, second, third]
    reply = "I see, you have " + " ".join(home) + "When do you want to eat?"
    return question(reply)

@ask.intent("TimeIntent")

def timing(time):
	recipes = {
    "recipe1":{
    "name":"Tomato and Avocado Salad",
    "prep_time_n":10,
    "prep_time":"Ten Minutes",
    "servings":"four servings",
    "description":"This easy salad, featuring a colorful array of summer tomatoes and creamy avocado, makes a good side dish with grilled steak or chicken, or fried catfish."
    },

    "recipe2":{
    "name":"Cremay Avocado Pasta Salad",
    "prep_time":"twenty Minutes",
    "prep_time_n":20,
    "servings": "six servings",
    "description": "The secret ingredient in this creamy avocado pasta salad will shock you! This avocado pasta salad is easy, creamy, vibrant, fresh and so satisfying!"
    }}  

	if time == "now" or time == "in ten minutes" or time == "in fifteen minutes" or time == "in five minutes":
		for i in recipes:
			if recipes[i]["prep_time_n"] <= 10:
				response = "How does " + recipes[i]["name"] + " sound?" + "it will take about " + recipes[i]["prep_time"] + " to prepare."
	else:
		for i in recipes:
			if recipes[i]["prep_time_n"] > 10: 
				response  = "How does " + recipes[i]["name"] + " sound?" + "you might have to buy some additional items, and will take " + recipes[i]["prep_time"] + " to prepare."
	return statement(response)

if __name__ == '__main__':

    app.run(debug=True)