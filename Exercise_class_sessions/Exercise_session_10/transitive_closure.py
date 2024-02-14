with open('input.txt', 'r') as f:
    lines = f.readlines()
print(lines)

def all_dependencies(p):
    """Return a set of all dependencies of p."""
    if p in lines:
        return lines[p]
    else:
        return set()