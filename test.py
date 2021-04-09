# S = 'BAOOLLNNOLOLGBAX'
# occurance = 0
# run = True
# while run:
#     counter = 0
#     temp_string = S
#     for balloon in 'BALLOON':
#         if balloon in temp_string:
#             temp_string = temp_string[0:temp_string.index(balloon)] + temp_string[temp_string.index(balloon) + 1:len(temp_string)]
#             counter += 1
#     if counter == 7:
#         occurance += 1
#         S = temp_string
#     else:
#         run = False
#         break
#
# print(occurance)

S = 'azABaabZA'
balanced_S = []
for i in range(0, len(S)):
    if S[i].lower() in S and S[i].upper() in S:
          continue
    else:
        balanced_S.append(S[0:i])




