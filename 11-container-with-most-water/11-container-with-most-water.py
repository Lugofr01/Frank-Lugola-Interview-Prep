class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area is length times width 
        #  we needd to maximazi area as much as possible

        begining = 0
        end = len(height)-1
        max_area = 0

        # we gonna keep calculating heght till begin meete with end


        while begining < end:
            max_area =max(max_area, min(height[begining],height[end])*(end -begining))
            
#             we usemin begonnog and end since water will over flow when it is at max height and maxes sense


            if height[begining] >=height[end]:
                # update end
                end = end -1

            else:
                begining = begining +1

        return max_area
# space o{1} ans linear o[n]
