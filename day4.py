#! /usr/bin/python3
import sys


def main():
    total = 0
    for x in range(264360, 746326):
        if qualify(x):
            total += 1
    print(total)

def qualify(number):
    dup = False
    repeat_count = 0
    last = '/'
    for i in str(number):
        if last == i:
            repeat_count += 1
        else:
            if repeat_count == 1:
                dup = True
            repeat_count = 0
        if i < last:
            return False
        last = i
    if repeat_count == 1:
        dup = True
    return dup
      
        

if __name__ == '__main__':
    main()
