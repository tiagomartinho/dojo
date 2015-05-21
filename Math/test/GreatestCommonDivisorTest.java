import static org.junit.Assert.*;

import org.junit.Test;

public class GreatestCommonDivisorTest {

	@Test
	public void reflexive() throws Exception {
		assertEquals(1, gcd(1, 1));
		assertEquals(2, gcd(2, 2));
		assertEquals(-1, gcd(-1, -1));
	}

	@Test
	public void relativelyPrimes() throws Exception {
		assertEquals(1, gcd(2,3));
		assertEquals(1, gcd(4,7));
		assertEquals(-1, gcd(-2,-3));
	}
	
	@Test
	public void oneIsMultpleOfTheOther() throws Exception {
		assertEquals(3, gcd(3,9));
		assertEquals(5, gcd(5,30));
	}
	
	private int gcd(int a, int b) {
		while(b!=0){
			int t = b;
			b = a % t;
			a = t;
		}
		return a;
	}

}
