public class Fraction {
	private final int numerator;
	private final int denominator;

	public Fraction(int integerValue) {
		this(integerValue, 1);
	}

	public Fraction(int numerator, int denominator) {
		final int signOfDenominator = denominator < 0 ? -1 : 1;
		final int gcd = NumberTheory.gcd(numerator, denominator)
				* signOfDenominator;
		if (gcd == 0 || denominator == 0) {
			this.numerator = 0;
			this.denominator = 1;
		} else {
			this.numerator = numerator / gcd;
			this.denominator = denominator / gcd;
		}
	}

	public Fraction plus(Fraction that) {
		return new Fraction(numerator * that.denominator + that.numerator
				* denominator, denominator * that.denominator);
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
