import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class HashSetExample {

	public static void main(String args[]) {

		Set<Integer> intSet = new HashSet<>();
		Random rand = new Random();
		for(int i = 0; i < 10; i++)
			intSet.add(rand.nextInt() & Integer.MAX_VALUE);

		
		intSet.forEach(ele -> {
			System.out.println(ele);
		});
			
	}
}