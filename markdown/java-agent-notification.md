에이전트 알림
=======

자바(Java) 에이전트를 통해 애플리케이션 서버에서 발생하는 다양한 이벤트에 대한 알림 설정 방법을 제공합니다. 트랜잭션 재귀 호출, 서비스 거절, HTTPC 연결 오류, 힙 및 디스크 사용량 초과, CPU 사용량 임계치 도달, DB 커넥션 중복 할당 및 예외 발생 시 이벤트 알림을 설정하는 옵션을 포함합니다. 각 이벤트별로 발행 간격, 발행 여부, 임계치 설정 등 세밀한 조정을 할 수 있습니다.

* **recursive\_event\_interval** MiliSeconds

기본값 `300000`

트랜잭션의 재귀 호출에 대한 이벤트 알림 발행 간격을 설정합니다.
* **reject\_event\_enabled** Boolean

기본값 `false`

서비스 거절(호출 부하 제한/거절) 시 이벤트 알림 발행 여부를 설정합니다.
* **reject\_event\_interval** MiliSeconds

기본값 `300000`

서비스 거절(호출 부하 제한/거절) 시 이벤트 알림 발행 간격을 설정합니다.
* **httpc\_event\_enabled** Boolean

기본값 `false`

HTTPC 연결 오류 발생 시 이벤트 알림 발행 여부를 설정합니다.
* **httpc\_event\_interval** MiliSeconds

기본값 `300000`

HTTPC 연결 오류 발생 시 이벤트 알림 발행 간격을 설정합니다.
* **heap\_event\_enabled** Boolean

기본값 `false`

힙 사용량 임계 도달 시 이벤트 알림 발행 여부를 설정합니다.
* **heap\_event\_percent** Percentage

기본값 `90`

힙 사용량 이벤트 알림 발행 기준 임계치를 설정합니다.
* **heap\_event\_duration** MiliSeconds

기본값 `30000`

힙 사용량 이벤트 알림 발행 기준 지속 시간을 설정합니다.
* **heap\_event\_interval** MiliSeconds

기본값 `300000`

힙 사용량 이벤트 알림 발행 간격을 설정합니다.
* **heap\_event\_action** String

기본값 `NONE`

힙 사용량 이벤트 발생 시 실행할 동적 로딩 코드를 설정합니다.

노트*`$WHATAP_HOME`/plugin/ActionScript.x* 파일에 작성한 Java 코드에 전달할 ID (`$id`로 전달함)
* **disk\_event\_enabled** Boolean

기본값 `false`

디스크 사용량 임계치 도달 시 이벤트 알림 발행 여부를 설정합니다.
* **disk\_event\_percent** Percentage

기본값 `90`

디스크 사용량 이벤트 알림 발행 기준 임계치를 설정합니다.
* **disk\_event\_interval** MiliSeconds

기본값 `300000`

디스크 사용량 이벤트 알림 발행 간격을 설정합니다.
* **disk\_event\_action** String

디스크 사용량 이벤트 발생 시 실행할 동적 로딩 코드를 설정합니다.

노트*`$WHATAP_HOME`/plugin/ActionScript.x* 파일에 작성한 Java 코드에 전달할 ID (`$id`로 전달함)
* **cpu\_event\_enabled** Boolean

기본값 `false`

CPU 사용량 임계 도달 시 이벤트 알림 발행 여부를 설정합니다.
* **cpu\_event\_percent** Percentage

기본값 `90`

CPU 사용량 이벤트 알림 발행 기준 임계치를 설정합니다.
* **cpu\_event\_duration** MiliSeconds

기본값 `30000`

CPU 사용량 이벤트 알림 발행 기준 지속시간을 설정합니다.
* **cpu\_event\_interval** MiliSeconds

기본값 `300000`

CPU 사용량 이벤트 알림 발행 간격을 설정합니다.
* **cpu\_event\_action** String

CPU 사용량 이벤트 발생 시, 실행할 동적 로딩 코드에 전달할 ID를 설정합니다.

노트*`$WHATAP_HOME`/plugin/ActionScript.x* 파일에 작성한 Java 코드에 전달할 ID (`$id`로 전달함)
* **dbc\_dup\_event\_enabled** Boolean

기본값 `false`

DB Connection이 중복 할당될 경우 이벤트 알림 발행 여부를 설정합니다.
* **dbc\_dup\_event\_fullstack\_enabled** Boolean

기본값 `false`

DB Connection이 중복 할당될 때 Stack 확보 여부를 설정합니다.
* **exception\_event\_enabled** Boolean

기본값 `false`

Exception 발생 시 이벤트 알림 발행 여부를 설정합니다.
* **exception\_event\_interval** MiliSeconds

기본값 `60000`

Exception 발생 시 이벤트 알림 발행 간격을 설정합니다.
* **exception\_event\_set** String

대상 Exception을 설정합니다. 여러 개인 경우 쉼표(,)를 구분자로 사용하세요.
* **exception\_event\_action** String

이벤트 발생 시 실행할 동적 로딩 코드를 설정합니다.

노트*`$WHATAP_HOME`/plugin/ActionScript.x* 파일에 작성한 Java  코드에 전달할 ID (`$id`로 전달함)
