class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-/*'

        for token in tokens:
            if not token in operators: stack.append(int(token))
            else: 
                right, left = stack.pop(), stack.pop()

                match(token):
                    case "+":
                        stack.append(left + right)
                    
                    case "-":
                        stack.append(left - right)
                    
                    case "*":
                        stack.append(left * right)
                    
                    case "/":
                        stack.append(int(left / right))

        return stack[0]
        