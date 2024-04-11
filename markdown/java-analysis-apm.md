스택
==

홈 화면 > 프로젝트 선택 > ***분석*** > ***스택***

와탭 모니터링 서비스 초기 화면에서 프로젝트를 선택한 다음 ***프로젝트 메뉴*** 하위에 ***분석*** > ***스택***을 선택하세요. ***탑 스택***과 ***유니크 스택***, ***액티브 스택***을 확인할 수 있습니다.

노트스택 분석 기능을 사용할 수 있는 애플리케이션은 **Java**와 **Python**, **.NET**입니다.

와탭은 10초(기본값) 간격으로 수집한 스레드 스택을 활용하여 메소드 레벨의 성능 지연 구간을 분석합니다.

![st1](https://img.whatap.io/media/user_guide_application/stack/st1.png)

예시 스택에서 **탑 라인**은 `socketRead0` 입니다.


```
java.net.SocketInputStream.socketRead0(Native Method)  

```
**탑 라인**은 덤프를 수행할 스레드가 해당 메소드를 수행 중이라는 것을 의미합니다. 순간적으로 잡혔을 가능성도 있지만 확률적으로 해당 모듈 처리 시간의 합의 비율만큼 스택에 나타납니다. 이 **탑 라인** 메소드의 빈도를 계산하여 메소드 레벨의 성능을 판단할 수 있습니다. 와탭은 **탑 라인 빈도 통계**를 ***탑 스택***(Top Stack)이라고 합니다.

![탑 스택](/img/apm-analysis-apm-top-stack-01.png)

***탑 스택*** 분석을 통해 도출된 메소드를 어떤 메소드가 호출했는지에 대한 빈도를 분석할 수 있습니다.

![탑 스택](/img/apm-analysis-apm-top-stack-02.png)

탑 스택 계층 분석에서는 원래 액티브 스택을 확인하기 어려웠습니다. 따라서 와탭은 ***액티브 스택***(Active Stack)을 조회할 수 있도록 동일 스택을 모아서 ***유니크 스택***(Unique Stack)이라는 조회 기능을 제공합니다.

***탑 스택***[​](#top-stack "top-stack에 대한 직접 링크")
-----------------------------------------------

Stack Trace 상의 각 Step 기준으로, Step과 Step 간의 호출 비율을 백분율로 분석한 정보를 제공합니다. 최상위 Step의 적체 빈도를 백분율로 산출하여 내림차순으로 정렬한 결과를 제시합니다.

각 Step을 클릭하면 해당 Step을 호출하는 상위 Step을 호출 빈도 기준 백분율로 산출하여 제공합니다.

***탑 스택*** 통계는 충분히 많은 데이터를 가지고 판단하는 것이 좋습니다. 수집한 스택의 개수가 10개 미만의 소수인 경우 통계 의미를 갖기에 부족합니다.

***탑 스택***은 튜닝 시 인지하기 힘들었던 부분의 튜닝 포인트를 찾아내는 데 유용합니다. 가장 빈번하게 나타난 스택은 현재 애플리케이션 서버에서 가장 많은 응답 지연을 발생하는 것으로 판단할 수 있습니다. 가장 왼쪽의 나타나는 비율은 애플리케이션 서버 성능에 영향을 미치는 정도입니다.

안정적인 애플리케이션 서버일지라도 빈번하게 나타난 스택은 성능 저하를 일으킬 가능성이 있으므로 해당 클래스는 유심히 보는 것이 좋습니다.

***탑 스택*** 클릭 시 해당 최상위 스택에 대한 호출 빈도를 확인할 수 있습니다. ***탑 스택***의 호출 관계는 1 대 1 관계이므로 ***탑 스택***의 depth가 밑으로 내려갈수록 정보의 정확성이 떨어질 수 있습니다. 하위 depth에 대한 정보는 참고 용도로 사용하며 튜닝을 진행하시기 바랍니다.

애플리케이션 성능 개선을 위해 최상위 Step의 적체 비율이 높은 모듈의 병목 가능성을 검토해야 합니다. 적체 비율이 높은 모듈의 경우 작은 성능 개선도 애플리케이션 전체에 상당한 개선 효과를 가져올 수 있습니다.

![탑 스택](/img/apm-analysis-apm-top-stack-03.png)


```
whatap.util.ThreadUtil.sleep  
// jdbc.Control.exec의 호출 비율은 40.02%  
jdbc.Control.exec   
// jdbc.FakePreparedStatement.executeQuery의 호출 비율은 68.06%  

```
`whatap.util.ThreadUtil.sleep` ← `jdbc.Control.exec` ← `jdbc.FakePreparedStatement.executeQuery`의 호출 비율이 40.02% \* 68.06%를 의미하지는 않습니다. `jdbc.Control.exec`에서 타 모듈의 호출 가능성이 존재하기 때문입니다.

***탑 스택***을 통해 호출 비율을 판단할 경우, 각 Step 간 호출 비율을 곱하여 전체 호출 관계 비율을 산출해서는 안 됩니다. Top Stack의 호출 비율은 Stack Trace 상에 노출된 정보의 Step 간 호출 비율의 산출 결과이기 때문에, Step 간 호출 비율로 전체 호출 비율을 도출할 경우 왜곡된 결과를 도출하게 됩니다.

***탑 스택*** 통계에서는 일정 기간을 기준으로 시간에 따른 비율 변화와 수집 건수에 대한 히스토리를 제공합니다.

![탑 스택](/img/apm-analysis-apm-top-stack-04.png)

* ***퍼센트***


	+ 조회 기간 선택된 탑 스택의 비율 변화를 나타냅니다.
	+ 장애 시점 현황 파악, 개선 전/후 비교에 유용하게 사용됩니다.
* ***건수***


	+ 수집되는 스택의 수는 액티브 트랜잭션 수에 비례합니다.
	+ 특정 구간에서 수집량이 증가했다면 서비스 지연이나 급격한 유입량 증가가 있었음을 알 수 있습니다.

다음과 같은 다이어그램으로도 확인 가능합니다.

![탑 스택](/img/apm-analysis-apm-top-stack-05.png)

* ***Stack Chart***

개별 탑 스택의 비율을 차트로 나타냅니다.

***유니크 스택***[​](#unique-stack "unique-stack에 대한 직접 링크")
-------------------------------------------------------

Stack Trace 전체의 Hash 값 기준의 산출 결과로 전체 Step이 동일한 호출 비율을 백분율로 분석한 정보를 제공합니다. ***탑 스택***은 Step 간의 호출 비율에 대한 정보를 제공합니다.

***유니크 스택***은 Stack Trace 전체의 정확한 호출 정보를 기반으로 한 데이터를 제공합니다. 상세 호출 관계를 파악하는 데 유용한 정보를 제공합니다. 예를 들면 적체 비율이 높은 Stack Trace를 식별할 수 있습니다.

![유니크 스택](/img/apm-analysis-apm-unique-stack.png)

상세 호출 Step 검토를 통한 호출 경로 상에 이상 모듈의 존재 여부를 파악할 수 있습니다.

***액티브 스택***[​](#active-stack "active-stack에 대한 직접 링크")
-------------------------------------------------------

진행 중인 트랜잭션을 액티브 트랜잭션이라고 합니다. **액티브 트랜잭션에서 정기적으로 덤프한 스택**을 ***액티브 스택***이라 합니다.

노트와탭 에이전트는 매 10초(옵션 가능)마다 **액티브 트랜잭션**에서 ***액티브 스택***을 덤프하고 이것을 서버에 전송합니다.  
`active_stack_second=10`

***액티브 스택*** 메뉴를 선택하면 수집된 ActiveStack을 차트로 확인할 수 있습니다. 차트는 5분간의 단위 통계 데이터를 ***Active Transaction***의 수를 막대로, ***TPS***를 꺾은 선으로 표시합니다.

막대를 클릭하면, 클릭한 시간대의 Active Transaction의 정보가 나오며, 그 정보를 클릭하면 해당 Transaction의 Active Stack을 볼 수 있습니다.

![액티브 스택](/img/apm-analysis-apm-active-stack.png)

노트액티브 트랜잭션에 관한 자세한 내용은 [다음 문서](/java/active-transactions)를 참조하세요.

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
