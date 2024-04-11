트랜잭션
====

트랜잭션이란?[​](#트랜잭션이란 "트랜잭션이란?에 대한 직접 링크")
---------------------------------------

사용자 브라우저의 요청을 처리하기 위한 서버 사이드의 LUW(Logical Unit of Work)를 말합니다. 개별 웹서비스(URL) 요청에 대한 처리 과정이 바로 트랜잭션입니다. 웹 애플리케이션에서 트랜잭션은 웹서비스(URL)에 대한 HTTP Request를 받아 Response를 반환하는 과정입니다.

애플리케이션의 성능은 이 트랜잭션들의 성능으로 요약할 수 있습니다. 트랜잭션 성능은 트랜잭션 시작에서부터 종료 시점, 응답시간 및 자원 사용량 혹은 트랜잭션 호출자 속성 등의 정보를 포함합니다.

기본적으로 트랜잭션 응답 분포와 트랜잭션 통계를 통해서 트랜잭션 성능을 분석할 수 있습니다.

트랜잭션의 이름[​](#트랜잭션의-이름 "트랜잭션의 이름에 대한 직접 링크")
-------------------------------------------

트랜잭션의 이름은 URL입니다. 단 Get 파라미터(Query String)는 제외됩니다.

**브라우저 요청**


```
http://www.whatap.io/hr/apply.do?name='kim'  

```
**트랜잭션 이름**


```
/hr/apply.do  

```
노트와탭에서는 **웹서비스 이름**과 **트랜잭션 이름**을 혼용하고 있습니다. 서비스 특정 URL과 그에 대한 요청을 처리하기 위한 모듈로 볼 수 있습니다. 트랜잭션 요청에 대한 처리 하나를 의미하기 때문에 둘의 이름은 동일하게 URL이라고 할 수 있습니다.

트랜잭션 이름 정규화[​](#트랜잭션-이름-정규화 "트랜잭션 이름 정규화에 대한 직접 링크")
----------------------------------------------------

MSA 기반의 시스템이 발전하면서 URL + ? 인자 파라미터 형식보다 URL 패스에 파라미터를 넣는 방식을 많이 사용하게 됩니다.


```
http://www.whatap.io/hr/kim/apply.do  

```
이렇게 패스 파라미터를 그대로 트랜잭션 이름으로 사용하게 되면 통계적 관점의 성능 분석이 어렵습니다. 이를 정규화할 필요가 있습니다. 와탭은 정규화를 위한 옵션과 기능을 제공합니다.

whtap.conf
```
trace_normalize_urls=/hr/{name}/apply.do  

```
위와 같이 설정하면 트랜잭션 이름이 */hr/kim/apply.do* → */hello/:name/apply.do*로 치환되어 수집됩니다. 만약 대상 URL 설정은 그대로 두고 기능만 off 하고자 한다면 다음과 같이 옵션을 지정할 수 있습니다. 기본값은 `true`입니다.

whatap.conf
```
trace_normalize_enabled=false  

```