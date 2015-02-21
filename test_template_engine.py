def templateEngine(expression,mapOfVariables):
	for variable in mapOfVariables:
		expression = expression.replace("${"+variable+"}",mapOfVariables[variable])
	return expression 

#TESTS
def test_singleVariableExpression():
	assert templateEngine("Hello ${name}", {"name": "Tiago"}) == "Hello Tiago"

def test_doubleVariableExpression():
	assert templateEngine("Hello ${firstName} ${lastName}", {"firstName": "Tiago","lastName":"Martinho"}) == "Hello Tiago Martinho"
