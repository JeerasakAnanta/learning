package arrays;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class SearchingAlgorithms {
    public static void main(String[] args) {

        List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        int intkey = 6;

        // Linear search
        System.out.println("linerar Search: " + list.contains(intkey));

        // Binaray search using Collections binarySearch
        // list must be sorted
        int index = Collections.binarySearch(list, intkey);

        System.out.println(index);
        if (index > 0) {
            System.out.println("Element found at index:" + index);

        } else {
            System.out.println("Element not found");
        }
    }
}
