package data_structures.array;

import java.util.Arrays;
import java.util.List;

public class DemoStringBuilder {

	public static void main(String[] args) {

		List<String> list = Arrays.asList("oak", "pine", "fir", "ash", "birch", "elm", "yew");
		System.out.println(listToString(list));
	}

	private static String listToString(List<String> list) {

		StringBuilder sb = new StringBuilder(32);

		list.forEach(ele -> {

			sb.append(ele).append(" ");
		});

		return sb.toString();
	}
}