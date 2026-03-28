public class sumofarray {

    public static int sum_array(int[] arr) {
        int sum = 0;
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            sum += arr[i];

        }
        return sum;

    }

    public static void main(String[] args) {
        int arr[] = { 3, 1, 2, 5, 4 };

        int result = sum_array(arr);
        System.out.println("sum of array values:  " + result);
    }

}