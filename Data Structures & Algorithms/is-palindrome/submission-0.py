class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for char in s:
            if char.isalnum():
                st += char.lower()
        st = st.lower()       

        return st == st[::-1]
