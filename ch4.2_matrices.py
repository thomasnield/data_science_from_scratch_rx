from rx import Observable


def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0

    return num_rows, num_cols


def get_row(A, i):
    return Observable.from_(A).find_index(lambda t: t.index == i).take(1)


if __name__ == "__main__":
    get_row([[1,1],[2,2]], 1).subscribe(lambda v: print(v))
