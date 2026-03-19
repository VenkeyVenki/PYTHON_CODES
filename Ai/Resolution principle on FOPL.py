#Implement resolution principle on FOPL related problems	


from typing import List, Tuple, Optional
from copy import deepcopy
def is_variable(x: str) -> bool:
    return x[0].islower()
def unify(x: str, y: str) -> Optional[dict]:
    if x == y:
        return {}
    elif is_variable(x):
        return {x: y}
    elif is_variable(y):
        return {y: x}
    else:
        return None
def substitute(clause: List[str], subs: dict) -> List[str]:
    result = []
    for literal in clause:
        neg = False
        if literal.startswith('¬'):
            neg = True
            literal = literal[1:]
        pred, args = literal.split('(')
        args = args.strip(')').split(',')
        new_args = [subs.get(arg, arg) for arg in args]
        new_literal = f"{pred}({','.join(new_args)})"
        if neg:
            new_literal = '¬' + new_literal
        result.append(new_literal)
    return result
def resolve(ci: List[str], cj: List[str]) -> List[List[str]]:
    resolvents = []
    for li in ci:
        for lj in cj:
            if li.startswith('¬') and not lj.startswith('¬') and li[1:].split('(')[0] == lj.split('(')[0]:
                xi = li[1:]
                xj = lj
            elif lj.startswith('¬') and not li.startswith('¬') and lj[1:].split('(')[0] == li.split('(')[0]:
                xi = li
                xj = lj[1:]
            else:
                continue
            pred_i, args_i = xi.split('(')
            args_i = args_i.strip(')').split(',')
            pred_j, args_j = xj.split('(')
            args_j = args_j.strip(')').split(',')
            if len(args_i) != len(args_j):
                continue
            subs = {}
            for a, b in zip(args_i, args_j):
                res = unify(a, b)
                if res is None:
                    break
                subs.update(res)
            else:
                new_ci = [l for l in ci if l != li]
                new_cj = [l for l in cj if l != lj]
                new_clause = substitute(new_ci + new_cj, subs)
                resolvents.append(new_clause)
    return resolvents
def resolution(clauses: List[List[str]]) -> bool:
    new = []
    while True:
        n = len(clauses)
        for i in range(n):
            for j in range(i + 1, n):
                resolvents = resolve(clauses[i], clauses[j])
                for r in resolvents:
                    if not r:
                        return True
                    if r not in new and r not in clauses:
                        new.append(r)
        if not new:
            return False
        clauses.extend(new)
kb = [
    ['¬Human(x)', 'Mortal(x)'],
    ['Human(Socrates)'],
    ['¬Mortal(Socrates)']
]
if resolution(kb):
    print("Query is entailed: Socrates is Mortal")
else:
    print("Query is NOT entailed")
