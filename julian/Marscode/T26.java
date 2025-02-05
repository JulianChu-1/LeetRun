package Marscode;

public class T26 {
    public static boolean compare(String a, String b, int i) {
        for (int j = 0; j < Math.min(b.length(), a.length()); j++) {
            if (b.charAt(j) > a.charAt(j + i)) {
                return true;
            }
        }
        return false;
    }


    public static int solution(int a, int b) {
        String strA = String.valueOf(a);
        String strB = String.valueOf(b);
        StringBuilder result = new StringBuilder();
        boolean flag = true;

        if (b == 0) {
            return a * 10;
        }

        for (int i = 0; i < strA.length(); i++) {
            if (compare(strA, strB, i)) {
                if (flag) {
                    result.append(strB);
                    flag = false;
                }
            }
            result.append(strA.charAt(i));
        }

        if (result.length() == strA.length()) {
            result.append(strB);
        }

        return Integer.parseInt(result.toString());
    }

    public static void main(String[] args) {
        System.out.println(solution(76543, 4) == 765443);
        System.out.println(solution(1, 0) == 10);
        System.out.println(solution(44, 5) == 544);
        System.out.println(solution(666, 6) == 6666);
    }
}
