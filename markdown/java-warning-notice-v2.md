이벤트 설정
======

홈 화면 > 프로젝트 선택 > ![아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik03LjkwNzM0IDJIMlYyMS42OTExSDcuOTA3MzRIOS44NzY0NUgxMS44NDU2VjE5LjcyMkg5Ljg3NjQ1VjkuODc2NDVIMTkuNzIyVjEyLjgzMDFIMjEuNjkxMVY5Ljg3NjQ1VjcuOTA3MzRWMkg5Ljg3NjQ1SDcuOTA3MzRaTTcuOTA3MzQgMy45NjkxMUgzLjk2OTExVjE5LjcyMkg3LjkwNzM0VjMuOTY5MTFaTTkuODc2NDUgMy45NjkxMVY3LjkwNzM0SDE5LjcyMlYzLjk2OTExSDkuODc2NDVaTTE5LjgyMzcgMTguNDMxM0MyMC43MTU3IDE2LjkyMTEgMjAuNTEyOCAxNC45NDMzIDE5LjIxNTMgMTMuNjQ1OEMxNy42NzczIDEyLjEwNzggMTUuMTgzNyAxMi4xMDc4IDEzLjY0NTggMTMuNjQ1OEMxMi4xMDc4IDE1LjE4MzcgMTIuMTA3OCAxNy42NzczIDEzLjY0NTggMTkuMjE1M0MxNC45NDMzIDIwLjUxMjggMTYuOTIxMSAyMC43MTU3IDE4LjQzMTMgMTkuODIzN0wyMC42MDc2IDIyTDIyIDIwLjYwNzZMMTkuODIzNyAxOC40MzEzWk0xNS4wMzgxIDE3LjgyMjlDMTUuODA3MSAxOC41OTE5IDE3LjA1MzkgMTguNTkxOSAxNy44MjI5IDE3LjgyMjlDMTguNTkxOSAxNy4wNTM5IDE4LjU5MTkgMTUuODA3MSAxNy44MjI5IDE1LjAzODFDMTcuMDUzOSAxNC4yNjkxIDE1LjgwNzEgMTQuMjY5MSAxNS4wMzgxIDE1LjAzODFDMTQuMjY5MSAxNS44MDcxIDE0LjI2OTEgMTcuMDUzOSAxNS4wMzgxIDE3LjgyMjlaIiBmaWxsPSIjNzU3NTc1Ii8+Cjwvc3ZnPgo=) 사이트맵 > 경고 알림 > 이벤트 설정 `New`

새로운 이벤트 설정 메뉴는 카테고리(**Category**)가 아닌 필드(**Field**) 중심의 사용자 경험을 강화한 메뉴입니다. 메트릭스 이벤트 설정과 같은 강력한 기능을 모두 필요치 않거나 단순한 알림 조건을 반복해서 사용하는 사용자에게 빠르게 경고 알림을 적용할 수 있는 이벤트 기능입니다. 생성한 프로젝트의 상품에 적합한 기본 이벤트 템플릿을 제공하여 빠르고 쉽게 원하는 경고 알림 이벤트를 설정할 수 있습니다.

카테고리가 아니라 필드를 먼저 선택해 사용자가 인지하는 지표와 이벤트 설정의 불일치를 해소합니다. 시뮬레이션이 주는 시각적 직관성을 결합하여 빠르고 정확하게 이벤트설정을 완료할 수 있습니다.

