import static org.junit.Assert.*;
import jdk.nashorn.internal.ir.annotations.Ignore;

import org.junit.Test;

public class AddFractionsTest {
	
	@Test
	public void zeroPlusZero() throws Exception {
		assertEquals(new Fraction(0), new Fraction(0).plus(new Fraction(0)));
	}
	
	@Test
	public void nonZeroPlusZero() throws Exception {
		assertEquals(new Fraction(3), new Fraction(3).plus(new Fraction(0)));
	}
	
	@Test
	public void zeroPlusNonZero() throws Exception {
		assertEquals(new Fraction(5), new Fraction(0).plus(new Fraction(5)));
	}
	
	@Test
	public void nonNegativeNonZeroOperands() throws Exception {
		assertEquals(new Fraction(7), new Fraction(3).plus(new Fraction(4)));
	}
	
	@Test
	public void negativeInputAndNegativeOutput() throws Exception {
		assertEquals(new Fraction(-2), new Fraction(-3).plus(new Fraction(1)));
	}
	
	@Test
	public void nonTrivialCommonDenominator() throws Exception {
		assertEquals(new Fraction(3,5), new Fraction(1,5).plus(new Fraction(2,5)));
	}
	
	@Test
	public void differentDenominatorsWithoutReducing() throws Exception {
		assertEquals(new Fraction(5,6), new Fraction(1,2).plus(new Fraction(1,3)));
	}
	
	@Test
	public void reduceResultToWholeNumber() throws Exception {
		assertEquals(new Fraction(1), new Fraction(1,3).plus(new Fraction(2,3)));
	}	
	
	@Test
	public void oneDenominatorIsMultipleOfAnother() throws Exception {
		assertEquals(new Fraction(11,8), new Fraction(3,4).plus(new Fraction(5,8)));
	}
	
	@Test
	public void commonFactorInDenominators() throws Exception {
		assertEquals(new Fraction(11,18), new Fraction(1,6).plus(new Fraction(4,9)));
	}
	
	@Test
	public void reduceResultEvenWhenDenominatorsAreTheSame() throws Exception {
		assertEquals(new Fraction(3,2), new Fraction(3,4).plus(new Fraction(3,4)));
	}
	
	@Test
	public void negativeFractionAndReducing() throws Exception {
		assertEquals(new Fraction(1,2), new Fraction(-1,4).plus(new Fraction(3,4)));
		assertEquals(new Fraction(-1,8), new Fraction(3,8).plus(new Fraction(-1,2)));
	}

	@Test
	public void crazyNegatives() throws Exception {
		assertEquals(new Fraction(1,2), new Fraction(1,-4).plus(new Fraction(-3,-4)));
	}
	
	@Test
	public void zeroDenominator() throws Exception {
		assertEquals(new Fraction(1,4), new Fraction(1,4).plus(new Fraction(-3,0)));
		assertEquals(new Fraction(1,4), new Fraction(1,4).plus(new Fraction(0,0)));
	}
}
