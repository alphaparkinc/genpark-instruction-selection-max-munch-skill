from client import MaximalMunchMatcher

def main():
    print("=== Testing Maximal Munch Instruction Selector ===")
    matcher = MaximalMunchMatcher()

    ast = ("+", "register_x", 16)
    instructions = matcher.munch(ast)
    print("Munched AST into target instructions:")
    for instr in instructions:
        print(" ", instr)

    assert instructions == ["ADDI register_x, 16"]
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
