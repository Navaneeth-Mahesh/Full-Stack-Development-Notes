public class UpperBound {
    public static void main(String[] args) {
        int[] arr = {5, 10, 10, 10, 20, 30, 40};
        int target = 10;
        int low = 0;
        int high = arr.length - 1;
        int result = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (arr[mid] > target) {
                result = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        System.out.println("Upper Bound: " + result);
    }
}