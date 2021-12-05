class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        mapA = set()
        while headA!=None:
            mapA.add(headA) 
            headA = headA.next
        
        while headB!=None:
            if headB in mapA:
                return headB
            headB = headB.next
        return None
