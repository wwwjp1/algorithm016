class NumDecodings {
    public int numDecodings(String s) {
        // 递归
//        if ("0".equals(s)) return 0;
//        if (s.length() == 0 || s.length() == 1) return 1;
//        int count = 0;
//        char[] chars = s.toCharArray();
//        if ('0' != chars[0]) {
//            count += numDecodings(s.substring(1));
//        }
//        int i = ((int)chars[0]) * 10 +(int) chars[1];
//        if (i <= 27 && i >= 10) {
//            count += numDecodings(s.substring(2));
//        }
//        return count;

        // DP
        if ("0".equals(s)) return 0;
        String string = "99" + s;
        int[] dp = new int[string.length()];
        dp[0] = 1;
        dp[1] = 1;

        char[] chars = string.toCharArray();
        for (int i = 2; i < dp.length; i++) {
            if ('0' != chars[i]) {
                dp[i] = dp[i-1];
            }
            int num = 10 * (chars[i-1] - '0') + (chars[i] - '0');
            if ( num <= 26 && num >= 10) {
                dp[i] += dp[i-2];
            }
        }
        return dp[dp.length - 1];
    }
}