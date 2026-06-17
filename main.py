# DNA Sequence Analyzer - My First Bioinformatics Project

def analyze_dna(sequence):
    sequence = sequence.upper()

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    if length == 0:
        print("Empty sequence")
        return

    gc = ((g + c) / length) * 100

    print("\n--- DNA ANALYSIS ---")
    print("Length:", length)
    print("A:", a, "T:", t, "G:", g, "C:", c)
    print("GC Content:", round(gc, 2), "%")


# Example
dna = "ATGCGATACGCTTGA"
analyze_dna(dna)
