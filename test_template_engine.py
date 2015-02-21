import pytest
import re

def templateEngine(expression,mapOfVariables):
	variablesInExpression=extractVariables(expression)
	for variable in variablesInExpression:
		if variable in mapOfVariables.keys():
			expression = expression.replace("${"+variable+"}",mapOfVariables[variable])
		else:
			raise Exception("missing value exception")
	return expression 

def extractVariables(expression):
	return list(set(re.findall("\${(\w*)}",expression)))

#TESTS
def test_singleVariableExpression():
	assert templateEngine("Hello ${name}", {"name": "Tiago"}) == "Hello Tiago"

def test_doubleVariableExpression():
	assert templateEngine("Hello ${firstName} ${lastName}", {"firstName": "Tiago","lastName":"Martinho"}) == "Hello Tiago Martinho"

def test_emptyMap():
	with pytest.raises(Exception) as excinfo:
		templateEngine("Hello ${name}", {}) 
	assert excinfo.value.message == 'missing value exception'
