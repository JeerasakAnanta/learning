import java.util.ArrayList;
import java.util.Arrays;

public class Array {

    public static void main(String[] args) {
        System.out.println("Arrays");
        int[] arr = { 10, 20, 30, 40, 50 };

        // sorting arrays
        Arrays.sort(arr);
        System.out.println(arr);
        System.out.println(Arrays.toString(arr));

        // Arrays list exampl
        ArrayList<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(20);
        list.add(30);
        System.out.println(list);
    }
}
