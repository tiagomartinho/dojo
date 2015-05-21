import static org.junit.Assert.*;

import org.junit.Test;

public class GreatestCommonDivisorTest {

	@Test
	public void reflexive() throws Exception {
		assertEquals(1, NumberTheory.gcd(1, 1));
		assertEquals(2, NumberTheory.gcd(2, 2));
		assertEquals(1, NumberTheory.gcd(-1, -1));
	}

	@Test
	public void relativelyPrimes() throws Exception {
		assertEquals(1, NumberTheory.gcd(2, 3));
		assertEquals(1, NumberTheory.gcd(4, 7));
		assertEquals(1, NumberTheory.gcd(-2, -3));
	}

	@Test
	public void oneIsMultpleOfTheOther() throws Exception {
		assertEquals(3, NumberTheory.gcd(3, 9));
		assertEquals(5, NumberTheory.gcd(5, 30));
	}

	@Test
	public void commonFactor() throws Exception {
		assertEquals(2, NumberTheory.gcd(6, 8));
		assertEquals(7, NumberTheory.gcd(49, 315));
	}

	@Test
	public void negatives() throws Exception {
		assertEquals(4, NumberTheory.gcd(-24, 28));
		assertEquals(4, NumberTheory.gcd(24, -28));
	}
}
