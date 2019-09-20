class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    #setup for the loop, we start at the head, and we'll need an intermediate variable to help keep track of where we are at
    current_node = self.head
    previous_node = None

    while current_node is not None:
      #next Node to work on
      next_one = current_node.next_node
      
      #reversal -- for the first node, it's at the end of the reversed list so this will be None
      current_node.next_node = previous_node

      #in the next loop, the previous node will be the current one
      previous_node = current_node

      #move onto the next node
      current_node = next_one
    
    #when the loop exits, previous_node will be the front of the list
    self.head = previous_node
