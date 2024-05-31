def partition_iterable_equal_chunks(iterable, batch_size, return_list=True):
    """Given an iterable, split the iterable into a list of lists, with a given batch size.  The final
    chunk will be smaller given an uneven-sized iterable.  By default, it returns a full list of batches,
    but for very large applications, it can be used in a generator expression by setting `return_list` to
    False.  The return value then is usable in a for-loop or other iterator context.

    :param iterable: any Python iterable
    :param batch_size: int, size of chunks desired
    :param return_list: bool, defaults to True.
    :return: list of lists, each of size `size`.
    """
    # k, m = len(iterable) / size, len(iterable) % size
    # return list((iterable[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in xrange(size)))
    def chunk_gen(iterable, batchsize):
        for i in range(0, len(iterable), batchsize):
            yield iterable[i : i + batchsize]

    if return_list is True:
        return list(chunk_gen(iterable, batch_size))
    else:
        return chunk_gen(iterable, batch_size)
