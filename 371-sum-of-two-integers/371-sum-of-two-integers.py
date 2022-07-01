class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        ## TIME COMPLEXITY : O(1) ##
		## SPACE COMPLEXITY : O(1) ##
        
        # 32 bit mask in hexadecimal
        mask = 0xffffffff # (python default int size is not 32bit, it is very large number, so to prevent overflow and stop running into infinite loop, we use 32bit mask to limit int size to 32bit )
        
        while (b & mask) >0: #because this is when the shift happens
            carry = (a &b) << 1
            
            a = a^b #this is the xor
            b = carry
            
        return (a & mask) if b>0 else a
        
        
        
        
         
        
#Because if b is positive (rather than zero) after we exit the loop, then we know a has "overflowed" past the number of bits in the mask.

# If you poke around the non-Python solutions you might notice they aren't checking if b is positive, and that's because Python supports infinite-bit integers. So where Java would simply truncate bits in the event of overflow (there b is always zero after the loop), Python won't. Instead, you have perform the truncation on your own by applying the mask.

# It might help if you step through an example. Try writing out the addition of -1 and 1 using the code above and you'll see what I mean. When you exit the loop (whatever mask size you use) you'll notice a is not zero but actually some negative number.