import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class T017 {
    // 回溯算法
    private static final String[] letterMap = {
        "", // 0
        "", // 1
        "abc", // 2
        "def", // 3
        "ghi", // 4
        "jkl", // 5
        "mno", // 6
        "pqrs", // 7
        "tuv", // 8
        "wxyz" // 9
    };

    List<String> res = new ArrayList<>();
    StringBuilder sb = new StringBuilder();

    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) return res;

        backTracking(digits, 0);
        return res;
    }

    private void backTracking(String digits, int num) {
        // num表示此时树的深度
        if (num == digits.length()) {
            res.add(sb.toString());
            return;
        }

        String str = letterMap[digits.charAt(num) - '0'];

        for (int i = 0; i < digits.length(); i++) {
            sb.append(str.charAt(i));
            backTracking(digits, num + 1);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    // 队列
    public List<String> letterCombinationsQ(String digits) {
        if (digits == null || digits.isEmpty()) return res;

        Queue<String> queue = new LinkedList<>();

        for (int i = 0; i < digits.length(); i++) {
            queue = queueCombinations(queue, letterMap[digits.charAt(i) - '0']);
        }

        for (String s : queue) {
            res.add(s);
        }

        return res;
    }

    private Queue<String> queueCombinations(Queue<String> queue, String letters) {
        if (queue.size() == 0) {
            for (char letter : letters.toCharArray()) {
                queue.add(String.valueOf(letter));
            }
        } else {
            int queueSize = queue.size();
            for (int i = 0; i < queueSize; i++) {
                String s = queue.poll();
                for (char letter : letters.toCharArray()) {
                    queue.add(s + letter);
                }
            }
        }

        return queue;
    }


    public static void main(String[] args) {
        T017 t017 = new T017();
        System.out.println(t017.letterCombinationsQ("23"));
    }
}
