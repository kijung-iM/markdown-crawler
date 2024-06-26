트랜잭션
====

트랜잭션이란 사용자 브라우저의 요청을 처리하기 위한 서버 사이드의 Logical Unit of Work(LUW)를 말합니다. 개별 웹서비스(URL) 요청에 대한 처리 과정이 바로 트랜잭션입니다. 웹 애플리케이션에서 트랜잭션은 웹서비스(URL)에 대한 HTTP Request를 받아 Response를 반환하는 과정입니다.

애플리케이션의 성능은 이 트랜잭션들의 성능으로 요약할 수 있습니다. 트랜잭션 성능은 트랜잭션 시작에서부터 종료 시점, 응답시간 및 자원 사용량 혹은 트랜잭션 호출자 속성 등의 정보를 포함합니다.

기본적으로 트랜잭션 응답 분포와 트랜잭션 통계를 통해서 트랜잭션 성능을 분석할 수 있습니다.

트랜잭션 트레이싱[​](#트랜잭션-트레이싱 "트랜잭션 트레이싱에 대한 직접 링크")
----------------------------------------------

* **profile\_basetime** MiliSecond

기본값 `500`

트레이스의 상세 정보를 수집할 최소 응답 시간을 설정합니다. 설정한 값 이하의 시간 내에 트랜잭션이 종료된 경우 트레이스 정보를 수집하지 않습니다. 단, 5분 단위로 최초 호출된 URL과 에러가 발생한 트랜잭션에 대한 트레이스 정보는 수집합니다.

노트`profile_basetime` 옵션에 상관없이 에러를 수집하려면 `profile_concern_error_enabled` 옵션을 `true`로 설정하세요. 기본값 `false`로 설정하면 에러를 샘플링하게 됩니다

* **profile\_step\_normal\_count** Int

기본값 `1000`

트랜잭션 트레이스의 최대 스텝 수를 설정합니다.
* **profile\_step\_heavy\_count** Int

기본값 `1020`

Heavy한 스텝의 경우 트레이스 기본 스텝 수를 초과하더라도 정해진 값만큼 기록합니다.
* **profile\_step\_max\_count** Int

기본값 `1024`

트레이스 스텝의 최대 수 를 설정합니다. 수집된 트레이스 스텝 수가 이 값을 초과하면 이후 수집되는 스텝들은 모두 버려집니다. `profile_step_heavy_count`을 최대 1000으로 설정하면 `profile_step_max_count`만큼 액티브 스택이 수집됩니다.
* **profile\_step\_heavy\_time** MiliSecond

기본값 `100`

Heavy한 스텝의 기준을 설정합니다. 설정한 값보다 수행 시간이 긴 경우 `profile_step_normal_count` 값을 초과하더라도 `profile_step_heavy_count`에 설정한 값만큼 기록합니다.
* **active\_stack\_count** Int

기본값 `100`

트랜잭션 내에서 수집하는 액티브 스택의 최대 수를 설정합니다.
* **profile\_method\_resource\_enabled** Boolean

기본값 `false`

트레이스에서 method 스텝을 수집할 때 해당 스텝에서 사용한 CPU와 메모리 사용량을 추적합니다.
* **profile\_position\_method** String

설정한 메소드를 수행하는 시점의 StackTrace를 기록합니다.
* **profile\_position\_depth** Int

기본값 `50`

position 추적을 위해 StackTrace를 기록할 때 최대 라인 수를 설정합니다.
* **trace\_error\_callstack\_depth** Int

기본값 `50`

Error 발생 시 수집하는 StackTrace의 최대 라인 수를 설정합니다.
* **trace\_active\_callstack\_depth** Int

기본값 `50`

액티브 스택에서 수집하는 StackTrace의 최대 라인수를 설정합니다.

* **trace\_active\_transaction\_yellow\_time** MiliSecond

기본값 `3000`

액티브 트랜잭션의 아크이퀄라이저에서 노란색으로 표현할 기준을 설정합니다.
* **trace\_active\_transaction\_red\_time** MiliSecond

기본값 `8000`

액티브 트랜잭션의 아크이퀄라이저에서 빨간색으로 표현할 기준을 설정합니다.
* **hook\_method\_patterns** String

응답시간을 측정할 메소드를 설정합니다. 마지막 마침표(.)를 구분자로 클래스 FullName과 메소드로 구분되며 별표(\*)를 와일드 카드로 사용할 수 있습니다. 대상이 여러 개인 경우 쉼표(,)로 구분합니다.

whatap.conf
```
hook_method_patterns=a.b.C1.*  

```
* **hook\_method\_supers** String

특정 클래스를 상속받은 메소드의 응답시간을 측정하고자 할 때 Super Class를 설정합니다. 클래스 FullName을 설정하며 대상이 여러 개인 경우 쉼표(,)로 구분합니다.

whatap.conf
```
hook_method_supers=a.b.C1  

```
* **hook\_method\_interfaces** String

특정 인터페이스를 구현한 메소드의 응답시간을 측정하고자 할 때 Interface를 설정합니다. 인터페이스 FullName을 설정하며 대상이 여러 개인 경우 쉼표(,)로 구분합니다.
* **hook\_method\_ignore\_classes** String

메소드  트레이스를 설정할 때 트레이스에서 제외하고 싶은 클래스들을 설정합니다.
* **hook\_method\_access\_public\_enabled** Boolean

기본값 `true`

메소드 트레이스를 설정할 때 public 메소드에 대해서만 별도 대상으로 처리할지 여부를 설정합니다.
* **hook\_method\_access\_private\_enabled** Boolean

기본값 `false`

메소드 트레이스를 설정할 때 private 메소드에 대해서만 별도 대상으로 처리할지 여부를 설정합니다.
* **hook\_method\_access\_protected\_enabled** Boolean

기본값 `true`

메소드 트레이스를 설정할 때 protected 메소드에 대해서만 별도 대상으로 처리할지 여부를 설정합니다.
* **hook\_method\_access\_none\_enabled** Boolean

기본값 `true`

메소드 트레이스를 설정할 때 no access indicated 메소드에 대해서만 별도 대상으로 처리할지 여부를 설정합니다.
* **stacklog\_socket\_port** TCP\_PortNumber

기본값 `0`

목적지의 TCP 포트를 설정하면 Socket.connect() 시점 StackTrace를 에이전트 로그로 기록합니다. 기본 설정으로 확인되지 않는 DB 연결, HTTPC 연결 등을 추적할 때 사용할 수 있습니다.

주의설정한 목적지로 연결 시마다 매번 StackTrace를 기록합니다. 성능 저하를 유발할 수 있습니다. 디버깅 용도로 선별한 에이전트에 한시적으로만 사용해야 합니다.

DB 연결 상태 추적 예시, `stacklog_socket_port=1521`
* **trace\_concern\_error\_enabled** Boolean

기본값 `true`

`trace_basetime` 또는 `profile_basetime` 옵션과 무관하게 에러가 있는 상세 트레이스에 대한 수집 여부를 설정합니다.

예외 처리[​](#exception "예외 처리에 대한 직접 링크")
--------------------------------------

* **biz\_exceptions** String

Business Exception을 등록합니다.

팁에러 클래스 수집 / 히트맵 표시 레벨: INFO(파란색) / 에러 통계 포함

노트Java 에이전트 [v2.2.20](/release-notes/java/java-2_2_20) 이상에서는 등록한 비즈니스 Exception을 에러 통계로 수집합니다. v2.2.20 미만에서는 등록한 비즈니스 Exception을 에러 통계에서 제외합니다. 다만 트레이스 상세에서는 나타납니다.
* **biz\_exceptions\_status** String `Java Agent v2.2.20 or later`

Business Exception 발생 시 이벤트 알림을 억제할 Business Exception과 Status를 설정합니다. 이 옵션에서 설정한 **Business Exception:Status**에 대해서는 이벤트 레벨이 INFO로 변경됩니다. Business Exception과 Status는 콜론(:)으로 구분하며, 하나의 Business Exception에 여러 개의 Status를 사용하는 경우 앰퍼샌드(&)로 구분합니다. 쉼표를 구분자로 이용해 여러 개를 설정할 수 있습니다.

whatap.conf
```
# example  
biz_exceptions_status=java.util.concurrent.TimeoutException:400&404&408,java.lang.Exception:200  

```
팁에러 클래스 수집 / 히트맵 표시 레벨: INFO(파란색) / 에러 통계 포함
* **ignore\_exceptions** String

등록한 Exception의 에러 자체를 무시합니다.

팁에러 클래스 무시 / 히트맵 표시 레벨: INFO(파란색) / 에러 통계 미포함
* **transaction\_status\_error\_enable** Boolean

기본값 `true`

HTTP 401, 403과 같이 정상 응답이 아닌 HTTP 상태 코드를 반환하는 경우 에러로 처리할지 여부를 설정합니다.
* **status\_ignore** String

무시하려는 HTTP 상태 코드를 설정할 수 있습니다. 여러 값을 대상으로 할 경우 쉼표(,)를 구분자로 사용하세요.

whatap.conf
```
# example  
status_ignore=408,500  

```
팁Status 에러 무시 / 히트맵 표시 레벨: INFO(파란색) / 에러 통계 미포함
* **status\_ignore\_set** String

`whatap.error.STATUS_ERROR`를 무시합니다. 여러 값을 대상으로 할 경우 쉼표(,)를 구분자로 사용하세요.

whatap.conf
```
# example  
status_ignore_set=/api/test/timeout/{time}:408,/api/test/timeout:200,/error:500  

```
팁Status 에러 세트 무시 / 히트맵 표시 레벨: INFO(파란색) / 에러 통계 미포함
* **httpc\_status\_error\_enable** Boolean

기본값 `true`

HTTP 상태 코드가 에러인 경우 수집 여부를 설정합니다. 클라이언트 에러 응답(`400` 이상), 서버 에러 응답(`500` 이상)이 해당됩니다.

노트HTTP 상태 코드에 대한 자세한 내용은 [다음 링크](https://developer.mozilla.org/docs/Web/HTTP/Status)를 참조하세요.
* **httpc\_status\_ignore** String

HTTP 상태 코드가 에러(`HTTPC_ERROR`)인 경우 무시할 수 있습니다. 여러 값을 대상으로 할 경우 쉼표(,)를 구분자로 사용하세요.

팁HTTP 상태 에러 코드 무시 / 에러 통계 미포함
* **httpc\_status\_url\_ignore\_set** String

`whatap.error.HTTPC_ERROR`를 무시합니다. 여러 값을 대상으로 할 경우 쉼표(,)를 구분자로 사용하세요.

`httpc_status_url_ignore_set=/a/b/c:400,/a/ab/c:404`와 같이 설정하세요. 이때 url은 통계/에러 분석에서 `HTTPC_URL` 값을 입력합니다.

팁HTTP 상태 에러 코드 무시 / 에러 통계 미포함
* **trace\_sql\_exception\_enabled** Boolean

기본값 `true`

JDBC 드라이버에서 SqlException 발생 시 추적 여부를 설정합니다. 옵션 값을 `false`로 설정하면 사용자 정의 예외 처리로 `biz_exceptions` 처리할 수 있습니다.

HTTP 트랜잭션 추적[​](#http-트랜잭션-추적 "HTTP 트랜잭션 추적에 대한 직접 링크")
-------------------------------------------------------

* **profile\_http\_header\_enabled** Boolean

기본값 `false`

트레이스 내역에 http 헤더 정보를 기록하려면 `true`로 설정하세요.
* **profile\_http\_parameter\_enabled** Boolean[​](/java/agent-transaction#profile_http_parameter)

기본값 `false`

트레이스 내역에 http 파라미터 정보를 기록하려면 `true`로 설정하세요. 파라미터는 별도 보안키를 입력해야 조회할 수 있습니다.

노트
	+ **Java 에이전트 2.2.2 버전 이전**: 보안 키는 WAS 서버 *`${WHATAP_AGENT_HOME}`/paramkey.txt* 파일 내에 6자리로 작성합니다. *paramkey.txt* 파일이 존재하지 않는 경우 랜덤 값으로 자동 생성합니다.
	+ **Java 에이전트 2.2.2 버전 이후**: 보안 키는 WAS 서버 *`${WHATAP_AGENT_HOME}`/security.conf* 파일 내에 `paramkey` 키값을 확인하세요. *security.conf* 파일이 존재하지 않을 경우 `paramkey` 키값을 **WHATAP**으로 자동 생성합니다.
	+ 보안키 설정 파일에 대한 자세한 내용은 [다음 문서](/java/install-agent#security)를 참조하세요.
* **profile\_http\_header\_url\_prefix** String

트레이스 내역에 http 헤더 정보를 기록할 대상 URL의 prefix를 정의할 때 사용합니다.
* **profile\_http\_parameter\_url\_prefix** String

트레이스 내역에 http 파라미터 정보를 기록할 대상 URL의 prefix를 정의할 때 사용합니다.
* **trace\_transaction\_name\_key** String

HTTP request parameter 값을 해당 옵션에 설정하면, 파라미터 값을 추출하여 트랜잭션의 이름 마지막에 추가합니다.

예를 들어, HTTP 파라미터로 `paramKey`를 가진 `/api/test` URL을 호출하는 경우 다음 예제와 같이 설정하면 트레이스 내역에 `/api/test$paramKey={value}`로 트랜잭션 이름을 표시합니다. 다만 여러 개의 파라미터를 등록할 수는 없습니다.

whatap.conf
```
# example  
trace_transaction_name_key=paramKey  

```

* **trace\_normalize\_enabled** Boolean

기본값 `true`

트랜잭션 URL을 파싱해 정규화하는 기능을 활성화합니다.

노트`false`로 값을 변경하면 패스 파라미터 파싱을 비활성화합니다. 이 경우 통계 데이터의 의미가 약화됨으로 디버그 용도로만 잠시 사용하는 것을 권장합니다.
* **trace\_auto\_normalize\_enabled** Boolean

기본값 `true`

트랜잭션 URL 정규화할 때 패턴 값을 어노테이션에서 추출해 자동으로 파싱하는 기능을 활성화합니다.
* **trace\_normalize\_urls** String

정규화할 트랜잭션 URL 패턴을 설정합니다. 호출 URL 패턴을 파싱해 패스 파라미터를 제거합니다.

노트예시, `/a/{v}/b`라고 선언하면 `a/123/b` → `a/{v}/b`로 치환합니다. 여러 개를 등록할 때는 쉼표(,)를 구  분자로 사용하세요. 치환 패턴 정리 후 보완이 필요합니다.
* **web\_static\_content\_extensions** String

기본값 `js, htm, html, gif, png, jpg, css, swf, ico`

스태틱 콘텐츠임을 판단하는 확장자를 설정합니다. 이 옵션에 설정한 확장자를 가진 트랜잭션들은 트레이스 추적과 카운팅에서 제외합니다.
* **trace\_transaction\_name\_header\_key** String

설정한 HTTP 헤더 키에서 추출한 값을 트랜잭션의 이름 마지막에 추가합니다.
* **recursive\_max** Int

기본값 `1000000`

트랜잭션의 재귀 호출 여부 검출을 위한 옵션입니다. 단일 트랜잭션으로부터 파생되는 재귀 호출 횟수를 카운트하여 이벤트 알림을 발행하기 위한 기준을 설정합니다.

노트HTTP URL 재귀 호출을 대상으로 합니다. jsp:forward를 통해 재호출하는 케이스도 카운트에 포함합니다.
* **hook\_httpservlet\_classes** String

HTTP 트랜잭션의 END POINT를 추가로 설정합니다. 메소드의 첫 번째 2개의 파라미터는 `HttpServletRequest`와 `HttpServletResponse`만 설정할 수 있습니다.
* **hook\_jsp\_patterns** String

기본값 `org.apache.jasper.servlet.JspServlet.serviceJspFile`

JSP 파일을 로딩하는 메소드를 설정합니다. 트랜잭션 호출 결과로 반환하는 JSP 정보를 트레이스에 표시합니다. 이 옵션을 통해 추가한 설정에 기본값이 자동 추가됩니다.
* **trace\_ignore\_url\_set** String

트랜잭션 추적에서 제외할 URL을 설정합니다. 2개 이상의 값을 설정하려면 쉼표(,)를 구분자로 이용하세요.
* **trace\_ignore\_url\_prefix** String

트랜잭션 추적에서 제외할 URL prefix를 설정합니다. 2개 이상의 값을 설정하려면 쉼표(,)를 구분자로 이용하세요.
* **ignore\_http\_method** String

기본값 `PATCH,OPTIONS,HEAD,TRACE`

설정한 HTTP 메소드(Method)로 요청된 트랜잭션 정보는 수집하지 않습니다. 여러 개를 설정하려면 쉼표(,)를 구분자로 이용하세요.

whatap.conf
```
# e.g. http_method가 OPTIONS, HEAD인 트랜잭션 "추적"  
ignore_http_method=PATCH,TRACE  
  
# e.g. http_method가 OPTIONS, HEAD인 트랜잭션 "무시"  
ignore_http_method=OPTIONS,HEAD  

```
* **trace\_tx\_name\_with\_method\_enabled** Boolean

기본값 `false`

통계 데이터에서 URL을 변경한 URL+method로 수집할 수 있습니다. 통계 또는 트랜잭션 검색 메뉴에서 URL+method로 확인 할 수 있습니다.


> 예시, /api/user+GET, /api/user+POST

NON HTTP 트랜잭션 추적[​](#non-http-트랜잭션-추적 "NON HTTP 트랜잭션 추적에 대한 직접 링크")
-------------------------------------------------------------------

* **trace\_auto\_transaction\_enabled** Boolean

기본값 `false`

트레이스 대상 메소드가 트랜잭션 시작점(`Javax.http.httpservlet`, `hook_service_*`) 내에서 수행하는 경우가 아니라면 수집되지 않습니다. 이 경우 트레이스 대상 메소드가 트랜잭션 시작점이 되도록 설정합니다.

노트주로 개발 환경에서 백그라운드 트랜잭션의 END POINT를 찾을 때 사용합니다.
* **trace\_auto\_transaction\_backstack\_enabled** Boolean

기본값 `true`

`trace_auto_transaction_enabled` 옵션의 값이 `true`인 경우 트랜잭션 시작 시 StackTrace  를 기록합니다. 이를 통해 트랜잭션의 시작점을 찾아낼 수 있습니다.
* **trace\_background\_socket\_enabled** Boolean

기본값 `true`

트랜잭션이 아닌 백그라운드 스레드에 의한 소켓이 오픈될 때도 이를 기록합니다.
* **async\_stack\_enabled** Boolean

기본값 `false`

백그라운드 스레드에 대한 Active Stack 기능 사용 여부를 설정합니다.
* **async\_thread\_match** String

액티브 스택을 덤프할 백그라운드 스레드 이름을 설정합니다. 여러 개를 설정하려면 쉼표(,)를 구분자로 사용하세요. 이름을 설정할 때 'Thread-\*' 처럼 별표(\*)를 사용해 비교 패턴을 사용할 수 있습니다.
* **async\_thread\_parking\_class** String

기본값 `sun.misc.Unsafe`

스택의 Top 메소드가 `async_thread_parking`에 등록한 클래스/메소드일 때 스레드가 파킹 상태에 있다고 판단하고 덤프를 생성하지 않습니다.
* **hook\_service\_patterns** String

NON-Http 트랜잭션 추적을 위한 시작점 패턴을 설정합니다. 와일드카드 문자를 사용할 수 없으며, 2개 이상의 값을 설정하려면 쉼표(,)를 구분자로 이용하세요.
* **hook\_serivce\_ignore\_methods** String

`hook_service_patterns`에서 설정한 내역 중 시작점으로 불필요한 메소드를 추가할 수 있습니다.
* **hook\_service\_supers** String

NON-HTTP 트랜잭션 추적을 위한 시작점의 공통 분모가 특정 클래스의 메소드를 상속 받은 경우라면 공통  분모의 메소드를 설정합니다. 메소드 전체 경로를 입력하세요. 와일드 카드(`*`)를 사용할 수 있으며, 쉼표(,)를 구분자로 이용해 여러 개의 메소드를 등록할 수 있습니다.

whatap.conf
```
hook_service_supers=a.b.C.method,a.b.C.*  

```
* **hook\_service\_interfaces** String

NON-Http 트랜잭션 추적을 위한 시작점의 공통 분모가 특정 인터페이스를 구현한 경우라면 이를 설정합니다.
* **hook\_service\_access\_public\_enabled** Boolean

기본값 `true`

Non Http Demon 프로세스의 트랜잭션을 설정할 때 public 메소드에 대해서만 Access 권한 기준을 on/off 설정합니다.
* **hook\_service\_access\_private\_enabled** Boolean

기본값 `true`

Non Http Demon 프로세스의 트랜잭션을 설정할 때 private 메소드에 대해서만 Access 권한 기준을 on/off를 설정합니다.
* **hook\_service\_access\_protected\_enabled** Boolean

기본값 `true`

Non Http Demon 프로세스의 트랜잭션을 설정할 때 protected 메소드에 대해서만 Access 권한 기준을 on/off를 설정합니다.
* **service\_name\_mode** String

기본값 `full`

트랜잭션 명으로 다음의 옵션을 사용할 수 있습니다.


	+ `full`: Full Class 이름 사용
	+ `class`: 서비스 명칭을 Class 이름으로 사용
	+ `method`: 서비스 명칭을 Method 이름으로 사용
	+ `string`: 서비스 명칭을 문자열 중에서 첫 번째 파라미터로 사용
	+ `arg`: 파라미터 중에서 `service_name_index` 옵션에 설정한 인덱스에 파라미터를 서비스 명칭으로 사용

멀티 트랜잭션 추적[​](#멀티-트랜잭션-추적 "멀티 트랜잭션 추적에 대한 직접 링크")
-------------------------------------------------

* **mtrace\_enabled** Boolean

기본값 `true`

멀티 트랜잭션 추적 기능(Multi Transaction ID, 이하 MTID) 사용 여부를 설정합니다. MTID를 추적하면 등록한 모든 애플리케이션 간의 호출을 확인할 수 있습니다.
* **mtrace\_rate** Percentage

기본값 `10`

최초 트랜잭션이 발생할 때 발급하는 MTID의 발급 비율을 설정하는 옵션입니다.
* **mtrace\_caller\_key** String

기본값 `x-wtap-mst`

MTID 추적에 사용할 Caller Key Name을 설정합니다.
* **mtrace\_callee\_key** String

기본값 `x-wtap-tx`

MTID 추적에 사용할 Callee Key Name을 정합니다.
* **mtrace\_send\_url\_length** Int

기본값 `80`

Http Caller는 Callee에게 자신의 URL을 넘겨줍니다. 이때 URL 길이를 제한하는데, 이 길이의 값을 설정합니다.
* **mtrace\_callee\_id\_send\_enabled** Boolean

기본값 `false`

MTID 추적 시 HTTPC 호출과 함께 발행된 Callee ID를 트레이스에 표현합니다.
* **mtrace\_callee\_id\_recv\_enabled** Boolean

기본값 `false`

MTID 추적 시 수신한 Callee ID를 트레이스에 표현합니다.
* **mtrace\_alltx\_enabled** Boolean

기본값 `false`

log4j와 같은 로깅 시스템과 연계하기 위해서 모든 트랜잭션의 MTID를 추적할 수 있습니다.
* **mtrace\_basetime** Miliseconds

기본값 `100`

`mtrace_alltx_enabled` 옵션의 값이 `true`이면 너무 많은 로그가 남을 수 있습니다. 이때는 트레이스 로깅량을 줄일 필요가 있습니다.
* **stat\_mtrace\_enabled** Boolean

기본값 `false`

Caller와 Callee의 상관관계 통계를 수집합니다. Caller에 적용하면 Caller의 상세 정보를 보내주고 Callee에 적용하면 url   단위 Caller-Callee 호출 통계를 수집 서버로 전송합니다.

트레이스 데이터 샘플링[​](#트레이스-데이터-샘플링 "트레이스 데이터 샘플링에 대한 직접 링크")
-------------------------------------------------------

`Java Agent v2.2.4 or later`* **trace\_sampling\_enabled** Boolean

기본값 `false`

트레이스 데이터 샘플링 수집 여부를 설정할 수 있습니다.
* **trace\_sampling\_tps** Int

기본값 `10000`

트레이스 데이터 샘플링 수를 설정할 수 있습니다. 설정한 샘플링 수를 초과하는 데이터는 전송하지 않으며, 5초마다 초기화합니다.
* **trace\_send\_enabled** Boolean

기본값 `true`

트레이스 데이터 전송 여부를 설정할 수 있습니다.
* **debug\_trace\_samling** Boolean

기본값 `false`

트레이스 데이터 샘플링 디버그 옵션을 켜거나 끌 수 있습니다.

트레이스 URL 이름 수정하기[​](#트레이스-url-이름-수정하기 "트레이스 URL 이름 수정하기에 대한 직접 링크")
-------------------------------------------------------------------

* **hook\_tx\_name\_patterns / hook\_tx\_name\_mode** string `Java Agent v2.2.4 or later`

특정 URL 및 특정 메소드(method)를 호출 시 트레이스 URL의 이름을 수정할 수 있습니다. 예를 들어 `io.home.test.TestController.test1`에 등록한 URL 호출 시 `test100000()` 메소드를 호출하는 경우, 서비스 화면에서 `/api/100000+test1+test100000`으로 확인할 수 있습니다.

`hook_tx_name_mode` 옵션을 통해 **class**, **method**, **string**, **return** 중 하나를 선택할 수 있습니다.

whatap.conf
```
# 호출 메소드의 전체 경로 (* 사용 가능)  
hook_tx_name_patterns=ab.cd.ef.GH.ij  
  
# class, method, string, return 중 택1  
hook_tx_name_mode=method  

```

특정 exception 무시하기[​](#특정-exception-무시하기 "특정 exception 무시하기에 대한 직접 링크")
----------------------------------------------------------------------

* **ignore\_exception\_tx\_pattern** String `Java Agent v2.2.4 or later`

특정 서비스에서 특정 exception을 무시할 수 있도록 설정할 수 있습니다. 여러 개를 등록할 때는 쉼표(,)를 구분자로 이용하세요.

whatap.conf
```
ignore_exception_tx_pattern=exception:service_url  
# e.g. java.util.concurrent.TimeoutException:/api/test/timeout,org.springframework.web.util.NestedServletException:/api/posts/test/cexception  

```

HttpURLConnection 추적하기[​](#httpurlconnection-추적하기 "HttpURLConnection 추적하기에 대한 직접 링크")
-------------------------------------------------------------------------------------

* **HttpURLConnection** Boolean

기본값 `true`

`HttpURLConnection` 클래스의 메소드를 추적하기 위한 옵션입니다.
* **hook\_HttpURLConnection\_startup\_enabled** Boolean `Java Agent v2.2.4 or later`

기본값 `false`

`HttpURLConnection` 클래스의 메소드를 최초 호출 시에도 추적할 수 있도록 설정할 수 있습니다.
* **HttpURLConnection\_weblogic** Boolean `Java Agent v2.2.4 or later`

기본값 `true`

Weblogic에서 `HttpURLConnection`으로 http 호출을 하는 경우 `weblogic.net.http.HttpURLConnection` 클래스의 메소드를 추적하기 위한 옵션입니다.
* **hook\_HttpURLConnection\_weblogic\_startup\_enabled** Boolean `Java Agent v2.2.4 or later`

기본값 `false`

`weblogic.net.http.HttpURLConnection` 클래스의 메소드를 최초 호출 시에도 추적할 수 있도록 설정할 수 있습니다.
