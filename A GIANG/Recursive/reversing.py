import random
def reverse(arr, start,stop):
    if start < stop -1:
        arr[start], arr[stop-1] = arr[stop -1], arr[start]
        reverse(arr, start+1,stop -1 )
if __name__ == '__main__':
    k = random.random()
    arr=[1 +i +k  for i in range(5)]
    print(arr)
    reverse(arr,0, len(arr))
    print(arr)