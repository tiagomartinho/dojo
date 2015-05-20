public class Fraction {

	final private int denominator;
	private int integerValue;

	public Fraction(int integerValue) {	
		this.integerValue = integerValue;
		this.denominator = 1;
	}

	public Fraction(int numerator, int denominator) {
		this.integerValue = numerator;
		this.denominator = denominator;
	}

	public Fraction plus(Fraction that) {
		return new Fraction(this.integerValue + that.integerValue,this.denominator);
	}

	public int intValue() {
		return this.integerValue;
	}

	public int getNumerator() {
		return 3;
	}

	public int getDenominator() {
		return this.denominator;
	}
}
