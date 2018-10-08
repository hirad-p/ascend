# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def add_two_numbers(list1, list2):
  result = ListNode(0)
  p = list1
  q = list2
  pointer = result
  carry = 0
  while p is not None or q is not None:
    x = p.val if p is not None else 0
    y = q.val if q is not None else 0
    summation = carry + x + y
    carry = int(summation / 10)
    pointer.next = ListNode(int(summation % 10))
    pointer = pointer.next
    if p is not None: 
      p = p.next
    if q is not None:
      q = q.next
  if carry > 0:
    pointer.next = ListNode(carry)
  return result.next

