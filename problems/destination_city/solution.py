class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        others = set()
        
        # des = ""
        # for path in paths:
        #     others.add(path[0])
        # print(others)
        # for path in paths:
        #     if path[1] not in others:
        #         des = path[1]
        #         break
        #sa= sb= set()
        sa, sb = map(set, zip(*paths))
        # if len(des) != 1:
        #     for d in des:
        #         if d in others:
        #             des.remove(d)
        #print(others, des)
        return (sb-sa).pop()