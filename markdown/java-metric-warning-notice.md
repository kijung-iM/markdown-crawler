메트릭스 경고 알림
==========

홈 화면 > 프로젝트 선택 > 경고 알림 > 이벤트 설정 > 메트릭스 탭 선택

메트릭스 이벤트란?[​](#메트릭스-이벤트란 "메트릭스 이벤트란?에 대한 직접 링크")
------------------------------------------------

메트릭스 이벤트는 기본 이벤트(애플리케이션 이벤트, 서버 이벤트 등)보다 구체적이고 복잡한 이벤트를 설정할 때 사용합니다. 프로젝트에서 실시간으로 수집 중인 메트릭스 데이터를 기반으로 이벤트를 설정할 수 있습니다. 사용에 따라 두 가지 설정 방법 중 하나를 선택해 이벤트를 설정할 수 있습니다.

* 메트릭스 이벤트
* 복합 메트릭스 이벤트

노트메트릭스에 대한 자세한 내용은 [다음 문서](/java/metrics-intro)를 참조하세요.

메트릭스 이벤트[​](#메트릭스-이벤트 "메트릭스 이벤트에 대한 직접 링크")
-------------------------------------------

경고 알림 > 이벤트 설정 메뉴에서 화면 위에 메트릭스를 선택하세요. 화면 오른쪽 위에 이벤트 추가를 선택하세요. 메트릭스 이벤트 창이 나타납니다.

![메트릭스 이벤트](/img/set-events-metrics.png)

### 기본 정보 입력[​](#basic-info "기본 정보 입력에 대한 직접 링크")

* 이벤트명: 추가하려는 이벤트 이름을 입력하세요.
* 이벤트 활성화: 이벤트를 활성화 여부를 선택하세요.
* 템플릿: 만들어진 템플릿을 선택해 빠르고 쉽게 이벤트를 설정할 수 있습니다. 템플릿을 사용하지 않을 경우 사용 안 함을 선택하세요.

노트템플릿 목록에 대한 자세한 내용은 [다음 문서](#template)를 참조하세요.
* 카테고리: 메트릭스 데이터를 구분하는 단위입니다. 메트릭스 이벤트 설정 시 필수 선택 값입니다.

![메트릭스 이벤트 - 카테고리](/img/set-event-select-category.png)


	+ 카테고리 선택 옵션에는 ![](/img/number-01.png) 이름과 ![](/img/number-02.png) 데이터 수집 간격, ![](/img/number-03.png) 키 정보를 표시합니다. 이벤트 설정 시 해당 카테고리의 키 값을 사용합니다.
	+ 카테고리는 최근 3시간 범위 내 프로젝트에서 수집 중인 메트릭스 데이터를 조회해 목록에 표시합니다. 카테고리 선택 옵션에 수집 간격이 표시되지 않는 경우 직접 입력하기 옵션을 선택해 카테고리 키를 입력할 수 있습니다.
* 레벨
	+ 이벤트 발생 시 경고 수준을 나타냅니다. Critical, Warning, Info 수준으로 나눕니다. Critical, Warning 레벨 설정 시 이벤트 상태가 해결되면 추가 알림 선택 옵션이 활성화됩니다.
	+ 이벤트 상태가 해결되면 추가 알림[​](/java/metric-warning-notice#scrollTo-resolve-event): 이벤트 항목 중 발생한 이벤트 상태가 해결되면 추가 알림 송신 여부를 선택할 수 있습니다. 토글 버튼을 선택해 기능을 켜거나 끌 수 있습니다.
* 메시지
	+ 이벤트 발생 시 출력하는 알림 메시지를  입력합니다. `${Tag}` 또는 `${Field}` 입력으로 메시지에 변수를 적용할 수 있습니다. 변수에 입력할 키는 선택한 메트릭스 데이터 카테고리에 포함된 값이여야 합니다. 메트릭스 조회 메뉴에서 입력할 수 있는 태그 또는 필드키를 확인할 수 있습니다.
	
	![Message example](/img/event-config-message-example.png)
	+ ![시간 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiPgogICAgPHBhdGggZmlsbD0iIzc1NzU3NSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMTcuNTYzIDQuMjFMMjIgNS40M2wtMS43OCAxLjA1NkExMC4wMDIgMTAuMDAyIDAgMCAxIDIxLjg2MyAxMmMwIDUuNTIzLTQuNDQ2IDEwLTkuOTMyIDEwLS4xNzggMC0uMzU2LS4wMDUtLjUzMi0uMDE0bC4wNzctMS45OTljLjE1LjAwOS4zMDIuMDEzLjQ1NS4wMTMgNC4zODkgMCA3Ljk0Ni0zLjU4MiA3Ljk0Ni04YTguMDAxIDguMDAxIDAgMCAwLTEuMzc0LTQuNDk4bC0yLjEzIDEuMjYyIDEuMTktNC41NTR6TTcuNjI3IDE4LjczMmE4LjExIDguMTEgMCAwIDAgMi4xOTYgMS4wMDNsLS41NSAxLjkyMy0uMzkxLS4xMjFhMTAuMTM0IDEwLjEzNCAwIDAgMS0yLjM1LTEuMTN6TTQuOTQ2IDE1Ljc5Yy4zNzcuNzExLjg1OCAxLjM2MSAxLjQyOCAxLjkyOGwtMS40MSAxLjQxOS0uMjYzLS4yNzNhMTAgMTAgMCAwIDEtMS41MjItMi4xMzd6TTEyLjc4NSA3djUuMDczbDQuMTEzIDIuNDU5TDE1Ljk3NiAxNmwtNS4wMzctMy4wMzJWN2gxLjg0NnpNMi4wMSAxMS44NjlsMiAuMDMzYTcuOTk0IDcuOTk0IDAgMCAwIC4zMjEgMi4zNzhsLTEuOTIuNTYyLS4wOTgtLjM2MWE5Ljk4NiA5Ljk4NiAwIDAgMS0uMzAzLTIuNjEyek0zLjMyNyA3LjA4bDEuNzM4Ljk5YTguMjA3IDguMjA3IDAgMCAwLS44NyAyLjI1OUwyLjI0MiA5LjlsLjA4NS0uMzU3YTEwLjA4IDEwLjA4IDAgMCAxIDEtMi40NjJ6bTMuNDYtMy41N2wxLjA0NCAxLjcwN2MtLjY4Ni40MTktMS4zMDQuOTM5LTEuODM1IDEuNTQ0TDQuNDkyIDUuNDQzbC4yNTctLjI4QTkuOTc0IDkuOTc0IDAgMCAxIDYuNzg4IDMuNTF6bTQuNzcyLTEuNDY0bC4wOTIgMS45OThhOC4wMiA4LjAyIDAgMCAwLTIuMzU1LjQ2OWwtLjY4LTEuODgxLjM1Ni0uMTJhMTAuMDEyIDEwLjAxMiAwIDAgMSAyLjU4Ny0uNDY2eiI+PC9wYXRoPgo8L3N2Zz4=) 버튼을 클릭하면 이전에 입력한 메시지 기록을 확인할 수 있습니다.
* 수신 테스트필수 항목인 이벤트명, 카테고리, 레벨, 메시지 정보를 기준으로 알림을 발생시켜 메시지를 점검하는 기능입니다.

노트수신 테스트를 이용하려면 필수 항목(이벤트명, 카테고리, 레벨, 메시지)에 값을 입력하거나 선택해야 합니다.
* 이벤트 발생 조건![이벤트 발생 조건](/img/set-event-condition.png)

![지시선 4](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3lpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NzViZDMyNzctMzBhNS00ZGFjLWEyOTItYzZlNDYwMGIxNzhjIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkRCRDFDMjg0QjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkRCRDFDMjgzQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6OWVmMWZkYmQtM2FiMS00MDBiLWEyYjAtZjU4ZGNmNjZkY2NiIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjc1YmQzMjc3LTMwYTUtNGRhYy1hMjkyLWM2ZTQ2MDBiMTc4YyIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PjAb6dMAAAJ4SURBVHjaYvy6g2HQABYS1YsBsRcQOwCxNhArADEfEP8H4s9AfB+IrwLxASDeDsSvSDGckciQsQXiMiD2IMEDv4F4GxB3AfExYjQwEZBXBuKtQHwIiH1IDElWIPYH4qNAvAmIFSlxTDQQX4BGC6XAF2pWGDmOaQTiJUDMQ8X0CUpbK4C4hhTHNAFxHY0yDCMQNwNxBTGOiQHiWjrk4jYgjsDnGBUgnkGnIgUUQjPREzVy7pgMxNykmnr/OQODTiKqGJHFBSgNTQRiP/SQcYCWISSDhnkU5zJrdMeUkmPSuoMMDGsOUxxlpciOkQRid1JN+PoDmP/nQ9jp3hQ5xgtazYAdAzKKmVQT5m5hYLjzAsL2tKDIMaywJAJyjB2puq8Aq8PKORC2vS4Dg6spxVHlAHOMLqk6u5ch2F1ZVMnq2jDHyJGbaMuBxZaOIlUcowhzjACxOl5/QCRaFQkGhswAqhWCvMQ0IVDA9A2IRFsPLOhEBRioCkAl8EcgFiSmpO1cgeAfuQTB2EDRZAjdl0u0Oz7DWnrngbQBMTnIPJPEsoj49vUpIDYHRdOVQdAWvwaLpkPQpgNeAMo1+HzK7UFWiMDAAVgCBrVx/w5gqPyB9iTAjnkGxDsH0DHbYF0aWNbuHUDHdGPrN+0gp/amEGyFdoEwmp05oLRHR4eAypZcXG3gO0CcRUfHZEC7wzh7B4uAuJ0ODgF1hZYR02+qgvZtaAXqcZnPhMfliVROQyCz4qCdRJL72guAWJ9KZdA2qFmLKRmFuAttnzqSUVKD1G6BNim9oWZRZXwGBqRA7W9Q0xdUXUFbibDmx3sgfog0WAQKjRekGA4QYAC/W4cAbCK1hAAAAABJRU5ErkJggg==) 필드, ![지시선 5](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA4dpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NzViZDMyNzctMzBhNS00ZGFjLWEyOTItYzZlNDYwMGIxNzhjIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkRCRDFDMjgwQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkI5Q0REM0UwQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6NGZkZTk4ZTUtMTdkMS00ZjdhLWE1NDYtMWVjNjk1MWNkMjFkIiBzdFJlZjpkb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6ZTE2ZmVkZDktZDVhNy1kYzQ3LWIzMzYtNzY5N2JiY2UyZDJjIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+GR8qLwAAAvVJREFUeNrMWE1IVFEUPmMJ5ZRkQmZFJLUInHIpmNXUxsxKF1JBEQZCVlYUWBlpZJAQtJAIFVpIRrQoCGmsiGiwsiKSFtrKGKygSKQfEYKS+k5zb29+muc9M28eHvh4982797xvzj33/DzPxD2aNjJTOH8BsBnwA4XAMiAb+A2MAyFgCAgCd4HPEuUeQ8usBY4DmwR/4CfQC1wA+k0WZEzxfDkQAPqALUJLZgKVwFOgByhIhcwu4LXallRlq9K1PRkyZ4FrwBwH/ZN96wZwWkKmBWhO04HxAOeAkyZkdgNNLpzi88BOOzIrgA6XQgpbqDPWqSNPxyXAa6LpGGZ2BuznvGgn8hVM6UNtwLZYy/hVDHFb+JStibVMg0TDw1fWuBrhMDc7fo53lrG6BhWL/kbgfFzfAzNMV3sjbOhAbuNIvYRTB29ThYRIGiRTuwiTWTcNErZfk1klWTXxwxqvx8qWrvC2FdWEx4OhpMgUap8Zw3W+6Sp+WfF++zmttUSHq0VkRrk8YcvMk6zKywmfIJZ98LbuRqLLRxAxF1pzGq8QPR8SkZmrLTNpUErESegjwmd+9PaV1BENfwrfn0Cwb64xVsebP5tJfEtmkyOJ6LhydId1fysoUjeuHXjEsRohyxprC5kaWpMZlJ4m3qL/yYdRa8z+JJA3mkyfZNVFlEdVcNoHL6N/53t2XC2lq0VkgtqBF+H6ziQK8wurmqLjzMqlRGPfiW4+jqhFcLL6O4zz0y9gMacD3R0ETGvdLjQgB9sSP2cit1vjHdxGelTh/q9V2cjJ2DhCfQX7Z0SPBiyLcOypLCUqKxZlbN0GPYntm3hU5nJOCqgWKK7srOfD4iIRji2HEtXAw8ABF8nU6fiSqDu4ynnOBSLcCl036ZtOqd4mXXImkf4MG+Z7HfYh1rVHNYniXhulEhUB9x0g0qt0dafyFeKtqk83qGM4KSDAc++okrJC6XLk+4wWTh3lnAkAH4BkQDnq2RdVAeiPRWwNUe7+I8AARDiqkQLMxlkAAAAASUVORK5CYII=) 연산자 선택, ![지시선 6](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA4dpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NzViZDMyNzctMzBhNS00ZGFjLWEyOTItYzZlNDYwMGIxNzhjIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkI5Q0REM0REQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkI5Q0REM0RDQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6YjQ0MDY0NmQtZDc5OS00MzcxLThkYTUtMTUzMWUyMTUyMTEzIiBzdFJlZjpkb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6Y2YxZjhkZDgtYTkwMy0yZTQ3LTk5ZWYtZWExODlhMGIyYzIyIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+iFZGSwAAAxtJREFUeNrMWF1IVEEUPmsJlREFGakRLfm2bj5E0IObm9HfWhQlEvSDQVBk9bZRUUkKBVEP1kMJhaIVPRSIuOoS0SYVWgRBWhCG5UPGFvQjC0JJfYed2Xt322v3tNelAx87y9xz7jdz5vzMdcV66L+R6cLnFwABwA94gCXAHOAXMAYMA4NABOgGohLjLps74wOOAhsEC/gBdAHngSd2FHL+Mr8UCAG9wCbhTuYCW4DHQAfgzoTMTuCFckumslnZqv4XMmeAG8BsB88nn63bwEkJmXrg9BQFjAtoAI7ZIbMLOJWFKD4L7JiMTDFwNUsphXeoKfVQm8lcBvIkFodHiS7dISqtgSKCPhAkakF2+fTV9hlqTJdnOIk9kBC594xoq4VDixdi2SC20mPLVJkK/8TOBCVE+gaTiZR7ifZXxkmwDH1EGM6ybS5oLgcFwHoJmfoWY3xuH9GRKuM/u6loPlGJ27a5gCozUSaDNdE0ya48fBkfV/mSibDUbBQf5lxVZlrZTaskmk9fm/LAOseiy6/d5JVovRs1HdRFxm59+ExUCPd4Uc3yZojJeDSZxRKtplCKw4OG23QkXaglWrtCRMatQ3vCRvVOCOcT84s5ctLJQDPeUGCbzDgwMydTZ9+/SMS5KtoeD28tbWG5LSbzTaKgcwnLzTojsfE5Ob7bmLsbEfEY02TeS7TWLLeey59rjK3cZ1VZNJkBiVbZMmP8ZiR5LjaefgdtyCtNplei5Ss1dWDNyQTC/cZ4u19EJqKjqRC/I5IszCm/ttGoS9UVRN9jODPXjGf6r9guCT+BIi4HumqHJL0u78b1zuSXm6W9QZRnOlTjnmghKjhKpaHIbUR3HxSfY2n58cjaVi4qkvoa9Cj13tQjrd4OSEhdgf7o9A6xB7JIhHPLYau2cwg4mEUyB3R+sbodtHK/lAUifBW6ZefedELdbaZK6qzs50zCfK/DZ4ht7VGXRPFdmztdzrdhB4h0KVttmXyFeKv609UqDCcEBPjZTtVSVipbjnyf0cKlg1tupDYqUV3iPDX3RXUA+mMR74aodv8WYACKXLbvvXLw3AAAAABJRU5ErkJggg==) 임계값을 입력해 이벤트 발생 조건을 설정하세요.
* 이벤트 대상 필터링![이벤트 대상 필터링](/img/set-event-filtering.png)

![지시선 7](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA4dpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NzViZDMyNzctMzBhNS00ZGFjLWEyOTItYzZlNDYwMGIxNzhjIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkE1Njk2NEFDQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkE1Njk2NEFCQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MGRiYzgxYTUtY2E4My00ODEwLTgzNmItYTgxYzU2OTk0MWZkIiBzdFJlZjpkb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6NGIzMzhlOTgtMjM4Ny03NjQxLWI3MTktMGIzNGQ2Yjg0MGE5Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+T+tVugAAAo1JREFUeNpi/LqDYdAAFhLViwGxFxA7ALE2ECsAMR8Q/wfiz0B8H4ivAvEBIN4OxK9IMZyRyJCxBeIyIPYgwQO/gXgbEHcB8TFiNDARkFcG4q1AfAiIfUgMSVYg9gfio0C8CYgVKXFMNBBfgEYLpcAXalYYOY5pBOIlQMxDxfQJSlsrgLiGFMc0AXEdjTIMIxA3A3EFMY6JAeJaOuTiNiCOwOcYFSCeQaciBRRCM9ETNXLumAzE3PhMuAIsRcwzibfx5HQGBh1FvGloIhD7oYeMA7QMoTcA5TJr9JApJUYnNwcDQ7o3bvkbjxgYDl6GsEOAxaSiJFEOKoWWReASGKTlMRAzU+LFrz8YGEJrEY65Mp9ox4BKahlQ1QGKJm9KHQICO08iHLK4kmiHwEpqD1iasaPUIa8/MDDEtkPY9roMDO7mJBvhAHOMLqWOWb4HwS4Mg6QtEoE2zDFylIZK5RxoQSXBwOBqSpYxijDHCFDimMMXEexkH7KN4SWmCUEQbDyCYGvKU2YWyDEfKYmiNYcRfANVst3xGeaYh+SacPcpKl+U/Ai/D3PMFXJNePYGwcZXMhMBrsEcc4hcE67cp1oddQDmGFAb9y85Jnz4jGArSJLtkD/QngTYMc9ApTk5poAqRhiQESXbMdtgXRpY1u4lxxRYXUQh6MbWbwKx3OncntkK7QJhNDtzQC0BOjoElOJycbWB7wBxFh0dkwErX3D1DhYBcTsdHALqCi0jpt9UBe3b0ArU4zKfCY/LE6mchkBmxUE7iST3tRcAsT65ZRCWsgRk1mJKRiHuQtunjmSU1CC1W6BNSm+oWVQZn4EBKSD2BDV1gVgH2koUhMq9h7YAYINFoNB4QYrhAAEGAJZYiElVcF/5AAAAAElFTkSuQmCC) 태그, ![지시선 8](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA4dpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NzViZDMyNzctMzBhNS00ZGFjLWEyOTItYzZlNDYwMGIxNzhjIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkE1Njk2NEI0QjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkE1Njk2NEIzQjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MGRiYzgxYTUtY2E4My00ODEwLTgzNmItYTgxYzU2OTk0MWZkIiBzdFJlZjpkb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6NGIzMzhlOTgtMjM4Ny03NjQxLWI3MTktMGIzNGQ2Yjg0MGE5Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+6nJs2gAAAx5JREFUeNrMWFtIVFEU3WP1kyU9QLKPHjQ/YdZXUFCNBdHoTCQhFRRBJBTSAwMje0kGCUFERVTkR2VFgUWIY1ZUavaQCIK0L2PqK1GihxhBRa3tPWfumXFmOtsZhzYs5sB5zLr77rP23tcz2EL/jY0Vrs8FioFCIB+YBeQAf4ABIAx0A63AXaBPcrjH0jNLgb2AX/AAP4Fm4DjwzGZD1j/m5wAhoB0ICj05DlgDPAUagdmpkNkIvFavJVVbrc5aNxIyR4CrwIQ0xifH1g3goIRMDXB4lC6MBzgK7LMhswk4lIFbfAzYkIyMFzifIUlhD12IDWqTzBkg2/a0By+J9mBHtt9FzSWiF92iGDoVT2dYxB7bnDD4A+/xIh4rlHhNbRnRrlJrUkvU9Y94ptJ2571Ol4h3GtHZ3UT1VQ4BbVV1RF1hazKVZjrIA1bZ7qxrcsfXqonmGW997kyiEhX+j15FzyWxYpVm+tgzAWCMLZm2N+449s9WLnTH7z+KlNqvX9MyyTXwFUQHsWn9X9zxfK/odhVqMgWSXRWGoPMrud3mkgg9d2MpsFhEJl/fpk/4nSLZebrBCVLTSpHXG544RO7UQkDyRGT6OW7YM5OkirU16PypaUxEz+VOFovgRJsSIq7OlJ8g6ul1CPG1Zq+Y15rneZ3UmMxXyQbWGe0FvtprfUSXDxB1nnO9xfO8TmADmswHyS6tM+wN82rzmMnF0yMLC2syXZJdWmem5gyfM8mZemRhbzWZ9pHoDKeEcIywmSnAJxKMoQJ+KB1wpvltq8JlQfepSxC8FeuRfscTfftOdPJm9DpL+6U6iUjWDklq3Xg6k0LWblSFe4TMCuChxK9ct9xHOrjV6lxztm3IckWLonOUZRvUEds3tUiyd5ospFqgYZXeDta0DBJhbdmZqOzsAcozSGa71pdE3cEVjr8MEOFW6LpN37Rf9TajZdWJzs9KwnxLmmOIz9qsmkRxr43GgxZwbkwDkWZ1Vn0qXyHeqfp0uaHUtsZrm1RJGVBnpeX7jLbpQBGnHs6LwAxAl1KfVQWgPxaxN3olh/8VYACrOccoocIl+QAAAABJRU5ErkJggg==) 연산자 선택, ![지시선 9](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA4dpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NzViZDMyNzctMzBhNS00ZGFjLWEyOTItYzZlNDYwMGIxNzhjIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkI5Q0REM0Q5QjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkI5Q0REM0Q4QjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MGRiYzgxYTUtY2E4My00ODEwLTgzNmItYTgxYzU2OTk0MWZkIiBzdFJlZjpkb2N1bWVudElEPSJhZG9iZTpkb2NpZDpwaG90b3Nob3A6NGIzMzhlOTgtMjM4Ny03NjQxLWI3MTktMGIzNGQ2Yjg0MGE5Ii8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+Y7L9UwAAAx1JREFUeNrMmG1Ik1EUx89WQWEEQUQaiKMIYkYfohr0torQuaygiMCIRkHR6ycjoxITEoI+VAQGfZAWEb0h0TYjymlWggSVFn1QRlH2YvSCCEFJ/Y+71+fZavOeNkcHfnjndu/+O+eec899HANN9N/YWOHnp4Iy4AVuUAQmgV+gH8TAcxAFEfBRsrjD0DNLwAFQKvgBP0AYnAAPTSY4R3h/BgiBVrBa6MlxYC14AG4CVyZiKsATFZZMrVyttfFfxNSAi2BiFvcn763L4LBEzDFwdJQSxgFqwUETMZvBkRxk8XGwKZ2YmaA+RyWFPXQueVPbs+MMyDNdrQsV5UYLUTuqyts+opXziHweolXzRXvoFFiTXGe4iDWbrnKng2hdimDWbSfahiKQN95Y1GKV/sNhqpR4xC6Ev/zsfsR4Wvx11Xmiq82ikFXa90w+KDGdyaHRFqwi2reBaKsPJbbeErQbzu/7aiymTB0zQ2L8YIzpzOtRa1yy0BpzWKoD1uv7T0WVulSLWSrxaff7RAF2m1VojdueiULl1WLmSGbpULClC8XdxyIxbi2mUDJrvde2eYNEA9/jY07xipq/e9DAXDq1Bw1O72GLvSMqDqT2ml2EoHHjnzTBKS2dLuReY21iuNiWIdiNdZl3et/AZMkkrrKcyp09RL2fiAqmEHncca9p2+EX6ejXYl5JxehM8riTMu2NNS7KFy0X0xu4K1unX6TdGi+YLZr6QotplX4pn00NkcT/nb6GYzhk7Z9kr41gUZ1NBfj72rQK27OJNzGf1i8xu6XTVmNOisT8BNP5JsF7phfcNu11P3y2UniIUOL7nGlCr4T1lUa3ECv4B5nO5sobekR05V7cIyyO24byRfHUFxpfg9qS701NktM7SxZSV6A/2s49XDRzKIRry95UPXA32JVDMTt1fUl1O7jA518OhPBV6JLJvemQutuMllWnWt+ZRnkgy3uI19qiLoniu3YDmKtqUKYWVmsFM3kK0aP60+UqDQcFAvizt1RL6VdrZeX5jDY+Onx8/IBi1SXqE/+L6gD0wyL2hqjf+y3AAP/bwhIWOJrvAAAAAElFTkSuQmCC) 필터링값을 입력해 대상을 필터링합니다. 입력값이 없을 경우 전체 에이전트를 대상으로 경고 알림을 보냅니다.

노트* 이벤트 발생 조건과 이벤트 대상 필터링에서 사용할 수 있는 기본 문법과 연산자 목록은 [다음 문서](#condition-guide)를 참조하세요.
* 이벤트 발생 조건과 이벤트 대상 필터링 옵션은 선택 입력 또는 직접 입력 옵션을 선택할 수 있습니다.
* 이벤트 설정 내용이 저장된 이후에는 해당 옵션값은 직접 입력 옵션으로 관리합니다. 이후 선택 입력 옵션으로 전환하면 옵션값이 초기화될 수 있습니다.
* 이벤트 발생 조건과 대상 입력 시 특수 문자(`~!@#$%^&*()_+=-[]``)를 포함하거나 숫자로 시작하는 필드명을 입력하면 오류가 발생할 수 있습니다. 이런 경우 직접 입력 옵션을 선택한 다음 예시와 같이 중괄호(`$`)로 묶어서 입력하세요.


```
${4xxErrorType} == '401'  

```
### 이벤트 수신 설정[​](#set-receive-event "이벤트 수신 설정에 대한 직접 링크")

![이벤트 수신 설정](/img/set-event-receive.png)

* 발생 횟수: 선택한 시간 동안 이벤트 발생 조건에서 설정한 이벤트가 입력 횟수만큼 발생하면 경고 알림을 보냅니다.

노트
	+ 선택 시간을 사용 안 함으로 설정하면 입력한 횟수만큼 연속 발생할 때 알림을 보냅니다.
	+ 이벤트 상태가 해결되면 추가 알림 옵션을 활성화한 경우 선택 시간은 사용 안 함으로 선택할 것을 권장합니다.
	+ 카테고리 옵션에서 선택한 항목의 수집 주기는 5초입니다.
* 이벤트 발생 일시 중지[​](/java/metric-warning-notice#scrollTo-event-pause): 과도한 경고 알림 발생을 방지할 수 있는 옵션입니다. 첫번째 경고 알림 이후 선택한 시간 동안 경고 알림을 보내지 않습니다. 또한 이벤트 기록 메뉴에 기록되지 않습니다.
* 관련 카테고리: 관련 카테고리를 5개까지 설정하고 알림 조회 시 참조합니다.
* 이벤트 수신 태그: 이벤트 수신 태그를 선택하면 해당 태그를 가진 프로젝트 멤버와 3rd-party 플러그인에 알림을 전송할 수 있습니다. 이벤트 수신 태그를 선택하지 않으면 프로젝트 전체 멤버에게 경고 알림을 보냅니다.

노트경고 알림 > 이벤트 수신 설정 메뉴에서 프로젝트 멤버와 3rd-party 플러그인에 태그를 설정할 수 있습니다.

### 알림 규칙 테스트[​](#알림-규칙-테스트 "알림 규칙 테스트에 대한 직접 링크")

![경고 알림 테스트](/img/set-event-test.png)

선택한 시간 동안 설정한 이벤트 조건을 실행해 몇 번의 경고 알림이 발생했는지 확인할 수 있습니다. 실행 버튼을 선택하면 알림 발생 건수 정보를 알 수 있으며, 이벤트 발생 조건에서 선택한 필드와 임계치를 차트상에 표시합니다.

복합 메트릭스 이벤트[​](#복합-메트릭스-이벤트 "복합 메트릭스 이벤트에 대한 직접 링크")
----------------------------------------------------

복합 메트릭스 이벤트를 이용하려면 다음의 개념에 대한 이해가 필요합니다.

* [메트릭스란?](/java/metrics-intro)

* [MXQL](/mxql/mxql-overview)

복합 메트릭스 이벤트는 메트릭스 데이터에 보다 복잡한 규칙을 활용해 이벤트를 생성하고 경고 알림을 보낼 수 있습니다. 복합 메트릭스은 다음과 같은 상황에서 효과적으로 사용할 수 있습니다.

* 여러 에이전트에서 수신된 데이터에 대해 종합적인 이벤트 판정을 해야할 때
* 과거 데이터와 현재 데이터를 비교해 이벤트 판정을 해야할 때

메트릭스 이벤트는 에이전트로부터 메트릭스를 수신할 때마다 이벤트 판정을 합니다. 반면, 복합 메트릭스 이벤트는 각 에이전트에서 수집한 메트릭스들을 데이터베이스에 저장합니다. 그리고 다시 조회해서 이벤트 판정을 합니다. 이와 같은 특성 때문에 여러 에이전트의 데이터를 종합적으로 활용하거나 과거의 데이터를 활용할 수 있습니다. 하지만 **MXQL**이라는 와탭 고유의 데이터 조회 언어를 사용해야한다는 진입장벽이 존재합니다. 따라서 사용자들이 기초적인 **MXQL**만 이해하더라도 효과적으로 이벤트를 설정할 수 있도록 이벤트 템플릿을 제공합니다. MXQL 기초 사용자는 이벤트 대상 필터링과 이벤트 조건에 대한 쿼리만 수정해서 이벤트를 적용할 수 있습니다.

1. 경고 알림 > 이벤트 설정 메뉴에서 화면 위에 메트릭스를 선택하세요.
2. 복합 메트릭스 섹션에서 오른쪽에 이벤트 추가 를 선택하세요.
3. 복합 메트릭스 창이 나타나면 차트로 생성하기를 선택하세요.

이벤트 설정 창이 나타납니다.

![복합 메트릭스 이벤트 설정](/img/set-event-cmetric.png)

노트복합 메트릭스 이벤트를 설정하려면 **이벤트 설정** 권한이 있어야 합니다.

노트복합 메트릭스에 이벤트 템플릿에 대한 자세한 내용은 [다음 문서](#composite-metrics-template)를 참조하세요.

### 이벤트 데이터 조회[​](#이벤트-데이터-조회 "이벤트 데이터 조회에 대한 직접 링크")

복합 메트릭스 이벤트는 메트릭스 데이터 질의 언어인 **MXQL**을 기반으로 이벤트 조건을 생성합니다. 차트로 생성하기 기능은 **MXQL**의 자동완성을 위한 콤보박스 기능을 제공합니다. 이벤트 데이터를 조회하여 차트를 구성한 다음 이벤트 발행 조건을 직접 입력하기 위한 템플릿입니다. 위젯 또는 텍스트 옵션을 선택해 이벤트를 설정하세요.

* 위젯
* 텍스트

시계열 차트를 구성하는 옵션을 통해 이벤트 설정 시 사용할 **MXQL**을 자동완성할 수 있습니다.

![이벤트 데이터 조회](/img/set-event-data-view.png)

* 필터: 이벤트 조건 대상을 선택합니다. ![](/img/number-01.png) 연산식, ![](/img/number-02.png) 태그, ![](/img/number-03.png) 필터링값을 입력해 필터링 조건을 생성합니다.

![필터](/img/set-event-cmetric-filter.png)
* 그룹화: 그룹화된 메트릭스 데이터를 선택합니다. 다중 선택할 수 있습니다.
* 타임 유닛: 그룹화된 데이터를 나눌 시간 기준을 설정합니다. 초, 분, 시간 단위로 선택하고 설정할 수 있습니다.
* 필드: 이벤트 발행 조건에 사용할 필드를 선택합니다. 다중 선택할 수 있습니다.
**MXQL**을 평문 그대로 수정할 수 있는 편집창이 나타납니다.

![메트릭스 이벤트 - 텍스트](/img/set-event-metrics-text.png)

### 알림[​](#알림 "알림에 대한 직접 링크")

경고 알림 설정의 기본 정보를 입력합니다.

* 이벤트 활성화: 토글 버튼을 클릭해 이벤트를 활성활 여부를 선택할 수 있습니다.
* 레벨: 위험(Critical), 경고(Warning), 정보 수준 중 하나의 레벨을 선택하세요.

이벤트 상태가 해결되면 추가 알림: 이벤트 항목 중 발생한 이벤트 상태가 해결되면 추가 알림 송신 여부를 선택할 수 있습니다. 토글 버튼을 선택해 기능을 켜거나 끌 수 있습니  다.
* 제목: 경고 알림의 제목을 입력하세요.
* 메시지: 이벤트 발생 시 출력하는 알림 메시지를 입력합니다. `${Tag}` 또는 `${Field}` 입력으로 메시지에 변수를 적용할 수 있습니다. 변수에 입력할 키는 선택한 메트릭스 데이터 카테고리에 포함된 값이여야 합니다. 메트릭스 조회 메뉴에서 입력할 수 있는 태그 또는 필드키를 확인할 수 있습니다.

![Message example](/img/event-config-message-example.png)

### 알림 정책[​](#알림-정책 "알림 정책에 대한 직접 링크")

경고 알림을 보낼 조건을 입력합니다.

* 데이터 조회 범위: 이벤트 조건에 사용할 **MXQL**의 실시간 데이터 조회 범위를 설정합니다. 이벤트 데이터 조회에 포함된 필드만 사용할 수 있습니다.

복합 메트릭스 이벤트는 DB에 저장된 메트릭스를 조회해서 활용합니다. 따라서 데이터를 조회할 시간 범위를 먼저 지정해야 합니다. 데이터 조회 시간을 5분으로 선택하면 최근 5분동안 수집된 데이터를 조회해서 이벤트 발생 조건을 확인합니다. 최근 데이터에 대해서 이벤트를 설정할 때에는 짧게, 넓은 시간에 대해서 통계적으로 접근하고 싶을 때에는 길게 설정할 수 있습니다.

노트실제 사용 예시는 [다음 문서](#template)를 참조하세요.
* 조건: MXQL에 반영한 필드와 연산 규칙, 임계치를 입력합니다.

### 부가 정보[​](#부가-정보 "부가 정보에 대한 직접 링크")

경고 알림 수신과 관련한 부가적인 옵션을 설정합니다.

* 인터벌: 선택한 시간 간격으로 알림 조건을 확인합니다.
* 무음: 과도한 경고 알림 발생을 방지할 수 있는 옵션입니다. 첫번째 경고 알림 이후 선택한 시간 동안 경고 알림을 보내지 않습니다. 또한 이벤트 기록 메뉴에 기록되지 않습니다.
* 이벤트 수신 태그: 이벤트 수신 태그를 선택하면 해당 태그를 가진 프로젝트 멤버와 3rd-party 플러그인에 알림을 전송할 수 있습니다. 이벤트 수신 태그를 선택하지 않으면 프로젝트 전체 멤버에게 경고 알림을 보냅니다.

노트경고 알림 > 이벤트 수신 설정 메뉴에서 프로젝트 멤버와 3rd-party 플러그인에 태그를 설정할 수 있습니다.

### 이벤트 규칙 테스트[​](#이벤트-규칙-테스트 "이벤트 규칙 테스트에 대한 직접 링크")

![이벤트 규칙 테스트](/img/set-event-cmetric-test.png)

선택한 시간 동안 설정한 이벤트 조건을 실행해 몇 번의 경고 알림이 발생했는지 확인할 수 있습니다. 실행 버튼을 선택하면 알림 발생 건수 정보를 알 수 있으며, 이벤트 발생 조건에서 선택한 필드와 임계치를 차트상에 표시합니다.

이벤트 설정에 포함된 대부분의 내용들이 **MXQL**을 사용해서 지정됩니다. **MXQL**이 적절하게 작성되었는지 시뮬레이션할 수 있는 기능을 제공합니다. 시뮬레이션 기능은 과거의 24시간 데이터를 조회해서 이벤트 판정을 한 다음 몇 건의 메트릭스가 조회되었고 그 중 몇 건에서 이벤트 판정이 성공했는지 알려줍니다.

메트릭스 이벤트 수정 및 삭제[​](#메트릭스-이벤트-수정-및-삭제 "메트릭스 이벤트 수정 및 삭제에 대한 직접 링크")
-------------------------------------------------------------------

1. 경고 알림 > 이벤트 설정 메뉴로 이동한 다음 메트릭스 탭을 선택하세요.
2. 이벤트 목록에서 수정 또는 삭제하려는 항목의 가장 오른쪽에 ![편집 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZWRpdDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02OC4wMDAwMDAsIC0xMzk1LjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iZWRpdG9yLWljb25zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MC4wMDAwMDAsIDEzNTAuMDAwMDAwKSI+CiAgICAgICAgICAgICAgICA8ZyBpZD0iaWMtZWRpdCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjguMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTIwLDE4IEwyMCwyMCBMMCwyMCBMMCwxOCBMMjAsMTggWiBNMTIuOTM5MzM5OCwxIEwxNy45MzMyMTA4LDYuMDA2NDA3NzggTDE3LjkwMSw2LjAzOCBMMTcuOTAzNzA4NSw2LjA0IEw4LjAwNDIxMzU2LDE1LjkzOTQ5NDkgTDgsMTUuOTM1IEw4LDE1Ljk0IEwzLDE1Ljk0IEwzLDEwLjk0IEwzLjAwNSwxMC45NCBMMywxMC45MzU1MzM5IEwxMi44OTk0OTQ5LDEuMDM2MDM4OTcgTDEyLjkwMSwxLjAzOCBMMTIuOTM5MzM5OCwxIFogTTEyLjkzNSwzLjgyOCBMNSwxMS43NjMgTDUsMTMuOTQgTDcuMTc1LDEzLjk0IEwxNS4xMDgsNi4wMDYgTDEyLjkzNSwzLjgyOCBaIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하세요.
3. 메트릭스 또는 복합 메트릭스 이벤트 설정 창이 나타나면 각 옵션을 수정한 다음 저장 버튼을 선택하세요.

선택한 이벤트를 삭제하려면 이벤트 설정 창의 오른쪽 위에 ![삭제 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIwIDIySDRWNmgydjE0aDEyVjZoMnYxNnptMi0xOGgtNWwtMS4xNDMtMkg4LjE0M0w3IDRIMnYyaDIwVjR6IgogICAgZmlsbD0iIzc1NzU3NSIgLz4KICA8cGF0aCBkPSJNOSA4aDJ2MTBIOVY4ek0xMyA4aDJ2MTBoLTJWOHoiIGZpbGw9IiM3NTc1NzUiIC8+Cjwvc3ZnPg==) 삭제 버튼을 선택하세요.

발생 조건, 대상 선택 가이드[​](#condition-guide "발생 조건, 대상 선택 가이드에 대한 직접 링크")
------------------------------------------------------------------

메트릭스 경고 알림의 이벤트 발생 조건과 이벤트 대상 선택은 동일한 문법을 사용합니다. 단, 이벤트 발생 조건은 태그(Tag)의 Key를 변수로 사용하고, 이벤트 대상 선택은 필드(Field)의 Key를 변수로 사용합니다.

### 기본 문법[​](#기본-문법 "기본 문법에 대한 직접 링크")

* 문자열을 그냥 입력하면 변수, 작은 따옴표('') 또는 큰 따옴표("")로 감싸면 text로 인식합니다.

oid == "oid"
```
1. oid : 변수  
2. == : 함수  
3. "oid" : text  

```

```
// oname가 ott-1235일 경우  
  
// 정상적인 경우  
onname = 'ott-1235' 또는 onname = "ott-1235"  
  
// 비정상적인 경우, 알림이 동작하지 않습니다.  
onname = ott-1235  

```
* 숫자를 그냥 입력하면 number, 작은 따옴표('') 또는 큰 따옴표("")로 감싸면 text로 인식합니다.

oid == 123
```
1. oid : 변수  
2. == : 함수  
3. 123 : number  

```

```
// oid가 123일 경우  
  
// 정상적인 경우  
oid = 123  
  
// 비정상적인 경우, 알림이 동작하지 않습니다.  
id == '123' 또는 oid == "123"  

```

### 사용 가능한 연산자 목록[​](#사용-가능한-연산자-목록 "사용 가능한 연산자 목록에 대한 직접 링크")



| 연산자 | 사용법 | 설명 |
| --- | --- | --- |
| == | operand1== operand2 | operand1과 operand2의 값이 동일한지 확인합니다. |
| != | operand1 != operand2 | operand1과 operand2의 값이 다른지 확인합니다. |
| > | operand1 > operand2 | operand1의 값이 operand2의 값보다 큰지 확인합니다. |
| >= | operand1 >= operand2 | operand1의 값이 operand2의 값보다 큰거나 같은지 확인합니다. |
| < | operand1 < operand2 | operand1의 값이 operand2의 값보다 작은지 확인합니다. |
| <= | operand1 <= operand2 | operand1의 값이 operand2의 값보다 작거나 같은지 확인합니다. |
| like | operand1 like operand2 | operand1에 operand2가 포함되어 있는 지를 패턴으로 검색합니다. |
| && | expression1 && expression2 | expression1과 expression2이 모두 `true`인지 확인합니다. |
| and | expression1 and expression2 | expression1과 expression2이 모두 `true`인지 확인합니다.\*\*&&\*\*와 동일한 역할을 수행하는 연산자입니다. |
| || | expression1 || expression2 | expression1 또는 expression2이 `true`인지 확인합니다. |
| or | expression1 or expression2 | expression1 또는 expression2이 `true`인지 확인합니다.\*\*||\*\*와 동일한 역할을 수행하는 연산자입니다. |

#### like 사용법[​](#like-사용법 "like 사용법에 대한 직접 링크")

와일드카드(`*`)를 통해 포함 문자열을 편리하게 검색할 수 있습니다.

* 특정 키워드로 시작하는 문자열 검색


```
  
Key like "Value*"  
  

```
* 특정 키워드로 끝나는 문자열 검색


```
  
Key like "*Value"  
  

```
* 특정 키워드가 포함된 문자열 검색


```
  
Key like "*Value*"  
  

```
* 키워드 중간에 와일드카드(`*`)를 사용할 수 없습니다.


```
  
// 지원하지 않는 문법  
Key like "Va*lue"  
  

```
* `like` 연산자에서 와일드카드(`*`)를 생략하는 경우 equals(`==`)로 동작합니다.


```
  
// 아래의 두 문장은 완전히 같은 결과를 가집니다.  
Key like "Value"  
Key == "Value"  
  

```

### 사용 가능한 함수 목록[​](#사용-가능한-함수-목록 "사용 가능한 함수 목록에 대한 직접 링크")



| 함수 | 사용법 | 설명 |
| --- | --- | --- |
| [startsWith](#startwith) | startsWith(param1, param2) | param1을 Key로 하는 Value가 param2로 시작하면 `true`, 반대의 경우 `false` |
| [endsWith](#endswith) | endsWith(param1, param2) | param1을 Key로 하는 Value가 param2로 끝나면 `true`, 반대의 경우 `false` |
| [isNull](#isnull) | isNull(param1) | param1이 `null`이면 `true`, 반대의 경우 `false` |
| [isNotNull](#isnotnull) | isNotNull(param1) | param1이 `null`이 아니면 `true`, 반대의 경우 `false` |
| [isEmpty](#isempty) | isEmpty(param1) | param1이 `null` 또는 `EmptyString("")`이면 `true`, 반대의 경우 `false` |
| [isNotEmpty](#isnotempty) | isNotEmpty(param1) | param1이 `null`도 아니고 `EmptyString("")`도 아니면 `true`, 반대의 경우 `false` |

#### startsWith[​](#startwith "startsWith에 대한 직접 링크")


```
startsWith(Key, "Value")  

```
#### endsWith[​](#endswith "endsWith에 대한 직접 링크")


```
endsWith(Key, "Value")  

```
#### isNull[​](#isnull "isNull에 대한 직접 링크")


```
isNull(Key)  

```
#### isNotNull[​](#isnotnull "isNotNull에 대한 직접 링크")


```
isNotNull(Key)  

```
#### isEmpty[​](#isempty "isEmpty에 대한 직접 링크")


```
isEmpty(Key)  

```
#### isNotEmpty[​](#isnotempty "isNotEmpty에 대한 직접 링크")


```
isNotEmpty(Key)  

```
템플릿[​](#template "템플릿에 대한 직접 링크")
---------------------------------

### 메트릭스 이벤트[​](#메트릭스-이벤트 "메트릭스 이벤트에 대한 직접 링크")

***경고 알림*** > ***이벤트 설정*** > ***메트릭스*** 섹션에서 ***+ 이벤트 추가*** 버튼을 선택하세요. ***템플릿***에서 원하는 항목을 선택하세요.

* ***WARNING\_OLD\_GENARATION\_GC***

힙 메모리(Heap Memory)의 Old Generation 영역에서 GC가 발생하면 경고 알림을 보냅니다.
* ***TOO\_SLOW\_SQL***

수행 중인 쿼리가 5초 이상으로 너무 느린 쿼리가 발생할 경우 경고 알림을 보냅니다.
* ***TOO\_MANY\_ACTX***

8초 초과 구간의 액티브 트랜잭션 수가 너무 많을 경우 경고 알림을 보냅니다.
* ***APDEX***

**APDEX** 수치가 0.7보다 작을 경우 경고 알림을 보냅니다.

### 복합 메트릭스 이벤트[​](#composite-metrics-template "복합 메트릭스 이벤트에 대한 직접 링크")

* ***Inactive agents has been found.***

조건: `num_of_current_agents` < 6

프로젝트에 포함된 모든 에이전트 중 정상 상태의 에이전트 수가 6개 미만으로 떨어지는 이벤트가 발생하면 경고 알림을 보냅니다.
* ***Very slow active transactions detected.***

조건: `very_slow_tx_cnt_m5_avg` > 10

프로젝트에 포함된 특정 `okind`에 속한 에이전트에서 8초 이상 소요되는 트랜잭션의 수의 합이 10개 초과 발생하면 경고 알림을 보냅니다.
* ***TPS has changed by more than 30% compared to the previous week.***

조건: `one_week_diff_abs` > `current_tps` \* 0.3

프로젝트에 포함된 특정 `okind`에 속한 에이전트들의 TPS합이 7일 전과 비교했을 때 30% 초과 달라지면 경고 알림을 보냅니다.

여러 에이전트에서 수신된 데이터에 대해서 종합적 이벤트 판정해야할 때 다음의 복합 메트릭스 템플릿을 설정하세요.

* ***Inactive agents has been found.***
* ***Very slow active transactions detected.***

과거 데이터와 현재 데이터를 비교해서 이벤트를 판정해야할 때 다음의 복합 메트릭스 템플릿을 설정하세요.

* ***TPS has changed by more than 30% compared to the previous week.***
