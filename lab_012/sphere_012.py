import sys
from math import pi
def sphere(r):
    area = 4 * pi * (r ** 2)
    vol = (4 / 3) * pi * (r ** 3)
    area_p = "{:.2f}".format(area)
    vol_p = "{:.2f}".format(vol)
    return '{:>10s} {:>15s} {:>15s}'.format(str(r), str(area_p), str(vol_p))

def main():
    start_r = float(sys.argv[1])
    inc_r = float(sys.argv[2])
    end_r = float(sys.argv[3])

    h1 = 'Radius (m)'
    h4 = '-' * len(h1)
    h2 = 'Area (m^2)'
    h5 = '-' * len(h2)
    h3 = 'Volume (m^3)'
    h6 = '-' * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))
    rad = start_r
    while rad <= end_r:
        print(sphere(rad))
        rad = rad + inc_r


if __name__ == '__main__':
    main()
