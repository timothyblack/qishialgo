"""
https://www.cnblogs.com/grandyang/p/4325432.html

https://blog.csdn.net/woliuyunyicai/article/details/44179743
解法二：

使用n&(n-1)的方法

假使 n =0x110101

                n                    n-1               n&(n-1)

step1:   110101          110100          110100

step2:   110100          110011          110000

step3:   110000          101111          100000

step4:   100000          011111          000000

发现有几个1，就循环几次n&(n-1)得到0，明显较于上者运行效率更高些。

时间复杂度：O(M),M是n中1的个数
--------------------- 
作者：流云易采 
来源：CSDN 
原文：https://blog.csdn.net/woliuyunyicai/article/details/44179743 
版权声明：本文为博主原创文章，转载请附上博文链接！
解法：bit manipulation, 每次右移一位，然后and1来求这一位是否是1。
public int hammingWeight(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            int tag = n & 1;
            if (tag == 1) {
                result += 1;
            }
            n = n >> 1;
        }
        return result;
    }
--------------------- 
作者：katrina95 
来源：CSDN 
原文：https://blog.csdn.net/katrina95/article/details/79372902 
版权声明：本文为博主原创文章，转载请附上博文链接！
https://fivezh.github.io/2015/04/07/LeetCode-191-Number-of-1-Bits/  


方法三：【分析】我们将一个整数减去1，都是把最右边的1变成0，如果它右边还有0，所有的0全部变成1，但是它左边数字均保持不变。我们把这个整数和它减去1的结果想&的话，可以得到最右边的1。 
/*方法3.移位，对于负数也适用*/
int hammingWeight(int32_t n) 
{
    int NumberOfOne = 0;

    while(n) {
        NumberOfOne ++;
        n = n&(n-1);
    }
    return NumberOfOne;
}
--------------------- 
作者：狂奔的乌龟 
来源：CSDN 
原文：https://blog.csdn.net/xy010902100449/article/details/48445863 
版权声明：本文为博主原创文章，转载请附上博文链接！

"""
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
         #利用 n&(n-1) 的trick。简单的说，运算 n = n&(n-1) #可以将n最低位的1变成0，这里不证明。循环进行该运算，循环次数就是n的二进制表示中1的个数。
      
        total = 0 
        for i in range(32):
            total += num & 1 
            num >>= 1    
        return total
        """
        TLE  for -1(11111111111111111111111111111111)
        count = 0
        while num:
            num = num & (num - 1)   
            count += 1 
        return count 
        """