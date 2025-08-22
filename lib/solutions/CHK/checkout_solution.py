from collections import Counter

class CheckoutSolution:

     # skus = unicode string
    def checkout(self, skus):
        # Validate input
        if not isinstance(skus, str):
            return -1
        valid = set("ABCDE")
        if any(ch not in valid for ch in skus):
            return -1

        PRICE = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}

        cnt = Counter(skus)

        total = 0

        # Offer: 2E -> 1B free
        free_bs = cnt.get("E", 0) // 2
        chargeable_b = max(cnt.get("B", 0) - free_bs, 0)

        # Multi-price for A: 5A for 200, 3A for 130, then singles
        a = cnt.get("A", 0)
        total += (a // 5) * 200
        a %= 5
        total += (a // 3) * 130
        a %= 3
        total += a * PRICE["A"]

        # B: 2B for 45 (after freebies), then singles
        total += (chargeable_b // 2) * 45
        total += (chargeable_b % 2) * PRICE["B"]

        # C, D, E at base price
        total += cnt.get("C", 0) * PRICE["C"]
        total += cnt.get("D", 0) * PRICE["D"]
        total += cnt.get("E", 0) * PRICE["E"]

        return total

