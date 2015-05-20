public class Fraction {
	private final int numerator;
	private final int denominator;

	public Fraction(int integerValue) {	
		this(integerValue, 1);
	}

	public Fraction(int numerator, int denominator) {
		this.numerator = numerator;
		this.denominator = denominator;
	}

	public Fraction plus(Fraction that) {
		return new Fraction(numerator + that.numerator,denominator);
	}

	public int intValue() {
		return numerator/denominator;
	}

	public int getNumerator() {
		return numerator;
	}

	public int getDenominator() {
		return denominator;
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + denominator;
		result = prime * result + numerator;
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Fraction other = (Fraction) obj;
		if (denominator != other.denominator)
			return false;
		if (numerator != other.numerator)
			return false;
		return true;
	}

	@Override
	public String toString() {
		return "Fraction [numerator=" + numerator + ", denominator="
				+ denominator + "]";
	}
}
