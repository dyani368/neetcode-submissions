class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        for i in range(len(s)):
            if s[i] not in map:
                stack.append(s[i])
            else:
                if stack:
                    top = stack[-1]
                    if map[s[i]] != top:
                        return False
                else:
                    return False
                stack.pop()

        if not stack:
            return True
        else:
            return False

        