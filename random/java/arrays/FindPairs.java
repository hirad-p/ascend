
import java.util.Arrays;

public class FindPairs {
	
	public static void main(String[] args) {
		int[] arr = { 8, 7, 2, 5, 3, 1 };
		int sum = 10;
		findPair(arr, sum);
	}
	
	public static void findPair(int[] arr, int sum) {
		// sort the array
		Arrays.sort(arr);
		
		int start = 0; 
		int end = arr.length - 1;
		int result;
		while (start < end) {
			result = arr[start] + arr[end];
			if (result == sum) {
				System.out.println("Pair Found: " + arr[start] + " , " + arr[end] + ".");
				return;
			} 
			
			if (result < sum) {
				start++;
			} else {
				end--;
			}
		}
		
		System.out.println("No pair found");
	}
}
