import asyncio
import collections
import itertools
import random

import aiohttp


def random_methods(n=100, word_file="/usr/share/dict/words", seed=0):
    prng = random.Random(x=seed)

    with open(word_file, mode="r") as f:
        words = [
            l.strip().encode("ascii", errors="ignore").decode("ascii").upper()
            for l in f
            if "'" not in l
        ]
    word_buckets = collections.defaultdict(list)
    for w in words:
        word_buckets[w[0]].append(w)

    letter_order = list(word_buckets)
    prng.shuffle(letter_order)

    methods = []
    for _, letter in zip(range(n), itertools.cycle(letter_order)):
        methods.append(prng.choice(word_buckets[letter]))

    prng.shuffle(methods)
    return methods


def check_theory1(ok, stuck):
    ok_starting_letters = "DEFIJKQVWXYZ"
    for m in ok:
        assert any(m.startswith(c) for c in ok_starting_letters)

    for m in stuck:
        assert not any(m.startswith(c) for c in ok_starting_letters)


async def main():
    methods = random_methods(n=100, seed=None)
    url = "http://localhost:8080/"

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=5)) as session:
        # check it's there at all
        await session.get(url)

        coros = [session.request(method, url) for method in methods]
        retvals = await asyncio.gather(*coros, return_exceptions=True)

    ok_methods = []
    stalled_methods = []
    for method, retval in zip(methods, retvals):
        if isinstance(retval, Exception):
            stalled_methods.append(method)
        else:
            ok_methods.append(method)

    ok_methods.sort()
    stalled_methods.sort()

    print("OK")
    print(ok_methods)
    print("\nSTUCK")
    print(stalled_methods)

    check_theory1(ok_methods, stalled_methods)


if __name__ == "__main__":
    asyncio.run(main())
