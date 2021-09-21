import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

public class DemoStrings {

	public static void main(String[] args) {

		List<String> list = Arrays.asList("oak", "pine", "fir", "ash", "birch", "elm", "yew");
		
		listToString(list).forEach(str -> System.out.println(str));
	}

	private static List<String> listToString(List<String> list) {

		// StringBuilder
		StringBuilder sb = new StringBuilder(32);

		list.forEach(ele -> sb.append(ele).append(" "));

		// String
		String str = "";

		for(String ele : list) str += ele + " ";

		return new ArrayList<>(Arrays.asList(str, sb.toString()));
	}

		public void palindrome() {
			String palindrome = "Dot saw I was Tod";
			int len = palindrome.length();
			char[] tempCharArray = new char[len];
			char[] charArray = new char[len];
			
			// put original string in an 
			// array of chars
			for (int i = 0; i < len; i++) {
				tempCharArray[i] = 
					palindrome.charAt(i);
			} 
			
			// reverse array of chars
			for (int j = 0; j < len; j++) {
				charArray[j] =
					tempCharArray[len - 1 - j];
			}
			
			String reversePalindrome =
				new String(charArray);
			System.out.println(reversePalindrome);
		}

			public void builderPalindrome() {
				String palindrome = "Dot saw I was Tod";
				 
				StringBuilder sb = new StringBuilder(palindrome);
				
				sb.reverse();  // reverse it
				
				System.out.println(sb);
			}
		
	
}