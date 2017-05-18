def my_reduce(value):
    mean_temperature = 0
    sum_temp=0
    div=0
    for val in value:
        for v in val:
            sum_temp+=float(v)
            div+=1
    mean_temperature=sum_temp/div
    return mean_temperature