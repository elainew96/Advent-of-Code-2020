# --- Day 1: Report Repair ---
# After saving Christmas five years in a row, you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
#
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them stars. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
#
# To save your vacation, you need to get all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
# Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
#
# Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?

expenses = [1150,1579,1361,1319,1201,1253,1806,1783,1164,1772,1920,1428,1918,245,1504,1952,1057,1977,704,1119,1971,1200,1650,1795,1877,1932,1811,1981,1803,1366,1580,1986,1976,1063,1895,1143,1991,1061,1855,1947,1134,1800,1898,1778,1964,1949,1103,1770,1321,2005,1758,1181,1140,1873,1946,1540,1909,1710,1705,1313,1196,1084,1870,1610,1708,1810,1133,1375,1264,1921,1624,41,1899,1226,1757,1978,1485,1385,1526,1653,1130,1223,1577,1912,1894,276,954,1269,1769,1924,93,1165,1812,1092,1402,1284,1903,1884,1581,1887,1963,1983,1233,1445,1974,1956,1691,1954,2000,1469,1875,955,1334,1116,1700,1818,1790,1704,1901,1072,1848,1990,1724,1719,1638,1311,1474,1837,1801,1929,1791,1317,1643,1632,1813,1488,1129,1998,1771,1793,1074,1826,1935,1462,1230,1797,1878,1751,1993,1437,1967,1844,1438,1969,1175,1823,1124,1922,154,936,1117,1145,1308,1320,1767,1850,1809,1350,1820,1082,1597,1913,1766,1701,1294,1556,2006,1480,1953,1104,1861,1966,1248,1671,1955,1863,1202,1356,1842,2010,1288,1067,1576,1295,1760,1888,1639,1282,1633,1619]

target = 2020

def find_two_expense_multiplication_output(target, expenses):
    for entry in expenses:
        target_entry = target-entry
        if target_entry in expenses:
            return target_entry * entry

def find_expense_multiplication_output(target, expenses, num_expenses):
    if num_expenses == 1:
        if target in expenses:
            return target
        else:
            return None
    for i in range(len(expenses)):
        entry = expenses[i]
        target_entry = target-entry
        next_expense = find_expense_multiplication_output(target_entry, expenses[(i+1):], num_expenses-1)
        if next_expense:
            return entry * next_expense


answer = find_two_expense_multiplication_output(target, expenses)
print(answer)

ans2 = find_expense_multiplication_output(target, expenses, 3)
print(ans2)
