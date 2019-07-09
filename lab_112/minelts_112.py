import sys
from priority_queue_112 import PQ

def main():
    pq = PQ()
    for lines in sys.stdin:
        pq.insert(int(lines.strip()))

    while pq.size() != int(sys.argv[1]):
        pq.delMax()

    while pq.size() != 0:
        print(pq.delMax())

if __name__ == '__main__':
    main()
