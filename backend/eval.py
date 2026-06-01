import re;

def build_expression(rules):
    rule_list = []
    mod_base = len(rules)
    i = 0
    for rule in rules:
        rule_entry = ("n % " + str(mod_base) + " == " + str(i), rule)
        rule_list.append(rule_entry)
        i += 1
    return rule_list

def get_function(rules):
    def f(n):
        env = {"__builtins__": {}, "n": n}
        for cond, expr in rules:
            if eval(cond, env):
                return eval(expr, env)
        raise ValueError("No rule matched for n = {}".format(n))
    return f

def generate_sequence(expr, start, limit=100):
    function = get_function(expr)
    sequence = [start]
    n = start

    for _ in range(limit):
        n = function(n)
        if n in sequence:
            sequence.append(n)
            break
        sequence.append(n)
        if n is None:
            break
    return sequence;