def gym():
    total_energy = int(input())
    machine = int(input())
    i = 0
    excesise = []
    for i in range(machine):
        temp = int(input())
        excesise.append(temp)
    machine_used = 0
    excesise = excesise.sort()
    for i in excesise:
        total_energy -= i
        machine_used += 1
        if total_energy <= 0:
            return (machine_used)
        total_energy -= i
        machine_used += 1
        if total_energy <= 0:
            return (machine_used)

    return (-1)
