if __name__ == '__main__':
    
    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]
    
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
   
    
# alternative
"""
    l = []
    second_lowest_names = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name, score])
        scores.add(score)
            
    second_lowest = sorted(scores)[1]

    for name, score in l:
        if score == second_lowest:
            second_lowest_names.append(name)

    for name in sorted(second_lowest_names):
        print(name, end='\n')

"""