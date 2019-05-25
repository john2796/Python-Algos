# Heap
class Node:

  # * `insert` adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap

  # * `delete` removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed.

  # * `get_max` returns the maximum value in the heap _in constant time_.

  # * `get_size` returns the number of elements stored in the heap.

  # * `_bubble_up` moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.

 # * `_sift_down` grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
