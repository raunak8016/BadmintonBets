def check_score(score):
    for game in score:
        for sc in game:
            if sc > 21:
                return False
    return True

def handle_score(score):
    try:
        sc = score.split(', ')
        ret_sc = []
        for game in sc:
            split_g = game.split('-')
            p1_g = int(split_g[0])
            p2_g = int(split_g[1])
            ret_sc.append([p1_g, p2_g])
        if len(ret_sc) < 3:
            ret_sc.append([0, 0])
        return ret_sc
    except:
        return [[0, 0], [0, 0], [0, 0]]
# this function is used to handle the scraped score of a match and was painfully written
def handle_score_complex(score: str):
    # sc = []
    # one = [-1, -1]
    # two = [-1, -1]
    # three = [0, 0]
    # num_games = 2
    # if score[1]=='-':
    #     num_games = 3
    #     one[0] = int(score[0])
    #     one[1] = 21
    #     score = score[4:]
    #     two[0] = 21
    #     score = score[3:]
    #     if score[4]=='-':
    #         two[1]=int(score[0:2])
    #         three[0]=int(score[2:4])
    #         three[1]=int(score[5:])
    #     elif score[3]=='-':
    #         two[1]=int(score[0:1])
    #         three[0]=int(score[1:3])
    #         three[1]=int(score[4:])
    # elif score[2]=='-':
    #     one[0] = int(score[0:2])
    #     score = score[3:]
    #  #   print(score)
    #     if score[4]=='-':
    #         one[1]=int(score[0:2])
    #         two[0]=int(score[2:4])
    #         score = score[5:]
    #         print(score)
    #         if len(score)>2:
    #             if score[4]=='-':
    #                 two[1]=int(score[0:2])
    #                 three[0]=int(score[2:4])
    #                 three[1]=int(score[5:])
    #             elif score[3]=='-':
    #                 two[1]=int(score[0:1])
    #                 three[0]=int(score[1:3])
    #                 three[1]=int(score[4:])
    #         else:
    #             two[1]=int(score)
    #     elif score[3]=='-':
    #         first = int(score[0:2])
    #         second = int(score[1:3])
    #         if first <= 21:
    #             one[1] = first
    #             two[0] = int(score[2:3])
    #             if second == 21:
    #                 one[1] = int(score[0:1])
    #                 two[0] = second
    #         elif second <= 21:
    #             one[1] = int(score[0:1])
    #             two[0] = second
    #         score = score[4:]
    #         if len(score)>2:
    #             if score[4]=='-':
    #                 two[1]=int(score[0:2])
    #                 three[0]=int(score[2:4])
    #                 three[1]=int(score[5:])
    #             elif score[3]=='-':
    #                 two[1]=int(score[0:1])
    #                 three[0]=int(score[1:3])
    #                 three[1]=int(score[4:])
    #         else:
    #             two[1]=int(score)
    #     elif score[2]=='-':
    #         one[1] = int(score[0:1])
    #         two[0] = int(score[1:2])
    #         score = score[3:]
    #         if score[4]=='-':
    #                 two[1]=int(score[0:2])
    #                 three[0]=int(score[2:4])
    #                 three[1]=int(score[5:])
    #         elif score[3]=='-':
    #             two[1]=int(score[0:1])
    #             three[0]=int(score[1:3])
    #             three[1]=int(score[4:])

    # sc.append(one)
    # sc.append(two)
    # sc.append(three)
    # for s in sc:
    #     for i, e in enumerate(s):
    #         if s[i]>21:
    #             s[i]=21
    return [[5, 21], [21, 5], [21, 5]]

# print(handle_score('9-21, 21-17, 21-11'))
# print(handle_score('21-1721-1721-11'))
# print(handle_score('21-1021-5'))
# print(handle_score('21-141-2121-12'))
# print(handle_score('21-88-211-21'))
# print(handle_score('22-201-2121-1'))
# print(handle_score('21-1521-16'))
