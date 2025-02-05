package Marscode;

public class T11 {
    public static int solution(int[] values) {
        // write code here
        int maxScore = 0;
        int leftMax = values[0];

        for (int j = 1; j < values.length; j++) {
            maxScore = Math.max(maxScore, leftMax + values[j] - j);
            leftMax = Math.max(leftMax, values[j] + j);
        }

        return maxScore;
    }

    public static void main(String[] args) {
        System.out.println(solution(new int[]{8, 3, 5, 5, 6}) == 11 ? 1 : 0);
        System.out.println(solution(new int[]{10, 4, 8, 7}) == 16 ? 1 : 0);
        System.out.println(solution(new int[]{1, 2, 3, 4, 5}) == 8 ? 1 : 0);
    }
}
