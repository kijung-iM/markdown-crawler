통계
==

자바(Java) 애플리케이션 모니터링을 위한 다양한 통계 수집 기능 관련 에이전트 옵션을 안내합니다. 성능 카운터 확장, 도메인별 트랜잭션 수집, 멀티 서버 트랜잭션 의존성 분석, 로그인 유형별 및 Referer 별 통계 수집 등을 포함합니다. 또한 SQL, HTTP Call, 오류 통계와 사용자 에이전트 정보 수집에 대한 최대 레코드 수 제한 설정도 확인할 수 있습니다.

* **addin\_monitor\_num** Int

기본값 `0`

성능 카운터 확장을 위해 추가 선언할 클래스 수를 설정합니다. `addin_monitor_num`에 설정한 값만큼 `addin_monitor_x`를 선언합니다.
* **addin\_monitor\_0** Int

기본값 `0`

whatap.conf
```
  
addin_monitor_num=2  
  
addin_monitor_0=a.a.Class1  
  
addin_monitor_1=a.a.Class2  
  

```
* **stat\_domain\_enabled** Boolean

기본값 `false`

클라이언트의 접속 도메인별 트랜잭션 통계 수집 기능을 활성화합니다.
* **stat\_domain\_max\_count** Int

기본값 `7000`

하나의 JVM에서 5분 동안 수집할 도메인별 트랜잭션 통계의 최대 레코드 수입니다.
* **stat\_mtrace\_enabled** Boolean

기본값 `false`

멀티 서버 트랜잭션에서 Caller & Callee 간에 버전 별 의존성 통계를 수집합니다.
* **mtrace\_spec** String

기본값 `v1`

현재 인스턴스의 애플리케이션 버전을 설정합니다. 임의의 문자열을 설정할 수 있습니다. 이 데이터는 호출 통계를 위해 사용합니다.
* **stat\_mtrace\_max\_count** Int

기본값 `7000`

멀티 서버 트랜잭션에서 Caller & Callee 간에 버전별 의존성 통계의 최대 레코드 수입니다.
* **stat\_login\_enabled** Boolean

기본값 `false`

로그인별 트랜잭션 통계를 수집합니다.
* **stat\_login\_max\_count** Int

기본값 `7000`

하나의 JVM에서 5분 동안 수집할 로그인 별 트랜잭션 통계의 최대 레코드 수입니다.
* **stat\_referer\_enabled** Boolean

기본값 `false`

Referer별 트랜잭션 통계를 수집합니다.
* **stat\_referer\_max\_count** Int

기본값 `7000`

하나의 JVM에서 5분 동안 수집할 Referer 별 트랜잭션 통계의 최대 레코드 수입니다.
* **stat\_tx\_max\_count** Int

기본값 `5000`

트랜잭션 통계 정보의 개수를 제한합니다. 5분 동안 수집해 서버에 전송하는 통계 정보의 최대 레코드 수를 제한합니다.
* **stat\_sql\_max\_count** Int

기본값 `5000`

SQL 통계 정보의 개수를 제한합니다. 5분 동안 수집해 서버에 전송하는 통계 정보의 최대 레코드 수를 제한합니다.
* **stat\_httpc\_max\_count** Int

기본값 `5000`

Http Call 통계 정보의 개수를 제한합니다. 5분 동안 수집해 서버에 전송하는 통계 정보의 최대 레코드 수를 제한합니다.
* **stat\_error\_max\_count** Int

기본값 `1000`

Error 통계 정보의 개수를 제한합니다. 5분 동안 수집해 서버에 전송하는 통계 정보의 최대 레코드 수를 제한합니다.
* **stat\_useragent\_max\_count** Int

기본값 `500`

User Agent 통계 정보의 개수를 제한합니다. 5분 동안 수집해 서버에 전송하는 통계 정보의 최대 레코드 수를 제한합니다.
