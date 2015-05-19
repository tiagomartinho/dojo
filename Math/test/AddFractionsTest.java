import static org.junit.Assert.*;

import org.junit.Test;


public class AddFractionsTest {
	
	@Test
	public void zeroPlusZero() throws Exception {
		Fraction sum = new Fraction(0).plus(new Fraction(0));
		assertEquals(0, sum.intValue());
	}
	
	@Test
	public void nonZeroPlusZero() throws Exception {
		Fraction sum = new Fraction(3).plus(new Fraction(0));
		assertEquals(3, sum.intValue());
	}
	
	@Test
	public void zeroPlusNonZero() throws Exception {
		Fraction sum = new Fraction(0).plus(new Fraction(5));
		assertEquals(5, sum.intValue());
	}
	
	@Test
	public void nonNegativeNonZeroOperands() throws Exception {
		Fraction sum = new Fraction(3).plus(new Fraction(4));
		assertEquals(7, sum.intValue());
	}
}
