#2309 도넛과 막대 그래프

from collections import defaultdict

def search(i, graph, visited):
    now = i
    while True:
        visited.add(now) # 방문한 노드는 set에 추가
        if len(graph[now]) == 1:
            if graph[now][0] not in visited:
                now = graph[now][0] # 다음 노드로 이동
            else:
                return 1 # 사이클이 만들어지면 도넛 그래프
        elif len(graph[now]) == 0: 
            return 2 # 다음 노드가 없다면 막대 그래프
        else:
            return 3 # 나가는 노드가 2개면 8자 그래프

def solution(edges):
    answer = [0]*4
    graph_in = defaultdict(list) # 나가는 노드 저장하는 그래프
    graph_out = defaultdict(list) # 들어오는 노드 저장하는 그래프
    
    for a, b in edges:
        graph_out[a].append(b)
        graph_in[b].append(a)

    # 생성한 정점은 나가는 화살표가 2개 이상이도 들어오는 화살표는 없는 정점
    for key in graph_out.keys():
        if len(graph_out[key])>1 and len(graph_in[key]) == 0:
            answer[0] = key # 새로운 정점 저장
            break
    
    visited = set() # 방문한 노드를 저장하는 set
    # 새로운 정점과 연결된 노드들을 탐색
    for i in graph_out[answer[0]]: 
        idx = search(i, graph_out, visited)
        answer[idx] += 1
    
    return answer
