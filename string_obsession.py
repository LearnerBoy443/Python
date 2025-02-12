def string_obsession(main_string, substrings):
    dict = {}

    def string_split(given_string):
        if given_string in list:
            return list[given_string]
        
        max_count = 0
        
        for substring in substrings:
            if substring in given_string:
                new_string = given_string.replace(substring, "", 1)
                count = 1 + string_split(new_string)
                max_count = max(max_count, count)
        
        list[given_string] = max_count
        return max_count

    return string_split(main_string)

N = int(input("Number of substrings"))
substrings = list(set(input("Substrings:").split()))
main_string = input("Mainstring:").strip()

result = string_obsession(main_string, substrings)
print(result)