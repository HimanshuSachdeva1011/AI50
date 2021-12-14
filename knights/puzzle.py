from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    
    # Basic Code For Character That they can be either Knight And Knave 
    Or(AKnave, AKnight),
    
    # They can't be Both at the Same time
    Not(And(AKnave, AKnight)),
    
    Biconditional(AKnight, And(AKnave, AKnight))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    
    # Basic Code For Character That they can be either Knight And Knave 
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    
    # They can't be Both at the Same time
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    
    # Statement Mentioned Above as one is knight and other is knave and we are assured that one is knight
    # This is because the other one didn't say anything
    # It leaves other as knave
    Biconditional(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    
    # A and B are either knights or knaves
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),

    # A says "We are the same kind."
    # B says "We are of different kinds."
    Biconditional(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    Biconditional(BKnight, Or(And(AKnave, BKnight), And(AKnight, BKnave))),
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    
    # Basic Code For Character That they can be either Knight And Knave 
    Or(AKnave, AKnight),
    Or(BKnave, BKnight),
    Or(CKnave, CKnight),
    
    # They can't be Both at the Same time
    Not(And(AKnave, AKnight)),
    Not(And(BKnave, BKnight)),
    Not(And(CKnave, CKnight)),
    
    # A can be either knight or knave 
    # B Depends on A's statement and says C is a knave
    # C says A is knight
    Biconditional(Or(AKnight, AKnave), Or(AKnight, AKnave)),
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    Biconditional(BKnight, CKnave),
    Biconditional(CKnight, AKnight)   
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
