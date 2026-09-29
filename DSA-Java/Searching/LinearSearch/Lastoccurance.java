public class Lastoccurance{
    public static void main(String[] args){
        int[] arr = {10, 20, 30 , 20, 40, 20};
        int target = 20;
        int Lastindex = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target){
                Lastindex = i;
            }
        }
        if (Lastindex != -1) {
            System.out.println("LastIndex :" + Lastindex);
        } else {
            System.out.println("element not found");
        }
    }
}