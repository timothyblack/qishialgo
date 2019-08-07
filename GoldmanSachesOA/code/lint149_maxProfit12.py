
"""
https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock/description
149. Best Time to Buy and Sell Stock
中文English
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example
Example 1

Input: [3, 2, 3, 1, 2]
Output: 1
Explanation: You can buy at the third day and then sell it at the 4th day. The profit is 2 - 1 = 1
Example 2

Input: [1, 2, 3, 4, 5]
Output: 4
Explanation: You can buy at the 0th day and then sell it at the 4th day. The profit is 5 - 1 = 4
Example 3

Input: [5, 4, 3, 2, 1]
Output: 0
Explanation: You can do nothing and get nothing.

https://www.jiuzhang.com/solution/best-time-to-buy-and-sell-stock/
"""

public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        // iterate from 0 to N -1 
        if (prices == null || prices.length == 0) {
            return 0; 
        }
        
        int min = Integer.MAX_VALUE; 
        int profit = 0; 
        for (int i: prices) {
            min = i < min ? i : min;  
            profit = (i - min) > profit ? i-min : profit;
        }
        
        return profit; 
    }
    
}

"""
https://www.jiuzhang.com/solution/best-time-to-buy-and-sell-stock/
"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices or len(prices) == 0: return 0 
        
        profit, min_price = 0, sys.maxsize   
        for i in prices: 
            min_price = min_price if min_price < i else i 
            profit = (i - min_price) if i - min_price > profit else profit 
        return profit 
        

"""
https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-ii/
150. Best Time to Buy and Sell Stock II
中文English
Given an array prices, which represents the price of a stock in each day.

You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, if you already have the stock, you must sell it before you buy again).

Design an algorithm to find the maximum profit.

Example
Example 1:

Input: [2, 1, 2, 0, 1]
Output: 2
Explanation: 
    1. Buy the stock on the second day at 1, and sell the stock on the third day at 2. Profit is 1.
    2. Buy the stock on the 4th day at 1, and sell the stock on the 5th day at 2. Profit is 1.
    Total profit is 2.
Example 2:

Input: [4, 3, 2, 1]
Output: 0
Explanation: No transaction, profit is 0.
http://www.jiuzhang.com/solution/best-time-to-buy-and-sell-stock-ii/
"""

public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        int n = prices.length; 
        int res = 0;   
        //  n - 1 here  becaause [i + 1] - i is calced for each i 
        for (int i = 0; i < n - 1; i++) {
            if (prices[i + 1] - prices[i] > 0) {
                res += prices[i + 1] - prices[i];  
            }
        }
        return res;
    }
}


class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices or len(prices) == 0: return 0 
        res = 0 
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                res += prices[i + 1] - prices[i]
        return res
		
"""
https://www.lintcode.com/problem/best-time-to-buy-and-sell-stock-iii/description
151. Best Time to Buy and Sell Stock III
中文English
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Example
Example 1

Input : [4,4,6,1,1,4,2,5]
Output : 6
Notice
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

https://www.jiuzhang.com/solution/best-time-to-buy-and-sell-stock-iii/  
this is hard,  just memerize it

"""

public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        int n = prices.length; 
        if (n == 0) {
            return 0;
        }
        
        int [][] f = new int[n + 1][5 + 1]; 
        int i, j, k;
        // first 0 days, phase 1, max profit = 0 
        f[0][1] = 0;
        f[0][2] = f[0][3] = f[0][4] = f[0][5] = Integer.MIN_VALUE; 
        
        for (i = 1; i <= n; ++i) {
            // 1, 3, 5 
            for( j = 1; j <= 5; j += 2) {
                // 
                f[i][j] = f[i - 1][j]; 
                if(j > 1 && i > 1 && f[i -1][j -1] != Integer.MIN_VALUE) {
                    f[i][j] = Math.max(f[i][j], f[i - 1][j -1] + prices[i - 1]-prices[i - 2]);
                } 
            }
            // 2, 4
            for (j = 2; j <= 5; j += 2) {
                f[i][j] = f[i - 1][j -1]; 
                if (i > 1 && f[i -1][j] != Integer.MIN_VALUE) {
                    f[i][j] = Math.max(f[i][j], f[i -1][j] + prices[i - 1] - prices[i - 2]); 
                }
                
                if (j > 2 && i > 1 && f[i - 1][j - 2] != Integer.MIN_VALUE) {
                    f[i][j] = Math.max(f[i][j], f[i -1][j -2] + prices[i - 1] - prices[i - 2]);
                }
            }
        }
        
        return Math.max(Math.max(f[n][1], f[n][3]), f[n][5]); 
    }
}