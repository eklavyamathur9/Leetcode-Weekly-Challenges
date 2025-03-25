class Solution(object):
    def minTime(self, skill, mana):
        n = len(skill)  # Number of wizards
        m = len(mana)   # Number of potions
        f = [0] * n     # Initialize a list to store the finish times for each wizard
        for j in range(m):  # Iterate over each potion
            x = mana[j]     # Mana capacity of the current potion
            nw = f[0]       # Initialize the new finish time for the first wizard
            # Calculate the finish time for each wizard for the current potion
            for i in range(1, n):
                nw = max(nw + skill[i - 1] * x, f[i])
            # Update the finish time for the last wizard
            f[n - 1] = nw + skill[n - 1] * x
            # Backpropagate to update the finish times for the previous wizards
            for i in range(n - 2, -1, -1):
                f[i] = f[i + 1] - skill[i + 1] * x
        # The total time is the finish time of the last wizard for the last potion
        return f[n - 1]