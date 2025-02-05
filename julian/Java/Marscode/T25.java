package Marscode;

public class T25 {
    public static int solution(String dna1, String dna2) {
        int m = dna1.length();
        // System.out.println(m);
        int n = dna2.length();

        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            dp[i][0] = i;
        }
        for (int j = 0; j <= n; j++) {
            dp[0][j] = j;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                int cost = dna1.charAt(i - 1) == dna2.charAt(j - 1) ? 0 : 1;
                dp[i][j] = Math.min(Math.min(dp[i -1][j] + 1, dp[i][j - 1] + 1), dp[i - 1][j - 1] + cost);
            }
        }

        return dp[m][n];
    }

    public static void main(String[] args) {
        //  You can add more test cases here
        System.out.println(solution("AGCTTAGC", "AGCTAGCT") == 2);
        System.out.println(solution("AGCCGAGC", "GCTAGCT") == 4);
    }
}
