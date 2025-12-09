# Matrix = [[0]*8]*8
# cont = []
# num =0
# for a in range(len(Matrix)):
#     for b in range(len(Matrix)):
#         if a==b or a== b+1 or a== b-1:
#             continue
#         for c in range(len(Matrix)):
#             if a==c or b==c or a==c +2 or a==c-2 or b == c+ 1 or b==c-1:
#                 continue
#             for d in range(len(Matrix)):
#                 if a==d or a==d+3 or a==d-3 or b==d or b==d+2 or b==d-2 or c==d or c==d+1 or c==d-1:
#                     continue
#                 for e in range(len(Matrix)):
#                     if a==e or a==e+4 or a==e-4 or b==e or b==e+3 or b==e-3 \
#                             or c==e or c==e+2 or c==e-2 or d == e or d == e+1 or d == e-1:
#                         continue
#                     for f in range(len(Matrix)):
#                         if a==f or a==f+5 or a==f-5 or b==f or b==f+4 or b==f-4 \
#                                 or c == f or c == f+3 or c == f-3 or d==f or d==f+2 or d==f-2\
#                                 or e==f or e==f+1 or e==f-1:
#                             continue
#                         for g in range(len(Matrix)):
#                             if a==g or a==g+6 or a==g-6 or b==g or b==g+5 or b==g-5 \
#                                     or c==g or c==g+4 or c==g-4 or d==g or d==g+3 or d==g-3 \
#                                     or e==g or e==g+2 or e==g-2 or f==g or f==g+1 or f==g-1:
#                                 continue
#                             for h in range(len(Matrix)):
#                                 if a==h or a==h-7 or a==h+7 or b==h or b==h-6 or b==h+6\
#                                         or c==h or c==h-5 or c==h+5 or d==h or d==h-4 or d==h+4\
#                                         or e==h or e==h-3 or e==h+3 or f==h or f==h-2 or f==h+2\
#                                         or g==h or g==h-1 or g==h+1:
#                                     continue
#                                 cont.append([a,b,c,d,e,f,g,h])
# print(len(cont),cont)



