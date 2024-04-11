Flex 보드 만들기
===========

대시보드 생성[​](#대시보드-생성 "대시보드 생성에 대한 직접 링크")
----------------------------------------

Flex 보드를 생성하고 위젯을 배치해 자신만의 대시보드를 만들 수 있습니다.

1. ***Flex 보드*** 메뉴에서 오른쪽 위에 ***+ 대시보드 생성하기*** 버튼을 선택하세요.
2. ***대시보드 생성하기*** 창이 나타나면 ***이름*** 입력 텍스트 상자에 대시 보드 이름을 입력하세요.
3. 위젯 배치 방법을 선택해 ***대시보드 생성하기*** 버튼을 클릭하세요.


	* ***고정 레이아웃 플렉스 보드***: 픽셀 기반으로 자유롭게 위젯을 배치할 수 있습니다.
	* ***반응형 플렉스 보드***: 브라우저 사이즈 기준으로 그리드 반응형 레이아웃을 제공합니다. ***반응형 플렉스 보드***를 선택하면 그리드를 설정한 다음 ***대시보드 생성하기*** 버튼을 선택하세요.
4. ***위젯 템플릿*** 선택 화면에서 대시보드에 배치할 위젯을 선택하세요. 메트릭스 위젯을 추가하려면 ***위젯 템플릿***의 오른쪽에 ***모든 메트릭스*** 버튼을 선택하세요.

노트
	* ***위젯 템플릿***: 일반적인 모니터링 상황에서 중요하게 다뤄지는 지표를 간추려 사전 정의된 위젯 목록을 선택할 수 있습니다.
	* ***모든 메트릭스***: 사용자의 프로젝트에서 수집 중인 모든 메트릭스 데이터를 기준으로 위젯을 생성할 때 사용합니다. 메트릭스 위젯에 대한 자세한 설명은 [다음 문서](/java/flexboard-metric-widget)를 참조하세요.
5. 배치한 위젯의 위치를 이동하거나 크기를 조절하세요.


	* 배치한 위젯의 위쪽으로 마우스 커서를 이동하세요. 커서 모양이 십자 형태로 변경되면 위젯을 마우스로 클릭한 상태에서 드래그하세요. 위치를 이동할 수 있습니다.
	* 배치한 위젯의 오른쪽 아래로 마우스 커서를 이동하세요. 커서 모양이 화살표 형태로 변경되면 위젯을 마우스로 클릭한 상태로 드래그하세요. 원하는 크기로 조절할 수 있습니다.
6. 추가할 위젯을 모두 배치를 완료한 다음 ***뷰 모드***를 선택해 레이아웃을 확인하세요. 레이아웃을 다시 수정하려면 ***수정 모드***를 선택해 위젯의 배치를 변경하세요.

모든 과정을 완료했다면 오른쪽 위에 ![목록으로 가기 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyMHB4IiBoZWlnaHQ9IjIwcHgiIHZpZXdCb3g9IjAgMCAyMCAyMCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtcy1sb2dvdXQ8L3RpdGxlPiAtLT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9Ikljb24tU2V0IiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4KICAgICAgICA8ZyBpZD0iV2hhVGFwX0ljb25fU2V0IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtOTM0LjAwMDAwMCwgLTU1NS4wMDAwMDApIiBmaWxsPSIjNzU3NTc1Ij4KICAgICAgICAgICAgPGcgaWQ9ImRpcmVjdGlvbmFsLWljb25zLWNvcHkiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQwLjAwMDAwMCwgNDI4LjAwMDAwMCkiPgogICAgICAgICAgICAgICAgPGcgaWQ9ImljLWxvZ291dCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODk0LjAwMDAwMCwgMTI3LjAwMDAwMCkiPgogICAgICAgICAgICAgICAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIuMDAwMDAwLCAyLjAwMDAwMCkiIGlkPSJpYy1sb2dpbi1jb3B5Ij4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTYuOCwxMiBMMTAuOCw4IEw2LjgsNCBMNS42NzIsNS4xMjggTDcuNzM2LDcuMiBMLTMuMzkyODQxNTZlLTEzLDcuMiBMLTMuMzkyODQxNTZlLTEzLDguOCBMNy43MzYsOC44IEw1LjY3MiwxMC44NzIgTDYuOCwxMiBaIE0zLjI5ODY5NDY1ZS0xMiwzLjk0MzUxMjE4ZS0xNCBMMy43NTM0NDJlLTEyLDQuOCBMMS42LDQuOCBMMS42LDEuNiBMMTQuNCwxLjYgTDE0LjQsMTQuNCBMMS42LDE0LjQgTDEuNiwxMS4yIEwzLjcwNzkyMjg2ZS0xMiwxMS4yIEwzLjkyMzk3MjI2ZS0xMiwxNiBMMTYsMTYgTDE2LDIuNjY0NTM1MjZlLTE0IEwzLjI5ODY5NDY1ZS0xMiwzLjk0MzUxMjE4ZS0xNCBaIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) (***목록으로 가기***) 버튼을 선택하세요. ***Flex 보드*** 메뉴의 **보드** 목록에서 생성한 보드를 확인할 수 있습니다. 생성한 보드를 선택해 새로 생성한 Flex 보드를 확인할 수 있습니다.

노트고객의 의견을 반영해 대시보드 템플릿 또는 위젯을 추가하려고 합니다. 필요한 대시보드 템플릿 또는 위젯이 있다면 [support@whatap.io](mailto:support@whatap.io)로 문의해 주세요.

