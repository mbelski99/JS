list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
i_o=0
i_i=0
tmp_i=0
tmp=list_to_sort[0]

while i_o<4:
    i_inner=i_o+1
    tmp_i=i_o
    while i_i<4:
        if list_to_sort[tmp_i][1]>=list_to_sort[i_i][1]:
            if list_to_sort[tmp_i][1]==list_to_sort[i_i][1]:
                if list_to_sort[tmp_i][2]>list_to_sort[i_i][2]:
                    tmp_i=i_i
            else:
                tmp_i=i_i
        i_i+=1
    tmp=list_to_sort[tmp_i]
    list_to_sort[tmp_i]=list_to_sort[i_o]
    list_to_sort[i_o]=tmp
    i_o+=1