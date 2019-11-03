# -*- coding: utf-8 -*-
"""
Aouther: Subic
Time: 2019/10/29: 8:51
"""
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        万年历 1971/01/01 星期五
        找闰年
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        What_day = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        Num_leap_year = 0
        for i in range(1971, year):
            if (i%4==0 and i%100 !=0) or i%400 == 0:
                Num_leap_year += 1
        Num_day = (year - 1971)*365 + Num_leap_year + sum(months[:month-1])+day
        if ((year % 4 == 0 and year % 100 != 0) or year % 400==0) and month>2:
            Num_day += 1
        count = Num_day % 7
        return What_day[count-1]


if __name__ == '__main__':
    day = 29
    month = 10
    year = 2019
    solver = Solution()
    r = solver.dayOfTheWeek(day, month, year)
    print(r)
