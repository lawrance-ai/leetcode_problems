class Solution {
    public int findKthPositive(int[] a, int k) {
        int l = 0;
        int r = a.length - 1;
        int m = (r + l) / 2;
        int num = 1;
        int n = 0;
        int b = 0;
        int ans = 0;

        if (k < a[0]) {
            return k;
        } else {
            while (l < r) {
                num = a[m] - m - 1;

                if (num < k) {
                    l = m;
                    m = (r + l) / 2;
                } 
                else if (k <= num) {
                    n = a[m - 1] - m;

                    if (n < k) {
                        b = k - n;
                        ans = a[m - 1] + b;
                        return ans;
                    } 
                    else {
                        r = m;
                        m = (r + l) / 2;
                    }
                }

                if (l == m) {
                    m = r;
                }
            }
        }

        return a[l] + (k - (a[l] - l - 1));
    }
}