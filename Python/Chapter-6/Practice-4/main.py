#두 배열의 원소 교체

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A) #오름차순
B = sorted(B, reverse = True) #내림차순

#A의 모든 원소 합이 최대가 될 수 있도록 B와 원소 교환
#단, K 번만 바꿀 수 있기 때문에 A의 원소 중 가장 작은 3개를 B와 교환해야 하며, 이때 B의 원소는 당연히 A보다 커야 한다.
#만약 A가 자신보다 더 작은 원소를 B에서 만난다면 더 이상 비교 연산할 필요가 없어진다.

for k in range(K):
    if A[k] > B[k]:
        break
    else:
        A[k] = B[k]

print(sum(A))



