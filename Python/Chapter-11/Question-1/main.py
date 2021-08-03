'''
모험가 길드
- N 명의 모험가
- 공포도: 모험가들을 대상으로 측정
- 공포도 X인 모험가는 반드시 X명 이상 구성된 모험가 그룹에 참여해야 여행 가능

입력
- N 명의 모험가에 대한 공포도 정보

출력
- N 명의 모험가들로 여행 가능한 최대 모험가 그룹 수
'''

N = int(input())
explorers = list(map(int, input().split()))
explorers.sort()

group_members_count = 0
result_count = 0

for explorer in explorers:
    group_members_count += 1

    # 새 모험가 그룹 형성 가능 조건일 경우
    if group_members_count == explorer:
        result_count += 1
        group_members_count = 0

print(result_count)