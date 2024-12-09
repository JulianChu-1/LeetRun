package Marscode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class T5 {
    public static int[] solution(int n, int max, int[] array) {
        Map<Integer, Integer> rankMap = new HashMap<>();
        Map<Integer, Integer> map = new HashMap<>();
        List<int[]> list = new ArrayList<>();

        for (int i = 1; i <= 13; i++){
            rankMap.put(i, i == 1 ? 14 : i);
        }

        for (int card : array) {
            map.put(card, map.getOrDefault(card, 0) + 1);
        }

        for (int key1 : map.keySet()) {
            if (map.get(key1) >= 3) {
                for (int key2 : map.keySet()) {
                    if (key1 != key2 && map.get(key2) >= 2) {
                        int sum = key1 * 3 + key2 * 2;
                        if (sum <= max) {
                            list.add(new int[]{key1, key2});
                        }
                    }
                }
            }
        }

        if (list.isEmpty()) {
            return new int[]{0, 0};
        }

        list.sort((a, b) -> {
            int A1 = rankMap.get(a[0]);
            int B1 = rankMap.get(b[0]);
            if (B1 != A1) {
                return Integer.compare(B1, A1);
            } else {
                int A2 = rankMap.get(a[1]);
                int B2 = rankMap.get(b[1]);
                return Integer.compare(B2, A2);
            }
        });

        return list.get(0);
    }

    public static void main(String[] args) {
        // Add your test cases here

        System.out.println(java.util.Arrays.equals(solution(9, 34, new int[]{6, 6, 6, 8, 8, 8, 5, 5, 1}), new int[]{8, 5}));
        System.out.println(java.util.Arrays.equals(solution(9, 37, new int[]{9, 9, 9, 9, 6, 6, 6, 6, 13}), new int[]{6, 9}));
        System.out.println(java.util.Arrays.equals(solution(9, 40, new int[]{1, 11, 13, 12, 7, 8, 11, 5, 6}), new int[]{0, 0}));
    }
}
