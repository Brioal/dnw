import re

# 编码向值的映射
code_value_dict = {'M': 4, 'X': 7, '3': 3, 'A': 1, 'R': 9, 'W': 6, 'T': 3, 'J': 1, 'L': 3, '4': 4, '2': 2, 'Z': 9, 'B': 2, '1': 1, 'N': 5, 'E': 5, 'G': 7, 'K': 2, '8': 8, 'U': 4, 'H': 8, '0': 0, 'D': 4, 'Y': 8, 'S': 2, '9': 9, 'F': 6, '7': 7, 'C': 3, 'P': 7, '5': 5, 'V': 5, '6': 6}
# 位置向权重的映射
position_weight_dict = {1: 8, 2: 7, 3: 6, 4: 5, 5: 4, 6: 3, 7: 2, 8: 10, 9: 0, 10: 9, 11: 8, 12: 7, 13: 6, 14: 5, 15: 4, 16: 3, 17: 2}
# 校验码向校验值的映射
check_dict = {'X': 10, '9': 9, '6': 6, '3': 3, '4': 4, '0': 0, '8': 8, '1': 1, '7': 7, '2': 2, '5': 5}


def pre_check_vin(vin):
    pattern = '\w+'
    text = vin
    result = re.findall(pattern, text, re.A)
    if(len(result) != 1):
        return False
    vin = result[0]
    if (len(vin) != 17):
        return False
    if((vin.find('I') != -1) or (vin.find('O') != -1) or (vin.find('Q') != -1)):
        return False
    try:
        is_exist = check_dict[vin[8]]
    except:
        return False
    return True


def check_vin(vin):
    vin = vin.upper()
    if(pre_check_vin(vin) == False):
        return False
    sum_value = 0
    for i in range(len(vin)):
        code = vin[i]
        value = code_value_dict[code]
        weight = position_weight_dict[i+1]
        sum_value = sum_value + (value * weight)
    check_value = sum_value % 11
    check_value_in_vin = int(vin[8])
    return check_value_in_vin == check_value

