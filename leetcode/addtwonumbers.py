class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1r = []
        l2r = []
        
        while l1:
            l1r.append(str(l1.val))
            l1 = l1.next
        
        while l2:
            l2r.append(str(l2.val))
            l2 = l2.next
                       
        value1 = int(''.join(l1r)[::-1])
        value2 = int(''.join(l2r)[::-1])
        
        result = str(value1 + value2)
        
        resultList = None
                       
        for value in result:
            resultList = ListNode(val=int(value), next=resultList)
        
        return resultList