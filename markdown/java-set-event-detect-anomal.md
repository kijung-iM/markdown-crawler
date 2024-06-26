이상치 탐지 경고 알림
============

홈 화면 > 프로젝트 선택 > ***경고 알림*** > ***이벤트 설정*** > ***이상치 탐지*** 탭 선택

이상치 탐지(Anomaly Detection)란 데이터 안에서 anomaly, outlier, abnormal과 같이 예상치 못한 패턴을 찾는 일련의 활동입니다. 사용자는 메트릭스의 데이터를 기반으로 상승 패턴과 하락   패턴의 움직임이 평소와 같지 않을 경우 경고 알림을 보내도록 설정할 수 있습니다.

![이상치 탐지](/img/set-event-abnormal.png)

***+ 이벤트 추가*** 버튼을 선택해 ***이상치 탐지*** 이벤트 설정을 진행할 수 있습니다. 모든 설정을 완료한 다음 ***저장*** 버튼을 선택하세요. ***이상치 탐지*** 창의 제목 오른쪽에 토글 버튼을 선택해 활성화 여부를 선택할 수 있습니다.

이상치 탐지 이벤트 생성[​](#이상치-탐지-이벤트-생성 "이상치 탐지 이벤트 생성에 대한 직접 링크")
----------------------------------------------------------

![이상치 탐지](/img/set-event-anormal-create.png)

### ***이벤트 기본 정보***[​](#이벤트-기본-정보 "이벤트-기본-정보에 대한 직접 링크")

이상치 탐지 이벤트의 기본 정보를 입력하세요.

* ***레벨***: 정보, 경고, 위험 수준 중 하나의 레벨을 선택하세요.
* ***메시지***: 벤트 발생 시 출력하는 알림 메시지를 입력합니다. `${태그 또는 필드키}` 입력으로 메시지에 변수를 적용할 수 있습니다. 변수에 입력할 키는 선택한 메트릭스 데이터 ***카테고리***에 포함된 값이여야 합니다.

### ***메트릭스***[​](#메트릭스 "메트릭스에 대한 직접 링크")

이벤트 발생 대상을 선택하세요.

* ***카테고리***: 메트릭스 데이터를 구분하는 단위입니다. 메트릭스 이벤트 설정 시 필수 선택 값입니다.
* ***필드***: 이벤트 발행 조건에 사용할 필드를 선택합니다. 다중 선택할 수 있습니다.
* ***필터***: 이벤트 조건 대상을 선택합니다. 다중 선택할 수 있습니다.
* ***오브젝트 병합***: 오브젝트 병합 방법을 선택할 수 있습니다.

### ***이상치 탐지***[​](#이상치-탐지 "이상치-탐지에 대한 직접 링크")

***상승 패턴*** 또는 ***하락 패턴***의 민감도를 선택할 수 있습니다. 각 항목의 토글 버튼을 선택해 기능을 켜거나 끌 수 있습니다.

이상치 탐지 이벤트 수정[​](#이상치-탐지-이벤트-수정 "이상치 탐지 이벤트 수정에 대한 직접 링크")
----------------------------------------------------------

1. ***경고 알림*** > ***이벤트 설정*** 메뉴에서 ***이상치 탐지*** 탭을 선택하세요.
2. ***이상치 탐지*** 목록에서 수정하려는 항목의 오른쪽에 ![편집 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZWRpdDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02OC4wMDAwMDAsIC0xMzk1LjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iZWRpdG9yLWljb25zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MC4wMDAwMDAsIDEzNTAuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8ZyBpZD0iaWMtZWRpdCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjguMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIwLDE4IEwyMCwyMCBMMCwyMCBMMCwxOCBMMjAsMTggWiBNMTIuOTM5MzM5OCwxIEwxNy45MzMyMTA4LDYuMDA2NDA3NzggTDE3LjkwMSw2LjAzOCBMMTcuOTAzNzA4NSw2LjA0IEw4LjAwNDIxMzU2LDE1LjkzOTQ5NDkgTDgsMTUuOTM1IEw4LDE1Ljk0IEwzLDE1Ljk0IEwzLDEwLjk0IEwzLjAwNSwxMC45NCBMMywxMC45MzU1MzM5IEwxMi44OTk0OTQ5LDEuMDM2MDM4OTcgTDEyLjkwMSwxLjAzOCBMMTIuOTM5MzM5OCwxIFogTTEyLjkzNSwzLjgyOCBMNSwxMS43NjMgTDUsMTMuOTQgTDcuMTc1LDEzLjk0IEwxNS4xMDgsNi4wMDYgTDEyLjkzNSwzLjgyOCBaIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하세요.
3. 이상치 탐지 설정 창이 나타납니다. 수정이 필요한 항목을 수정한 다음 ***저장*** 버튼을 선택하세요.

이상치 탐지 이벤트 삭제[​](#이상치-탐지-이벤트-삭제 "이상치 탐지 이벤트 삭제에 대한 직접 링크")
----------------------------------------------------------

***경고 알림*** > ***이벤트 설정*** 메뉴에서 ***이상치 탐지*** 탭을 선택하세요. 목록에서 삭제하려는 항목의 오른쪽에 ![삭제 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIwIDIySDRWNmgydjE0aDEyVjZoMnYxNnptMi0xOGgtNWwtMS4xNDMtMkg4LjE0M0w3IDRIMnYyaDIwVjR6IgogICAgZmlsbD0iIzc1NzU3NSIgLz4KICA8cGF0aCBkPSJNOSA4aDJ2MTBIOVY4ek0xMyA4aDJ2MTBoLTJWOHoiIGZpbGw9IiM3NTc1NzUiIC8+Cjwvc3ZnPg==) 버튼을 선택하세요. 확인 팝업 메시지가 나타나면 ***삭제*** 버튼을 선택하세요.

