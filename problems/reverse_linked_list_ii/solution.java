/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (m == n) return head;
        Stack<ListNode> st = new Stack<>();
        ListNode left = null;
        ListNode node = head;
        if (m != 1) {
            for (int i = 1; i < m - 1; ++i) node = node.next;
            left = node;
            node = node.next; // position m
        }
        
        for (int i = m; i <= n; ++i) {
            st.push(node);
            node = node.next;
        }
        
        ListNode l1 = st.pop(), l2 = null;
        if (m == 1)
            head = l1;
        else
            left.next = l1;
        while (!st.isEmpty()) {
            l2 = st.pop();
            l1.next = l2;
            l1 = l2;                
        }
        l1.next = node;
        
        return head;
    }
}