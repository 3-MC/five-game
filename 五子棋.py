# x=[[0 for i in range(9)]for j in range(9)]
# while True:
#     try:
#         h=list(map(int,input().split()))
#         b=list(map(int,input().split()))
#
#         if 0<=h[0]<=8 and 0<=h[1]<=8 and x[h[0]][h[1]]==0:
#             x[h[0]][h[1]]=1
#         if 0<=b[0]<=8 and 0<=b[1]<=8 and x[b[0]][b[1]]==0:
#             x[b[0]][b[1]]=2
#         for i in x:
#             print(i)
#         count = 0
#         for i in x:
#             for j in range(9):
#                 if i[j] == 1:
#                     count += 1
#                     if count >= 5:
#                         print('winer is h')
#                         break
#                 else:
#                     count = 0
#         # if count >= 5:
#         #     print('winer is h')
#         for i in x:
#             for j in range(9):
#                 if i[j] == 2:
#                     count += 1
#                     if count >= 5:
#                         print('winer is b')
#                         break
#                 else:
#                     count = 0
#         # if count >= 5:
#         #     print('winer is b')
#     except:
#         continue

# for i in range(9):
#     for j in range(9):
#         if sum(x[i][j:j+5])==5 or sum(x[i:i+5][j])==5:
#             print('winer is h')
#         elif sum(x[i][j:j+5])==10 or sum(x[i:i+5][j])==10:
#             print('winer is b')

x=[[0 for i in range(9)]for j in range(9)]
while True:
    try:
        h=list(map(int,input().split()))
        b=list(map(int,input().split()))

        if 0<=h[0]<=8 and 0<=h[1]<=8 and x[h[0]][h[1]]==0:
            x[h[0]][h[1]]=1
        if 0<=b[0]<=8 and 0<=b[1]<=8 and x[b[0]][b[1]]==0:
            x[b[0]][b[1]]=2
        for i in x:
            print(i)
        for i in range(9):
            for j in range(9):

                if sum(x[i][j:j+5])==5 or sum([x[i][j], x[i+1][j]])==5:
                    print('winer is h')
                    exit()
                elif sum(x[i][j:j+5])==10 or sum(x[i:i+5][j])==10:
                    print('winer is b')
                    exit()
    except:
        continue