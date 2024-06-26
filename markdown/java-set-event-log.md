로그 경고 알림
========

노트* 이 기능은 로그 모니터링을 활성화해야 이용할 수 있습니다. **로그 모니터링 활성화**에 대한 자세한 내용은 [다음 문서](../log/log-java)를 참조하세요.
* 로그 모니터링의 주요 메뉴에 대한 자세한 내용은 [다음 문서](../log/learn-main-menu)를 참조하세요.
홈 화면 > 프로젝트 선택 > ***경고 알림*** > ***이벤트 설정*** > ***로그*** 탭

수집한 로그 데이터를 조건에 맞춰 필터링해 경고 알림을 설정할 수 있습니다. ***+ 이벤트 추가*** 버튼을 선택해 로그 이벤트 경고 알림을 설정하세요. 모든 설정을 완료한 다음 ***저장*** 버튼을 선택하세요.

![로그 알림 설정](/img/log-alert-config.png)

추가할 수 있는 로그 이벤트 다음과 같습니다.

* ***실시간 로그 이벤트*** : 실시간으로 수집한 로그에서 검색 값이 등장하면 경고 알림을 보냅니다.
* ***복합 로그 이벤트*** : 최근에 수집한 로그 중 일정 조건을 만족하는 로그가 일정 개수 이상 수집한 경우에 경고 알림을 보냅니다.

