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

		//StringBuffer
		StringBuffer sbf = new StringBuffer();		

		return new ArrayList<>(Arrays.asList(str, sb.toString()));
	}
}