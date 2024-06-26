통합 보고서
======

홈 화면 > ***통합 보고서***

와탭 모니터링 서비스 초기 화면에서 프로젝트를 선택하지 않고 기본 ***메뉴*** 하위에 ***통합 보고서***를 선택하세요. ***통합 보고서***는 여러 프로젝트에 대한 보고서를 간편하게 생성할 수 있습니다.

보고서 종류와 원하는 프로젝트를 선택하여 보고서를 생성할 수 있고, 보고서 생성 목록에서 작업 진행 상태를 확인할 수 있습니다. 보고서 생성 중 특정 프로젝트에서 에러가 발생한 경우 에러 내용을 확인할 수 있습니다. 작업이 완료된 보고서를 바로 조회하거나, 다운로드 및 인쇄 기능을 통해 다른 사람에게 보고서를 공유할 수 있습니다.

![](/img/integration_report_01.png)

***통합 보고서***의 기능은 다음과 같습니다.

* **멀티 프로젝트 지원**

***통합 보고서*** 메뉴에서 여러 프로젝트를 선택해 한 번에 보고서를 생성할 수 있어 편리합니다. 기존 ***보고서*** 메뉴는 프로젝트마다 보고서를 생성해야 했습니다.
* **업무 단위 보고서 생성**

***보고서 생성*** 메뉴에서 업무 단위로 프로젝트를 선택해 템플릿으로 저장할 수 있습니다. 보통 업무 단위로 프로젝트를 나누어 사용하는 마이크로 서비스 아키텍처(MSA, Micro Service Architecture) 환경에서 유용한 기능입니다.
* **대용량 데이터 최적화**

***통합 보고서*** 메뉴는 보고서 생성 시간이 획기적으로 줄어들었습니다. 그리고 일부 프로젝트 보고서 작성 과정에서 오류가 발생하더라도 보고서 결과를 조회  할 수 있습니다.
* **보고서 생성 중 동시 작업 가능**

***통합 보고서*** 메뉴에서 보고서를 생성하는 동시에 다른 업무를 보는 것이 가능합니다. 기존 ***보고서*** 메뉴는 생성 작업이 완료될 때까지 기다려야만 했습니다.

***통합 보고서*** 메뉴에서 보고서 생성을 시작한 후 다른 페이지로 이동할 수 있습니다. 또한 보고서 결과 목록에서 진행 상태와 완료된 보고서를 조회할 수 있습니다.
* **보고서 작업 공유**

동일 프로젝트 권한을 가진 사용자라면 누구든 생성한 보고서를 조회할 수 있습니다. 관련 보고서가 이미 생성됐는지 확인할 수 있어 중복으로 작성하지 않을 수 있습니다.

