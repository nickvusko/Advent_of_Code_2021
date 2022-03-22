
def parse_input(fh:str)->list:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
        lst = [int(x) for x in lines[0].split(",")]
    return sorted(lst)

def sort_crabs_1(herd:list)->dict:
    consumption = {}
    for i in range(min(herd), max(herd)+1):
        delta = 0
        for e in herd:
            delta += abs(e-i)
        consumption[i] = delta
    print(min(consumption, key = consumption.get), consumption[min(consumption, key = consumption.get)])
    return consumption

def sort_crabs_2(herd:list)->dict:
    consumption = {}
    for i in range(min(herd), max(herd)+1):
        delta = 0
        for e in herd:
            delta += sum([x for x in range(0,abs(e-i)+1)])
        consumption[i] = delta
    print(min(consumption, key = consumption.get), consumption[min(consumption, key = consumption.get)])
    return consumption

herd = parse_input("day_7")
x = sort_crabs_1(herd)
y = sort_crabs_2(herd)