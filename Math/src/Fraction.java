public class Fraction {

	private int integerValue;

	public Fraction(int integerValue) {
		this.integerValue = integerValue;
	}

	public Fraction plus(Fraction fraction) {
		if (fraction.integerValue != 0)
			return fraction;
		else
			return this;
	}

	public int intValue() {
		return this.integerValue;
	}

}
