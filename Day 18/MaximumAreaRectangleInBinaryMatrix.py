
def maximum_area_histogram(histogram):
    right_index = []
    left_index = []
    width = []
    area = []
    def nearest_small_left(histogram):
        stack = []
        psudoIndex = -1
        for i in range(len(histogram)):
            if len(stack) == 0:
                left_index.append(psudoIndex)
            
            elif len(stack) > 0 and stack[-1][0] < histogram[i]:
                left_index.append(stack[-1][1])

            elif len(stack) > 0 and stack[-1][0] >= histogram[i]:

                while len(stack) > 0 and stack[-1][0] >= histogram[i]:
                    stack.pop()
                
                if len(stack) == 0:
                    left_index.append(psudoIndex)
                else:
                    left_index.append(stack[-1][1])

            stack.append((histogram[i],i))

    
    def nearest_small_right(histogram):
        stack = []
        psudoIndex = len(histogram)
        
        for i in range(len(histogram)-1,-1,-1):
            if len(stack) == 0:
                right_index.append(psudoIndex)
            
            elif len(stack) > 0 and stack[-1][0] < histogram[i]:
                right_index.append(stack[-1][1])

            elif len(stack) > 0 and stack[-1][0] >= histogram[i]:

                while len(stack) > 0 and stack[-1][0] >= histogram[i]:
                    stack.pop()
                
                if len(stack) == 0:
                    right_index.append(psudoIndex)
                else:
                    right_index.append(stack[-1][1])

            stack.append((histogram[i],i))

        right_index.reverse()


    nearest_small_right(histogram)
    nearest_small_left(histogram)
    # print(left_index,right_index)

    for i in range(len(histogram)):
        width.append(right_index[i]-left_index[i]-1)

    max_area = 0
    for i in range(len(histogram)):
        # area = l * b -> l is length of building and b is width
        area = histogram[i] * width[i]
        max_area = max(area,max_area)
        

    return max_area

def max_area_rectangle_binary_matrix(mat):
    ans = []
    r = len(mat)
    c = len(mat[0])

    for j in range(r):
        ans.append(mat[0][j])

    max_ans = maximum_area_histogram(ans)

    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                ans[j] = 0

            else:
                ans[j] = ans[j] + mat[i][j]

    
        max_ans = max(max_ans,maximum_area_histogram(ans))

    return max_ans

mat = [[0,1,1,0],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0]]

print(max_area_rectangle_binary_matrix(mat))


    