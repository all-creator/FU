import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import com.lab2.Vector3;

class VectorTests {

    @Test
    @DisplayName("Vector sum")
    void testVectorSum() {
        assertEquals(new Vector3(2,1,1), new Vector3(1, 0, 0).sum(new Vector3(1,1, 1)));
    }

    @Test
    @DisplayName("Vector minus")
    void testVectorMinus() {
        assertEquals( new Vector3(0,1,1), new Vector3(1, 1, 1).minus(new Vector3(1,0, 0)));
    }

    @Test
    @DisplayName("Vector abs")
    void testVectorAbs() {
        assertEquals(5, Math.round(new Vector3(1, 3, 4).abs()));
    }

    @Test
    @DisplayName("Vector scalar")
    void testVectorScalar() {
        assertEquals(1.0, new Vector3(1, 3, 4).scalar(new Vector3(1,0, 0)));
    }

    @Test
    @DisplayName("Vector vector vel")
    void testVectorVecVel() {
        assertEquals(new Vector3(0,4, -3), new Vector3(1, 3, 4).vector(new Vector3(1,0, 0)));
    }

    @Test
    @DisplayName("Vector angle")
    void testVectorAngle() {
        assertTrue(new Vector3(1, 3, 4).angle(new Vector3(1,0, 0)) > 1.37 && new Vector3(1, 3, 4).angle(new Vector3(1,0, 0)) < 1.38);
    }
}