class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0, head)
        curr = head
        
        while curr and curr.next:
            if curr.val <= curr.next.val:
                curr = curr.next
            else:
                insert_node = curr.next
                curr.next = insert_node.next
                
                prev = dummy
                while prev.next.val <= insert_node.val:
                    prev = prev.next
                    
                insert_node.next = prev.next
                prev.next = insert_node
                
        return dummy.next