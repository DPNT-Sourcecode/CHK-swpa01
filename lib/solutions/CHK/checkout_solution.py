from collections import Counter

class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        # Validate input
        if not isinstance(skus, str):
            return -1
        valid = set("ABCDEF")
        if any(ch not in valid for ch in skus):
            return -1

        PRICE = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10}

        cnt = Counter(skus)
        total = 0

        # E offer: 2E -> 1B free (reduce chargeable B's)
        free_b = cnt.get("E", 0) // 2
        chargeable_b = max(cnt.get("B", 0) - free_b, 0)

        # A offers: 5A for 200, then 3A for 130, then singles
        a = cnt.get("A", 0)
        total += (a // 5) * 200
        a %= 5
        total += (a // 3) * 130
        a %= 3
        total += a * PRICE["A"]

        # B offer: 2B for 45 on remaining (chargeable) B's
        total += (chargeable_b // 2) * 45
        total += (chargeable_b % 2) * PRICE["B"]

        # C, D, E at base price
        total += cnt.get("C", 0) * PRICE["C"]
        total += cnt.get("D", 0) * PRICE["D"]
        total += cnt.get("E", 0) * PRICE["E"]

        # F offer: "buy 2 get 1 free" => every 3 Fs cost 2*10 = 20
        f = cnt.get("F", 0)
        total += (f // 3) * (2 * PRICE["F"])  # pay for 2 out of each 3
        total += (f % 3) * PRICE["F"]

        return total