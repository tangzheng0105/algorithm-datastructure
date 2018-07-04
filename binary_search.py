import time
def binary_search(lis, item):
    pos = int(len(lis)/2)
    highPos = int(len(lis))
    lowPos = 0
    while(lis[pos] != item):
        print('current pos:%d' % pos)
        if(item < lis[pos]):
            highPos = pos          
        else:
            lowPos = pos
        pos = lowPos + int((highPos - lowPos)/2)
        time.sleep(1)

    print('finnally pos:%d' % pos)

if __name__ == "__main__":
    lis = [1,2,4,7,8,9,12,15,16,19,35,64,68]
    item = 68
    binary_search(lis, item)
