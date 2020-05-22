class RomanToInteger:

    def romanToInt(self, s: str) -> int:
        letters = list(s)
        romanMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        total = 0
        prev_value = 0
        for index in range(len(letters)):
            current_val = romanMap[letters.pop()]

            if current_val >= prev_value:
                total = total + current_val
            else:
                total = total - current_val

            prev_value = current_val

        return total
