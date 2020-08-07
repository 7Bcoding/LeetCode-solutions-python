class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        win = dict()
        num = arr[0]
        win[num] = 0
        while win[num] < k:
            if arr[0] > arr[1]:
                tmp = arr[1]
                arr.remove(arr[1])
                arr.append(tmp)
                win[arr[0]] += 1
                num = arr[0]
            else:
                win[arr[1]] = 1
                num = arr[1]
                tmp = arr[0]
                arr.pop(0)
                arr.append(tmp)
            if win[num] == len(arr)-1 and len(arr) < k:
                break

        return num