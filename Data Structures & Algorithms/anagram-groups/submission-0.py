class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # output = [];
        output = {};
        stringbucket = {};
        # uniqueid = str;

        for i, string in enumerate(strs):
            charmap = {};
            for char in string:
                if char in charmap:
                    charmap[char] += 1;
                else:
                    charmap[char] = 1;

            # for char in charmap:
            #     uniqueid += char*charmap[char];
            uniqueid = tuple(sorted(charmap.items()))

            if uniqueid in stringbucket:
                stringbucket[uniqueid].append(i);
                output[stringbucket[uniqueid][0]].append(string);
            else:
                stringbucket[uniqueid] = [i];
                output[i] = [string];
        
        # print(list(output.values()));
        return list(output.values());