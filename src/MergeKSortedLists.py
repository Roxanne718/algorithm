# =================================
# 合并K个升序链表：利用优先队列实现
# 此题可以用优先队列 heapq 秒杀
# =================================


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # init
        heap = []
        for i in lists:
            node = i
            while(node!=None):
                heapq.heappush(heap, node.val)
                node = node.next
        # sort
        dummy = ListNode()
        p = dummy
        for i in range(len(heap)):
            p.next = ListNode(val=heapq.heappop(heap))
            p = p.next
        return dummy.next