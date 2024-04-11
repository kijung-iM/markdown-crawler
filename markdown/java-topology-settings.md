에이전트 옵션 설정
==========

토폴로지 기능을 이용하기 위해 에이전트에 옵션을 적용하는 방법을 제공합니다.

적용 가능 에이전트 및 버전[​](#적용-가능-에이전트-및-버전 "적용 가능 에이전트 및 버전에 대한 직접 링크")
----------------------------------------------------------------

Java 에이전트 1.7.1 버전 이상

whatap.conf 설정[​](#whatapconf-설정 "whatap.conf 설정에 대한 직접 링크")
------------------------------------------------------------

다음은 토폴로지 표현을 위해 *whatap.conf* 파일에 설정할 수 있는 정보 수집 옵션입니다.

* **tx\_caller\_meter\_enabled** Boolean

기본값 `false`

트랜잭션 정보로 토폴로지 통계를 생성합니다. `mtrace_enabled` 옵션의 값이 `true`이면 동작합니다.
* **sql\_dbc\_meter\_enabled** Boolean

기본값 `false`

데이터 베이스 연결 정보로 토폴로지 통계를 생성합니다.
* **httpc\_host\_meter\_enabled** Boolean

기본값 `false`

토폴로지 맵에서 httpc outbound 정보를 표현합니다.
* **actx\_meter\_enabled** Boolean

기본값 `false`

토폴로지 맵에서 액티브 트랜잭션 상태를 표현합니다.

그룹 및 통합 토폴로지 사용을 위해 다음과 같이 옵션을 추가하세요.

Java: add JVM option
```
-Dwhatap.okind={그룹 식별자}  

```
