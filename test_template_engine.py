def templateEngine(expression,mapOfVariables):
	return "" 

#TESTS
def test_singleVariableExpression():
	assert templateEngine("Hello {$name}", {"name": "Tiago"}) == "Hello Tiago"

