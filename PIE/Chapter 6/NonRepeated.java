import java.util.HashMap; 

public class NonRepeated {

    public static void main(String[] args) {
        System.out.println("Finding the first non-repeated character in a string");
        System.out.println("Testing 'total', got: " + firstNonRepeated("total"));
        System.out.println("Testing 'teeter', got: " + firstNonRepeated("teeter"));
    }

    public static Character firstNonRepeated(String s) {
        HashMap<Character, Integer> tracker = new HashMap<Character, Integer>();
        int i;
        Character c;
        // counting the characters
        for (i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (tracker.containsKey(c)) {
                tracker.put(c, tracker.get(c) + 1);
            } else {
                tracker.put(c, 1);
            }
        }

        // find the first non-repeated letter
        for (i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (tracker.get(c) == 1) return c;
        } 
        
        // found nothing
        return null;
    }
}