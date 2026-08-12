public class Fundamentals {

    public static void main(String[] args) {

        // Create array
        int[] arr = {10, 20, 30, 40, 50};

        // Length
        System.out.println("Length: " + arr.length);

        // Access
        System.out.println("Element at index 2: " + arr[2]);

        // Update
        arr[2] = 100;

        // Traversal
        System.out.println("Array:");

        for (int i = 0; i < arr.length; i++) {
            System.out.println(
                "Index " + i + " = " + arr[i]
            );
        }
    }
}