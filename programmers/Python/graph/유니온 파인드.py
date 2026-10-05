# ============================================================
# 문제
# ------------------------------------------------------------
# 1번부터 N번까지 N개의 원소가 있다.
# 처음에는 모든 원소가 각각 별도의 그룹에 속한다.
#
# M개의 연산을 순서대로 처리하시오.
#   0 a b : a와 b가 속한 그룹을 합친다.
#   1 a b : a와 b가 같은 그룹인지 확인한다.
#
# 같은 그룹이면 YES, 다른 그룹이면 NO를 출력한다.

# 입력
# 첫째 줄: 원소 개수 N, 연산 개수 M
# 이후 M개의 줄:
#   연산 종류, 원소 a, 원소 b

# 예제 입력
# 5 7
# 0 1 2
# 1 1 2
# 1 1 3
# 0 2 3
# 0 4 5
# 1 1 3
# 1 3 5

# 예제 출력
# YES
# NO
# YES
# NO
#
# ============================================================

N, M = map(int, input().split())

# parent[x]: x의 부모 원소
# 처음에는 자기 자신이 부모이자 그룹의 대표
parent = list(range(N + 1))

# size[root]: root가 대표인 그룹의 원소 개수
size = [1] * (N + 1)


def find(x):
    # 자기 자신이 부모라면 그룹의 대표
    if parent[x] == x:
        return x

    # 대표를 찾고, x의 부모를 대표로 바꾼다.
    # 이 과정을 '경로 압축'이라고 한다.
    parent[x] = find(parent[x])

    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)

    # 이미 같은 그룹이면 합칠 필요가 없다.
    if root_a == root_b:
        return

    # 작은 그룹을 큰 그룹에 붙인다.
    # root_a가 더 큰 그룹의 대표가 되도록 조정
    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    # root_b를 root_a 아래에 연결
    parent[root_b] = root_a

    # 합쳐진 그룹의 크기 갱신
    size[root_a] += size[root_b]


for _ in range(M):
    command, a, b = map(int, input().split())

    if command == 0:
        union(a, b)

    elif command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")