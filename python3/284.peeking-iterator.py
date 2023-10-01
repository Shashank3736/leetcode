#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#

# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
        
class PeekingIterator:
  def __init__(self, iterator):
    self.iterator = iterator
    self.buffer = self.iterator.next() if self.iterator.hasNext() else None

  def peek(self) -> int:
    """
    Returns the next element in the iteration without advancing the iterator.
    """
    return self.buffer

  def next(self) -> int:
    next = self.buffer
    self.buffer = self.iterator.next() if self.iterator.hasNext() else None
    return next

  def hasNext(self) -> bool:
    return self.buffer is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

