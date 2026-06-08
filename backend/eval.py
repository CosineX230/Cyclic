# For maintaining clear variables:
# relation refers to the function that is associated with one of the mod conditions
# rule refers to both the relation and the mod condition

import re

def replace_coefficients(relation):
    relation = relation.replace('^', '**')
    relation = re.sub(r'(\d+)(?=[A-Za-z(])', r'\1*', relation)
    return relation.strip()

def build_expression(relations):
    rule_list = []
    modulus = len(relations)
    i = 0
    for relation in relations:
        relation = replace_coefficients(relation)
        #Appends a tuple to the rule list containing the modular condition and the expression itself
        rule_entry = ("x % " + str(modulus) + " == " + str(i), relation)
        rule_list.append(rule_entry)
        i += 1
    return rule_list

#returns the lambda function for each rule
def get_function(rules):
    def f(x):
        env = {"__builtins__": {}, "x": x, "n": x}
        for cond, expr in rules:
            if eval(cond, env):
                return eval(expr, env)
        raise ValueError("No rule matched for x = {}".format(x))
    return f

def generate_sequence(expr, start, max_terms=1000, max_value=10**12):
    function = get_function(expr)
    sequence = [start]
    seen = {start}
    x = start

    while len(sequence) < max_terms:
        x = function(x)
        if x is None:
            break

        if abs(x) > max_value:
            raise ValueError(
                f"Divergence detected: value exceeded max_value={max_value} ({x})"
            )

        sequence.append(x)
        if x in seen:
            break
        seen.add(x)

    if len(sequence) >= max_terms:
        raise ValueError(
            f"Sequence exceeded max_terms={max_terms} without repeating, possible divergence"
        )

    return sequence
