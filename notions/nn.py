#simple neural net
def w_sum(a, b):
    assert(len(a)== len(b))
    output = 0
    for i in range(len(a)):
        output += (a[i] * b[i])
    return output

weights = [0.1, 0.2, 0]

# steps
def w_sum_p(a, b):
    assert(len(a)== len(b))
    output = 0
    for i in range(len(a)):
        print(f"vector: {i}")
        print(f" a[{i}] = {a[i]}")
        print(f" b[{i}] = {b[i]}")
        print(f"a[{i}] * b[{i}] = {a[i] * b[i]}")
        print(f"temp sum: {output}")
        output += (a[i] * b[i])
    return output

def nn(input, weights):
    prediction = w_sum_p(input, weights)
    return prediction

r1 = [8.5, 9.5, 9.9, 9.0]
r2 = [0.65, 0.8, 0.8, 0.9]
r3 = [1.2, 1.3, 0.5, 1.0]

input = [r1[0], r2[0], r3[0]]

pred = nn(input, weights)
print(pred)

