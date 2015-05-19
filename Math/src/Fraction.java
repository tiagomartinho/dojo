public class Fraction {

	private int integerValue;

	public Fraction(int integerValue) {
		this.integerValue = integerValue;
	}

	public Fraction plus(Fraction that) {
		if (that.integerValue != 0)
			return new Fraction(this.integerValue + that.integerValue);
		else
			return this;
	}

	public int intValue() {
		return this.integerValue;
	}
}
