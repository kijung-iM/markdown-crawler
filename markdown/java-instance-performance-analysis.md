인스턴스 성능 관리
==========

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리

애플리케이션의 환경을 확인하고 성능과 관련한 설정을 확인할 수 있습니다.

에이전트 목록[​](#에이전트-목록 "에이전트 목록에 대한 직접 링크")
----------------------------------------

화면 왼쪽에 애플리케이션 목록에서는 프로젝트에 할당된 에이전트 목록을 확인할 수 있습니다. 개별 에이전트 항목을 선택하면 오른쪽 화면에 설정된 환경 변수 및 에이전트 설정, 성능과 관련한 정보를 조회할 수 있습니다.

![에이전트 목록](/img/ipa-agent-list.png)

에이전트 목록을 갱신하거나 비활성화된 에이전트를 재기동한 다음 목록에 자동으로 표시되지 않는다면 ![새로 고침 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAyMHB4O2hlaWdodDogMjBweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtcmVmcmVzaDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02NDcuMDAwMDAwLCAtMjI0Mi4wMDAwMDApIiBmaWxsPSIjNzU3NTc1Ij4KICAgICAgICAgICAgPGcgaWQ9InRpbWUtaWNvbnMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQzLjAwMDAwMCwgMjE5Ny4wMDAwMDApIj4KICAgICAgICAgICAgICAgIDxnIGlkPSJpYy1yZWZyZXNoIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDQuMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTEwLDIyIEwxNC41LDE4LjkwNzQyNDIgTDEwLDE2IEwxMCwyMiBaIE0xMCw2LjEgTDUuNSwzLjAwNzQyNDE5IEwxMCwwLjEgTDEwLDYuMSBaIiBpZD0iSWNvbiIgZmlsbC1ydWxlPSJldmVub2RkIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0yLjQzNDgwMDEsNi4xMjI3ODYxOCBMNC4wMzc5MDMwOSw3LjMzMDI0MzQ5IEMzLjM3OTczNzcsOC4zOTcyNjMxNiAzLDkuNjU0Mjg1MzQgMywxMSBDMywxNC44NjU5OTMyIDYuMTM0MDA2NzUsMTggMTAsMTggQzEwLjU3Nzg3NjQsMTggMTEuMTM5Mzk3OCwxNy45Mjk5NzU5IDExLjY3NjU0MTksMTcuNzk3OTQ5OSBMMTMuNjAyNjQ2OCwxOS4yNDk5NjQ0IEMxMi40OTk1MTY3LDE5LjczMjM2NjYgMTEuMjgxMDEyOSwyMCAxMCwyMCBDNS4wMjk0MzcyNSwyMCAxLDE1Ljk3MDU2MjcgMSwxMSBDMSw5LjIwMjUwMTgxIDEuNTI2OTUwOTYsNy41MjgwNzk2MSAyLjQzNDgwMDEsNi4xMjI3ODYxOCBaIE0xMCwyIEMxNC45NzA1NjI3LDIgMTksNi4wMjk0MzcyNSAxOSwxMSBDMTksMTIuODI1MzY5NyAxOC40NTY1ODA4LDE0LjUyMzgxNzEgMTcuNTIyNjk1MSwxNS45NDIzODk0IEwxNS45MjA5ODg2LDE0LjczNTU4MjMgQzE2LjYwNDQyNSwxMy42NTQ1ODg3IDE3LDEyLjM3MzQ5MDEgMTcsMTEgQzE3LDcuMTM0MDA2NzUgMTMuODY1OTkzMiw0IDEwLDQgQzkuMzg3ODEyMTcsNCA4Ljc5Mzk3OTE2LDQuMDc4NTg2MzUgOC4yMjgwMzg3Nyw0LjIyNjIyMTI3IEw2LjMxNTQ1ODEzLDIuNzg2MzM3ODkgQzcuNDQwMDU3NCwyLjI4MTA3ODU5IDguNjg3MjAzOTksMiAxMCwyIFoiIGlkPSJDb21iaW5lZC1TaGFwZSIgZmlsbC1ydWxlPSJub256ZXJvIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하세요.

에이전트 및 애플리케이션 상세 정보[​](#에이전트-및-애플리케이션-상세-정보 "에이전트 및 애플리케이션 상세 정보에 대한 직접 링크")
----------------------------------------------------------------------------

화면 오른쪽에서는 에이전트 및 애플리케이션과 관련한 상세 정보를 확인할 수 있습니다.

* 오른쪽 위에 텍스트 입력란을 통해 원하는 항목을 필터링할 수 있습니다.
* 모니터링 대상 서버에 위치한 에이전트 및 애플리케이션의 변경 사항이 자동 반영되지 않는다면 ![새로 고침 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAyMHB4O2hlaWdodDogMjBweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtcmVmcmVzaDwvdGl0bGU+IC0tPgogICAgPGRlc2M+Q3JlYXRlZCB3aXRoIFNrZXRjaC48L2Rlc2M+CiAgICA8ZyBpZD0iSWNvbi1TZXQiIHN0cm9rZT0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIiBmaWxsPSJub25lIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiPgogICAgICAgIDxnIGlkPSJXaGFUYXBfSWNvbl9TZXQiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02NDcuMDAwMDAwLCAtMjI0Mi4wMDAwMDApIiBmaWxsPSIjNzU3NTc1Ij4KICAgICAgICAgICAgPGcgaWQ9InRpbWUtaWNvbnMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQzLjAwMDAwMCwgMjE5Ny4wMDAwMDApIj4KICAgICAgICAgICAgICAgIDxnIGlkPSJpYy1yZWZyZXNoIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDQuMDAwMDAwLCA0NS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyLjAwMDAwMCwgMS4wMDAwMDApIj4KICAgICAgICAgICAgICAgICAgICAgICAgPHBhdGggZD0iTTEwLDIyIEwxNC41LDE4LjkwNzQyNDIgTDEwLDE2IEwxMCwyMiBaIE0xMCw2LjEgTDUuNSwzLjAwNzQyNDE5IEwxMCwwLjEgTDEwLDYuMSBaIiBpZD0iSWNvbiIgZmlsbC1ydWxlPSJldmVub2RkIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgICAgIDxwYXRoIGQ9Ik0yLjQzNDgwMDEsNi4xMjI3ODYxOCBMNC4wMzc5MDMwOSw3LjMzMDI0MzQ5IEMzLjM3OTczNzcsOC4zOTcyNjMxNiAzLDkuNjU0Mjg1MzQgMywxMSBDMywxNC44NjU5OTMyIDYuMTM0MDA2NzUsMTggMTAsMTggQzEwLjU3Nzg3NjQsMTggMTEuMTM5Mzk3OCwxNy45Mjk5NzU5IDExLjY3NjU0MTksMTcuNzk3OTQ5OSBMMTMuNjAyNjQ2OCwxOS4yNDk5NjQ0IEMxMi40OTk1MTY3LDE5LjczMjM2NjYgMTEuMjgxMDEyOSwyMCAxMCwyMCBDNS4wMjk0MzcyNSwyMCAxLDE1Ljk3MDU2MjcgMSwxMSBDMSw5LjIwMjUwMTgxIDEuNTI2OTUwOTYsNy41MjgwNzk2MSAyLjQzNDgwMDEsNi4xMjI3ODYxOCBaIE0xMCwyIEMxNC45NzA1NjI3LDIgMTksNi4wMjk0MzcyNSAxOSwxMSBDMTksMTIuODI1MzY5NyAxOC40NTY1ODA4LDE0LjUyMzgxNzEgMTcuNTIyNjk1MSwxNS45NDIzODk0IEwxNS45MjA5ODg2LDE0LjczNTU4MjMgQzE2LjYwNDQyNSwxMy42NTQ1ODg3IDE3LDEyLjM3MzQ5MDEgMTcsMTEgQzE3LDcuMTM0MDA2NzUgMTMuODY1OTkzMiw0IDEwLDQgQzkuMzg3ODEyMTcsNCA4Ljc5Mzk3OTE2LDQuMDc4NTg2MzUgOC4yMjgwMzg3Nyw0LjIyNjIyMTI3IEw2LjMxNTQ1ODEzLDIuNzg2MzM3ODkgQzcuNDQwMDU3NCwyLjI4MTA3ODU5IDguNjg3MjAzOTksMiAxMCwyIFoiIGlkPSJDb21iaW5lZC1TaGFwZSIgZmlsbC1ydWxlPSJub256ZXJvIj48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 새로고침 버튼을 선택하세요.

### 에이전트 관련 항목[​](#에이전트-관련-항목 "에이전트 관련 항목에 대한 직접 링크")

#### 실행 환경 변수

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 실행 환경 변수

![실행 환경 변수](/img/ipa-run-env-var-java.png)

에이전트 실행과 관련한 환경 변수를 조회할 수 있습니다. 에이전트 버전 및 설치 경로, 이름, IP 주소 등을 확인할 수 있습니다.

#### 에이전트 로그[​](#-2 "-2에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 에이전트 로그

![에이전트 로그](/img/ipa-agent-log-java.png)

모니터링 대상 서버에 저장된 에이전트 로그를 조회할 수 있습니다. 로그 파일의 이름은 *whatap-`YYYYMMDD`.log* 형식입니다. 각 로그를 선택해 로그에 캡쳐되는 오류 및 이벤트에 대한 정보를 액세스할 수 있습니다.

노트로그와 관련한 에이전트 설정은 [다음 문서](/java/agent-log)를 참조하세요.

#### 에이전트 설정[​](#-3 "-3에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 에이전트 설정 `Old`

모니터링 대상 서버에 위치한 *whatap.conf* 파일을 직접 수정하지 않고 에이전트 설정 옵션을 추가하거나 수정, 삭제할 수 있습니다.

정보에이전트 설정 기능은 사용성과 기능을 개선한 관리 > 에이전트 설정 메뉴를 이용할 것을 권장합니다. 화면 오른쪽 위에 신규 에이전트 설정 버튼을 선택하세요. 자세한 내용은 [다음 문서](/java/set-agent#set-agent-service)를 참조하세요.

### 애플리케이션 관련 항목[​](#애플리케이션-관련-항목 "애플리케이션 관련 항목에 대한 직접 링크")

#### 환경변수[​](#-4 "-4에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 환경변수

![환경 변수](/img/ipa-env-var-java.png)

애플리케이션 실행과 관련한 환경 변수 정보를 조회할 수 있습니다.

#### 힙 히스토그램[​](#-5 "-5에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 힙 히스토그램

![힙 히스토그램](/img/ipa-heap-histogram-java.png)

JVM(자바 가상 머신)의 메모리에 올라가 있는 Heap 점유 객체 현황(힙 메모리상의 객체별 사이즈)을 조회할 수 있습니다.

노트Java 6 ~ 8 버전에서는 JVM 옵션 없이 기본 지원하지만, 일부 Java 버전에 따라 다음과 같이 JVM 옵션을 적용해야 합니다.

* Java 9 ~ Java 15 버전


```
-Djdk.attach.allowAttachSelf=true  

```
example
```
java -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -Djdk.attach.allowAttachSelf=true -jar {application.jar}  

```
* Java 16 버전 이상


```
-Djdk.attach.allowAttachSelf=true  
--add-opens=jdk.attach/sun.tools.attach=ALL-UNNAMED  

```
example
```
java -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -Djdk.attach.allowAttachSelf=true --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=jdk.attach/sun.tools.attach=ALL-UNNAMED -jar {application.jar}  

```
* Java 5 버전 이하, IBM Java는 지원하지 않습니다.
#### 로딩된 클래스[​](#-6 "-6에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 로딩된 클래스

![로딩된 클래스](/img/ipa-loaded-class-java.png)

Java 애플리케이션에 로딩된 클래스 정보를 확인할 수 있습니다.

#### 라이브러리 버전[​](#-7 "-7에 대한 직접 링크")

홈 화면 > 프로젝 트 선택 > 인스턴스 성능 관리 > 라이브러리 버전

![라이브러리 버전](/img/ipa-library-version-java.png)

Java 애플리케이션을 구성하는 라이브러리의 버전을 확인할 수 있습니다.

#### 스레드 목록/덤프[​](#-8 "-8에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 스레드 목록/덤프

![스레드 목록/덤프](/img/ipa-thread-list-java.png)

Java 프로세스의 모든 스레드 상태에 대한 스냅샷 정보를 확인할 수 있습니다. Java 애플리케이션의 성능 문제를 진단하는데 이용할 수 있습니다. 스레드 목록에서 각 스레드의 ![확장 아이콘](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iU1ZHSW5saW5lLXN2ZyIgc3R5bGU9IndpZHRoOiAyNHB4O2hlaWdodDogMjRweDsiIHdpZHRoPSIyNHB4IiBoZWlnaHQ9IjI0cHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KICAgIDwhLS0gR2VuZXJhdG9yOiBTa2V0Y2ggNTkuMSAoODYxNDQpIC0gaHR0cHM6Ly9za2V0Y2guY29tIC0tPgogICAgPCEtLSA8dGl0bGU+aWMtY2FyZXQtcmlnaHQ8L3RpdGxlPiAtLT4KICAgIDxkZXNjPkNyZWF0ZWQgd2l0aCBTa2V0Y2guPC9kZXNjPgogICAgPGcgaWQ9Ikljb24tU2V0IiBzdHJva2U9Im5vbmUiIHN0cm9rZS13aWR0aD0iMSIgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIj4KICAgICAgICA8ZyBpZD0iV2hhVGFwX0ljb25fU2V0IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTY0LjAwMDAwMCwgLTI0NC4wMDAwMDApIiBmaWxsPSIjOTU5NTk1Ij4KICAgICAgICAgICAgPGcgaWQ9ImRpcmVjdGlvbmFsLWljb25zIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MC4wMDAwMDAsIDExOS4wMDAwMDApIj4KICAgICAgICAgICAgICAgIDxnIGlkPSJpYy1jYXJldC1yaWdodCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTI0LjAwMDAwMCwgMTI1LjAwMDAwMCkiPgogICAgICAgICAgICAgICAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMDAwMDAwLCA2LjAwMDAwMCkiPgogICAgICAgICAgICAgICAgICAgICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0LjAwMDAwMCwgNi4wMDAwMDApIHNjYWxlKC0xLCAxKSByb3RhdGUoLTI3MC4wMDAwMDApIHRyYW5zbGF0ZSgtNC4wMDAwMDAsIC02LjAwMDAwMCkgIiBkPSJNLTIgMiA0IDEwIDEwIDJ6Ij48L3BhdGg+CiAgICAgICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICAgICAgPC9nPgogICAgICAgICAgICA8L2c+CiAgICAgICAgPC9nPgogICAgPC9nPgo8L3N2Zz4=) 버튼을 선택하면 스레드 덤프 정보를 확인할 수 있습니다. 자세한 내용은 [다음 문서](#thread-details)를 참조하세요.

#### 소켓 오픈 개수[​](#-9 "-9에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 소켓 오픈 개수

![소켓 오픈 개수](/img/ipa-open-socket-java.png)

Java 애플리케이션이 TCP 기능을 수행하기 위해 오픈한 소켓(Socket) 정보를 확인할 수 있습니다.

#### 메소드 성능 상태[​](#-10 "-10에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 메소드 성능 상태

Java 애플리케이션에서 수행 중인 메소드(Method)의 상세 정보를 확인할 수 있습니다.

#### 데이터소스 상태[​](#-11 "-11에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 데이터소스 상태

![데이터소스 상태](/img/ipa-datasource-java.png)

데이터소스(DataSource)의 상태를 확인할 수 있습니다.

#### 시스템 GC[​](#-12 "-12에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 시스템 GC

![시스템 GC](/img/ipa-system-gc-java.png)

JVM(자바 가상 머신)의 Heap 영역에서 동적으로 할당했던 메모리 중 필요 없게 된 메모리 객체(garbage)를 모아 제거할 수 있습니다. 실행 버튼을 선택하면 GC 프로세스를 실행하게 되며, 실행 전 후의 메모리 용량을 확인할 수 있습니다.

#### 힙 덤프[​](#-13 "-13에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 힙 덤프

![힙 덤프](/img/ipa-heap-dump-java.png)

Java 애플리케이션 실행 중 메모리 누수 등의 문제가 발생하면 관련된 문제를 정리하여 덤프 파일을 생성할 수 있습니다. 힙 덤프 확보 버튼을 선택하세요.

노트이 기능은 Java 에이전트 1.5.2 버전 이상에서 지원합니다. 에이전트 설정에서 `heapdump_enabled` 옵션을 `true`로 설정하세요. 힙 덤프 확보 버튼을 선택해 힙 덤프 파일을 만드는 기능을 활성화합니다. 매번 힙 덤프를 자동 생성하지 않으며 해당 옵션이 성능에 영향을 주진 않습니다. 그러나 덤프 확보 작업은 성능에 영향을 미칠 수 있습니다.

힙 덤프 확보 작업은 부하가 큰 작업에 속합니다. 부하와 별개로 힙 덤프가 모두 추출될 때까지 애플리케이션의 코드는 실행이 중지(stop the world)되기 때문에 사용자가 느끼는 성능 차이는 더 심할 수 있습니다.

#### 쓰로틀링 설정[​](#-14 "-14에 대한 직접 링크")

홈 화면 > 프로젝트 선택 > 인스턴스 성능 관리 > 쓰로틀링 설정

![쓰로틀링 설정](/img/ipa-set-throttling-java.png)

Java 애플리케이션의 부하량 제어와 관련한 에이전트 설정을 확인하고 옵션을 설정할 수 있습니다. 부하량 제어와 관련한 에이전트 설정에 대한 자세한 내용은 [다음 문서](/java/agent-load-amount)를 참조하세요.

스레드 덤프 분석하기[​](#thread-details "스레드 덤프 분석하기에 대한 직접 링크")
-------------------------------------------------------

스레드 목록/덤프 탭에서 확인할 수 있는 정보에 대해 안내합니다.

### 스레드 상태[​](#stateofthread "스레드 상태에 대한 직접 링크")

스레드의 상태는 `java.lang.Thread` 클래스 내부에 `State`라는 이름의 Enumerated Types(열거형)으로 선언된 항목들입니다.

* `NEW`: 스레드가 생성되었지만 아직 실행되지 않은 상태입니다.
* `RUNNABLE`: 현재 CPU를 점유하고 작업을 수행 중인 상태입니다. 운영체제의 자원 분배로 `WAITING` 상태가 될 수도 있습니다.
* `WAITING`: `wait()`, `join()`, `park()` 메소드 등를 이용해 대기하고 있는 상태입니다.
* `TIMED_WAITING`: `sleep()`, `wait()`, `join()`, `park()` 메소드 등을 이용해 대기하고 있는 상태, `WAITING` 상태와 다른 점은 주어진 시간 동안 대기하고 있는 상태입니다. 외부적인 변화 뿐만 아니라 시간에 의해서도 대기 상태가 해제될 수 있습니다.
* `BLOCKED`: 사용하려는 개체의 락(Lock)이 풀릴 때까지 대기하고 있는 상태입니다.
* `TERMINATED`: 실행을 마친 상태입니다.

### 스레드 덤프 정보[​](#스레드-덤프-정보 "스레드 덤프 정보에 대한 직접 링크")

스레드 목록에서 각 스레드의 ![](/img/ico-expander-black.svg) 버튼을 선택하면 스레드 덤프 정보를 확인할 수 있습니다.

![스레드 덤프 정보](/img/ipa-java-thread-list.png)

#### 스택



| 항목 | 속성 | 설명 |
| --- | --- | --- |
| 스레드 ID | `threadId` | 스레드에 할당된 고유 ID |
| Lock 소유주 ID | `lockOwnerId` | 스레드가 차단된 개체의 모니터(Monitor) 잠금을 유지하는 스레드 ID |
| 대기수 | `waitedCount` | 스레드가 `WAITING` 또는 `TIMED_WAITING` 상태가 된 총 횟수 |
| 블록 개수 | `blockedCount` | 스레드가 `BLOCKED` 상태가 된 총 횟수 |
| 대기 시간 | `waitedTime` | 스레드가 `WAITING` 상태를 지속한 경과 시간(밀리초), 스레드 경합 모니터링이 비활성화된 경우 `-1` 반환 |
| 스레드 CPU 시간 | `threadCpuTime` | 스레드의 CPU 시간 합계(나노초)를 밀리초로 계산하여 표시, CPU 시간 측정을 비활성화한 경우 `-1` 반환 |
| 상태 | `threadstate` | 스레드 상태 |
| 블록 시간 | `blockedTime` | 스레드가 `BLOCKED` 상태가 된 후 경과 시간(밀리초), 스레드 경합 모니터링이 비활성화된 경우 `-1` 반환 |
| 스레드 명 | `threadName` | 스레드 고유 이름 |
| Lock 이름 | `lockName` | 스레드의 입력이 차단되거나 `Object.wait` 메소드를 통해   통지를 기다리는 모니터 잠금을 표시한 문자열 |
| Lock 소유주 이름 | `lockOwnerName` | 스레드가 차단되는 객체의 모니터 잠금을 수용하는 스레드 이름 |
| 스레드 사용자 시간 | `threadUserTime` | 스레드가 사용자 모드에서 실행한 CPU 시간(나노초)을 밀리초로 계산하여 표시 |

노트스레드 정보에 대한 자세한 내용은 [다음 링크](https://docs.oracle.com/javase/8/docs/api/java/lang/management/ThreadInfo.html)를 참조하세요.

#### Stack 추적[​](#-1 "-1에 대한 직접 링크")

예외가 발생했을 때 스택(Stack) 추적을 표시합니다. 스택 프레임 목록으로 코드가 호출한 메소드 정보가 포함되어 있습니다.

