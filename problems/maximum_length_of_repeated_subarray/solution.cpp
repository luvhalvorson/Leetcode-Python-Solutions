class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size(), res = 0;
        for (int offset = 0; offset < m; ++offset) {
            for (int i = offset, j = 0; i < m && j < n;) {
                int cnt = 0;
                while (i < m && j < n && A[i++] == B[j++]) ++cnt;
                res = max(res, cnt);
            }
        }
        for (int offset = 0; offset < n; ++offset) {
            for (int i = 0, j = offset; i < m && j < n;) {
                int cnt = 0;
                while (i < m && j < n && A[i++] == B[j++]) ++cnt;
                res = max(res, cnt);
            }
        }
        return res;
    }
};