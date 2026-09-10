class MaximalMunchMatcher:
    """
    Maximal Munch Tree-Rewriting Instruction Selection.
    Tiles expression trees with target ISA instruction patterns greedily picking largest tiles.
    """
    def __init__(self):
        self.tiles = {
            ("+", "*", "const"): "MADD",
            ("+", "var", "const"): "ADDI",
            ("+", "var", "var"): "ADD",
            ("*", "var", "var"): "MUL",
        }

    def munch(self, expr):
        op, left, right = expr
        left_t = left[0] if isinstance(left, tuple) else ("const" if isinstance(left, int) else "var")
        right_t = right[0] if isinstance(right, tuple) else ("const" if isinstance(right, int) else "var")

        pattern = (op, left_t, right_t)
        if pattern in self.tiles:
            return [f"{self.tiles[pattern]} {left}, {right}"]

        code = []
        if isinstance(left, tuple):
            code.extend(self.munch(left))
        if isinstance(right, tuple):
            code.extend(self.munch(right))
        code.append(f"OP_{op} {left}, {right}")
        return code
