class Solution {
    public long maxAlternatingSum(int[] nums) {
        long[] squares = new long[nums.length];
        for (int i = 0; i < nums.length; i++) {
            squares[i] = (long) nums[i] * nums[i];
        }
        java.util.Arrays.sort(squares);
        
        long sum = 0;
        int n = squares.length;
        int minusCount = n / 2;
        
        for (int i = 0; i < n; i++) {
            if (i < minusCount) {
                sum -= squares[i];
            } else {
                sum += squares[i];
            }
        }
        return sum;
    }
}
