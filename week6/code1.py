class Solution(object):
    def maxContainers(self, n, container_weight, max_weight):
        # Calculate the total number of cells on the n x n deck
        total_cells = n * n
        # Calculate the maximum number of containers based on weight capacity
        max_containers_by_weight = max_weight // container_weight
        # Return the minimum of the two values to ensure both constraints are satisfied
        return min(total_cells, max_containers_by_weight)