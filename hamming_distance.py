class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        if len(bin_x) > len(bin_y):
            bin_y = '0' * (len(bin_x) - len(bin_y)) + bin_y
        else:
            bin_x = '0' * (len(bin_y) - len(bin_x)) + bin_x
        count = 0
        for i, c  in  enumerate(bin_x):
            if c != bin_y[i]:
                count += 1
        return count
        
        
        
        