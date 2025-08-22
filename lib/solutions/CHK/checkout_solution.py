from collections import Counter

class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus):
        # Validate input
        if not isinstance(skus, str):
            return -1
        valid = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        if any(ch not in valid for ch in skus):
            return -1

        PRICE = {
            "A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10,
            "G": 20, "H": 10, "I": 35, "J": 60, "K": 80, "L": 90,
            "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
            "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90,
            "Y": 10, "Z": 50
        }

        def apply_multibuy(count, offers, unit_price):
            """
            Apply tiered offers, preferring larger bundles first.
            offers: list of (bundle_size, bundle_price)
            """
            subtotal = 0
            rem = count
            for size, price in sorted(offers, key=lambda x: -x[0]):
                take = rem // size
                if take:
                    subtotal += take * price
                    rem -= take * size
            subtotal += rem * unit_price
            return subtotal

        cnt = Counter(skus)
        total = 0

        # -------- Cross-item freebies (adjust chargeable counts first) --------
        # 2E -> 1B free
        free_B = cnt.get("E", 0) // 2
        chargeable_B = max(cnt.get("B", 0) - free_B, 0)

        # 3N -> 1M free
        free_M = cnt.get("N", 0) // 3
        chargeable_M = max(cnt.get("M", 0) - free_M, 0)

        # 3R -> 1Q free
        free_Q = cnt.get("R", 0) // 3
        chargeable_Q = max(cnt.get("Q", 0) - free_Q, 0)

        # -------------------- Per-item pricing --------------------
        # A: 5 for 200, then 3 for 130
        total += apply_multibuy(cnt.get("A", 0), [(5, 200), (3, 130)], PRICE["A"])

        # B: 2 for 45 (after E freebies)
        total += apply_multibuy(chargeable_B, [(2, 45)], PRICE["B"])

        # C, D: unit prices
        total += cnt.get("C", 0) * PRICE["C"]
        total += cnt.get("D", 0) * PRICE["D"]

        # E: unit price
        total += cnt.get("E", 0) * PRICE["E"]

        # F: buy 2 get 1 free => every 3 costs 2 * 10
        f = cnt.get("F", 0)
        total += (f // 3) * (2 * PRICE["F"]) + (f % 3) * PRICE["F"]

        # G: unit
        total += cnt.get("G", 0) * PRICE["G"]

        # H: 10 for 80, 5 for 45
        total += apply_multibuy(cnt.get("H", 0), [(10, 80), (5, 45)], PRICE["H"])

        # I, J: unit
        total += cnt.get("I", 0) * PRICE["I"]
        total += cnt.get("J", 0) * PRICE["J"]

        # K: 2 for 150
        total += apply_multibuy(cnt.get("K", 0), [(2, 150)], PRICE["K"])

        # L: unit
        total += cnt.get("L", 0) * PRICE["L"]

        # M: unit after N freebies applied
        total += chargeable_M * PRICE["M"]

        # N: unit
        total += cnt.get("N", 0) * PRICE["N"]

        # O: unit
        total += cnt.get("O", 0) * PRICE["O"]

        # P: 5 for 200
        total += apply_multibuy(cnt.get("P", 0), [(5, 200)], PRICE["P"])

        # Q: 3 for 80 (after R freebies)
        total += apply_multibuy(chargeable_Q, [(3, 80)], PRICE["Q"])

        # R: unit
        total += cnt.get("R", 0) * PRICE["R"]

        # S, T: unit
        total += cnt.get("S", 0) * PRICE["S"]
        total += cnt.get("T", 0) * PRICE["T"]

        # U: "3U get one U free" => every 4 pay for 3
        u = cnt.get("U", 0)
        total += (u - (u // 4)) * PRICE["U"]

        # V: 3 for 130, 2 for 90
        total += apply_multibuy(cnt.get("V", 0), [(3, 130), (2, 90)], PRICE["V"])

        # W, X, Y, Z: unit
        total += cnt.get("W", 0) * PRICE["W"]
        total += cnt.get("X", 0) * PRICE["X"]
        total += cnt.get("Y", 0) * PRICE["Y"]
        total += cnt.get("Z", 0) * PRICE["Z"]

        return total

