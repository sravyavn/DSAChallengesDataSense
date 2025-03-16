#Day1Question1: Sort tuples by sum of its elements

#t1=[(7,3),(1,2),(4,5),(0,1)]
# t2=tuple(t1)
# def sortbysum(t1):
#     sum=0
#     output=[]
#     for i in range(len(t1)):
#         if t1[i][0]+t1[i][1]>=sum:
#             sum=t1[i][0]+t1[i][1]
#             output.append(t1[i])
#     return output
#     print(output)
# sortbysum(t1)

t1=[(7,3),(1,2),(4,5),(0,1)]
t2=[(3, 1),(2, 2),(5, -1),(0, 0)]
t3=[(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]
def sort_by_tuple_sum(a):
    dict={i:i[0]+i[1] for i in t1}   #creating a dictionery with sum &sorting it using 'values'
    print(f"sum values are:{dict}")
    sorted_dict=sorted(dict.items(), key=lambda x:x[1])
    output=list(map(lambda x:x[0],sorted_dict))
    print(f"output is:{output}")
    return
sort_by_tuple_sum(t1)