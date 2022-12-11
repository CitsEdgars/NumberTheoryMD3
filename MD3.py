import os

def find_N1(R_values: list, S_values: list):
    N1 = 0
    R_values = R_values[1:]
    for idx, S_val in enumerate(S_values):
        N1 += S_val * (R_values[idx]*R_values[idx] - 1) / 8
    return N1

def find_N2(R_values: list):
    N2 = 0
    R_values = R_values[1:]
    for idx, R_val in enumerate(R_values[:-2]):
        N2 += (R_val - 1) * (R_values[idx + 1] - 1) / 4
    return N2

def get_R_S_values(a):
    log = 0
    while a % 2 == 0:
        log += 1
        a /= 2
    return a, log

def prepare_input(R_values: list):
    inverted = False
    if R_values[0] < R_values[1]:
        inverted = True
        temp = R_values[0]
        R_values[0] = R_values[1]
        R_values[1] = temp
    return inverted, R_values

if __name__ == "__main__":
    R_values = []
    S_values = []
    inverted = False
    processing = True

    with open(os.getcwd() + "\\ieeja.txt") as input:
        for line in input.readlines():
            R_values.append(int(line))

    if (len(R_values) != 2):
        print("Invalid input, stopping execution: {}". format(R_values))

    inverted, R_values = prepare_input(R_values)
    iter = 0
    
    while processing:
        R_val_temp = R_values[iter] % R_values[iter+1]
        R_val, S_val = get_R_S_values(R_val_temp)
        R_values.append(R_val)
        S_values.append(S_val)
        iter += 1
        if R_val == 1:
            N = find_N1(R_values, S_values) + find_N2(R_values)
            if (N % 2 == 0) == (not inverted): jacobi = 1
            else: jacobi = -1
            print("Jacobi Symbol is: {}, N value is: {}".format(jacobi, N))
            processing = False