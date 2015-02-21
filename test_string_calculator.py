def add(numbers):
	delimiters=getDelimiters(numbers) 
	numbersSplitted=splitNumbers(numbers,delimiters)
	return getSumResult(numbersSplitted)

CUSTOM_DELIMITERS = [',']
STRING_BEGINNING="//"
def getDelimiters(numbers):
	delimiters=CUSTOM_DELIMITERS
	if numbers.startswith(STRING_BEGINNING):
		delimitersArgs = numbers[len(STRING_BEGINNING):numbers.find('\n')]
		delimiters = delimitersArgs.replace("]",'')
		delimiters = delimiters.split('[')
		if '' in delimiters:
			delimiters.remove('')
	return delimiters

def splitNumbers(numbers,delimiters):
	if numbers.startswith(STRING_BEGINNING):
		numbers = numbers[numbers.find('\n'):]
	for delimiter in delimiters:
		numbers = numbers.replace(delimiter,' ')
	return numbers.split()

def getSumResult(numbersSplitted):
	result=0
	for number in numbersSplitted:
		result+=convertStringToInt(number)
	return result

def convertStringToInt(number):
	if number != "" and int(number)<=1000:
		print(number)
		return int(number)
	else:
		return 0

#TESTS
def test_emptyString():
	assert add("")==0

def test_oneDigitString():
	assert add("1")==1
	assert add("25")==25

def test_twoDigitString():
	assert add("1,2")==3
	assert add("11,22")==33

def test_malformedComma():
	assert add("1,,2")==3

def test_threeDigitString():
	assert add("1,2,3")==6

def test_manyDigitString():
	assert add("1,2,3,6")==12

def test_threeDigitStringSeparatedByNewLine():
	assert add("1\n2\n3")==6

def test_threeDigitStringSeparatedByCommaAndNewLine():
	assert add("1\n2,3")==6

def test_oneDigitStringSeparatedByCommaAndNewLine():
	assert add("1\n,")==1

def test_customDelimitorsSemicolon():
	assert add("//;\n1;2;3")==6

def test_customDelimitorsColon():
	assert add("//:\n9:1:2")==12

def test_customDelimitorsAnySize():
	assert add("//***\n9***1***2")==12

def test_anyNumberCustomDelimitorse():
	assert add("//[*][%]\n1*2%3")==6

def test_negativeNumbers():
	assert add("//:\n-9:1:2")==-6

def test_ignoreBigNumbers():
	assert add("1,1001,3")==4

def test_customWeirdDelimiter():
	assert add("//[*2*]\n3*2*4")==7

def test_anyNumberCustomDelimitorsAnySize():
	assert add("//[***][:]\n9***1:2")==12

def test_emptySpaceAsDelimiter():
	assert add("// \n3 2 4")==9

def test_slashSlashAsDelimiter():
	assert add("////\n3//2//4")==9
