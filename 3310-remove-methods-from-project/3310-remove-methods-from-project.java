class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        ArrayList<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : invocations) {
            graph[edge[0]].add(edge[1]);
        }
        boolean[] visited = new boolean[n];
        boolean[] remain = new boolean[n];
        Arrays.fill(remain, true);
        Stack<Integer> st = new Stack<>();
        st.push(k);
        while (!st.isEmpty()) {
            int cur = st.pop();
            if (visited[cur])
                continue;
            visited[cur] = true;
            remain[cur] = false;
            for (int next : graph[cur]) {
                if (!visited[next]) {
                    st.push(next);
                }
            }
        }

        for (int[] edge : invocations) {
            int u = edge[0];
            int v = edge[1];
            if (remain[u] && visited[v]) {
                List<Integer> ans = new ArrayList<>();
                for (int i = 0; i < n; i++)
                    ans.add(i);
                return ans;
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (remain[i])
                ans.add(i);
        }
        return ans;
    }
}