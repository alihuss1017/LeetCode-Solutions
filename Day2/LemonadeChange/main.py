class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cost = 5
        inventory = []
        for bill in bills:
            change = bill - cost
            inventory.append(bill)

            if bill == 20:
                if (5 in inventory and 10 in inventory):
                    inventory.remove(5)
                    inventory.remove(10)
                    continue
                elif inventory.count(5) >= 3:
                    for _ in range(3):
                        inventory.remove(5)
                else:
                    return False
            if bill == 10:
                if 5 in inventory:
                    inventory.remove(5)
                    continue
                else:
                    return False
        return True