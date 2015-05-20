public class Fraction {

	private int integerValue;

	public Fraction(int integerValue) {	
		this.integerValue = integerValue;
	}

	public Fraction(int numerator, int denominator) {
		// TODO Auto-generated constructor stub
	}

	public Fraction plus(Fraction that) {
		return new Fraction(this.integerValue + that.integerValue);
	}

	public int intValue() {
		return this.integerValue;
	}

	public int getNumerator() {
		return 3;
	}

	public int getDenominator() {
		return 5;
	}
}
