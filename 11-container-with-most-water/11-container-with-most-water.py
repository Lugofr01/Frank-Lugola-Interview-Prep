class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area is length times width 
        #  we needd to maximazi area as much as possible
#Brute Force: testing areas from first pointer to evry pointer and seeing how they compare and ends up with O(n^2)


        begining = 0
        end = len(height)-1
        max_area = 0

        # we gonna keep calculating height till begin meete with end


        while begining < end:
            max_area =max(max_area, min(height[begining],height[end])*(end -begining))
            
#             we usemin begonnog and end since water will over flow when it is at max height and maxes sense


            if height[begining] >=height[end]:
                # update end
                end = end -1

            else:
                begining = begining +1

        return max_area
# space o{1} ans linear time  o[n]









# Brute Force:
# res = 0
# for l in range(len(height)):
# for r in range(l+1, len(height)):
# area = (r-l)*min(height[l],height[r])
# res = max(area,res)
# return res
# o(n^2) complexity

