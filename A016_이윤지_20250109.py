#사람들을 몸무게 제한 내에서 한 번에 최대 2명씩 구명보트에 태운다고 할 때,  필요한 보트의 최소 개수구하기

'''
1. 사람들의 몸무게 배열을 오름차순 정렬
2. 가장 가벼운 사람과 가장 무거운 사람의 합이 무게 제한보다 작거나 같으면 두 사람을 태움
3. 그렇지 않으면 무거운 사람만 태움
4. 포인터를 이동하며 반복
'''

def solution(people, limit):
    # 사람들의 몸무게를 정렬
    people.sort()
    left = 0  # 가장 가벼운 사람의 인덱스
    right = len(people) - 1  # 가장 무거운 사람의 인덱스
    boats = 0  # 필요한 보트 개수
    
    while left <= right:
        # 가장 가벼운 사람과 가장 무거운 사람의 무게 합이 제한을 넘지 않으면 둘 다 태움
        if people[left] + people[right] <= limit:
            left += 1
        # 가장 무거운 사람만 태움
        right -= 1
        # 보트를 하나 추가
        boats += 1
    
    return boats