노트* 이벤트를 추가하거나 설정하려면 **알림 설정** 권한이 있어야합니다. 사용자별 권한에 대한 자세한 내용은 [다음 문서](/project/project-structure#project-auth)를 참조하세요.
* 경고 알림과 관련해 모니터링 플랫폼별 지원되는 이벤트 종류를 확인하려면 [다음 문서](/support-env#support-notice)를 참조하세요.
이벤트 추가 공통 옵션[​](#log-event-add-common "이벤트 추가 공통 옵션에 대한 직접 링크")
---------------------------------------------------------------

다음은 이벤트 추가 시 공통으로 설정할 수 있는 옵션입니다.

* ***이벤트 이름*** : 추가하려는 이벤트 이름을 입력하세요.
* ***이벤트 활성화*** : 토글 버튼을 클릭해 경고 알림 활성화 여부를 선택할 수 있습니다.
* ***레벨*** : 위험, 경고, 정보 중 하나의 레벨을 선택하세요.
* ***메시지*** : 이벤트 발생 시 출력하는 알림 메시지를 입력합니다. `${태그 또는 필드키}` 입력으로 메시지에 변수를 적용할 수 있습니다. 변수에 입력할 키는 선택한 메트릭스 데이터 ***카테고리***에 포함된 값이여야 합니다.
* ***카테고리*** : 로그 구분 명칭(로그 폴더명)을 목록에서 선택하거나 직접 입력할 수 있습니다.
* ***이벤트 발생 일시 중지*** : 과도한 경고 알림 발생을 방지할 수 있는 옵션입니다. 첫 번째 경고 알림 이후 선택한 시간 동안 경고 알림을 보내지 않습니다. 또한 ***이벤트 기록*** 메뉴에 기록되지 않습니다.
* ***이벤트 수신 태그*** : 이벤트 수신 태그를 선택하면 해당 태그를 가진 프로젝트 멤버와 3rd-party 플러그인에 알림을 전송할 수 있습니다. 이벤트 수신 태그를 선택하지 않으면 프로젝트 전체 멤버에게 경고 알림을 보냅니다.

태그를 추가하지 않으면 전체 멤버에게 경고 알림을 보냅니다. ***+ 태그 추가***를 클릭한 다음 ***태그 목록***에서 경고 알림 수신 대상을 선택하세요. ***+ 새 태그 생성***을 선택해 태그를 추가할 수도 있습니다.

노트***경고 알림*** > ***이벤트 수신 설정*** 메뉴에서 프로젝트 멤버와 3rd-party 플러그인에 태그를 설정할 수 있습니다. ***이벤트 수신 설정*** 메뉴에 대한 자세한 내용은 [다음 문서](/java/set-receive-event)를 참조하세요.

실시간 로그 이벤트 추가[​](#rt-log-event "실시간 로그 이벤트 추가에 대한 직접 링크")
---------------------------------------------------------

![실시간 로그 이벤트 추가 sc](/img/log-alert-rt.png)

* ***검색 키*** : 로그 데이터 내에서 특정 값에 접근하기 위한 식별자를 의미합니다. 목록에서 선택하거나 직접 입력할 수 있습니다.


> 예시, HTTP 응답 상태 코드를 나타내는 값에 접근하고자 할 경우 ***검색 키*** `status`
* ***검색 값*** : ***검색 키***에 해당하는 실제 데이터를 의미합니다. 로그에서 입력한 단어를 포함할 경우 경고 알림을 보냅니다. 목록에서 선택하거나 직접 입력할 수 있습니다.


> 예시, ***검색 키*** `status` ***검색 값*** `200`을 설정한 경우 HTTP 응답 상태 코드 200을 포함하는 로그 데이터 수집 시 경고 알림 발생
* ***이벤트 대상 필터링*** : ***선택 입 력*** 옵션을 통해 ***검색 키***와 ***연산자***, ***검색 값***을 선택해 대상을 필터링하거나 ***직접 입력*** 옵션을 선택할 수 있습니다. 입력값이 없을 경우 실시간으로 수집하는 데이터 전체에 대한 알림 발생 여부를 판단합니다.


> 예시, `AppLog` 카테고리의 로그 중 `level`이 `ERROR`인 로그를 찾습니다. 일치하는 로그 중에서 ***oid***가 **12345678**인 경우 경고 알림을 보냅니다.

복합 로그 이벤트 추가[​](#cp-log-event "복합 로그 이벤트 추가에 대한 직접 링크")
-------------------------------------------------------

![복합 로그 이벤트 추가 sc](/img/log-alert-cp.png)

* ***템플릿*** : 복합 로그 템플릿을 제공합니다.
* ***로그 검색 조건***


	+ ***검색 키***에서 이벤트 발생 조건 대상을 선택할 수 있습니다. 선택한 ***검색 키***에 해당하는 검색 값을 선택할 수 있습니다.
	+ ***검색 키***에서 동일한 항목을 추가할 경우 'OR' 조건으로, 다른 항목을 추가할 경우 'AND' 조건으로 동작합니다.
	+ ***제외*** 체크 박스를 선택해 선택한 검색 값을 이벤트 발행 조건에서 제외할 수 있습니다.
	+ ***+ 추가***를 선택해 여러개의 이벤트 발행 조건을 추가 또는 제외 설정할 수 있습니다.
* ***데이터 조회 범위*** : 선택한 시간동안 수집한 로그를 조회합니다. 데이터 조회 시간을 5분으로 선택하면 최근 5분 동안 수집한 데이터를 조회해서 이벤트 발생 조건을 확인합니다.
* ***이벤트 발행 조건*** : 이벤트가 입력한 횟수와 선택한 연산자의 조건과 같이 발생할 때 경고 알림을 보냅니다.


> 예시, `AppLog` 카테고리의 로그 중 `조건 입력`에 해당하는 로그를 필터링 합니다. 조건 입력에서 ***제외***를 체크한 경우 해당 조건으로 찾은 로그를 제외하겠다는 의미입니다. 따라서 `level`이 `ERROR`인 로그는 제외합니다. 최근 10분 동안 수집한 로그 중 이벤트가 `5`보다 작을 경우 경고 알림을 보냅니다.

로그 이벤트 설정 수정하기[​](#로그-이벤트-설정-수정하기 "로그 이벤트 설정 수정하기에 대한 직접 링크")
-------------------------------------------------------------

1. ***경고 알림*** > ***이벤트 설정*** 메뉴로 이동하세요.
2. ***로그*** 탭을 선택하세요.
3. 로그 이벤트 목록 중 수정하려는 이벤트 항목에서 오른쪽에 ![편집 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZWRpdDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02OC4wMDAwMDAsIC0xMzk1LjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iZWRpdG9yLWljb25zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MC4wMDAwMDAsIDEzNTAuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8ZyBpZD0iaWMtZWRpdCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjguMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIwLDE4IEwyMCwyMCBMMCwyMCBMMCwxOCBMMjAsMTggWiBNMTIuOTM5MzM5OCwxIEwxNy45MzMyMTA4LDYuMDA2NDA3NzggTDE3LjkwMSw2LjAzOCBMMTcuOTAzNzA4NSw2LjA0IEw4LjAwNDIxMzU2LDE1LjkzOTQ5NDkgTDgsMTUuOTM1IEw4LDE1Ljk0IEwzLDE1Ljk0IEwzLDEwLjk0IEwzLjAwNSwxMC45NCBMMywxMC45MzU1MzM5IEwxMi44OTk0OTQ5LDEuMDM2MDM4OTcgTDEyLjkwMSwxLjAzOCBMMTIuOTM5MzM5OCwxIFogTTEyLjkzNSwzLjgyOCBMNSwxMS43NjMgTDUsMTMuOTQgTDcuMTc1LDEzLjk0IEwxNS4xMDgsNi4wMDYgTDEyLjkzNSwzLjgyOCBaIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하세요.
4. ***이벤트 설정*** 창이 나타나면 옵션을 수정한 다음 ***저장*** 버튼을 선택하세요.

선택한 로그 이벤트를 삭제하려면 이벤트 설정 창에서 오른쪽 위에 ***삭제*** 버튼을 선택하세요.

로그 이벤트 끄기[​](#로그-이벤트-끄기 "로그 이벤트 끄기에 대한 직접 링크")
----------------------------------------------

1. ***경고 알림*** > ***이벤트 설정*** 메뉴로 이동하세요.
2. ***로그*** 탭을 선택하세요.
3. 로그 이벤트 목록 중 경고 알림을 끄려는 이벤트 항목의 가장 오른쪽에 토글 버튼을 선택하세요.

다시 토글 버튼을 선택하면 해당 경고 알림이 활성화됩니다.

로그 이벤트 내보내기/불러오기[​](#로그-이벤트-내보내기불러오기 "로그 이벤트 내보내기/불러오기에 대한 직접 링크")
------------------------------------------------------------------

로그 이벤트의 설정 내용을 json 파일로 저장한 다음 불러와 재사용할 수 있습니다.

1. ***경고 알림*** > ***이벤트 설정*** 메뉴로 이동하세요.
2. ***로그*** 탭을 선택하세요.
3. 로그 이벤트 목록 위에 ***JSON*** ![내보내기 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZXhwb3J0PC90aXRsZT4gLS0+CiAgICA8ZGVzYz5DcmVhdGVkIHdpdGggU2tldGNoLjwvZGVzYz4KICAgIDxnIGlkPSJJY29uLVNldCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGcgaWQ9IldoYVRhcF9JY29uX1NldCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTc0MC4wMDAwMDAsIC0yOTUxLjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iYXBwbGljYXRpb24taWNvbnMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQwLjAwMDAwMCwgMjM0Ni4wMDAwMDApIj4KICAgICAgICAgICAgICAgIDxnIGlkPSJpYy1leHBvcnQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDcwMC4wMDAwMDAsIDYwNS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMi4wMDAwMDApIiBpZD0iSWNvbiI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0xOCwxOCBMMiwxOCBMMiwyIEwxMCwyIEwxMCwtMS44NDc2ODg2N2UtMTMgTC04LjExNzk1MDc2ZS0xMywtMS44NDc2ODg2N2UtMTMgTC04LjExNzk1MDc2ZS0xMywyMCBMMjAsMjAgTDIwLDEwIEwxOCwxMCBMMTgsMTcgTDE4LDE4IFogTTEzLjEyNjg4ODIsMS45NjM3NDYyMiBMMTYuNjUxODEyNywxLjk2Mzc0NjIyIEw3LDExLjYxNTU1ODkgTDguMzg0NDQxMDksMTMgTDE4LjAzNjI1MzgsMy4zNDgxODczMSBMMTguMDM2MjUzOCw2Ljg3MzExMTc4IEwyMCw2Ljg3MzExMTc4IEwyMCwtMS41NjMxOTQwMmUtMTMgTDEzLjEyNjg4ODIsLTEuNTYzMTk0MDJlLTEzIEwxMy4xMjY4ODgyLDEuOTYzNzQ2MjIgWiI+PC9wYXRoPgogICAgICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+) 버튼을 선택하세요. ***JSON 내보내기*** 창이 나타납니다.
4. 내보내기 할 항목을 수정 또는 편집하세요.
5. 오른쪽 위에 ![내보내기 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZXhwb3J0PC90aXRsZT4gLS0+CiAgICA8ZGVzYz5DcmVhdGVkIHdpdGggU2tldGNoLjwvZGVzYz4KICAgIDxnIGlkPSJJY29uLVNldCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGcgaWQ9IldoYVRhcF9JY29uX1NldCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTc0MC4wMDAwMDAsIC0yOTUxLjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iYXBwbGljYXRpb24taWNvbnMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQwLjAwMDAwMCwgMjM0Ni4wMDAwMDApIj4KICAgICAgICAgICAgICAgIDxnIGlkPSJpYy1leHBvcnQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDcwMC4wMDAwMDAsIDYwNS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMi4wMDAwMDApIiBpZD0iSWNvbiI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0xOCwxOCBMMiwxOCBMMiwyIEwxMCwyIEwxMCwtMS44NDc2ODg2N2UtMTMgTC04LjExNzk1MDc2ZS0xMywtMS44NDc2ODg2N2UtMTMgTC04LjExNzk1MDc2ZS0xMywyMCBMMjAsMjAgTDIwLDEwIEwxOCwxMCBMMTgsMTcgTDE4LDE4IFogTTEzLjEyNjg4ODIsMS45NjM3NDYyMiBMMTYuNjUxODEyNywxLjk2Mzc0NjIyIEw3LDExLjYxNTU1ODkgTDguMzg0NDQxMDksMTMgTDE4LjAzNjI1MzgsMy4zNDgxODczMSBMMTguMDM2MjUzOCw2Ljg3MzExMTc4IEwyMCw2Ljg3MzExMTc4IEwyMCwtMS41NjMxOTQwMmUtMTMgTDEzLjEyNjg4ODIsLTEuNTYzMTk0MDJlLTEzIEwxMy4xMjY4ODgyLDEuOTYzNzQ2MjIgWiI+PC9wYXRoPgogICAgICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+) ***내보내기*** 버튼을 선택하세요. 브라우저에서 json 파일을 다운로드합니다.
6. 로그 이벤트 목록 위에 ![가져오기 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAyMHB4O2hlaWdodDogMjBweDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiPgogICAgPHBhdGggZmlsbD0iIzc1NzU3NSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMjAgMjBINFY0aDhWMkgydjIwaDIwVjEyaC0ydjh6bS00LjEyNy02Ljk2NGgtMy41MjVMMjIgMy4zODQgMjAuNjE2IDJsLTkuNjUyIDkuNjUyVjguMTI3SDlWMTVoNi44NzN2LTEuOTY0eiI+PC9wYXRoPgo8L3N2Zz4=) 버튼을 선택하세요.
7. 파일 선택 창이 나타나면 앞서 다운로드 받은 json 파일을 선택하세요.
8. ***JSON 가져오기*** 창이 나타나면 내용을 수정한 다음 ***+ 목록에 추가하기*** 버튼을 선택하세요.

노트**이벤트에 id가 존재합니다. id를 제거한 뒤 다시 시도하세요.**

* 메시지가 나타나면 ***JSON 가져오기*** 창에서 `id` 항목을 삭제한 다음 ***+ 목록에 추가하기*** 버튼을 선택하세요.
* 기존의 이벤트 항목에 덮어쓰기를 하려면 `id` 항목을 삭제한 다음 ***덮어쓰기*** 버튼을 선택하세요.
