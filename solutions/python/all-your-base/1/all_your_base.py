def rebase(input_base, digits, output_base):
    base_ten = 0
    final_ans = []
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < input_base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if input_base != 10:
        for idx, stuff in enumerate(digits):
            base_ten += stuff * input_base**(len(digits)-idx-1)
    else:
        base_ten = int("".join([str(x) for x in digits]))
    if output_base == 10:
        return [int(x) for x in str(base_ten)]
    answer = int(base_ten / output_base)
    final_ans.append(base_ten % output_base)
    while answer != 0:
        final_ans.append(answer % output_base)
        answer = int(answer / output_base)
    return final_ans[::-1]
