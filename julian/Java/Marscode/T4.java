package Marscode;

public class T4 {
    public static int solution(int[] numbers) {
        int even_count = 1;
        int odd_count = 0;

        for (int i = 0; i < numbers.length; i++) {
            String s = String.valueOf(numbers[i]);
            int even = 0;
            int odd = 0;

            for (char c : s.toCharArray()) {
                int num = c - '0';
                if (num % 2 == 0) {
                    even++;
                } else {
                    odd++;
                }
            }

            int new_even_count = even_count * even + odd_count * odd;
            int new_odd_count = even_count * odd + odd_count * even;
            even_count = new_even_count;
            odd_count = new_odd_count;
        }

        return even_count;
    }

    public static void main(String[] args) {
        // You can add more test cases here
        System.out.println(solution(new int[]{123, 456, 789}) == 14);
        System.out.println(solution(new int[]{123456789}) == 4);
        System.out.println(solution(new int[]{14329, 7568}) == 10);
    }
}
