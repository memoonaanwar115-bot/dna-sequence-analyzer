def analyze_dna(sequence):
    sequence = sequence.upper()

    length = len(sequence)
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    gc = ((g + c) / length) * 100

    print("Length:", length)
    print("A:", a)
    print("T:", t)
    print("G:", g)
    print("C:", c)
    print("GC Content:", round(gc, 2), "%")


dna = "ATGCGATACGCTTGA"
analyze_dna(dna)
