import re;

def build_expression(rules):
    rule_list = []
    mod_base = len(rules)
    i = 0
    for rule in rules:
        rule_entry = ("x % " + str(mod_base) + " == " + str(i), rule)
        rule_list.append(rule_entry)
        i += 1
    return rule_list

def get_function(rules):
    def f(x):
        env = {"__builtins__": {}, "x": x}
        for cond, expr in rules:
            if eval(cond, env):
                return eval(expr, env)
        raise ValueError("No rule matched for x = {}".format(x))
    return f

def generate_sequence(expr, start, limit=100):
    function = get_function(expr)
    sequence = [start]
    x = start

    for _ in range(limit):
        x = function(x)
        if x in sequence:
            sequence.append(x)
            break
        sequence.append(x)
        if x is None:
            break
    return sequence;