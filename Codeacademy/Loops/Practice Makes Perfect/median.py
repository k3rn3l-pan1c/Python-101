def median(sequence):
    sequence.sort()
    length = len(sequence)

    if (not length % 2) and length > 1:
        return (sequence[int(length/2)-1] + sequence[int(length/2)])/2.0
    else:
        return sequence[int(length /2)]
