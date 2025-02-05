package Marscode;

import java.util.*;

public class T14 {
    public static int solution(int n, int k) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += k * i;
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(solution(3, 1) == 6);
        System.out.println(solution(2, 2) == 6);
        System.out.println(solution(4, 3) == 30);
    }
}
