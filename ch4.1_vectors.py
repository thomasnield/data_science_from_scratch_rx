from rx import Observable


def vector_add(obs1, obs2):
    return Observable.zip(obs1, obs2, lambda x, y: x + y)


def vector_subtract(obs1, obs2):
    return Observable.zip(obs1, obs2, lambda x, y: x - y)


def vector_sum(obs):
    return obs.sum()


def scalar_multiply(obs, scalar):
    return obs.map(lambda i: i * scalar)


def vector_mean(obs):
    return obs.average()


def dot_product(obs1, obs2):
    return Observable.zip(obs1, obs2, lambda x, y: x * y).sum()


def sum_of_squares(obs):
    return dot_product(obs, obs)


def magnitude(obs):
    return sum_of_squares(obs).map(lambda i: math.sqrt(i))


def squared_distance(obs1, obs2):
    return sum_of_squares(vector_subtract(obs1, obs2))


if __name__ == "__main__":
    x = Observable.from_([1, 5, 10])
    y = Observable.from_([10, 100, 1000])

    squared_distance(x, y).subscribe(lambda i: print(i))


