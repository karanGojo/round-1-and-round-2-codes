class UserMainCode(object):
    @classmethod
    def largestSubarray(cls,input1,input2):
        sum=0
        maxsize=-1
        for i in range(0,input2-1):
            sum=-1 if (input1[i]==0)else 1
            for j in range(i+1,input2):
                sum=sum + (-1) if (input1[j]==0) else sum + 1
                if (sum==0 and maxsize<j-i +1):
                    maxsize=j-i+1
                    startindex=i
        if (maxsize==-1):
            print("no such subarray")
        else:
            print(startindex,"to",startindex + maxsize-1)
            print(input1[startindex:startindex + maxsize])
        return maxsize
def main():
    obj =UserMainCode()
    print("ans:",obj.largestSubarray([1,1,0,1],4))
    
if __name__ == '__main__':
    main()