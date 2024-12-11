package Marscode;
import java.util.*;

public class T13 {
    public static int[] solution(int n) {
        //write code here
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            int temp = n;
            while (temp >= i) {
                list.add(temp);
                temp--;
            }
        }

        return list.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        System.out.println(Arrays.equals(solution(3), new int[]{3, 2, 1, 3, 2, 3}));
        System.out.println(Arrays.equals(solution(4), new int[]{4, 3, 2, 1, 4, 3, 2, 4, 3, 4}));
        System.out.println(Arrays.equals(solution(5), new int[]{5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5}));
    }
}
