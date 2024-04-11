토폴로지 맵
======

자바(Java) 에이전트가 수집한 데이터를 사용하여 애플리케이션의 토폴로지 맵을 생성하는 에이전트 설정 옵션을 안내합니다. 트랜잭션 호출자, 데이터베이스 연결 정보, HTTPC 아웃바운드 정보, 액티브 트랜잭션 상태 등의 다양한 지표를 통해 시스템의 토폴로지를 시각화하고 분석할 수 있습니다.

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