노트* 신규 프로젝트는 별도의 설정없이 이 기능을 이용할 수 있으나 이미 생성된 프로젝트에서는 이벤트 템플릿 생성 버튼을 선택하세요. 새로운 기능에 최적화된 이벤트 목록을 자동으로 생성합니다.
* 상품에 따라 제공하는 이벤트 템플릿은 다를 수 있습니다.
* 이 기능은 알림 설정 권한이 있는 멤버만 이용할 수 있습니다. 멤버 권한에 대한 자세한 설명은 [다음 문서](/project/project-structure#project-auth)를 참조하세요.
기본 이벤트 템플릿[​](#basic-template "기본 이벤트 템플릿에 대한 직접 링크")
-----------------------------------------------------

생성한 프로젝트의 상품에 따라 기본 이벤트 템플릿을 제공합니다. 이벤트 목록의 가장 왼쪽에 활성화 버튼을 선택해 원하는 이벤트를 활성화할 수 있습니다.

![이벤트 목록](/img/event-config-v2-apm.png)

제공하는 이벤트 템플릿은 다음과 같습니다. 지표 항목에 설정된 기본값은 사용자가 원하는 값으로 수정할 수 있습니다.

* ***Active Transaction***

카테고리: [`app_counter`](/java/metrics-app#app_counter)

액티브 트랜잭션 발생 건수(`active_tx_count`)가 100개를 초과한 상태하면 경고(Warning) 수준의 알림을 보냅니다.
* ***Server CPU***

카테고리: [`app_host_resource`](/java/metrics-app#app_host_resource)

호스트의 CPU 사용률(`cpu`)이 70%를 초과하면 경고(Warning) 수준의 알림을, 90%를 초과하면 위험(Critical) 수준의 알림을 보냅니다.
* ***Server Disk***

카테고리: [`app_host_resource`](/java/metrics-app#app_host_resource)

호스트의 디스크 사용률(`disk`)이 70%를 초과하면 경고(Warning) 수준의 알림을, 90%를 초과하면 위험(Critical) 수준의 알림을 보냅니다.
* ***Server Memory***

카테고리: [`app_host_resource`](/java/metrics-app#app_host_resource)

호스트의 메모리 사용률(`mem`)이 70%를 초과하면 경고(Warning) 수준의 알림을, 90%를 초과하면 위험(Critical) 수준의 알림을 보냅니다.
* ***Transaction Error Count***

카테고리: [`app_counter`](/java/metrics-app#app_counter)

트랜잭션 에러 건수(`tx_error`)가 10개를 초과하면 경고(Warning) 수준의 알림을 보냅니다.
* ***Transaction Response Time***

카테고리: [`app_counter`](/java/metrics-app#app_counter)

트랜잭션의 평균 응답 시간(`resp_time`)이 10회 연속, 2,000ms(2초)를 초과한 상태로 지속되면 경고(Warning) 수준의 알림을 보냅니다.

노트기본 이벤트 템플릿에 적용된 필드에 대한 자세한 내용은 [다음 문서](/java/metrics-app)를 참조하세요.

이벤트 수정하기[​](#modify-event "이벤트 수정하기에 대한 직접 링크")
-----------------------------------------------

기본 이벤트 템플릿에 적용된 지표값을 수정해 경고 알림이 발생 기준을 변경할 수 있습니다. 그 외에도 다양한 옵션 설정을 통해 알림 발생 기준을 변경할 수 있습니다. 수정하려는 이벤트 항목에서 ![수정 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZWRpdDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02OC4wMDAwMDAsIC0xMzk1LjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iZWRpdG9yLWljb25zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MC4wMDAwMDAsIDEzNTAuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8ZyBpZD0iaWMtZWRpdCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjguMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIwLDE4IEwyMCwyMCBMMCwyMCBMMCwxOCBMMjAsMTggWiBNMTIuOTM5MzM5OCwxIEwxNy45MzMyMTA4LDYuMDA2NDA3NzggTDE3LjkwMSw2LjAzOCBMMTcuOTAzNzA4NSw2LjA0IEw4LjAwNDIxMzU2LDE1LjkzOTQ5NDkgTDgsMTUuOTM1IEw4LDE1Ljk0IEwzLDE1Ljk0IEwzLDEwLjk0IEwzLjAwNSwxMC45NCBMMywxMC45MzU1MzM5IEwxMi44OTk0OTQ5LDEuMDM2MDM4OTcgTDEyLjkwMSwxLjAzOCBMMTIuOTM5MzM5OCwxIFogTTEyLjkzNSwzLjgyOCBMNSwxMS43NjMgTDUsMTMuOTQgTDcuMTc1LDEzLjk0IEwxNS4xMDgsNi4wMDYgTDEyLjkzNSwzLjgyOCBaIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하면 이벤트 수정 화면으로 이동합니다. 다음의 항목을 차례로 수정한 다음 저장 버튼을 선택하세요.

### 이벤트 조건 정의

이벤트 발생 조건 기준을 설정할 수 있습니다.

![이벤트 조건 정의](/img/event-config-v2-condition-common.png)

* 실행: 이벤트 조건을 설정한 다음 버튼을 선택하면 설정한 이벤트를 시뮬레이션할 수 있습니다.

![이벤트 시뮬레이션](/img/event-config-v2-simulation-common.png)
* 지표 설정: Warning 또는 Critical 알림에 대한 임곗값를 설정할 수 있습니다. 연산자를 설정하고 임곗값을 입력하세요.


	+ 연산자 종류: `>`(보다 큼), `>=`(보다 크거나 같음), `<`(보다 작음), `<=`(보다 작거나 같음), `==`(같음)
	+ 임곗값으로 양수, 음수, 0을 입력할 수 있지만, 선택한 이벤트 템플릿에 따라 음수 입력 여부는 다를 수 있습니다.노트
	+ 제공되는 이벤트 템플릿에 따라 설정할 수 있는 알림 수준(Level)은 다를 수 있습니다.
	+ Warning 또는 Critical 수준 하나만 선택할 수 있지만, 두 항목을 모두 비활성화할 수는 없습니다.
* 연속: 설정한 이벤트 조건을 충족하는 횟수에 따라 알림을 보낼 수 있습니다.


	+ 사용 안함: 이벤트가 발생할 때마다 알림을 보냅니다.
	+ 연속: 입력한 횟수만큼 이벤트가 발생하면 알림을 보냅니다.
* 일시 중지: 알림 수신 후 선택한 시간 동안 이벤트가 발생하지 않습니다.
* 해결된 알림: 이벤트가 해결되면 **RECOVERED** 상태의 알림을 보냅니다.

팁다음 조건에 따라 알림을 보내는 기준이 달라집니다.



| 연속 | 해결된 알림 | 동작 |
| --- | --- | --- |
| 사용 안함 | **On** | 설정한 이벤트 조건을 충족하거나 해결되면 알림을 보냅니다. |
| **Off** | 설정한 조건을 충족할 때마다 알림을 보냅니다. |
| 연속 N 회 발생 | **On** | N 회 이상 조건을 충족하거나 N 회 이상 이벤트가 해결되면 알림을 보냅니다. |
| **Off** | N 회 이상 설정한 이벤트 조건을 충족하면 알림을 보냅니다. 알림을 보낸 후 횟수를 초기화해 횟수를 다시 집계합니다. |

### 이벤트 대상 선택[​](#-1 "-1에 대한 직접 링크")

특정 에이전트에서만 발생하는 이벤트를 알림으로 보내도록 설정할 수 있습니다. 에이전트 (인스턴스) 항목을 클릭한 다음 원하는 에이전트를 선택하세요.

![이벤트 대상 선택](/img/event-config-v2-target-apm.png)

노트* 제공되는 템플릿에 따라 선택할 수 있는 대상은 다를 수 있습니다.
* 선택한 대상에 대한 이벤트 발생 현황을 확인하려면 이벤트 조건 정의에서 실행 버튼을 선택하세요.
* 대상을 선택하지 않으면 프로젝트에 포함된 전체 에이전트를 대상으로 알림을 보냅니다. 전체 에이전트를 대상으로 이벤트가 실행되면 많은 알림이 발생할 수 있습니다.
### 기본 정보 및 수신 설정[​](#-2 "-2에 대한 직접 링크")

알림으로 수신되는 이벤트의 제목과 메시지를 작성하고, 수신 대상을 선택할 수 있습니다.

![기본 정보 및 수신 설정](/img/event-config-v2-info-receive-common.png)

* 이벤트 활성화: 현재 이벤트를 활성화할 수 있습니다.
* 이벤트 이름: 기본 제공된 템플릿의 이벤트 이름이 입력되어 있습니다. 사용자가 원하는 이벤트 이름으로 편집할 수 있습니다.
* 메시지: 기본 제공된 템플릿의 메시지가 입력되어 있습니다. 사용자가 원하는 메시지로 편집할 수 있습니다. ![시간 아이콘](/img/ico-timing.svg) 버튼을 클릭하면 이전에 입력한 메시지 기록을 확인할 수 있습니다.

팁메시지 입력 창에 `${Tag}` 또는 `${Field}` 변수를 입력해 메시지를 작성할 수 있습니다.

분석 > 메트릭스 조회 메뉴에서 카테고리를 선택한 다음 입력할 수 있는 `${Tag}` 또는 `${Field}` 변수를 확인하세요. 현재 이벤트 템플릿의 카테고리 이름은 [다음 문서](#basic-template)의 **카테고리** 항목을 참조하세요.
* 수신 테스트: 현재 이벤트로 발생하는 알림 수신 시 입력한 이벤트 이름과 메시지를 사전 점검할 수 있습니다. 필수 항목(지표 설정, 이벤트 이름, 메시지)을 모두 입력해야 테스트할 수 있습니다.

노트테스트 중에는 실제 메트릭스 값이나 변수에 대한 치환 기능이 작동하지 않으며, 수신자 태그가 설정된 사용자에게만 알림을 보낼 수 없습니다.
* 이벤트 수신: 현재 이벤트로 발생하는 알림을 수신할 멤버를 선택할 수 있습니다.


	+ 전체 수신: 프로젝트에 소속된 멤버 전원에게 알림을 보냅니다.
	+ 태그 선택 수신: 선택한 태그를 가진 프로젝트 멤버와 3rd-party 플러그인에 알림을 보냅니다. 태그 추가 또는 ![](/img/ico-add.svg) 버튼을 클릭해 태그 목록에서 원하는 태그를 선택하세요.노트경고 알림 > 이벤트 수신 설정 메뉴에서 프로젝트 멤버와 3rd-party 플러그인에 태그를 설정할 수 있습니다. 자세한 내용은 [다음 문서](/java/set-receive-event#set-notice-by-team-or-users)를 참조하세요.

이벤트 추가하기[​](#이벤트-추가하기 "이벤트 추가하기에 대한 직접 링크")
-------------------------------------------

기본 제공되는 이벤트 템플릿을 편집해 사용자가 원하는 알림을 추가할 수 있습니다.

1. 화면 오른쪽 위에 이벤트 추가 버튼을 선택하세요.
2. 템플릿 목록에서 추가하려는 이벤트 항목을 선택하세요.
3. 이벤트 대상 선택 및 이벤트 대상 선택, 기본 정보 및 수신 설정 섹션의 옵션을 차례로 설정하세요.
4. 모든 설정을 완료한 다음 화면 오른쪽 위에 저장 버튼을 선택하세요.

이벤트 목록에서 새로 추가한 이벤트를 확인할 수 있습니다.

노트* 기본 제공되는 이벤트 템플릿과 구별하여 사용하려면 이벤트 이름 항목을 편집해 저장하세요.
* 기본 제공하는 이벤트 템플릿에 대한 자세한 내용은 [다음 문서](#basic-template)를 참조하세요.
* 이벤트 조건 설정의 각 섹션에 대한 자세한 내용은 [다음 문서](#modify-event)를 참조하세요.
이벤트 삭제하기[​](#이벤트-삭제하기 "이벤트 삭제하기에 대한 직접 링크")
-------------------------------------------

기본 제공된 이벤트 또는 새로 추가한 이벤트를 삭제할 수 있습니다.

1. 이벤트 목록에서 삭제하려는 이벤트 항목에서 ![수정 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZWRpdDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02OC4wMDAwMDAsIC0xMzk1LjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iZWRpdG9yLWljb25zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MC4wMDAwMDAsIDEzNTAuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8ZyBpZD0iaWMtZWRpdCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjguMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIwLDE4IEwyMCwyMCBMMCwyMCBMMCwxOCBMMjAsMTggWiBNMTIuOTM5MzM5OCwxIEwxNy45MzMyMTA4LDYuMDA2NDA3NzggTDE3LjkwMSw2LjAzOCBMMTcuOTAzNzA4NSw2LjA0IEw4LjAwNDIxMzU2LDE1LjkzOTQ5NDkgTDgsMTUuOTM1IEw4LDE1Ljk0IEwzLDE1Ljk0IEwzLDEwLjk0IEwzLjAwNSwxMC45NCBMMywxMC45MzU1MzM5IEwxMi44OTk0OTQ5LDEuMDM2MDM4OTcgTDEyLjkwMSwxLjAzOCBMMTIuOTM5MzM5OCwxIFogTTEyLjkzNSwzLjgyOCBMNSwxMS43NjMgTDUsMTMuOTQgTDcuMTc1LDEzLjk0IEwxNS4xMDgsNi4wMDYgTDEyLjkzNSwzLjgyOCBaIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하세요.
2. 이벤트 수정 화면으로 이동하면 화면 오른쪽 위에 삭제 버튼을 선택하세요.
3. 삭제 확인 메시지가 나타나면 다시 한번 삭제 버튼을 선택하세요.

노트삭제한 이벤트는 복구할 수 없습니다.

JSON 형식으로 수정하기[​](#json-형식으로-수정하기 "JSON 형식으로 수정하기에 대한 직접 링크")
-------------------------------------------------------------

이벤트 설정을 JSON 형식으로 수정할 수 있습니다.

1. 화면 오른쪽 위에 JSON ![](/img/ico-export.svg) 버튼틀 선택하세요.
2. 편집 창이 나타나면 JSON 형식에 맞춰 내용을 수정하세요.
3. 수정을 완료하면 화면 오른쪽 위에 저장 버튼을 선택하세요.

노트수정한 내용이 JSON 형식에 맞지 않으면 화면 아래에 에러 메시지가 표시되며, 저장할 수 없습니다. 표시되는 에러 메시지는 형식에 따라 다를 수 있습니다.

![JSON error](/img/event-config-v2-json-error.png)

JSON 데이터의 구조는 다음과 같습니다.


```
{  
    "metaId": "infra001",  
    "displayName": "CPU",  
    "stateful": true,  
    "selectCondition": {},  
    "warningEnabled": true,  
    "criticalEnabled": true,  
    "receiver": [],  
    "warningThreshold": "cpu > 70",  
    "criticalThreshold": "cpu > 90",  
    "repeatCount": 1,  
    "silentPeriod": 60000,  
    "enabled": false,  
    "message": "CPU = ${cpu}"  
},  

```
JSON 데이터의 필드는 이벤트 설정에서 다음 옵션 항목과 연결됩니다.



| JSON 필드 | 옵션 |
| --- | --- |
| `metaId` | 사용자가 선택한 템플릿의 고유 식별자 값 |
| `displayName` | 이벤트 이름 |
| `stateful` | 해결된 알림 |
| `selectCondition` | 대상 선택 |
| `warningEnabled` | Warning 이벤트 활성 여부 |
| `criticalEnabled` | Critical 이벤트 활성 여부 |
| `receiver` | 이벤트 수신 > 태그 선택 수신 옵션의 수신 태그 키값 목록 |
| `warningThreshold` | Warning 이벤트의 임곗값 설정 |
| `criticalThreshold` | Critical 이벤트의 임곗값 설정 |
| `repeatCount` | 연속 N 회 발생 |
| `silentPeriod` | 일시 중지 |
| `enabled` | 이벤트 활성화 |
| `message` | 메시지 |

JSON 파일로 공유하기[​](#json-파일로-공유하기 "JSON 파일로 공유하기에 대한 직접 링크")
----------------------------------------------------------

이벤트 설정을 JSON 파일로 저장해 다른 사용자와 설정을 공유하거나 다른 사용자의 설정을 가져올 수 있습니다.

### 내보내기[​](#내보내기 "내보내기에 대한 직접 링크")

1. 화면 오른쪽 위에 JSON ![](/img/ico-export.svg) 버튼틀 선택하세요.
2. JSON 편집 창이 나타나면 ![](/img/ico-export.svg) 내보내기 버튼을 선택하세요.
3. JSON 파일이 다운로드되면 공유할 다른 사용자에게 전달하세요.

노트JSON 파일 이름은 *event-rules-`YYYY`-`MM`-`DD`.json* 형식입니다.

### 가져오기[​](#가져오기 "가져오기에 대한 직접 링크")

1. 화면 오른쪽 위에 ![](/img/ico-import.svg) 버튼틀 선택하세요.
2. 내보내기 기능을 통해 다운로드한 JSON 파일을 선택하세요.
3. JSON 편집 창이 나타나면 목록에 추가하기 또는 덮어쓰기 버튼을 선택하세요.

주의이 기능은 같은 종류의 상품 간에 이용할 것을 권장합니다. 다른 상품의 프로젝트로부터 이벤트 설정을 가져올 수는 있지만 정상 작동하지 않습니다.

이벤트 검색하기[​](#이벤트-검색하기 "이벤트 검색하기에 대한 직접 링크")
-------------------------------------------

이벤트 목록에서 이벤트 이름 또는 지표를 기준으로 검색할 수 있습니다. 검색 입력란에 문자열을 입력한 다음 ![검색 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtc2VhcmNoPC90aXRsZT4gLS0+CiAgICA8ZGVzYz5DcmVhdGVkIHdpdGggU2tldGNoLjwvZGVzYz4KICAgIDxnIGlkPSJJY29uLVNldCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGcgaWQ9IldoYVRhcF9JY29uX1NldCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTU0OC4wMDAwMDAsIC00MjYyLjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iaWMtc2VhcmNoLWNvcHktMTAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDU0OC4wMDAwMDAsIDQyNjIuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8ZyBpZD0iaWMtc2VhcmNoIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMi4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8cGF0aCBkPSJNMi4zNDMxNDU3NSwyLjM0MzE0NTc1IEM1LjQ2NzM0MDA4LC0wLjc4MTA0ODU4MyAxMC41MzI2NTk5LC0wLjc4MTA0ODU4MyAxMy42NTY4NTQyLDIuMzQzMTQ1NzUgQzE2LjU0MTYyNTUsNS4yMjc5MTcgMTYuNzYyNzAwNCw5Ljc2NzY5Njk5IDE0LjMyMDA3ODgsMTIuOTA2MTMxOSBMMTkuMzYzNjAzOSwxNy45NDkzOTAzIEwxNy45NDkzOTAzLDE5LjM2MzYwMzkgTDEyLjkwNjEzMTksMTQuMzIwMDc4OCBDOS43Njc2OTY5OSwxNi43NjI3MDA0IDUuMjI3OTE3LDE2LjU0MTYyNTUgMi4zNDMxNDU3NSwxMy42NTY4NTQyIEMtMC43ODEwNDg1ODMsMTAuNTMyNjU5OSAtMC43ODEwNDg1ODMsNS40NjczNDAwOCAyLjM0MzE0NTc1LDIuMzQzMTQ1NzUgWiBNMTIuMjQyNjQwNywzLjc1NzM1OTMxIEM5Ljg5OTQ5NDk0LDEuNDE0MjEzNTYgNi4xMDA1MDUwNiwxLjQxNDIxMzU2IDMuNzU3MzU5MzEsMy43NTczNTkzMSBDMS40MTQyMTM1Niw2LjEwMDUwNTA2IDEuNDE0MjEzNTYsOS44OTk0OTQ5NCAzLjc1NzM1OTMxLDEyLjI0MjY0MDcgQzYuMTAwNTA1MDYsMTQuNTg1Nzg2NCA5Ljg5OTQ5NDk0LDE0LjU4NTc4NjQgMTIuMjQyNjQwNywxMi4yNDI2NDA3IEMxNC41ODU3ODY0LDkuODk5NDk0OTQgMTQuNTg1Nzg2NCw2LjEwMDUwNTA2IDEyLjI0MjY0MDcsMy43NTczNTkzMSBaIiBpZD0iQ29tYmluZWQtU2hhcGUiPjwvcGF0aD4KICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+) 버튼을 선택하세요.

