def interp(x_knots, y_knots, x_input):
    coords = list(zip(x_knots, y_knots))

    coords.sort(key=lambda x: (x[0], x[1]))
    print(coords)
    # extract case

    if x_input < coords[0][0]:
        print("extract lower")
        print(coords[0][0])
        print(coords[1][1])
        slope = (coords[1][1] - coords[0][1]) / (coords[1][0] - coords[0][0])
        iy = coords[0][1] + slope * (x_input - coords[0][0])
        print(slope, iy)
        return iy

    if x_input > coords[-1][0]:
        print("extract  upp")
        slope = (coords[-1][1] - coords[-2][1]) / (coords[-1][0] - coords[-2][0])
        iy = coords[-2][1] + slope * (x_input - coords[-2][0])
        print(slope, iy)
        return iy
    for i in range(1, len(coords)):
        print(coords[i - 1][1])

        if x_input == coords[i][0]:
            print("found x " + str(coords[i][1]))
            return  coords[i][1]

        if coords[i - 1][0] < x_input < coords[i][0]:
            print("x range")
            print(coords[i - 1][0], coords[i][0])
            print("y range")
            print(coords[i - 1][1], coords[i][1])
            slope = (coords[i][1] - coords[i - 1][1]) / (coords[i][0] - coords[i - 1][0])
            iy = coords[i - 1][1] + slope * (x_input -coords[i - 1][0] )
            print(slope, iy)
            return iy



if __name__ == "__main__":
    x = [1, 2.5, 3.4, 6, 5.8]
    y = [2, 4, 5.8, 4, 4.3]
    nx = 4
    print(interp(x, y, nx))
    x0 = [-2.0, -1.0, -1, 0, 1, 2]
    y0 = [0, 9, 10,  15, 0, 5]
    nx0 = -0.3
    print(interp(x0, y0, nx0))
    x1 = [1, 2.0, -2, -1, 0]
    y1 = [0, 9,   0, 10, 15]
    nx1 = -0.3
    print(interp(x1, y1, nx1))

    x2 = [-2.0, -1.0,  0, 1, 2]
    y2 = [0,  10,   15,   0, 5]
    nx2 = 3
    print(interp(x2, y2, nx2))