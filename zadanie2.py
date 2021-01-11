list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]
i_outer=0
i_inner=0
tmp_i=0
tmp=list_to_sort[0]

while i_outer<4:
    i_inner=i_outer+1
    tmp_i=i_outer
    while i_inner<4:
        if list_to_sort[tmp_i][1]>=list_to_sort[i_inner][1]:
            if list_to_sort[tmp_i][1]==list_to_sort[i_inner][1]:
                if list_to_sort[tmp_i][2]>list_to_sort[i_inner][2]:
                    tmp_i=i_inner
            else:
                tmp_i=i_inner
        i_inner+=1
    tmp=list_to_sort[tmp_i]
    list_to_sort[tmp_i]=list_to_sort[i_outer]
    list_to_sort[i_outer]=tmp
    i_outer+=1