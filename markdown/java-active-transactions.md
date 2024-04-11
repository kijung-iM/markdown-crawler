액티브 트랜잭션
========

진행 중인 트랜잭션을 액티브 트랜잭션이라고 합니다. **액티브 트랜잭션에서 정기적으로 덤프한 스택을 액티브 스택**이라 합니다.

노트와탭 에이전트는 매 10초(옵션 가능)마다 액티브 트랜잭션에 대해서 액티브 스택을 덤프하고 이것을 서버에 전송합니다. `active_stack_second=10`

컴팩트한 액티브 스택 수집[​](#컴팩트한-액티브-스택-수집 "컴팩트한 액티브 스택 수집에 대한 직접 링크")
-------------------------------------------------------------

액티브 스택은 스레드 덤프를 정기적으로 수행하기 때문에 잘못 구현되면 에이전트에 오버헤드가 커질 수 있습니다. 와탭은 에이전트 부하를 최소화하면서 액티브 스택을 수집하기 위해 다양한 옵션들을 가지고 있습니다.

팁***사이트맵*** > ***스레드 목록/덤프*** 메뉴에서 스레드 목록 중에 ***WhaTap-ActiveStackDump*** 스레드의 ***CPU Time***을 확인하면 오버헤드를 판단할 수 있습니다.

**액티브 스택 예시**

JAVA
```
java.lang.StringBuffer.append(StringBuffer.java:309)  
java.util.regex.Matcher.appendReplacement(Matcher.java:839)  
java.util.regex.Matcher.replaceAll(Matcher.java:906)  
java.lang.String.replaceAll(String.java:2162)  
core.log.triggers.TriggerRegister.changeNotify(TriggerRegister.java:114)  
core.log.aop.handler.DaoInfo.log(DaoInfo.java:141)  
core.log.aop.handler.DaoInfo.doAround(DaoInfo.java:102)  
core.log.aop.reflection.profiler.AroundProfiler.invoke(AroundProfiler.java:19)  
com.sun.proxy.$Proxy39.getUpdateCount(Unknown Source)  
org.apache.ibatis.executor.resultset.DefaultResultSetHandler.getNextResultSet(DefaultResultSetHandler.java:256)  
org.apache.ibatis.executor.resultset.DefaultResultSetHandler.handleResultSets(DefaultResultSetHandler.java:193)  
org.apache.ibatis.executor.statement.PreparedStatementHandler.query(PreparedStatementHandler.java:64)  
  
* * *  
  
sun.reflect.GeneratedMethodAccessor140.invoke(Unknown Source)  
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)  
java.lang.reflect.Method.invoke(Method.java:606)  
org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:221)  
org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:136)  
org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:114)  
org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:827)  

```
**최적화된 데이터 수집**

* 트랜잭션을 수행 중인 스레드에 대해서만 스택을 덤프합니다.
* 액티브 스택 덤프 시간 간격을 조정할 수 있습니다.

`active_stack_second=10`
* 액티브 스택의 최대 라인에 제한되어 있습니다. Top 라인에서부터 기본 50라인을 수집합니다.

`trace_active_callstack_depth=50`
* 액티브 스택의 각 라인은 해시 처리되어 수집됩니다. text는 한 번만 수집됩니다.
* 한 타임에 수집되는 최대 액티브 스택 개수도 제한되어 있습니다.

`active_stack_count=100`

Background Thread에 대한 액티브 스택[​](#background-thread에-대한-액티브-스택 "Background Thread에 대한 액티브 스택에 대한 직접 링크")
-------------------------------------------------------------------------------------------------------

기본적으로 액티브 스택은 트랜잭션이 수행되고 있는 스레드의 스택을 말합니다. 하지만 일부 백그라운드 스레드에 대해서도 스택을 분석할 필요가 있을 수 있습니다. 이때 옵션을 통해서 백그라운드 스레드에 대한 액티브 스택을 확보할 수 있습니다. 1.6.2 버전 이후부터 가능합니다.

* `async_stack_enabled`의 값을 `true`로 설정하면 활성화됩니다.


```
async_stack_enabled=false  

```
* 스택 덤프 간격은 포그라운드 액티브 스택 설정에 따라갑니다.


```
active_stack_second=10  

```
* 대상 스레드 이름을 지정할 때는 `*`를 사용하여 문자열 패턴을 지정합니다.


```
async_thread_match=http*,abc*  

```
스레드 이름으로 스택 덤프 대상을 식별합니다. `,`를 사용하여 match를 여러 개 지정할 수 있습니다.
* 스택의 Top 메소드가 `async_thread_parking`에 등록된 클래스 / 메소드일 때 스레드가 파킹 상태에 있다고 판단하고 덤프를 생성하지 않습니다.


```
async_thread_parking_class=sun.misc.Unsafe  
async_thread_parking_method=park  

```

참고 자료[​](#참고-자료 "참고 자료에 대한 직접 링크")
----------------------------------

* [액티브 트랜잭션](https://brunch.co.kr/@leedongins/152)
* [장애를 가장 빠르게 알아내는 액티브 트랜잭션](https://brunch.co.kr/@leedongins/31)
