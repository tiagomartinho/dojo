import pytest
import re

def templateEngine(expression,mapOfVariables):
	variablesInExpression=extractVariables(expression)
	return replaceVariables(expression,mapOfVariables,variablesInExpression)

REGEX_TO_EXTRACT_VARIABLES = "\${(\w*)}"
def extractVariables(expression):
	return list(set(re.findall(REGEX_TO_EXTRACT_VARIABLES,expression)))

def replaceVariables(expression,mapOfVariables,variablesInExpression):
	for variable in variablesInExpression:
		expression = replaceVariable(expression,mapOfVariables,variable)
	return expression

def replaceVariable(expression,mapOfVariables,variable):
	if variable in mapOfVariables.keys():
		return expression.replace("${"+variable+"}",mapOfVariables[variable])
	raise Exception("missing value exception")

#TESTS
def test_singleVariableExpression():
	assert templateEngine("Hello ${name}", {"name": "Tiago"}) == "Hello Tiago"

def test_doubleVariableExpression():
	assert templateEngine("Hello ${firstName} ${lastName}", {"firstName": "Tiago","lastName":"Martinho"}) == "Hello Tiago Martinho"

def test_emptyMap():
	with pytest.raises(Exception) as excinfo:
		templateEngine("Hello ${name}", {}) 
	assert excinfo.value.message == 'missing value exception'

def test_complexCase():
	assert templateEngine("Hello ${${name}}", {"name": "Tiago"}) == "Hello ${Tiago}"
