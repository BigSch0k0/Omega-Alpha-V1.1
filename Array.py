

def array_sort(arr:list, crit:int = 0) -> list:

    if crit != 0:

        for i in range(len(arr)):
            for i in range(len(arr)-1):

                if arr[i+1] > arr[i]:
                    hold = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = hold
        
            return arr

    else:

        for i in range(len(arr)):
            for i in range(len(arr)-1):

                if arr[i+1[crit]] > arr[i[crit]]:
                    hold = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = hold
        
            return arr
