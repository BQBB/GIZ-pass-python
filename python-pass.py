class Solution:
    # Solution using Mancher's Algorithm
    @staticmethod
    def longest_palindromic(s: str) -> str:
            if(type(s) != str):
                raise ValueError(f"{type(s)} not allowed only string type is allowed")
            def adjust_string(s: str) -> str:                    # method to adjust the string
                    list_from_s = list(s.strip())               # Create List From {s}
                    modified_s = "#".join(list_from_s)          # Modified {s} By adding Hash After every Char in list
                    return "#" + modified_s + "#"               # return new {s} like : #a#b#b#a# 
        

            if(len(s)<=1):                                      # Check is {s} Empty or has length equal 1 
                return s;
            s = adjust_string(s)                                 # Get new {s} adjusted from {adjust_string} method
            max_length = 0                                      # Variable indicate to maximum palindromic length in the string
            index = 0                                           # Variable indicate to the index of CENTER of the palindromic
            P = [0] * len(s)                                    # Create Array with length equal to new {s} length and fill it zeros
            center = right_boundary = 0                          # center and right_boundary variables that indicates to first index
            for i in range(0, len(s)):                          # start the functionallity by looping around the {s} from zero to the last element
                mirror = 2*center - i                                # mirror Variable indicate to the mirror index of current string ex:   aczbzca the mirror of z is z
                if(i < right_boundary):                          # check if i lower than right_boundary
                    P[i]= min(right_boundary-i,P[mirror])        # fill the location P[i] minimum value of { right_boundary - i } or value of the P[mirror]
                right = i + (P[i]+1)                            # right Variable is expanding to the right side
                left = i - (P[i]+1)                             # left Variable is expanding to the left side
                while(left >= 0  and  right < len(s)  and  s[right] == s[left]):        # check how many expantion is equal in left and right side and increase element of P[i]
                    left-=1
                    right+=1
                    P[i]+=1

                if(i + P[i] > right_boundary):                               # check if value of { i + P[i] > right_boundary} 
                    center = i                                              # set {center} equal to {i}
                    right_boundary = i + P[i]                                # set {right_boundary} equal to last index in right expantion
                    if(P[i] > max_length):                                  # set max_length and index 
                        max_length = P[i]
                        index=i
            start_position = index - max_length + 1
            end_position = index + max_length
            s = "".join(s[start_position:end_position].split("#"))
            return s    # return the result after delete hashes 



list_of_examples = ["babad","cbbd","a","ac"]
for example in list_of_examples:
    print(f"Input : {example} , Output : {Solution.longest_palindromic(example)}")
