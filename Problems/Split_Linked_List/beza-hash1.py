
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        
       
        part_size, remainder = divmod(n, k)
        
        result = []
        current = head
        
        for i in range(k):
            part_head = current
            size = part_size + (1 if remainder > 0 else 0)
            remainder -= 1 if remainder > 0 else 0
            
           
            for j in range(size - 1):
                if current:
                    current = current.next
            
            
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            result.append(part_head)
        
        return result
