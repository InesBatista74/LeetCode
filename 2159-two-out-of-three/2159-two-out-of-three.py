class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        x = nums1[:] 
        y = nums2[:]
        z = nums3[:]
        result = set()
        for i in range(len(x)):
            if x[i] in y or x[i] in z:
                result.add(x[i])
        for j in range(len(y)):
            if y[j] in x or y[j] in z:
                result.add(y[j])
        for k in range(len(z)):
            if z[k] in x or z[k] in y:
                result.add(z[k])
        return list(result)
        