class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        l = 0
        r = 0
        n = len(chars)

        while r < n:
            curr = chars[r]
            cnt = 0

            # Count the current group
            while r < n and chars[r] == curr:
                r += 1
                cnt += 1

            # Write the character
            chars[l] = curr
            l += 1

            # Write the count if > 1
            if cnt > 1:
                for digit in str(cnt):
                    chars[l] = digit
                    l += 1

        return l
"""

        n = len(chars)
        read = 0
        write = 0

        while read < n:
            curr = chars[read]
            count = 0

            while read < n and chars[read] == curr:
                read += 1
                count += 1

            chars[write] = curr
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write