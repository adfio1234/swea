#dfs&백트레킹 통해푼다.

T=int(input())
for t in range(T):
    result=[0]
    #data[0]에서는 숫자 data[1]에는 시행횟수가 들어간다
    data=input().split()

    #중복부분 제어를 위한 딕셔너리
    visited=dict()

    #list로 변환
    arr=list(data[0])
    change=int(data[1])

    #dfs구현부분
    def dfs(arr, change):
        #list를 join해서 문자열로 만들어준다.
        key=("".join(arr),change)

        #이미 탐색한 key인지 확인
        if key in visited:
            return
        #중복을 막기위해 이미 시행했다는 의미로 True
        #ex)111이면 111 111 111으로 3번실행을 막고 1번실행하기위함
        visited[key]=True

        #교환횟수가0이면 종료(주어진횟수만큼 교환이 끝났으므로 change횟수가 0인것들중에서 최댓값을구한다)
        if change==0:
            result[0]=max(result[0],int(''.join(arr)))
            return

        #[0,0],[0,1],[0,2]...번째 요소끼리 순서를 바꾸는 for문
        #123에서 실행하면
        #change가 1회 감소된채로
        #213 321 132에 대해서 dfs가 실행된다.
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):#i==j인 경우를 제외해 반드시 다른자리의요소끼리만 교환
                arr[i],arr[j]=arr[j],arr[i] #자리변경 수행
                dfs(arr,change-1) #change횟수를 줄여서 dfs다시 실행
                arr[i],arr[j]=arr[j],arr[i] #다음번 j를 위해 교환을 원상복구시킨다.
    dfs(arr,change)
    print("#{} {}".format(t+1,result[0]))
#