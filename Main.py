class Evaluate:
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here


  def __init__(self, size):
    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      top:An integer which points to the top most element in the stack.
      size_of_stack: An integer which represents size of stack.
      stack: A list which maintians the elements of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = []


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    return self.top == -1


  def pop(self):
    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if not self.isEmpty():
      self.top -= 1
      return self.stack.pop()


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    if self.top < self.size_of_stack:
      self.stack.append(operand)


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
    count = 0
    for i in expression:
      if i.isdigit():
        count += 1
      elif '+' or '-' or '*' or '/' or '(' or ')':
        count -= 1
      else:
        return False
      if count<1:
        return False
    return count == 1


  def evaluate_postfix_expression(self, expression):
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
    for i in expression:
      if i.isdigit():
        self.top += 1
        self.push(i)
      else:
        self.top -= 1
        val1 = self.pop()
        val2 = self.pop()
        self.push(str(eval(val2 + i + val1)))
    return self.pop()


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression')
