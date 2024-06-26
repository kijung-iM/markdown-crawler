사용자 수
=====

자바(Java) 웹 애플리케이션 서버에 연결된 사용자 수를 에이전트 설정을 통해 집계하는 방법을 안내합니다. 실시간 사용자 집계 활성화 여부 설정, 사용자 수를 집계하기 위한 쿠키 제한 설정, IP 주소 또는 HTTP 헤더 특정 값을 기준으로 한 사용자 집계 방법, 클라이언트 IP 정보 추적을 위한 HTTP 헤더 설정 등을 포함합니다.

* **trace\_user\_enabled** Boolean

기본값 `true`

실시간 사용자 집계 여부를 설정합니다. 사용자 추적 옵션이 중복 설정된 경우 동작 우선 순위는 다음과 같습니다.


> 1. **trace\_user\_using\_ip** / **wclient\_using\_ip**
> 	2. **trace\_user\_using\_jsession**
> 	3. **user\_header\_ticket** / **wclient\_header\_ticket**

노트Java 에이전트 2.2.0 버전 이상의 경우 `wclient_using_ip`, `wclient_header_ticket` 옵션을 이용하세요.

* **trace\_user\_cookie\_limit** / **wclient\_cookie\_limit** Int

기본값 `2048`

사용자 집계를 위해 쿠키를 발행하는 경우 기존 쿠키가 너무 많다면 쿠키 오버플로어가 발생할 수 있습니다. 이를 방지하기 위해 limit을 설정합니다.

노트Java 에이전트 2.2.0 버전 이상의 경우 `wclient_cookie_limit` 옵션을 이용하세요.
* **trace\_user\_using\_ip** / **wclient\_using\_ip** Boolean

기본값 `true`

실  시간 사용자를 IP 주소 기반으로 집계합니다. IP 주소가 아닌 쿠키를 기반으로 사용자를 구분하고 싶으면 값을 `false`로 변경하세요.

노트Java 에이전트 2.2.0 버전 이상의 경우 `wclient_using_ip` 옵션을 이용하세요.
* **user\_header\_ticket** / **wclient\_header\_ticket** String

HTTP 헤더의 특정 값으로 사용자 수를 집계하고자 하는 경우 해당 Key 값을 설정합니다. 모바일 클라이언트인 경우 사용자 구분을 위해 header를 사용한다면 다음 옵션을 이용할 수 있습니다.

whatap.conf
```
user_header_ticket=login  

```
노트Java 에이전트 2.2.0 버전 이상의 경우 `wclient_header_ticket` 옵션을 이용하세요.

* **trace\_http\_client\_ip\_header\_key** String [​](/java/agent-number-of-user#trace_http_client_ip_header_key)

클라이언트 IP(Remote IP)의 정보를 특정 HTTP 헤더의 값으로 변경해 설정하는 기능입니다. 프록시(Proxy) 환경에서 `X-Forwarded-For` 헤더 값을 클라이언트 IP로 설정할 수 있습니다.

WEB/WAS 앞에 L4와 같은 로드밸런서가 위치한 경우 클라이언트의 IP 주소가 아닌 L4의 IP 주소가 Remote Address가 되는 경우가 있습니다. 이 상황에서 실제 클라이언트 IP 정보가 http 헤더에 특정 키 값으로 기록되는 경우라면 해당 키 값으로 대체할 수 있습니다.
* **trace\_user\_using\_jsession** Boolean

기본값 `false`

실시간 사용자를 SESSIONID 기반으로 집계합니다.
