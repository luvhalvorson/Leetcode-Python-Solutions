# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head : return None
        c = head.next
        nnode = c
        pnode = head
        head.next = None
        while c:
            nnode = c.next #記錄下個node
            c.next = pnode #把next只回前面一個node
            pnode = c #更新前一個node為現在的node
            #self.printlist(p)
            c = nnode #往下一個node處理
        return pnode
    
    def printlist(self, head):
        while head:
            print(head.val,end=" ")
            head = head.next
        print(" ====")