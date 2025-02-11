import re
from itertools import batched
data = open("inputs/2023-5.txt").read().split("\n\n")
seeds, *mappings = data

seeds = re.findall(r"\d+", seeds)
seeds = [int(x) for x in seeds]
mappings = {(name_source, name_destination): info
    for section in mappings
    for section in [section.splitlines()]
    for header, *info in [section]
    for header in [re.search(r"(\w+)-to-(\w+)", header).groups()]
    for name_source, name_destination in [header]
    for info in [[[int(x) for x in line.split()] for line in info]]
}

def goto_end(target_value):
    for section in mappings.values():
        for destination, source, ranging in section:
            if target_value in range(source, source+ranging):
                target_value = target_value-source+destination
                break
    return target_value

print(min(goto_end(seed) for seed in seeds))

def translate(to_be_translated, translators):
    for translator_destination, translator_source, translator_range in translators:
        translator_start = translator_source
        translator_end = translator_source + translator_range
        translator_offset = translator_destination - translator_source

        untranslated = []
        for untranslated_start, untranslated_end in to_be_translated:
            if untranslated_end <= translator_start or untranslated_start >= translator_end:
                no_overlap = (untranslated_start, untranslated_end)
                untranslated.append(no_overlap)
                continue

            if untranslated_start < translator_start:
                before_overlap = (untranslated_start, min(untranslated_end, translator_start))
                untranslated.append(before_overlap)
                untranslated_start = translator_start
            if untranslated_end > translator_end:
                after_overlap = (max(untranslated_start, translator_end), untranslated_end)
                untranslated.append(after_overlap)
                untranslated_end = translator_end

            yield untranslated_start + translator_offset, untranslated_end + translator_offset

        to_be_translated = untranslated

    yield from untranslated

to_be_translated = ((start, start + size) for start, size in batched(seeds, 2))
for translators in mappings.values():
    to_be_translated = translate(to_be_translated, translators)

print(min(start for start, end in to_be_translated))
