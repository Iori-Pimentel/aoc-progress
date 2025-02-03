def follow_ahead(ahead, behind):
    delta = ahead - behind
    distance = max(abs(delta.real), abs(delta.imag))

    if distance <= 1:
        return behind

    clamped_delta = [max(-1, min(1, component)) for component in (delta.real, delta.imag)]
    return behind + complex(*clamped_delta)

def track_tail_positions(size):
    segments = [0] * size
    HEAD, TAIL = 0, -1
    visited = set()
    for instruction in open("inputs/2022-9.txt"):
        direction, steps = instruction.split()
        direction = { "U": 1j, "D": -1j, "R": 1, "L": -1 }[direction]
        steps = int(steps)

        for _ in range(steps):
            segments[HEAD] += direction

            for ahead in range(size-1):
                behind = ahead + 1
                segments[behind] = follow_ahead(segments[ahead], segments[behind])

            visited.add(segments[TAIL])

    return len(visited)

print(track_tail_positions(2), track_tail_positions(10))
