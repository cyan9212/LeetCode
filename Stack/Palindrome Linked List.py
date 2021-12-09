class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node_list = []
        pointer = head
        if head.next == None:
            return True
        while pointer!=None:  
            node_list.append(pointer.val)
            pointer = pointer.next
        
        length = len(node_list)
        if length%2 == 1:
            node_list.pop(length//2)
            length-=1
        
        s1 = node_list[:length//2]
        s2 = node_list[length//2:]
        s2.reverse()
        return s1 == s2
