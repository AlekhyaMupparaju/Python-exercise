n=raw_input()
if n.isalnum():
    for c in n:
        if c.isdigit():
            print c,
