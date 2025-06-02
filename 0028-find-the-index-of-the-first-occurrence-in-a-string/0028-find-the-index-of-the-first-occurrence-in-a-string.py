class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0

        # Get the lengths of haystack and needle
        n, m = len(haystack), len(needle)

        # Slide through haystack with a window of size m
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i

        # If needle is not found
        return -1