보고서와 통합 보고서의 차이[​](#보고서와-통합-보고서의-차이 "보고서와 통합 보고서의 차이에 대한 직접 링크")
----------------------------------------------------------------

***보고서***는 하나의 프로젝트에 대한 보고서를 생성하는 메뉴입니다. 따라서 프로젝트를 선택 후 좌측의 ***통계/보고서*** 메뉴를 통해 접근이 가능합니다.

***통합 보고서***는 여러 프로젝트에 대한 보고서를 생성하는 메뉴입니다. 프로젝트를 선택하지 않고 기본 메뉴에서 접근이 가능합니다. ***보고서***의 상세 내용은 [다음 문서](/java/report-intro)에서 확인할 수 있습니다.

보고서 생성 방법[​](#보고서-생성-방법 "보고서 생성 방법에 대한 직접 링크")
----------------------------------------------

1. **보고서 종류 선택**

![](/img/integration_report_02.png)

***보고서 종류*** 메뉴에서 원하는 보고서 유형을 선택하면 ***보고서 생성*** 버튼이 활성화됩니다. 보고서 이름 앞의 ***아이콘***은 보고서의 양식이 지원하는 프로젝트 플랫폼을 의미합니다.


	* ![플랫폼 애플리케이션 icon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yOS4zMzMzIDQuNjY2NjlDMjkuMzMzMyAzLjU2MjEyIDI4LjQzNzkgMi42NjY2OSAyNy4zMzMzIDIuNjY2NjlINC42NjY2N0MzLjU2MjEgMi42NjY2OSAyLjY2NjY3IDMuNTYyMTIgMi42NjY2NyA0LjY2NjY5VjI3LjMzMzRDMi42NjY2NyAyOC40Mzc5IDMuNTYyMSAyOS4zMzM0IDQuNjY2NjcgMjkuMzMzNEgyNy4zMzMzQzI4LjQzNzkgMjkuMzMzNCAyOS4zMzMzIDI4LjQzNzkgMjkuMzMzMyAyNy4zMzM0VjQuNjY2NjlaTTIxLjMzMzMgMTAuMzQzMkwxOS40NDc3IDEyLjIyODhMMjMuMjE5IDE2TDE5LjQ0NzcgMTkuNzcxM0wyMS4zMzMzIDIxLjY1NjlMMjUuMTA0NiAxNy44ODU2TDI2Ljk5MDIgMTZMMjUuMTA0NiAxNC4xMTQ0TDIxLjMzMzMgMTAuMzQzMlpNMTIuNTUyMyAxMi4yMjg4TDEwLjY2NjcgMTAuMzQzMkw2Ljg5NTQ0IDE0LjExNDRMNS4wMDk4MiAxNkw2Ljg5NTQ0IDE3Ljg4NTZMMTAuNjY2NyAyMS42NTY5TDEyLjU1MjMgMTkuNzcxM0w4Ljc4MTA1IDE2TDEyLjU1MjMgMTIuMjI4OFpNMTkuNTMzMSAxMC4xOTE0TDE3LjAyNzIgOS4yNzkzOEwxMi40NjY5IDIxLjgwODZMMTQuOTcyOCAyMi43MjA3TDE5LjUzMzEgMTAuMTkxNFoiIGZpbGw9IiMwMEIwRTIiLz4KPC9zdmc+Cg==) ***애플리케이션*** 프로젝트 플랫폼을 나타냅니다.
	* ![플랫폼 쿠버네티스 icon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xNC42NjY3IDBIMTcuMzMzM1Y0LjA3MzI0QzIwLjc0NDggNC40NTAzNiAyMy43MjUzIDYuMjU3NTUgMjUuNjYyIDguODgyMDZMMjkuMTg5NyA2Ljg0NTNMMzAuNTIzMSA5LjE1NDdMMjYuOTk3MyAxMS4xOTAzQzI3LjY0MjIgMTIuNjYyOCAyOCAxNC4yODk2IDI4IDE2QzI4IDE3LjcxMDQgMjcuNjQyMiAxOS4zMzcyIDI2Ljk5NzMgMjAuODA5N0wzMC41MjMxIDIyLjg0NTNMMjkuMTg5NyAyNS4xNTQ3TDI1LjY2MiAyMy4xMTc5QzIzLjcyNTMgMjUuNzQyNCAyMC43NDQ4IDI3LjU0OTYgMTcuMzMzMyAyNy45MjY4VjMySDE0LjY2NjdWMjcuOTI2OEMxMS4yNTUyIDI3LjU0OTYgOC4yNzQ3MyAyNS43NDI0IDYuMzM4MDMgMjMuMTE3OUwyLjgxMDI2IDI1LjE1NDdMMS40NzY5MyAyMi44NDUzTDUuMDAyNzQgMjAuODA5N0M0LjM1Nzg0IDE5LjMzNzIgNCAxNy43MTA0IDQgMTZDNCAxNC4yODk2IDQuMzU3ODQgMTIuNjYyOCA1LjAwMjc0IDExLjE5MDNMMS40NzY5MyA5LjE1NDdMMi44MTAyNiA2Ljg0NTNMNi4zMzgwMyA4Ljg4MjA2QzguMjc0NzMgNi4yNTc1NSAxMS4yNTUyIDQuNDUwMzYgMTQuNjY2NyA0LjA3MzI0VjBaTTI1LjMzMzMgMTZDMjUuMzMzMyAxNy4yMjQ1IDI1LjA5NzUgMTguMzkzOSAyNC42Njg4IDE5LjQ2NTRMMTkuOTMzMyAxNi43MzEzQzE5Ljk3NzEgMTYuNDk0MiAyMCAxNi4yNDk4IDIwIDE2QzIwIDE1Ljc1MDIgMTkuOTc3MSAxNS41MDU4IDE5LjkzMzMgMTUuMjY4N0wyNC42Njg4IDEyLjUzNDZDMjUuMDk3NSAxMy42MDYxIDI1LjMzMzMgMTQuNzc1NSAyNS4zMzMzIDE2Wk0xOC41OTk0IDEyLjk1OTZMMjMuMzMzNyAxMC4yMjYzQzIxLjg4NDcgOC4zODgzMSAxOS43NTk1IDcuMTA4MjIgMTcuMzMzMyA2Ljc2MTE5VjEyLjIyNzZDMTcuODAxNSAxMi4zOTMxIDE4LjIyOTYgMTIuNjQzMiAxOC41OTk0IDEyLjk1OTZaTTE0LjY2NjcgMTIuMjI3NlY2Ljc2MTE5QzEyLjI0MDUgNy4xMDgyMiAxMC4xMTUzIDguMzg4MzEgOC42NjYzMyAxMC4yMjYzTDEzLjQwMDYgMTIuOTU5NkMxMy43NzA0IDEyLjY0MzIgMTQuMTk4NSAxMi4zOTMxIDE0LjY2NjcgMTIuMjI3NlpNMTIuMDY2NyAxNS4yNjg3TDcuMzMxMTYgMTIuNTM0NkM2LjkwMjQ4IDEzLjYwNjEgNi42NjY2NyAxNC43NzU1IDYuNjY2NjcgMTZDNi42NjY2NyAxNy4yMjQ1IDYuOTAyNDggMTguMzkzOSA3LjMzMTE2IDE5LjQ2NTRMMTIuMDY2NyAxNi43MzEzQzEyLjAyMjkgMTYuNDk0MiAxMiAxNi4yNDk4IDEyIDE2QzEyIDE1Ljc1MDIgMTIuMDIyOSAxNS41MDU4IDEyLjA2NjcgMTUuMjY4N1pNMTMuNDAwNiAxOS4wNDA0QzEzLjc3MDQgMTkuMzU2OCAxNC4xOTg1IDE5LjYwNjkgMTQuNjY2NyAxOS43NzI0VjI1LjIzODhDMTIuMjQwNSAyNC44OTE4IDEwLjExNTMgMjMuNjExNyA4LjY2NjMzIDIxLjc3MzdMMTMuNDAwNiAxOS4wNDA0Wk0xNy4zMzMzIDE5Ljc3MjRDMTcuODAxNSAxOS42MDY5IDE4LjIyOTYgMTkuMzU2OCAxOC41OTk0IDE5LjA0MDRMMjMuMzMzNyAyMS43NzM3QzIxLjg4NDcgMjMuNjExNyAxOS43NTk1IDI0Ljg5MTggMTcuMzMzMyAyNS4yMzg4VjE5Ljc3MjRaIiBmaWxsPSIjNDQ4NUZGIi8+Cjwvc3ZnPgo=) ***쿠버네티스*** 프로젝트 플랫폼을 나타냅니다.
	* ![플랫폼 서버 icon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhlaWdodD0iMzAiIHZpZXdCb3g9IjAgMCAzMCAzMCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yNS41IDIuMTY2NjlWOS4xNjY2OUg0LjVWMi4xNjY2OUgyNS41Wk00LjUgMTEuNUgyNS41VjE4LjVINC41VjExLjVaTTQuNSAyMC44MzM0VjI3LjgzMzRIMjUuNVYyMC44MzM0SDQuNVpNNi44MzMzMyA0LjUwMDAySDkuMTY2NjdWNi44MzMzNUg2LjgzMzMzVjQuNTAwMDJaTTkuMTY2NjcgMTMuODMzNEg2LjgzMzMzVjE2LjE2NjdIOS4xNjY2N1YxMy44MzM0Wk02LjgzMzMzIDIzLjE2NjdIOS4xNjY2N1YyNS41SDYuODMzMzNWMjMuMTY2N1pNMjMuMTY2NyA0LjUwMDAySDEyLjY2NjdWNi44MzMzNUgyMy4xNjY3VjQuNTAwMDJaTTEyLjY2NjcgMTMuODMzNEgyMy4xNjY3VjE2LjE2NjdIMTIuNjY2N1YxMy44MzM0Wk0yMy4xNjY3IDIzLjE2NjdIMTIuNjY2N1YyNS41SDIzLjE2NjdWMjMuMTY2N1oiIGZpbGw9IiMwMEM1QjEiLz4KPC9zdmc+Cg==) ***서버*** 프로젝트 플랫폼을 나타냅니다.
2. **상세 설정**

![](/img/master_report.png)

보고서 종류 선택 후 ***보고서 생성*** 버튼을 클릭하세요. 다음과 같이 상세 설정을 할 수 있습니다.


	* **보고서 제목**
	
	같은 타입의 보고서가 여러 개인 경우 이름을 지정하면 보고서 결과를 구분하기 쉽습니다.
	* **시간**
	
	보고서에 사용될 데이터의 기간을 선택하세요. 기간은 보고서 타입(일, 주, 월)에 따라 달라집니다.
	* **프로젝트 선택**
	
	보고서를 작성할 프로젝트를 선택하세요. 그룹 및 개별 프로젝트 단위로 선택이 가능합니다.
	* **보고서 양식 저장과 불러오기**
	
	지금 입력된 보고서의 설정을 템플릿으로 저장하고 다음 생성 시 타입 목록에서 불러올 수 있습니다. 업무 단위로 프로젝트를 자주 사용하시는 분들에게 유용한 기능입니다.
3. **보고서 생성**

설정을 완료했다면 ***보고서 생성*** 버튼을 눌러 보고서를 생성하세요.

작업 목록 확인[​](#작업-목록-확인 "작업 목록 확인에 대한 직접 링크")
-------------------------------------------

![](/img/integration_report_03.png)

***보고서 생성 목록***에서 이전에 만들었던 보고서와 현재 작업 중인 보고서를 확인할 수 있습니다.

***전체*** 목록에  서는 내가 생성한 보고서 외에도 나와 같은 권한을 가진 사람이 생성한 보고서를 함께 볼 수 있습니다. ***내 보고서*** 목록에서는 내가 생성한 보고서만 필터링하여 볼 수 있습니다.

에러 없이 생성된 보고서는 ![체크 icon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xOC40NTI3IDZMOS41NzQ3NiAxNS4xMTFMNS41NDczMyAxMC43Nzc2TDQgMTIuMzA1MUw5LjU3NDc2IDE4TDIwIDcuNTI3NTRMMTguNDUyNyA2VjZaIiBmaWxsPSIjNDQ4NUZGIi8+Cjwvc3ZnPgo=) 체크 아이콘으로 표시되며, 에러가 포함된 경우는 ![경고 icon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMS4xMjYgMy40MTg0QzExLjUxOSAyLjc5OTI3IDEyLjQyMjcgMi43OTk3NyAxMi44MTUgMy40MTkzMkwyMi4yODcxIDE4LjM3NjFDMjIuNzA4OCAxOS4wNDE5IDIyLjIzMDQgMTkuOTExMSAyMS40NDIzIDE5LjkxMTFIMi40NzUxNkMxLjY4NjU2IDE5LjkxMTEgMS4yMDgyNiAxOS4wNDA5IDEuNjMwOTEgMTguMzc1MUwxMS4xMjYgMy40MTg0Wk00LjI5NDcxIDE3LjkxMTFMMTkuNjI1NiAxNy45MTExTDExLjk2OTQgNS44MjE3OUw0LjI5NDcxIDE3LjkxMTFaTTEwLjk5OTkgMTQuOTU0NUgxMi45OTk5VjE2Ljk1NDVIMTAuOTk5OVYxNC45NTQ1Wk0xMi45OTk5IDguOTU0NTRIMTAuOTk5OVYxMy45NTQ1SDEyLjk5OTlWOC45NTQ1NFoiIGZpbGw9IiNGRjk5MDAiLz4KPC9zdmc+Cg==) 경고 아이콘이 함께 표시됩니다. ![경고 icon](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMS4xMjYgMy40MTg0QzExLjUxOSAyLjc5OTI3IDEyLjQyMjcgMi43OTk3NyAxMi44MTUgMy40MTkzMkwyMi4yODcxIDE4LjM3NjFDMjIuNzA4OCAxOS4wNDE5IDIyLjIzMDQgMTkuOTExMSAyMS40NDIzIDE5LjkxMTFIMi40NzUxNkMxLjY4NjU2IDE5LjkxMTEgMS4yMDgyNiAxOS4wNDA5IDEuNjMwOTEgMTguMzc1MUwxMS4xMjYgMy40MTg0Wk00LjI5NDcxIDE3LjkxMTFMMTkuNjI1NiAxNy45MTExTDExLjk2OTQgNS44MjE3OUw0LjI5NDcxIDE3LjkxMTFaTTEwLjk5OTkgMTQuOTU0NUgxMi45OTk5VjE2Ljk1NDVIMTAuOTk5OVYxNC45NTQ1Wk0xMi45OTk5IDguOTU0NTRIMTAuOTk5OVYxMy45NTQ1SDEyLjk5OTlWOC45NTQ1NFoiIGZpbGw9IiNGRjk5MDAiLz4KPC9zdmc+Cg==) 경고 아이콘을 클릭하시면 어떤 프로젝트에서 에러가 발생했는지 확인할 수 있습니다.

조회 및 공유[​](#조회-및-공유 "조회 및 공유에 대한 직접 링크")
----------------------------------------

![](/img/integration_report_04.png)

보고서는 3가지 방식으로 제공됩니다.

* **화면 조회**

작업 목록에서 생성한 보고서를 선택하면 화면에서 바로 조회하여 볼 수 있습니다.
* **다운로드**

***다운로드*** 버튼을 클릭하면 바로 보기의 보고서와 같은 파일이 html 형식으로 다운로드 됩니다. 모니터링 관리 권한이 없는 사람에게 보고서를 공유할 수 있습니다.
* **인쇄 및 PDF 저장**

***인쇄*** 버튼을 누르면 컴퓨터에 연결된 프린터로 인쇄하거나 또는 PDF 형식으로 저장할 수 있습니다.
