public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> m = new HashMap<>();
        for (int num : nums) {
            m.put(num, m.getOrDefault(num, 0) + 1);
        }
        List<Integer>[] op = new List[nums.length + 1];
        for (Map.Entry<Integer, Integer> entry : m.entrySet()) {
            int f = entry.getValue();
            int num = entry.getKey();
            
            if (op[f] == null) {
                op[f] = new ArrayList<>();
            }
            op[f].add(num);
        }
        int[] res = new int[k];
        int index = 0;
        for (int i = op.length - 1; i >= 0 && index < k; i--) {
            if (op[i] != null) {
                for (int num : op[i]) {
                    res[index++] = num;
                    if (index == k) {
                        return res;
                    }
                }
            }
        }
        return res;
    }
}
