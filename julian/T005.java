public class T005 {
    public String longestPalindrome(String s) {
        // 中心扩散算法
        if (s == null || s.isEmpty()) {
            return "";
        }
        int start = 0, end = 0;

        for (int i = 0; i < s.length(); i++) {
            int len1 = expandCenter(s, i, i);
            int len2 = expandCenter(s, i, i + 1);
            int len = Math.max(len1, len2);

            if (len > end - start) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
            }
        }

        return s.substring(start, end + 1);
    }

    private int expandCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }

        return right - left - 1;
    }

    public String longestPalindromeDP(String s) {
        // 动态规划
        if (s == null || s.length() < 2) {return s;}

        int n = s.length();
        int maxLen = 1;
        int begin = 0;
        int end = 0;
        boolean[][] dp = new boolean[n][n]; //dp[i][j]表示i到j的子串是否为回文串

        for (int r = 1; r < n; r++) {
            for (int l = 0; l < r; l++) {
                if (s.charAt(l) == s.charAt(r) && (r - l <= 2 || dp[l + 1][r - 1])) {
                    dp[l][r] = true;
                    if (r - l + 1 > maxLen) {
                        maxLen = r - l + 1;
                        begin = l;
                        end = r;
                    }
                }
            }
        }

        return s.substring(begin, end + 1);
    }
    public static void main(String[] args) {

    }
}
