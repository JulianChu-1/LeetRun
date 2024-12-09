import java.util.*;


public class Test {
    public static String solution(String s) {

        String[] ss = s.split("\\."); // 正确分割小数点
        StringBuilder sb = new StringBuilder();
        StringBuilder res = new StringBuilder();
        int count = 0;

        String integerPart = String.valueOf(Long.parseLong(ss[0])); //去除0

        for (int i = integerPart.length() - 1; i >= 0; i--) {
            sb.append(integerPart.charAt(i));
            count++;
            if (count % 3 == 0 && i != 0) { // 每3个字符插入逗号，但避免最后多余的逗号
                sb.append(",");
            }
        }

        res.append(sb.reverse());

        if (ss.length > 1) {
            res.append(".").append(ss[1]);
        }

        return res.toString();
    }

    public static void main(String[] args) {
        System.out.println(solution("1294512.12412").equals("1,294,512.12412"));
        System.out.println(solution("0000123456789.99").equals("123,456,789.99"));
        System.out.println(solution("987654321").equals("987,654,321"));
    }
}