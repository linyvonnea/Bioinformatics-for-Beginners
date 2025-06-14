# Code Challenge
def Reverse(Pattern):
    rev = ""
    for char in Pattern:
         rev = char + rev
    return rev 

def Complement(Pattern):
     comp = ""
     for char in Pattern:
        if char == "A":
               comp += "T"
        elif char == "T":
               comp += "A"
        elif char == "C":
               comp += "G"
        elif char == "G":
               comp += "C"
     return comp


def ReverseComplement(Pattern):
    rev = Reverse(Pattern)
    revcom = Complement(rev)
    return revcom

def PatternMatching(Pattern, Genome):
    positions = []
    k = len(Pattern)
    for i in range(len(Genome) - k + 1):
        if Genome[i:i+k] == Pattern:
            positions.append(i)
    return positions


# Exercise
import requests
with open("Vibrio_cholerae.txt", "r") as f:
    Genome = f.read().strip()

Pattern1 = "CTTGATCAT"
positions = PatternMatching(Pattern1, Genome)
print(positions)