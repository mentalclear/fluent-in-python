def eval_scores(a_list):
    a_list.remove(max(a_list))
    a_list.remove(min(a_list))
    return sum(a_list) / len(a_list)

the_scores = [8.5, 6.0, 8.5, 8.7, 9.9, 9.0]

print(eval_scores(the_scores))
