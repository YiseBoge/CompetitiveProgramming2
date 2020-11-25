class Solution:
    def readBinaryWatch(self, num: int) -> list:
        results = []
        for hour in range(12):
            for minute in range(60):
                hour_bits, h = 0, hour
                while h:
                    q, r = divmod(h, 2)
                    if r == 1:
                        hour_bits += 1
                    h = q

                minute_bits, m = 0, minute
                while m:
                    q, r = divmod(m, 2)
                    if r == 1:
                        minute_bits += 1
                    m = q

                if hour_bits + minute_bits == num:
                    hour_string = str(hour)
                    minute_string = str(minute) if minute > 9 else "0" + str(minute)
                    results.append(hour_string + ":" + minute_string)
        return results
