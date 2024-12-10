package Marscode;

import java.util.HashMap;
import java.util.Map;

public class T8 {
    public static int solution(int[] array) {
        Map<Integer, Integer> map = new HashMap<>();
        int max_value = 0;
        int res = 0;

        for (int num : array) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() > max_value) {
                max_value = entry.getValue();
                res = entry.getKey();
                System.out.println(res);
            }
        }

        return res;
    }

    public static void main(String[] args) {
        // Add your test cases here

        System.out.println(solution(new int[]{1, 3, 8, 2, 3, 1, 3, 3, 3}) == 3);
    }
}
