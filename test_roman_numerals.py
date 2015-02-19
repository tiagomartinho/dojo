numbers_map={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

def roman(number):
	if number == 0:
		return ""

	if number in numbers_map.keys():
		return numbers_map[number]

	for key in sorted(numbers_map, reverse=True):
		if(number>key):
			return roman(key)+roman(number-key)

#TESTS
def check(numberDecimal,numberRoman):
	assert roman(numberDecimal)==numberRoman

def test_zeroIsEmpty():
	check(0,"")

def test_oneTillTen():
	check(1,"I")
	check(2,"II")
	check(3,"III")
	check(4,"IV")
	check(5,"V")
	check(6,"VI")
	check(7,"VII")
	check(8,"VIII")
	check(9,"IX")
	check(10,"X")

def test_elevenTillTwenty():
	check(11,"XI")
	check(12,"XII")
	check(13,"XIII")
	check(14,"XIV")
	check(15,"XV")
	check(16,"XVI")
	check(17,"XVII")
	check(18,"XVIII")
	check(19,"XIX")
	check(20,"XX")

def test_fourty():
	check(40,"XL")

def test_fiftty():
	check(50,"L")

def test_fifttyFour():
	check(54,"LIV")

def test_ninety():
	check(90,"XC")

def test_hundred():
	check(100,"C")
	
def test_fourHundred():
	check(400,"CD")
	
def test_fiveHundred():
	check(500,"D")
	
def test_nineHundred():
	check(900,"CM")

def test_thousand():
	check(1000,"M")

def test_specialCases():
	check(89,"LXXXIX");
	check(145,"CXLV");
	check(691,"DCXCI");
	check(1983,"MCMLXXXIII");
	check(2412,"MMCDXII");
	check(3309,"MMMCCCIX");
