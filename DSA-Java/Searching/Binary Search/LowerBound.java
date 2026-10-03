public class LowerBound{
    public static void main(String[] args){
        int arr[] = {10,20,20,30,40,50};
        int target = 25;
        int low = 0;
        int high = arr.length - 1;
        int result = -1;
        while(low <= high) {
            int mid = low + (high - low) / 2;
            if(arr[mid] >= target) {
                result = mid;
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
        }
        System.out.println("Lower Bound : " + result);
    }
}