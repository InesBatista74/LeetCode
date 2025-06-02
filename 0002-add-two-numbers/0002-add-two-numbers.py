# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0  #guarda o carry da soma dos números
        head = None 
        tail = None

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            soma = val1 + val2 + carry
            carry = soma // 10
            novo_no = ListNode(soma % 10)

            if not head:
                head = novo_no
                tail = novo_no
            else:
                tail.next = novo_no
                tail = novo_no

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head