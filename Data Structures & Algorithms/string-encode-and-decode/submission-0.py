class Solution:
    
    # Encode should turn a list of strings into one string
    def encode(self, strs: List[str]) -> str:
        string = "".join(f"{len(s)}#{s}" for s in strs)
        return string
        
    # Decode should turn one string into a list of strings
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = s.index("#", i)        
            length = int(s[i:j])       
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length         
        return result


        # Come back to didnt really understand
            


