class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res=[[1]]
        for i in range(n-1):
            temp=[0]+res[-1]+[0]
            temp_res=[]
            for i in range(len(temp)-1):
                temp_res.append(temp[i]+temp[i+1])
            res.append(temp_res)
        return res


        