class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        # Sort box types in descending order based on units per box
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        
        for num_boxes, units_per_box in boxTypes:
            # Take as many boxes of this type as possible
            boxes_to_take = min(truckSize, num_boxes)
            total_units += boxes_to_take * units_per_box
            truckSize -= boxes_to_take
            
            # Stop if the truck is completely full
            if truckSize == 0:
                break
                
        return total_units