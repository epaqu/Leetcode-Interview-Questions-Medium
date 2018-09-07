class Solution(object):
    def increasingTriplet(self, nums):
        sequence = []
        for num in nums:
            for seq_index, seq_num in enumerate(sequence):
                if seq_num >= num:
                    sequence[seq_index] = num
                    break
            else:
                sequence.append(num)
            if len(sequence) >= 3:
                return True
        return False
