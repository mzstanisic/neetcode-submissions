class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {};
        stringbucket = {};

        for i, string in enumerate(strs):
            charmap = {
                'a':0,
                'b':0,
                'c':0,
                'd':0,
                'e':0,
                'f':0,
                'g':0,
                'h':0,
                'i':0,
                'j':0,
                'k':0,
                'l':0,
                'm':0,
                'n':0,
                'o':0,
                'p':0,
                'q':0,
                'r':0,
                's':0,
                't':0,
                'u':0,
                'v':0,
                'w':0,
                'x':0,
                'y':0,
                'z':0
            };

            for char in string:
                charmap[char] += 1;

            index = tuple(charmap.values());

            if index in stringbucket:
                stringbucket[index].append(i);
                output[stringbucket[index][0]].append(string);
            else:
                stringbucket[index] = [i];
                output[i] = [string];
        
        return list(output.values());