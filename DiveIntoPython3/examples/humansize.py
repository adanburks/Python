SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PIB', 'ZiB', 'YiB']}

def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    ''' Convert a file size into human-readable form

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000
    returns: string

    '''
    if size < 0:
        raise ValueError('Number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES [multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('Number is too large')

if __name__ == '__main__':
    print(approximate_size(1234567890, False))
    print(approximate_size(1234567890))
