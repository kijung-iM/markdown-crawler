에이전트 설정
=======

와탭 에이전트는 에이전트 별 필요한 설정을 *whatap.conf* 파일에 작성합니다. 에이전트는 환경변수를 통해 설정 파일의 위치를 파악하고 로딩합니다.

별도 설정이 없는 경우 에이전트는 자기 자신(*whatap.agent-X.Y.Z.jar*)이 위치한 디렉터리에서 *whatap.conf* 파일을 찾도록 구현했습니다. 5초에 한번씩 *whatap.conf* 파일의 변경 여부를 체크하고 리로딩합니다.

사용자의 편의성을 위해 [와탭 모니터링 서비스](https://service.whatap.io)에서도 에이전트 설정 기능을 제공하고 있습니다.

기본 설정[​](#기본-설정 "기본 설정에 대한 직접 링크")
----------------------------------

whatap.conf
```
whatap.home=.  
whatap.config=whatap.conf  

```
* `whatap.home`: 기본값은 *whatap.agent.jar* 파일의 경로를 입력하세요.
* `whatap.config`: 파일명만 입력할 것을 권고합니다. 상대 패스를 같이 입력할 수는 있습니다.

에이전트가 데이터를 수집하고, 서버로 데이터를 전송하기 위해서는 최소한 액세스 키와 서버 주소는 설정돼 있어야 합니다.

whatap.conf
```
license=x220g160hgd29-x3qpff0garcus7-z4p0kao58un11a  
whatap.server.host=10.10.0.1  

```
와탭 에이전트는 최초 실행시 다음과 같이 어떤 jar 파일이 에이전트로 사용됐는지, 어떤 경로에서 *whatap.conf* 파일을 로딩하는지 확인할 수 있습니다.

![Java start screen](/assets/images/set-java-agent-start-beae520c7b8c4c9087af6797dfc5779d.png)

서버 연결 및 데이터전송[​](#서버-연결-및-데이터전송 "서버 연결 및 데이터전송에 대한 직접 링크")
----------------------------------------------------------

와텝 에이전트는 *whatap.conf* 파일에 설정한 서버 주소로 연결합니다.

whatap.conf
```
whatap.server.host=10.10.1.1  
whatap.server.port=6600 # 기본값  

```
* TCP 세션을 연결하면 `license`를 이용해 서버로부터 통신키를 전달 받습니다. 잘못된 `license`를 설정하면 서버는 세션을 종료합니다.
* TCP 연결이 반복적으로 종료되면 방화벽 문제 확인하거나 `license` 값이 올바른지 확인하세요.
* TCP 세션을 연결하면 서버로부터 받은 비밀키를 기반으로 보안 통신으로 데이터를 전송합니다.

여러 애플리케이션 서버의 설정 파일 관리[​](#여러-애플리케이션-서버의-설정-파일-관리 "여러 애플리케이션 서버의 설정 파일 관리에 대한 직접 링크")
-------------------------------------------------------------------------------------

한 서버에 여러 애플리케이션을 운영할 경우, 각 애플리케이션 별 설정 파일을 별도로 관리하려면 *whatap.conf* 파일명을 변경하고 시작 스크립트에 JVM 옵션을 추가하세요.

Service A
```
-Dwhatap.config=whatap_Aservice.conf  

```
Service B
```
-Dwhatap.config=whatap_Bservice.conf  

```
주의*whatap.conf* 설정 파일은 반드시 `${WHATAP_HOME}` 경로에 위치해야 합니다.

서비스 화면에서 에이전트 설정하기[​](#set-agent-service "서비스 화면에서 에이전트 설정하기에 대한 직접 링크")
------------------------------------------------------------------------

홈 화면 > 프로젝트 선택 > ***관리*** > ***에이전트 설정***

모니터링 대상 서버에 위치한 *whatap.conf* 파일을 직접 수정하  지 않고 [와탭 모니터링 서비스](https://service.whatap.io)에서 에이전트 설정 옵션을 추가하거나 수정, 삭제할 수 있습니다.

노트* 이 기능은 **수정** 권한을 가진 멤버만 이용할 수 있습니다. **수정** 권한이 없는 멤버는 설정 내용을 조회만 할 수 있습니다.
* 옵션 값으로 설정할 수 있는 형식은 다음과 같습니다.


	+ Boolean 형식의 값은 `true` 또는 `false`를 선택하세요.
	+ 숫자 형식의 값은 숫자만 입력할 수 있습니다.
	+ 텍스트(String) 형식의 값을 입력 또는 수정할 경우 옵션 셜명을 자세히 확인하세요.
* 수정할 수 없는 옵션은 선택할 수 없습니다. (예, `license`)
* 추가 또는 수정, 삭제한 옵션에 따라 에이전트를 재시작해야할 수 있습니다.
* 애플리케이션 종류 및 에이전트의 버전에 따라 적용할 수 있는 옵션 키는 다를 수 있습니다.
### 옵션 추가하기[​](#옵션-추가하기 "옵션 추가하기에 대한 직접 링크")

![에이전트 설정](/img/app-set-agent-in-service-java.png)

1. ***에이전트 목록***에서 옵션을 추가하려는 ![숫자 1](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3lpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6Yzg0YmZlYjgtYTgzZS00NTU3LWFiNGYtODQ3ZTFjMGQ5MjNlIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjA3QTM1RTJEQjU2QjExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjA3QTM1RTJDQjU2QjExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6OTZlMmZhMDktMjhmZS00ZGUxLTg3NGQtNDQwYjgxNTBmMzI4IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOmM4NGJmZWI4LWE4M2UtNDU1Ny1hYjRmLTg0N2UxYzBkOTIzZSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Ppgo9sAAAAJPSURBVHjazJhNSBtBGIYnNiejFDwIzUEbKh5U0FsPWqOFSlTw5EFEpbeSgxdRUZFSi4rgMZS0p2KrICKiWIN6kPgH7cnfgAcl6EEhCErbQKGV9v3MDG6XxMwmu5t94cGom+Fhdubbb9YWXWZa4gQNoBqUgQKQB/6CK3AKQmAdBMCFlsFtkjK1oBe8AA8kx74BNPo4l0uarCT/LwIrYA14NIgwfm0jCIIl8CQdmZdgF9Sx9EO3dg+0a5WxgWHwETiYfqGxPoHXiS6wx/nbKOhjxmWI/3ybbGY6DBZRCrXeJ0OL1c/My3vgSiTzDmSbKJMLfPFknmvZNdFfjM2hcpRjvzk8MVIMbf1n6gXcLfPNr6it/nnGZjd1naEesClmxik7K+eXuotQ6kG+mJlG2cpajCfR5/7Y5619xj4s6SJj50IT9MEt+60yVwwRnWQoNSRDt6mUZT4lYs0UWkDGJWQeWkAmV6aFMDUkc20Bjx9C5swCMmEhc2ABmZCQ2bCATFDIUOn6k0GR37xxvy3FdJxY5X1q4puKq3yzd78fqVZal6IZ6GxG4XgkLUOTEVEeVdxiqhLlEEvsqVdu9G/+/x8bSVIFtpV1Zl1MlclZFCLqQxy1nTsgxySR76BCbGt1BT4GXpNE6Dj8SikS73EwqThKGJkBMC1ziHtjoBDNyCAY03K8JaE28FPnNdICRlI5a0/xBRbQadfQWDPpvIU44T0yvY/5orFSU2VdAJWgSb1Y03k/I5LPK7Wbt6uPRWPE24Awf+gFed2KGPGyyJT8E2AAc7l5zWfLLegAAAAASUVORK5CYII=) 에이전트를 선택하세요.
2. ![숫자 2](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3lpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6NjVlMjMwYmYtMTI4OS00ODUyLWE3NjYtZDU2NzhlZjdkZWE5IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjA3QTM1RTI5QjU2QjExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjA3QTM1RTI4QjU2QjExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6ZWUyNmRlM2EtZTU1MS00YTNhLTg5ODUtNTliOTQzOTNkMTg0IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjY1ZTIzMGJmLTEyODktNDg1Mi1hNzY2LWQ1Njc4ZWY3ZGVhOSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Plwn9wAAAALTSURBVHjaxJhLSFRRGMe/sYLADDdJUlST7YapaNXTsVWa0QujqMCIoCg0CKPsaQ8rGpIwIiIX0TtyIT00KQiNaKJNaLbSLFoU2cKygWAW9f+653OuecVz7r1z+8NvHtx7zvznnO9853w3lHxMJpoESkAMREAYZKtrSdALOkE7aAHfTDoPaZpZCPaCUjBOs+8UeAjOgoROg6xRrs8ED8ALsNrACKl714CXoAlM92JmI3gDVpB3rQIdYJ0bM0fATZBD/mkiuAsOmpg5Co5RZhQCJ8F+HTObQQ1lXqecpsxuZha4RMGIR6hBpQZHM/Vggk5Pff1EV5FFymuRZIot9lwgevLaOIbOO+WZQtCm0wP/YNVFou4vztdPbyOqLDMytViljsGR2afTKtGFZHM4bSQWJdpear2LqhuMR6jKPk35YJlOq2gBUdkS6/P1aqLmOFFdhfXOIyJqSRiZ4ayeJ9PE3VzRbZn8hc2nh2h+ZHgczdhgu89szysH17JUvGgre/xwI3930FxPq6tIpinqx1rlkRHJVBooImam+WHm9tP056XzjJuHxUyuVyO9n61VNBiRC4y7yNE5QmgF9K669HdeZW7jh81892Jm5zlky850rKyNuepmQMx8dGukvpGo8bna2CZjh93qfqbFzFu3RuxxchmH0nC+azPvxEybVyNNJ5xzj4GeSQbm//MJjNEJVo4RmRqJk4IpRP0DQ++djQPJlhLtg/tU8HUsXrAwqRUsH61V66uhRlj/fhfxBqqpZjZiX9px+n+KO9VNXHQVB2yEy6CVTie9ClUVBqUfYPdIx85usCMgI785rCS/jFQd3MhgmWLXAXBHp26qUbVTpkbkEDhjUlEeB5vAT59jZD2odVNr3wJzwSMfjNwHc8A9L08helThX6g6TBkYSKmnD4tU4f/Br+czojyVi4psD4uk8OMpfQ+61H7HeasvEw+LAtEfAQYAv2+q6mxeFyYAAAAASUVORK5CYII=) ***옵션 작성***에서 추가할 옵션 항목을 선택하세요.

![](/img/add-agent-option.png)


	* ***검색***에서 추가할 옵션을 찾을 수 있습니다. 텍스트를 입력하면 일치하는 옵션을 필터링합니다.
	* ***직접 입력***을 선택하면 옵션 키와 값을 입력할 수 있습니다.
3. 선택한 옵션 키에 대한 설명과 기본값을 확인한 다음 설정값을 입력하세요.

![](/img/add-agent-option-value.png)


	* 선택한 옵션을 취소하려면 ![삭제 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIwIDIySDRWNmgydjE0aDEyVjZoMnYxNnptMi0xOGgtNWwtMS4xNDMtMkg4LjE0M0w3IDRIMnYyaDIwVjR6IgogICAgZmlsbD0iIzc1NzU3NSIgLz4KICA8cGF0aCBkPSJNOSA4aDJ2MTBIOVY4ek0xMyA4aDJ2MTBoLTJWOHoiIGZpbGw9IiM3NTc1NzUiIC8+Cjwvc3ZnPg==) 버튼을 선택하세요.
	* 옵션을 추가 설정하려면 ***+ 추가하기*** 버튼을 선택하고 2번의 과정을 반복하세요.
4. 원하는 모든 옵션을 추가했으면 화면 오른쪽 위에 ***적용*** 버튼을 선택하세요.

선택한 옵션 및 설정값을 에이전트에 적용합니다.

노트* 수정 중인 내용을 초기화하려면 화면 오른쪽 위에 ![초기화 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAyMHB4O2hlaWdodDogMjBweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtcmVmcmVzaDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02NDcuMDAwMDAwLCAtMjI0Mi4wMDAwMDApIiBmaWxsPSIjNzU3NTc1Ij4KICAgICAgICAgICAgPGcgaWQ9InRpbWUtaWNvbnMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQzLjAwMDAwMCwgMjE5Ny4wMDAwMDApIj4KICAgICAgICAgICAgICAgIDxnIGlkPSJpYy1yZWZyZXNoIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDQuMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTEwLDIyIEwxNC41LDE4LjkwNzQyNDIgTDEwLDE2IEwxMCwyMiBaIE0xMCw2LjEgTDUuNSwzLjAwNzQyNDE5IEwxMCwwLjEgTDEwLDYuMSBaIiBpZD0iSWNvbiIgZmlsbC1ydWxlPSJldmVub2RkIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0yLjQzNDgwMDEsNi4xMjI3ODYxOCBMNC4wMzc5MDMwOSw3LjMzMDI0MzQ5IEMzLjM3OTczNzcsOC4zOTcyNjMxNiAzLDkuNjU0Mjg1MzQgMywxMSBDMywxNC44NjU5OTMyIDYuMTM0MDA2NzUsMTggMTAsMTggQzEwLjU3Nzg3NjQsMTggMTEuMTM5Mzk3OCwxNy45Mjk5NzU5IDExLjY3NjU0MTksMTcuNzk3OTQ5OSBMMTMuNjAyNjQ2OCwxOS4yNDk5NjQ0IEMxMi40OTk1MTY3LDE5LjczMjM2NjYgMTEuMjgxMDEyOSwyMCAxMCwyMCBDNS4wMjk0MzcyNSwyMCAxLDE1Ljk3MDU2MjcgMSwxMSBDMSw5LjIwMjUwMTgxIDEuNTI2OTUwOTYsNy41MjgwNzk2MSAyLjQzNDgwMDEsNi4xMjI3ODYxOCBaIE0xMCwyIEMxNC45NzA1NjI3LDIgMTksNi4wMjk0MzcyNSAxOSwxMSBDMTksMTIuODI1MzY5NyAxOC40NTY1ODA4LDE0LjUyMzgxNzEgMTcuNTIyNjk1MSwxNS45NDIzODk0IEwxNS45MjA5ODg2LDE0LjczNTU4MjMgQzE2LjYwNDQyNSwxMy42NTQ1ODg3IDE3LDEyLjM3MzQ5MDEgMTcsMTEgQzE3LDcuMTM0MDA2NzUgMTMuODY1OTkzMiw0IDEwLDQgQzkuMzg3ODEyMTcsNCA4Ljc5Mzk3OTE2LDQuMDc4NTg2MzUgOC4yMjgwMzg3Nyw0LjIyNjIyMTI3IEw2LjMxNTQ1ODEzLDIuNzg2MzM3ODkgQzcuNDQwMDU3NCwyLjI4MTA3ODU5IDguNjg3MjAzOTksMiAxMCwyIFoiIGlkPSJDb21iaW5lZC1TaGFwZSIgZmlsbC1ydWxlPSJub256ZXJvIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하세요.
* 옵션값으로 아무것도 입력하지 않은 상태에서 ***적용*** 버튼을 선택하면 해당 옵션을 삭제합니다.
* 이미 추가한 옵션은 옵션 목록에서 선택할 수 없습니다.
* 애플리케이션 종류 및 에이전트의 버전에 따라 적용할 수 있는 옵션 키는 다를 수 있습니다.
* 예시로 제공한 이미지는 애플리케이션 종류 및 에이전트에 따라 다를 수 있습니다.
### 옵션 수정 또는 삭제하기[​](#옵션-수정-또는-삭제하기 "옵션 수정 또는 삭제하기에 대한 직접 링크")

![옵션 수정](/img/modify-agent-java.png)

1. 화면을 위 또는 아래로 스크롤하거나 왼쪽의 옵션 목록에서 수정 또는 삭제하려는 옵션을 선택하세요.
2. 변경하려는 옵션에서 원하는 값을 선택하거나 수정하세요. 옵션을 삭제하려면 ![삭제 아이콘](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIGZpbGw9Im5vbmUiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIwIDIySDRWNmgydjE0aDEyVjZoMnYxNnptMi0xOGgtNWwtMS4xNDMtMkg4LjE0M0w3IDRIMnYyaDIwVjR6IgogICAgZmlsbD0iIzc1NzU3NSIgLz4KICA8cGF0aCBkPSJNOSA4aDJ2MTBIOVY4ek0xMyA4aDJ2MTBoLTJWOHoiIGZpbGw9IiM3NTc1NzUiIC8+Cjwvc3ZnPg==) 버튼을 선택하세요.
3. 변경한 사항을 적용하려면 ***적용*** 버튼을 선택하세요.

노트* 화면 가장 위로 이동하려면 ![숫자 3](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAjCAYAAAAe2bNZAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3lpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAxIDc5LjE0ZWNiNDJmMmMsIDIwMjMvMDEvMTMtMTI6MjU6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIiB4bWxuczpzdFJlZj0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL3NUeXBlL1Jlc291cmNlUmVmIyIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6MjNjODFkMGUtOTAzMy00NmVhLWI3MzQtZWVmNzY0Y2U4ODY1IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOkRCRDFDMjg4QjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOkRCRDFDMjg3QjU2QTExRURBNTlDQzcxMUE1QURGQ0YzIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyNC4wIChNYWNpbnRvc2gpIj4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6ODNkOGM4MWEtNWE2MS00MmRiLTk2YTgtYTc1NjI2MTU1MDg1IiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjIzYzgxZDBlLTkwMzMtNDZlYS1iNzM0LWVlZjc2NGNlODg2NSIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PhIBdIgAAAMcSURBVHjazFh9aI1hFD93KIw1hZDkZn+oOyklFLar5ONiSzNqUmqF+UqakFmjKMWSiCSaj3wlaXcmaV8YKQ2bf0xL/rDIR1uTYvE73ee573vf3bud5953b0792t37cd7fe57zO885r6+nlv4bG2p4/XhgOZALBICpQAbwF+gGOoA2oB64D3w2ce4TRmYBsAdYavACv4Ea4BjwVHJD2gDnpwFhoBFYYRjJYUAe8AS4B/hTIVMEtKhlSdVWKl+FyZCpAK4Ao1zMT86t68ABEzKHgIODJBgfcBjYKyGzHijzQMVHgHX9kckCznpUUjhC55xJbVfHKSBd4unLD0ismajuJdHtpsixAog/OIsoNI9oXKY4h04Cq5x1hotYncTDnQZk90Wi9s7457MmEF0tJ8r2i6M0X8k/ukylkrt6fsUS4QdvCkWioo3PFVVErhVaqT0yE/H3IzBEcmfHJ6KtJ4iKUQJX51jHH74gyrel/l1oZvFscaWezFsH50xISoTND+q38KD04bHHnQ/u/mlUqXmbqeJlWmgqBScRndR2mzTWyGWuVtOMVDTKJFreEVXetI5xHs0NGLkJaDJTkiHRimZhzpa+x0/vJFoTNHbn12rKdKuS5SDGGSPjL+MANlqrqVfQSsRdnqZXRF1I1NftKKdh6xxL/cxuI1JcCEYwmW/4MSbVqLDk8/dZNehoMdGOAvm7cRfJEfngxhKx5Hettf6vfW72LjpnWk0jIKmuDW+MyLzVZBqldzAJXoqS4xE1OUlW3oiVt4HVa2lz6vVKqvCF6khOMHi3ZvVMR2H42mXt3toKF4mJ/FGTRHTXDkt6XY5M2flY5cQzg32JVLOeZyfD7/FIejdvis2Yjp61WbmRRD9jH4MeO+cm/rXE4yEyrEagPm3nNl4JD4nwBLo9UQ+MOkolHpLZrOtLoumgiounB0R4FLommZv2q9lmsKw8kf+0fphvdDmH2NcGNSQaz9qXgJnAAxeI1Chfl1P5CvFe9adBW6WWGl9brVrKkPLlyveZaGsLLOM+CshWXaJuP76rDkB/LOJodJo4/yfAABNxzftn0khZAAAAAElFTkSuQmCC) ***옵션 추가로 이동*** 버튼을 선택하세요.
* 옵션값으로 아무것도 입력하지 않은 상태에서 ***적용*** 버튼을 선택하면 해당 옵션을 삭제합니다.
### 여러 에이전트에 동시 적용하기[​](#여러-에이전트에-동시-적용하기 "여러 에이전트에 동시 적용하기에 대한 직접 링크")

프로젝트에 소속된 여러 개의 에이전트에 변경한 옵션을 동시에 적용할 수 있습니다.

1. 화면 오른쪽 위에 ***다중 에이전트 적용*** 체크박스를 선택하면 각 옵션 항목에 체크박스가 생성됩니다.
2. 동시에 적용하길 원하는 옵션의 체크박스를 선택하세요. 여러 개를 선택할 수 있습니다.
3. 화면 오른쪽 위에 ***적용*** 버튼을 선택하세요.
4. ***에이전트 적용*** 창이 나타나면 변경한 옵션을 적용할 에이전트를 선택하세요. 모두 선택하려면 ***전체 선택*** 체크박스를 선택하세요.

![](/img/multiple-apply-agent.png)
5. ***적용*** 버튼을 선택하세요.

### 에이전트 기본값 설정하기[​](#에이전트-기본값-설정하기 "에이전트 기본값 설정하기에 대한 직접 링크")

프  로젝트에 새로운 에이전트를 추가할 경우 기존의 설정값을 반복해서 적용하는 번거로움을 피하고 싶다면 프로젝트별, 업무별 기본 설정값을 만들어 적용할 수 있습니다.

![](/img/set-agent-category.png)

* 업무 디폴트: *whatap.conf* 파일에서 `whatap.okind` 항목으로 분류한 에이전트들에 옵션을 공통 적용할 수 있고, 적용된 옵션을 확인할 수 있습니다.
* 프로젝트 디폴트: 프로젝트에 소속된 모든 에이전트들에 옵션을 공통 적용할 수 있고, 적용된 옵션을 확인할 수 있습니다.

노트* ***업무 디폴트*** 또는 ***프로젝트 디폴트*** 탭을 선택한 다음 옵션을 적용하는 것은 에이전트를 공통으로 관리하는 데 유용합니다.
* 옵션의 적용 우선 순위는 ***업무 디폴트***, ***프로젝트 디폴트***, ***에이전트 설정*** 순입니다.


	+ ***프로젝트 디폴트***에서 b 옵션값을 1000을 적용하고, ***업무 디폴트***에서 b 옵션값을 2000으로 적용하면, ***업무 디폴트***에서 설정한 옵션값 2000을 우선 적용합니다.
	+ ***프로젝트 디폴트***에서 b 옵션값을 아무것도 입력하지 않았고 ***업무 디폴트***에 b 옵션값에 2000이 적용된 경우에도 ***업무 디폴트***에서 설정한 옵션값을 우선 적용합니다.
### 에이전트 설정 공유하기[​](#에이전트-설정-공유하기 "에이전트 설정 공유하기에 대한 직접 링크")

에이전트 설정 내용을 json 형식의 파일로 저장하고 파일을 불러와 다른 에이전트에 적용할 수 있습니다.

1. ***에이전트 목록***에서 설정 내용을 json 파일로 내보낼 에이전트를 선택하세요.
2. 화면 오른쪽 위에 ![내보내기 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAxNnB4O2hlaWdodDogMTZweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtZXhwb3J0PC90aXRsZT4gLS0+CiAgICA8ZGVzYz5DcmVhdGVkIHdpdGggU2tldGNoLjwvZGVzYz4KICAgIDxnIGlkPSJJY29uLVNldCIgc3Ryb2tlPSJub25lIiBzdHJva2Utd2lkdGg9IjEiIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPGcgaWQ9IldoYVRhcF9JY29uX1NldCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTc0MC4wMDAwMDAsIC0yOTUxLjAwMDAwMCkiIGZpbGw9IiM3NTc1NzUiPgogICAgICAgICAgICA8ZyBpZD0iYXBwbGljYXRpb24taWNvbnMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQwLjAwMDAwMCwgMjM0Ni4wMDAwMDApIj4KICAgICAgICAgICAgICAgIDxnIGlkPSJpYy1leHBvcnQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDcwMC4wMDAwMDAsIDYwNS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMi4wMDAwMDApIiBpZD0iSWNvbiI+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0xOCwxOCBMMiwxOCBMMiwyIEwxMCwyIEwxMCwtMS44NDc2ODg2N2UtMTMgTC04LjExNzk1MDc2ZS0xMywtMS44NDc2ODg2N2UtMTMgTC04LjExNzk1MDc2ZS0xMywyMCBMMjAsMjAgTDIwLDEwIEwxOCwxMCBMMTgsMTcgTDE4LDE4IFogTTEzLjEyNjg4ODIsMS45NjM3NDYyMiBMMTYuNjUxODEyNywxLjk2Mzc0NjIyIEw3LDExLjYxNTU1ODkgTDguMzg0NDQxMDksMTMgTDE4LjAzNjI1MzgsMy4zNDgxODczMSBMMTguMDM2MjUzOCw2Ljg3MzExMTc4IEwyMCw2Ljg3MzExMTc4IEwyMCwtMS41NjMxOTQwMmUtMTMgTDEzLjEyNjg4ODIsLTEuNTYzMTk0MDJlLTEzIEwxMy4xMjY4ODgyLDEuOTYzNzQ2MjIgWiI+PC9wYXRoPgogICAgICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgICAgIDwvZz4KICAgICAgICAgICAgPC9nPgogICAgICAgIDwvZz4KICAgIDwvZz4KPC9zdmc+) 버튼을 선택하세요.
3. json 파일을 다운로드하세요.
4. ***에이전트 목록***에서 다른 에이전트를 선택하세요.
5. 화면 오른쪽 위에 ![가져오기 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAyMHB4O2hlaWdodDogMjBweDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiPgogICAgPHBhdGggZmlsbD0iIzc1NzU3NSIgZmlsbC1ydWxlPSJldmVub2RkIiBkPSJNMjAgMjBINFY0aDhWMkgydjIwaDIwVjEyaC0ydjh6bS00LjEyNy02Ljk2NGgtMy41MjVMMjIgMy4zODQgMjAuNjE2IDJsLTkuNjUyIDkuNjUyVjguMTI3SDlWMTVoNi44NzN2LTEuOTY0eiI+PC9wYXRoPgo8L3N2Zz4=) 버튼을 선택하세요.

json 파일을 통해 가져온 에이전트 설정을 확인하세요.

에이전트 설정 옵션 안내[​](#에이전트-설정-옵션-안내 "에이전트 설정 옵션 안내에 대한 직접 링크")
----------------------------------------------------------

다음 링크를 통해 설정할 수 있는 옵션들에 대한 설명을 제공합니다.

[에이전트 이름 식별
----------

모니터링 대상을 구별하기 위한 애플리케이션 서버의 고유 식별자 설정에 대해 안내합니다. 모니터링 대상 시스템 내에서 애플리케이션 서버를 정확히 구분하는 데 필수적입니다. 서버 유형, IP 등의 정보를 기반으로 한 자동 이름 지정 방식과 사용자가 직접 whatap.conf 파일이나 JVM 옵션을 통해 에이전트 이름을 설정하는 방법을 확인할 수 있습니다.](/java/agent-name)[에이전트 기능 제어
----------

자바(Java) 애플리케이션 서버의 모니터링을 위한 에이전트 기능을 세밀하게 조정하는 방법을 안내합니다. 에이전트의 활성화/비활성화, 트랜잭션 및 성능 카운터 추적, OS 정보 수집 등의 기능을 포함하며, 각 기능을 제어하는 다양한 설정 옵션들에 대해 확인할 수 있습니다.](/java/agent-control-function)[CPU/메모리/디스크 사용량 수집
------------------

자바(Java) 에이전트가 CPU, 메모리, 디스크 사용량을 수집하는 방법을 안내합니다. 자바(Java)의 JMX 라이브러리를 기본적으로 활용하며, 필요에 따라 Linux의 proc 디렉터리나 oshi, sigar 라이브러리를 통한 성능 지표 수집 방법을 확인할 수 있습니다.](/java/agent-usage)[에이전트 통신 설정
----------

자바(Java) 에이전트가 애플리케이션 서버로부터 수집한 데이터를 서버로 전송하기 위한 네트워크 설정 방법을 안내합니다. 주요 설정 옵션으로는 수집 서버 호스트, 포트, 타임아웃 값, 네트워크 전송 크기, 데이터 전송 큐 크기 등이 있으며, 에이전트의 효율적인 데이터 관리 및 안정적인 서버 통신을 보장하는 데 중요합니다.](/java/agent-network)[에이전트 성능
-------

자바(Java) 에이전트의 성능 관련 옵션을 안내합니다. 동시에 처리할 수 있는 최대 트랜잭션 수와 트랜잭션 데이터를 저장하는 버퍼의 초기 크기 설정을 확인할 수 있습니다. 이는 시스템의 부하와 자원 사용을 최적화하는 데 중요한 역할을 합니다.](/java/agent-performance)[에이전트 로그 설정
----------

자바(Java) 애플리케이션 환경에서 발생하는 로그 데이터를 에이전트를 통해 관리하는 방법을 안내합니다. 로그 파일의 경로 및 이름 설정, 보관 기간 설정, 로그 모니터링, 사용자 정의 로그 추적 활성화 방법 등을 포함합니다. 로그 관리를 위한 다양한 설정 옵션을 제공해 시스템의 효율적인 로그 관리를 도와줍니다.](/java/agent-log)[트랜잭션
----

자바(Java) 애플리케이션 내 각 트랜잭션의 성능 데이터를 에이전트가 추적하고 분석할 수 있는 설정 방법을 안내합니다. 트랜잭션의 요청 처리, 응답 시간, 자원 사용량 등을 추적하여 애플리케이션 성능을 평가합니다.](/java/agent-transaction)[DB, SQL
-------

데이터베이스 및 SQL 성능 데이터 수집을 위한 자바(Java) 에이전트의 다양한 옵션을 안내합니다. DBCP, Hikari, Tomcat 등 다양한 DB 연결 풀(Connection Pool) 정보 추적 및 SQL 실행 세부 사항을 기록할 수 있습니다. 또한, SQL 파라미터 정보 기록, DB 연결 누수 추적 등 성능 최적화에 필수적인 정보 수집 옵션을 제공합니다.](/java/agent-dbsql)[HTTPC, API Call
---------------

HTTP 외부 호출과 API 호출 관련 데이터를 수집, 분석을 위한 자바(Java) 에이전트의 옵션 설정 방법을 안내합니다. TOO SLOW 에러 처리 및 CPU와 메모리 사용량 추적, 호출 시점의 스택 트레이스 기록, URL 정규화 등 세밀한 모니터링을 위한 다양한 옵션을 제공합니다. 이를 통해 개발자는 애플리케이션의 외부 의존성을 효율적으로 관리하고 성능 문제를 식별할 수 있습니다.](/java/agent-httpcapicall)[스크립트 플러그인
---------

자바(Java) 에이전트에서 제공하는 플러그인 옵션을 통해 사용자가 원하는 코드를 트레이스 데이터에 주입하거나 메소드 수행 전후로 부가 정보를 추가하는 방법을 제공합니다. 메소드 시작/종료 시점에 특정 코드를 실행할 위치를 설정하는 옵션과 사용자 정의 pool을 모니터링하기 위한 클래스 설정 방법을 포함합니다. 실제 플러그인 적용 사례를 통해 구체적인 활용 방안을 제시하며, 모니터링의 유연성과 세밀함을 높일 수 있는 다양한 설정 예시와 API 사용법을 안내합니다.](/java/script-plugin)[사용자 수
-----

자바(Java) 웹 애플리케이션 서버에 연결된 사용자 수를 에이전트 설정을 통해 집계하는 방법을 안내합니다. 실시간 사용자 집계 활성화 여부 설정, 사용자 수를 집계하기 위한 쿠키 제한 설정, IP 주소 또는 HTTP 헤더 특정 값을 기준으로 한 사용자 집계 방법, 클라이언트 IP 정보 추적을 위한 HTTP 헤더 설정 등을 포함합니다.](/java/agent-number-of-user)[부하량 제어
------

자바(Java) 애플리케이션 서버의 트래픽 쓰로틀링 옵션을 설정하는 에이전트 옵션을 안내합니다. 애플리케이션의 최대 동시 요청 수를 제한하고, 특정 사용자나 URL을 기준으로 서비스 접근을 제어하는 기능을 포함합니다. 사용자 정의 메시지 전송, URL 리다이렉션 설정, 이벤트 알림 활성화 등 다양한 옵션을 제공하여 과부하 상황에서 애플리케이션의 안정성을 보장할 수 있습니다.](/java/agent-load-amount)[에이전트 알림
-------

자바(Java) 에이전트를 통해 애플리케이션 서버에서 발생하는 다양한 이벤트에 대한 알림 설정 방법을 제공합니다. 트랜잭션 재귀 호출, 서비스 거절, HTTPC 연결 오류, 힙 및 디스크 사용량 초과, CPU 사용량 임계치 도달, DB 커넥션 중복 할당 및 예외 발생 시 이벤트 알림을 설정하는 옵션을 포함합니다. 각 이벤트별로 발행 간격, 발행 여부, 임계치 설정 등 세밀한 조정을 할 수 있습니다.](/java/agent-notification)[Apdex
-----

사용자 만족도를 측정하는 Apdex 점수를 설정하는 자바(Java) 에이전트 옵션을 안내합니다. Apdex 지표를 통해 애플리케이션의 성능을 객관적으로 평가하고 사용자 경험을 개선할 수 있습니다.](/java/agent-apdex)[통계
--

자바(Java) 애플리케이션 모니터링을 위한 다양한 통계 수집 기능 관련 에이전트 옵션을 안내합니다. 성능 카운터 확장, 도메인별 트랜잭션 수집, 멀티 서버 트랜잭션 의존성 분석, 로그인 유형별 및 Referer 별 통계 수집 등을 포함합니다. 또한 SQL, HTTP Call, 오류 통계와 사용자 에이전트 정보 수집에 대한 최대 레코드 수 제한 설정도 확인할 수 있습니다.](/java/agent-static)[토폴로지 맵
------

자바(Java) 에이전트가 수집한 데이터를 사용하여 애플리케이션의 토폴로지 맵을 생성하는 에이전트 설정 옵션을 안내합니다. 트랜잭션 호출자, 데이터베이스 연결 정보, HTTPC 아웃바운드 정보, 액티브 트랜잭션 상태 등의 다양한 지표를 통해 시스템의 토폴로지를 시각화하고 분석할 수 있습니다.](/java/agent-toplogy)[트랜잭션 에러 스택
----------

자바(Java) 애플리케이션에서 트랜잭션 중 발생하는 에러를 감지하고 이에 대한 스택 트레이스를 표시하는 에이전트 설정 옵션을 안내합니다. 트랜잭션, 메소드, SQL, HTTP 호출, SOCKET 호출 등 다양한 영역에서 에러 정보를 수집하고, 에러 스택의 길이, 제목 길이 등을 설정하는 방법을 포함합니다. 에이전트 설정을 통해 에러 관리를 개선하고, 애플리케이션의 오류 진단을 보다 효율적으로 수행할 수 있도록 지원합니다.](/java/agent-transaction-error-stack)[부가 기능
-----

자바(Java) 애플리케이션의 모니터링 수준을 사용자의 필요에 맞게 조정할 수 있는 추가적인 에이전트 설정 옵션을 안내합니다. SQL 파라미터 수집, HTTP 파라미터 및 헤더 정보 수집, 사용자 IP 정보 추출, 사용자 수 추적 방법 선택, SAP Function 추적 등을 포함합니다. 이 옵션들을 통해 보다 세밀한 데이터 수집 및 분석이 가능하며, 특히 보안이 중요한 환경에서 필요에 따라 옵션을 조정할 수 있습니다.](/java/agent-additional-option)[비동기 추적
------

자바(Java) 에이전트 설정을 통해 비동기 애플리케이션 활동을 추적하는 방법을 안내합니다. CompletableFuture 메소드 수집 방법과 사용자 애플리케이션에 해당 메소드를 hooking하는 방식을 포함합니다. 설정 예시와 함께 whatap.conf 파일에 추가해야 할 옵션을 제공하여 비동기 호출의 성능 모니터링을 강화할 수 있도록 지원합니다.](/java/async-tracking)[오픈소스 추적
-------

자바(Java) 애플리케이션에서 사용하는 프레임워크나 오픈소스 라이브러리를 에이전트를 통해 추적하는 설정 방법을 제공합니다. Java 에이전트 설정 파일(whatap.conf)에 weaving 옵션을 추가하여 설정하며, 다양한 프레임워크 및 라이브러리 버전에 대응하는 방법을 안내합니다.](/java/agent-weaving)