class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()): stack.append(int(token))
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
        