import java.util.HashMap;

public class Unique {
    public static void main(String[] args) {
        // Testing 1.1
        test_1_1();
    }

    // 1.1
    public static boolean isUnique(String s) {
        HashMap<Character, Boolean> tracker = new HashMap<Character, Boolean>();
        for (char c : s.toCharArray()) {
            if (tracker.containsKey(c)) {
                return false;
            } else {
                tracker.put(c, true);
            }
        }

        return true;
    }

    public static void test_1_1() {
        // Testing Problem 1.1
        String test1 = "unique";
        System.out.println("Testing the string: " + test1);
        String result1 = isUnique(test1)? "Unique" : "Not Unique";
        System.out.println("Got: " + result1);

        String test2 = "racecar";
        System.out.println("Testing the string: " + test2);
        String result2 = isUnique(test2)? "Unique" : "Not Unique";
        System.out.println("Got: " + result2);
    }
}