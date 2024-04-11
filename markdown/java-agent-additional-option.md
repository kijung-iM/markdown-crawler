부가 기능
=====

자바(Java) 애플리케이션의 모니터링 수준을 사용자의 필요에 맞게 조정할 수 있는 추가적인 에이전트 설정 옵션을 안내합니다. SQL 파라미터 수집, HTTP 파라미터 및 헤더 정보 수집, 사용자 IP 정보 추출, 사용자 수 추적 방법 선택, SAP Function 추적 등을 포함합니다. 이 옵션들을 통해 보다 세밀한 데이터 수집 및 분석이 가능하며, 특히 보안이 중요한 환경에서 필요에 따라 옵션을 조정할 수 있습니다.

다음은 자주 사용하지만 보안 등의 이유로 에이전트 기본 설정에서 제외한 옵션입니다. 필요하다면 아래 옵션을 추가해 적용할 수 있습니다.

* **profile\_sql\_param\_enabled** Boolean

기본값 `true`

SQL 파라미터를 수집합니다.
* **profile\_http\_parameter\_enabled** Boolean

기본값 `true`

HTTP 파라미터를 수집합니다.
* **profile\_http\_header\_enabled** Boolean

기본값 `false`

HTTP 헤더 정보를 수집합니다.
* **trace\_http\_client\_ip\_header\_key** String

기본값 `X-Forwarded-For`

사용자 IP 정보를 HTTP 헤더의 키에서 추출합니다.
* **trace\_user\_method** / **wclient\_cookie\_limit** Boolean

기본값 `cookie`

사용자 수 추적을 쿠키 기반으로 합니다.

노트Java 에이전트 2.2.0 버전 이상의 경우 `wclient_trace_type` 옵션을 이용하세요.
* **hook\_httpc\_sap3\_enabled** Boolean

기본값 `true`

SAP JCO을 사용하는 경우 SAP Function을 추적합니다.
