class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return None
        if len(tokens) == 1:
            return int(tokens[0])
        computes = ["+", "-", "*", "/"]
        i = 0
        while i < len(tokens):
            if tokens[i] in computes:
                if tokens[i] == "+":
                    tokens[i] = int(tokens[i-2]) + int(tokens[i-1])
                elif tokens[i] == "-":
                    tokens[i] = int(tokens[i-2]) - int(tokens[i-1])
                elif tokens[i] == "*":
                    tokens[i] = int(tokens[i-2]) * int(tokens[i-1])
                elif tokens[i] == "/":
                    sign = 1
                    if int(tokens[i-2]) < 0:
                        tokens[i-2] = abs(int(tokens[i-2]))
                        sign *= -1
                    if int(tokens[i-1]) < 0:
                        tokens[i-1] = abs(int(tokens[i-1]))
                        sign *= -1
                    tokens[i] = int(tokens[i-2]) // int(tokens[i-1])
                    tokens[i] *= sign
                del tokens[i-2]
                del tokens[i-2]
                i -= 2
            i += 1
        return int(tokens[0])
