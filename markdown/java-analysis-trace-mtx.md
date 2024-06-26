멀티 트랜잭션 추적
==========

**멀티 트랜잭션**은 다른 에이전트나 프로젝트와 연관된 트랜잭션을 의미합니다. 와탭 프로젝트에 등록된 애플리케이션 서비스 간의 호출을 추적하는 것이 **멀티 트랜잭션 추적**입니다.

정보Java 에이전트는 세 개의 HTTP 헤더 키값(`x-wtap-po`, `x-wtap-mst`, `x-wtap-sp1`)으로 멀티 트랜잭션을 추적합니다. 게이트웨이를 통과하는 HTTP 트랜잭션이 연계 추적이 안 된다면 HTTP 헤더 조건을 확인하세요.

노트**멀티 트랜잭션 활성화**

멀티 트랜잭션을 추적하려면 관리 > 에이전트 설정 메뉴에서 `mtrace_enabled` 옵션을 `true`로 설정하세요. 에이전트 설정에 대한 자세한 내용은 [다음 문서](/java/set-agent#set-agent-service)를 참조하세요.

멀티 트랜잭션 ID 확인하기[​](#멀티-트랜잭션-id-확인하기 "멀티 트랜잭션 ID 확인하기에 대한 직접 링크")
----------------------------------------------------------------

멀티 트랜잭션 추적 메뉴를 이용하려면 **MTID**(Multi Transaction ID)가 필요합니다. 다음 과정을 통해 **MTID** 값을 확인할 수 있습니다.

1. 분석 > 히트맵 메뉴에서 차트 영역을 드래그하세요.
2. 드래그한 차트 영역의 트랜잭션 정보가 다음과 같이 하단 TX 트레이스 목록에 나타납니다.

![mtrace_M](/img/tx-trace-table.png)
3. ![아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHZpZXdCb3g9IjAgMCAyMCAyMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTAiIGN5PSIxMCIgcj0iOSIgZmlsbD0iIzQ0ODVGRiIvPgo8cGF0aCBkPSJNOC4xMDU0NyA2LjE3OTY5TDEwLjExNDMgMTEuODUxNkwxMi4xMTIzIDYuMTc5NjlIMTQuMjI4NVYxNEgxMi42MTE4VjExLjg2MjNMMTIuNzcyOSA4LjE3MjM2TDEwLjY2MjEgMTRIOS41NTU2Nkw3LjQ1MDIgOC4xNzc3M0w3LjYxMTMzIDExLjg2MjNWMTRINlY2LjE3OTY5SDguMTA1NDdaIiBmaWxsPSJ3aGl0ZSIvPgo8cGF0aCBkPSJNOC4xMDU0NyA2LjE3OTY5TDEwLjExNDMgMTEuODUxNkwxMi4xMTIzIDYuMTc5NjlIMTQuMjI4NVYxNEgxMi42MTE4VjExLjg2MjNMMTIuNzcyOSA4LjE3MjM2TDEwLjY2MjEgMTRIOS41NTU2Nkw3LjQ1MDIgOC4xNzc3M0w3LjYxMTMzIDExLjg2MjNWMTRINlY2LjE3OTY5SDguMTA1NDdaIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K) 아이콘이 표시된 트레이스를 선택하면 트랜잭션 정보 창이 나타납니다.
4. 레코드 요약 탭에서 멀티 트랜잭션 ID 값을 확인할 수 있습니다.

![레코드 요약](/img/tx-trace-dt-up.png)

노트* 트랜잭션에서 외부 호출을 하는 경우에도 동일한 멀티 트랜잭션 ID가 생성됩니다. 서비스별로 프로젝트가 분리되어 있더라도 처음 발급한 멀티 트랜잭션 ID를 통해 애플리케이션 간의 모든 트랜잭션을 확인할 수 있습니다. 트랜잭션 정보 창을 활용한 트랜잭션 트레이스 상세 분석에 관한 자세한 내용은 [다음 문서](/java/trs-profile#transaction-info)를 참조하세요.
* 트랜잭션 정보 창에서 멀티 트랜잭션 ID를 선택하면 멀티 트랜잭션 탭으로 이동합니다.   시스템 내 또는 시스템 간에 발생하는 다양한 호출 관계를 한 눈에 파악하고 어느 부분에서 문제가 발생했는지 식별하여 개선할 수 있도록 트랜잭션과 트레이스 정보를 제공합니다.
멀티 트랜잭션 추적 기능 이용하기[​](#멀티-트랜잭션-추적-기능-이용하기 "멀티 트랜잭션 추적 기능 이용하기에 대한 직접 링크")
-------------------------------------------------------------------------

1. 분석 > 멀티 트랜잭션 추적 메뉴로 이동하세요.
2. 트랜잭션 정보 창에서 확인한 **MTID** 값을 MTID / CUSTID 조회 항목에 입력하세요.

![MTID](/img/trace-mtx-mtid.png)
3. 조회할 날짜와 프로젝트를 선택하세요.
4. 화면 아래에 적용 버튼을 선택하세요.

오른쪽 차트 탭에 각 트랜잭션의 호출 관계를 파악할 수 있는 다이어그램이 표시됩니다.

![멀티 트랜잭션 추적](/img/trace-mtx-mtid-chart.png)

### 차트

차트는 각 트랜잭션의 호출 관계를 빠르고 명확하게 사용자에게 제공합니다. 동일한 멀티 트랜잭션 ID를 갖는 트랜잭션 서비스들의 개별 수행 시간을 확인할 수 있습니다. 트랜잭션 노드의 배경색으로 표현되어 있는 소요 시간(![number 1](/img/number-01.png) 타임바)를 통해 트랜잭션 간 호출 관계를 확인할 수 있습니다. 차트에서는 마우스를 이용해 원하는 위치로 이동하거나 스크롤을 통해서 확대, 축소할 수 있습니다.

![Chart](/assets/images/trace-mtx-chart-timebar-5aa9bc221958b2d236a1d1a071dc639a.png)

트랜잭션 노드를 선택하면 트랜잭션 정보 창이 추가로 나타납니다. 트랜잭션 트레이스를 통해 해당 트랜잭션의 상세 내역을 확인할 수 있습니다. 트랜잭션 정보 창을 활용한 트랜잭션 트레이스 상세 분석에 관한 자세한 내용은 [다음 문서](/java/trs-profile#transaction-info)를 참조하세요

* ***A***작음 / ***A***큼: 노드에 표시된 폰트 크기를 조절할 수 있습니다.
* 타임바: 각 노드에 소요 시간(타임바)을 표시하거나 숨길 수 있습니다.
* 애플리케이션명: 각 노드에 에이전트 이름(oname)을 표시하거나 숨길 수 있습니다.
* 프로젝트: 각 노드에 프로젝트 이름을 표시하거나 숨길 수 있습니다.
* 데이터베이스 / 외부 호출 / 내부 호출: 해당 트랜잭션에서 발생한 다른 데이터베이스 커넥션 요청이나 HTTP Call의 정보 또한 차트의 노드로 확인할 수 있습니다.

### 테이블[​](#-1 "-1에 대한 직접 링크")

테이블 탭에서는 멀티 트랜잭션 내에 포함된 각 트랜잭션 별 정보를 테이블 형식으로 확인할 수 있습니다.

![테이블](/img/trace-mtx-table.png)

각 트랜잭션 항목을 선택하면 차트 탭의 노드 선택과 마찬가지로 선택한 트랜잭션에 대한 트랜잭션 정보 창이 나타납니다. 트랜잭션 트레이스를 통해 해당 트랜잭션의 상세 내역을 확인할 수 있습니다. 트랜잭션 정보 창을 활용한 트랜잭션 트레이스 상세 분석에 관한 자세한 내용은 [다음 문서](/java/trs-profile#transaction-info)를 참조하세요.

![컬럼 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yIDRWMjBIMjJWNEgyWk0xNCA2VjE4SDEwVjZIMTRaTTQgNkg4VjE4SDRWNlpNMjAgMThIMTZWNkgyMFYxOFoiIGZpbGw9IiM3NTc1NzUiLz4KPC9zdmc+Cg==) 컬럼 설정: 테이블 내 컬럼을 편집할 수 있습니다.

### 트리[​](#-2 "-2에 대한 직접 링크")

트리 탭에서는 각 트랜잭션과 그에 속해 있는 트레이스의 세부 정보를 확인할 수 있습니다. 전체 트랜잭션 소요 시간 내의 각 하위 트랜잭션이나 트레이스의 시작 및 소요 시간을 시각화해 트랜잭션 호출 관계를 트리 형식으로 제공합니다.

![Tree](/img/trace-mtx-tree.png)

* ![한 줄 보기 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE2IDNIMlY3SDRWNUg4VjE5SDVWMjFIMTNWMTlIMTBWNUgxNFY3SDE2VjNaIiBmaWxsPSIjNzU3NTc1Ii8+CjxwYXRoIGQ9Ik0xMy4yNSAxMy41QzEzLjk0MDQgMTMuNSAxNC41IDEyLjk0MDQgMTQuNSAxMi4yNUMxNC41IDExLjU1OTYgMTMuOTQwNCAxMSAxMy4yNSAxMUMxMi41NTk2IDExIDEyIDExLjU1OTYgMTIgMTIuMjVDMTIgMTIuOTQwNCAxMi41NTk2IDEzLjUgMTMuMjUgMTMuNVoiIGZpbGw9IiM3NTc1NzUiLz4KPHBhdGggZD0iTTE3LjI1IDEzLjVDMTcuOTQwNCAxMy41IDE4LjUgMTIuOTQwNCAxOC41IDEyLjI1QzE4LjUgMTEuNTU5NiAxNy45NDA0IDExIDE3LjI1IDExQzE2LjU1OTYgMTEgMTYgMTEuNTU5NiAxNiAxMi4yNUMxNiAxMi45NDA0IDE2LjU1OTYgMTMuNSAxNy4yNSAxMy41WiIgZmlsbD0iIzc1NzU3NSIvPgo8cGF0aCBkPSJNMjIuNSAxMi4yNUMyMi41IDEyLjk0MDQgMjEuOTQwNCAxMy41IDIxLjI1IDEzLjVDMjAuNTU5NiAxMy41IDIwIDEyLjk0MDQgMjAgMTIuMjVDMjAgMTEuNTU5NiAyMC41NTk2IDExIDIxLjI1IDExQzIxLjk0MDQgMTEgMjIuNSAxMS41NTk2IDIyLjUgMTIuMjVaIiBmaWxsPSIjNzU3NTc1Ii8+Cjwvc3ZnPgo=) 한 줄 보기: 각 구간 별 수행 정보에 표시된 텍스트를 한 줄로 표시해 트리 형식을 간격하게 정리할 수 있습니다.
* ![여러 줄 보기 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE2IDNIMlY3SDRWNUg4VjE5SDVWMjFIMTNWMTlIMTBWNUgxNFY3SDE2VjNaIiBmaWxsPSIjNzU3NTc1Ii8+CjxwYXRoIGQ9Ik0yMCAxMEgxMlYxMkgyMFYxMFoiIGZpbGw9IiM3NTc1NzUiLz4KPHBhdGggZD0iTTIwIDE2VjE0SDEyVjE2SDIwWiIgZmlsbD0iIzc1NzU3NSIvPgo8L3N2Zz4K) 여러 줄 보기: 각 구간 별 수행 정보에 표시된 텍스트를 줄바꿈해 모두 표시합니다.
* 최장 경로: 가장 긴 경로로 이동할 수 있습니다.
* ![차트 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIHZpZXdCb3g9IjAgMCA0OCA0OCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDRWMTFINDRWNEg0Wk00IDIyVjE1TDMzIDE1VjIyTDQgMjJaTTQgMjZWMzNIMjNWMjZMNCAyNlpNNCAzN1Y0NEgxMlYzN0g0WiIgZmlsbD0iIzc1NzU3NSIvPgo8L3N2Zz4K) 시간바 표시: 경과 시간을 막대 형식의 차트로 표시합니다.
* ![시간 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yIDEyQzIgNi40OCA2LjQ3IDIgMTEuOTkgMkMxNy41MiAyIDIyIDYuNDggMjIgMTJDMjIgMTcuNTIgMTcuNTIgMjIgMTEuOTkgMjJDNi40NyAyMiAyIDE3LjUyIDIgMTJaTTEyIDRDNy41OCA0IDQgNy41OCA0IDEyQzQgMTYuNDIgNy41OCAyMCAxMiAyMEMxNi40MiAyMCAyMCAxNi40MiAyMCAxMkMyMCA3LjU4IDE2LjQyIDQgMTIgNFpNMTEgN0gxMi44NTgxVjEyLjA3MjlMMTcgMTQuNTMxOEwxNi4wNzA5IDE2TDExIDEyLjk2ODJWN1oiIGZpbGw9IiM3NTc1NzUiLz4KPC9zdmc+Cg==) 시간 표시: 각 구간별 타임 스탬프, 갭, 경과 시간을 텍스트 형식으로 표시합니다.


	+ 8초 이상: 초과 지연 상태로 빨간색으로 표현합니다.
	+ 3초 이상 8초 미만: 지연 상태로 주황색으로 표현합니다.
	+ 3초 미만: 정상 상태로 파란색으로 표현합니다.노트시작 및 소요 시간의 경우 트랜잭션 호출 환경에 따라 발생하는 시차를 상위 트랜잭션 내 트레이스와 매핑을 통해 보정하여 표현하기 때문에 실제 수집된 시간 데이터와 차이가 발생할 수 있습니다.
* ![감추기 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xNC44NzYxIDQuMzY4OUMxMy45OSA0LjExOTY2IDEzLjAzMTggMy45ODY5OSAxMiAzLjk4Njk5QzcgMy45ODY5OSAzLjczIDcuMTAyMzkgMiAxMS41QzIuNTQwMDQgMTIuODcyOCAzLjIzMDEzIDE0LjEyMDYgNC4wNzYwNyAxNS4xODc3TDcuMDQ5NzYgMTIuMjA4OEM3LjAxNjk2IDExLjk3NzMgNyAxMS43NDA2IDcgMTEuNUM3IDguNzM1MjEgOS4yNCA2LjQ5MTMzIDEyIDYuNDkxMzNDMTIuMjQwMiA2LjQ5MTMzIDEyLjQ3NjQgNi41MDgzMiAxMi43MDc2IDYuNTQxMTdMMTQuODc2MSA0LjM2ODlaTTE4LjU0NDggNi4zNjA1NkwxNi4xNzExIDguNzM4M0MxNi42OTQ5IDkuNTMwMTcgMTcgMTAuNDc5NiAxNyAxMS41QzE3IDE0LjI2NDggMTQuNzYgMTYuNTA4NyAxMiAxNi41MDg3QzEwLjk4MTQgMTYuNTA4NyAxMC4wMzM2IDE2LjIwMyA5LjI0MzA4IDE1LjY3ODRMNy4xMTcyOCAxNy44MDc5QzguNTEwNzQgMTguNTc5NiAxMC4xMzUgMTkuMDEzIDEyIDE5LjAxM0MxNyAxOS4wMTMgMjAuMjcgMTUuODk3NiAyMiAxMS41QzIxLjE5MTMgOS40NDQyMiAyMC4wNDYgNy42Njg2NCAxOC41NDQ4IDYuMzYwNTZaTTEwLjcwNTggMTQuMjEzMUMxMS4wOTc0IDE0LjQwMDQgMTEuNTM2MiAxNC41MDUyIDEyIDE0LjUwNTJDMTMuNjYgMTQuNTA1MiAxNSAxMy4xNjI5IDE1IDExLjVDMTUgMTEuMDM1NCAxNC44OTU0IDEwLjU5NTggMTQuNzA4NCAxMC4yMDM1TDEwLjcwNTggMTQuMjEzMVpNOS45NDk1MiA5LjMwNDAzQzkuOTAwNzQgOS4zNDk3NSA5Ljg1MzQ4IDkuMzk3MDkgOS44MDc4NCA5LjQ0NTk3TDkuOTQ5NTIgOS4zMDQwM1pNMTkuMDcxMSAzTDIwLjQ4NTMgNC40MTY2N0w0LjkyODkzIDIwTDMuNTE0NzIgMTguNTgzM0wxOS4wNzExIDNaIiBmaWxsPSIjNzU3NTc1Ii8+Cjwvc3ZnPgo=) 시간 숨기기: 시간 정보를 숨깁니다.

노트해당 트레이스의 ![통계 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yIDJWMjJINEgyMlYyMEg0VjJIMlpNMTYgMTcuOTk5OEgxNFYyLjk5OThIMTZWMTcuOTk5OFpNMTggMTcuOTk5OEgyMFY2Ljk5OThIMThWMTcuOTk5OFpNMTAgMTcuOTk5OEgxMlY4Ljk5OThIMTBWMTcuOTk5OFpNOCAxNy45OTk4SDZWMTIuOTk5OEg4VjE3Ljk5OThaIiBmaWxsPSIjNzU3NTc1Ii8+Cjwvc3ZnPgo=) 버튼 또는 ![팝업 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yMiAyVjE3SDdWMkgyMlpNMjAgNEg5VjZIMjBWNFpNMjAgOFYxNUg5VjhIMjBaTTIgOVYyMkgxNUgxN1YyMFYxOEgxNVYyMEg0VjlINlY3SDRIMlY5WiIgZmlsbD0iIzc1NzU3NSIvPgo8L3N2Zz4K) 버튼을 선택하면 HTTP 호출 통계, 액티브 스택 등의 요약 창을 확인할 수 있습니다.

팁SQL 변수와 HTTP 쿼리를 조회하려면 다음 옵션을 에이전트 설정에 추가하세요.

* SQL 파라미터 정보 기록과 관련한 에이전트 설정은 [다음 문서](/java/agent-dbsql#profile-sql-param)를 참조하세요.
* HTTP 파라미터 정보 기록과 관련한 에이전트 설정은 [다음 문서](/java/agent-transaction#profile_http_parameter)를 참조하세요.

whatap.conf
```
# SQL 파라미터 조회 옵션: 옵션이 적용되면 SQL 파라미터를 암호화하여 수집합니다.  
profile_sql_param_enabled=true   
  
# HTTP 파라미터 조회 옵션: 옵션이 적용되면 HTTP 쿼리 파라미터를 암호화하여 수집합니다.  
profile_http_parameter_enabled=true   

```
