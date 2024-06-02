def parse_ranges(ranges_string):
    """
    Given a string in the format 1-3, 6, 8-10, return a list of those
    numbers in the order they appear in the string.
    """
    
    ranges = (i.split('-') for i in ranges_string.split(','))
    numbers = (i for start, stop in ranges for i in range(int(start), int(stop) + 1))
    return numbers
    
print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))