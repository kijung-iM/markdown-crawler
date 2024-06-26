트랜잭션 엔드포인트 설정
=============

트랜잭션 엔드포인트는 트랜잭션의 시작 메소드입니다. HTTP 트랜잭션의 경우에는 `HttpServlet.service()` 혹은 `Filter.doFilter()`가 트랜잭션의 시작점이고 이곳을 **트랜잭션 엔드 포인트**라고 부릅니다.

NON HTTP 추적[​](#non-http-추적 "NON HTTP 추적에 대한 직접 링크")
----------------------------------------------------

트랜잭션 엔드포인트로 지정된 메소드가 시작해서 종료될 때까지의 성능을 트랜잭션 성능이라고 합니다. Non http 트랜잭션을 추적하기 위해서는 **엔드포인트**를 지정해야 합니다.

노트**엔드포인트** 찾기

1. 트랜잭션이 호출될 것으로 추정되는 모든 메소드에 대해 트레이스 추적을 설정하세요.
2. 다시 시작 후 트랜잭션을 발생시켜 모니터링하세요.
3. `back stack` 옵션을 켜서 진입 메소드를 정확히 파악하세요.
대상 선정[​](#대상-선정 "대상 선정에 대한 직접 링크")
----------------------------------

1. **메소드 트레이스 설정**

메소드 트레이스를 설정하세요. 확실하게 트랜잭션에서 호출되는 클래스를 지정하세요. DB를 사용하는 프로그램에서는 **JDBC 드라이버**가 유용합니다.

whatap.conf
```
hook_method_patterns=jdbc.*.*  
hook_method_access_public_enabled=true  
hook_method_access_protected_enabled=true  
hook_method_access_none_enabled=true  

```
2. **트랜잭션 시작 옵션 설정**

메소드가 호출되면 트랜잭션을 시작하세요. 트랜잭션 시작 옵션과 트랜잭션 시작 시 스택을 덤프하는 옵션을 켜세요.

whatap.conf
```
trace_auto_transaction_enabled=true  
trace_auto_transaction_backstack_enabled=true  

```
3. **재시작 후 트레이스 분석**

다시 시작하세요. 이후 서비스를 호출하면 트랜잭션이 추적되는 것을 볼 수 있습니다.

트랜잭션을 조회하면 `jdbc.*`로 시작하는 모든 클래스의 메소드가 이 트랜잭션으로 나타나는 것을 알 수 있습니다. 트랜잭션 트레이스를 조회하면 **TRANSACTION BACKSTACK**라는 메시지 스텝을 확인할 수 있습니다.

TRANSACTION BACKSTACK
```
jdbc.FakePreparedStatement.executeQuery(FakePreparedStatement.java),  
com.virtual.dao.SelectDAO.execute2(SelectDAO.java:29),  
com.virtual.web.SimulaNonHttp.execute(SimulaNonHttp.java:147),  
com.virtual.web.SimulaNonHttp.process(SimulaNonHttp.java:76),  
com.virtual.web.SimulaNonHttp.run(SimulaNonHttp.java:100)  

```
4. **스택 내용 확인**

스택 내용을 확인하면 어떤 메소드로부터 출발하고 있는지 추정할 수 있습니다.

Example
```
com.virtual.web.SimulaNonHttp.execute(SimulaNonHttp.java:147),  
com.virtual.web.SimulaNonHttp.process(SimulaNonHttp.java:76),  
com.virtual.web.SimulaNonHttp.run(SimulaNonHttp.java:100)  

```
위 3개의 메소드 중에 하나를 트랜잭션 시작점으로 판단할 수 있습니다. 이 상황에서는 역 컴파일을 수행해서 적절한 **트랜잭션 엔드포인트**를 결정해야 합니다.

로직을 보면 `SimulaNonHttp.run` 내에서 `while()`가 돌면서 `SimulaNonHttp.process()`을 호출하고 `SimulaNonHttp.execute()`가 수행됩니다. `process()`가 적당하다는 것을 알 수 있습니다. 이 부분은 소스를 보고 판단해야 합니다.

팁**엔드포인트**의 가장 **중요한 기준은 종료되어야 한다는 것**입니다. 정상적인 상황에서 지연되지 않고 곧바로 종료되어야 성능적인 판단을 할 수 있습니다.

트랜잭션 엔드포인트 지정[​](#트랜잭션-엔드포인트-지정 "트랜잭션 엔드포인트 지정에 대한 직접 링크")
----------------------------------------------------------

1. 트랜잭션 시작 지점을 다음과 같이 설정하세요.

whatap.conf
```
hook_service_patterns=com.virtual.web.SimulaNonHttp.process  

```
2. 애플리케이션을 다시 시작하세요.

`process()` 메소드가 새로운 트랜잭션의 **엔드포인트**가 됩니다.

노트`hook_service_patterns` 옵션은 와일드카드 문자를 사용할 수 없으며, 2개 이상의 값을 설정하려면 쉼표(,)를 구분자로 이용하세요.

트랜잭션 이름 정의[​](#트랜잭션-이름-정의 "트랜잭션 이름 정의에 대한 직접 링크")
-------------------------------------------------

일반적으로 메소드 명칭으로 트랜잭션을 구분할 수 있습니다.

whatap.conf
```
service_name_mode=[full,class,method,string,arg]  
service_name_index=0  

```
* **service\_name\_mode**

`full`, `class`, `method`, `string`, `arg` 5가지 옵션을 지정할 수 있습니다.


	+ `full`: Full Class 이름을 서비스 명으로 사용합니다.
	+ `class`: Class 이름을 서비스 명으로 사용합니다.
	+ `method`: Method 이름을 서비스명으로 사용합니다.
	+ `string`: 문자열 중에서 첫 번째 파라미터를   서비스 명으로 사용합니다.
	+ `arg`: 파라미터 중에서 `service_name_index` 옵션에 지정한 인덱스에 파라미터를 서비스 명으로 사용합니다.

플러그인 사용[​](#플러그인-사용 "플러그인 사용에 대한 직접 링크")
----------------------------------------

주의플러그인은 충분히 이해한 경우에만 사용하길 권장합니다.

*WHATAP\_HOME* 경로 아래에 *plugin* 폴더를 만드세요. 그리고 vi를 통해 *AppServiceStart.x* 파일을 만드세요.

![플러그인 사용 예시](https://img.whatap.io/media/agent_python/data/app_start_plug.png)

`println("test");`라고 타이핑하고 저장하면 화면에 "test"라는 문자열이 출력되는 것을 확인할 수 있습니다. 확인 후 파라미터에서 정보를 추출하세요.

예시에서는 파라미터가 HashMap에 전달되고 거기에 url 파라미터가 전달되고 있습니다.


```
Object url =((java.util.HashMap)$point.getArgs()[0]).get("url");  
$ctx.service((String)url);  
//println("url="+url);  

```
이렇게 플러그인을 만들면 트랜잭션 이름이 변경됩니다.

