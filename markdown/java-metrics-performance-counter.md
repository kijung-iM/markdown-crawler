애플리케이션 성능 카운터
=============

와탭 에이전트는 애플리케이션 성능과 관련된 다양한 정보를 수집합니다. 크게 3가지로 분류할 수 있습니다.

* **User** : 실시간 사용자 혹은 방문 사용자
* **Service** : 트랜잭션, SQL, 외부 호출 건수 및 응답, 에러율 등
* **Resource** : 시스템, 프로세스 자원 사용량

User Counter[​](#user-counter "User Counter에 대한 직접 링크")
-------------------------------------------------------

사용자는 모니터링 대상 시스템을 사용하는 클라이언트를 말합니다. 클라이언트에서는 일반적으로는 브라우저를 기준으로 사용자 수를 계산합니다.

웹 시스템 성능에서 사용자는 부하를 발생시키는 시작이기 때문에 중요합니다. 사용자 추적을 위해서는 사용자는 어떤 기준으로 구분하고, 어떻게 카운팅 할지에 대한 고려가 필요합니다.

### 사용자 구분[​](#사용자-구분 "사용자 구분에 대한 직접 링크")

와탭 에이전트 사 용자를 구분하기 위해 다양한 옵션을 제공합니다.

* **Remote IP**

기본값은 remote ip를 사용하여 사용자를 구분합니다. remote ip는 실제 사용자를 구분하는 데 한계가 있습니다.
* **Cookie**

쿠키를 사용하여 사용자를 구분합니다. 모든 접속 클라이언트를 대상으로 **WHATAP**이라는 쿠키에 UUID를 저장합니다.

whatap.conf
```
trace_user_using_ip=false  
  
# Java agent v2.2.0 or later  
wclient_using_ip=false  

```
* **Header Key**

HTTP 헤더에 전달되는 값으로 사용자를 구분할 수 있습니다.

whatap.conf
```
user_header_ticket=USER  
  
# Java agent v2.2.0 or later  
wclient_header_ticket=USER  

```

### 사용자 카운팅[​](#사용자-카운팅 "사용자 카운팅에 대한 직접 링크")

사용자를 카운팅 하는 방법에 따라서 다르게 사용합니다. 실시간 사용자는 현재 시스템을 사용하는 사용자의 수를 알기 위해서 측정합니다. 일일 방문 사용자는 하루 동안 해당 서비스에 관심을 갖는 사용자가 몇 명인지에 대한 비즈니스적인 관리를 위해 측정합니다.

* **실시간 사용자**

최근 5분 동안 사용자 수를 카운팅 합니다. 5초마다 shifting 하면 사용자를 카운팅 합니다. 각 서버에서 카운팅 된 숫자는 HyperLogLog 알고리즘을 통해서 머지 됩니다.
* **일일 방문자**(**DAU**, Daily Active User)

하루 동안 시스템에 접속한 사용자를 카운팅 합니다. 24시간 동안 접속한 사용자를 HyperLogLog를 통해서 계산합니다.

팁와탭에서는 장기간 사용자를 카운팅 하기 위해 사용자 데이터에 대한 byte block을 서버로 수집합니다. 이 데이터를 Hyperloglog로 머지하면 이론적으로 한 달 이상의 방문 사용자를 계산할 수 있습니다.

Service Counter[​](#service-counter "Service Counter에 대한 직접 링크")
----------------------------------------------------------------

트랜잭션과 트랜잭션이 사용하는 SQL 혹은 외부 호출 등에 대한 건수, 응답시간 에러 건수 등에 대한 성능지표가 포함됩니다.

* **Transaction Counter**

트랜잭션을 수행하면 측정하는 카운터입니다.


	+ **건수**
	+ **응답 시간**
	+ **에러 건수**
* **Active Transaction Counter**

진행 중인 트랜잭션의 수를 카운팅 합니다.


	+ **건수**
	+ **Active Status**
	
	진행 상태는 METHOD, SQL, HTTPC, DBC, SOCKET 5가지 상태로 고정되어 있습니다.
	
	
		- METHOD - 일반 함수를 호출하는 상태
		- SQL - db sql을 수행 중인 상태
		- HTTPC - 외부 Http Api(서비스)를 호출 중인 상태
		- DBC - DB 연결을 요청한 상태, 일반적으로 Pool에서 가져옴
		- SOCKET - TCP 세션을 Connecting 중인 상태
* **SQL**

SQL 수행 현황을 카운팅 합니다.


	+ **건수**
	+ **응답 시간**
	+ **에러 건수**
	+ **패치 건수**
* **HTTP Call**

외부 Http 호출에 대한 현황을 카운팅 합니다.


	+ **건수**
	+ **응답 시간**
	+ **에러 건수**

Resource Counter[​](#resource-counter "Resource Counter에 대한 직접 링크")
-------------------------------------------------------------------

서버 자원 혹은 node 프로세스 내부의 자원 사용량을 카운팅 합니다.



---

* **CPU** (sys, usr, wait, steal, irq, cores)

CPU 사용량 %입니다. 각 종류별로 수집됩니다. 가상환경에서만 Steal이 의미가 있습니다. Cpu Core 개수를 같이 수집하고 있습니다.
* **Process CPU**

자바 프로세스가 사용하는 CPU%입니다.
* **Memory**

시스템 메모리 사용률(%)입니다.
* **Swap**

Swap 메모리 사용률(%)입니다.
* **Disk**

Disk는 Java Process의 Current 디렉터리의 사용률(%)입니다.
* **Heap** (Total, Used, Perm)

Java Heap 메모리의 Total, Used, Perm 양입니다. 데이터 단위는 KBytes 입니다.
* **GC** (Count, Time)

5초 동안 발생한 GC 건수와 시간의 합계입니다.
* **ObjectPendingFinalizationCount**

GC 호출되는 도중에 finalize() 수행하기 위해 대기 중인 객체 숫자입니다. 이 값이 커지면 GC time이 지연될 수 있습니다.
* **Thread** (start Count, Count, Daemon, Peak Count)

JVM이 실행된 이후부터 시작된 스레드 수, 현재 돌고 있는 스레드 수, 데몬, 최대 스레드 수를  수집합니다. 스레드 풀이 필요한지에 대한 판단 등을 할 수 있습니다.
* **DB Connection Count** (active,idle)

Connection Pool의 idle와 active 카운트를 수집합니다.
* **Tomcat Thread Pool** (active, queueSize)

톰캣의 Executor 스레드 풀이 설정되었을 때 성능 정보를 수집합니다.

XML
```
    <Executor name="tomcatThreadPool" namePrefix="catalina-exec-"  
    maxThreads="50" minSpareThreads="2" maxQueueSize="78"/>  

```



---

### DB Connection Pool 카운터[​](#db-connection-pool-카운터 "DB Connection Pool 카운터에 대한 직접 링크")

DB Connection Pool은 DataSource라고 합니다. WAS가 제공하는 경우가 일반적이지만 일부에서는 오픈소스 Pool을 사용하기도 합니다. 사용량 정보가 JMX로 노출되기도 하지만 그렇지 않은 경우도 많습니다.

와탭은 2가지 방식을 제공하고 있습니다. 하나의 BCI에 의한 직접 조회 방식과 JMX를 이용한 방식입니다. 기본은 BCI 방식을 사용하고 보조로 JMX를 사용할 수 있도록 제공하고 있습니다.

다음은 개별 옵션별 디폴트 값과 연관되어 ByteCode Injection되는 클래스입니다.

hikari\_pool\_enabled=false
```
com.zaxxer.hikari.pool.HikariPool  

```
dbcp\_pool\_enabled=true
```
org.apache.commons.dbcp.BasicDataSource  
org.apache.commons.dbcp2.BasicDataSource  
org.apache.tomcat.dbcp.dbcp.BasicDataSource  
org.apache.tomcat.dbcp.dbcp2.BasicDataSource  

```
tomcat\_pool\_enabled=true
```
org.apache.tomcat.jdbc.pool.ConnectionPool  

```
weblogic\_pool\_enabled=true
```
weblogic.jdbc.common.internal.ConnectionPool  

```
jeus\_pool\_enabled=true
```
jeus.jdbc.connectionpool.ConnectionPoolImpl  

```
jboss\_pool\_enabled=true
```
org.jboss.jca.core.connectionmanager.pool.PoolStatisticsImpl  

```
주의옵션을 변경한다면 BCI 관련 옵션이기 때문에 **다시 시작**해야 합니다. 클래스가 instrument된 후에도 추적 테이블에 등록되는 과정이 필요합니다. 따라서 실행 중에 redefine을 해도 동작하지 않습니다.

#### DataSource 현황 JMX로 가져오기[​](#datasource-현황-jmx로-가져오기 "DataSource 현황 JMX로 가져오기에 대한 직접 링크")


```
dbcp_pool_enabled==true 이면 tomcat_ds_enabled=false  
weblogic_pool_enabled== true 이면 weblogic_ds_enabled=false  

```
1. **옵션 자동 결정** 내용을 확인하세요.
2. 관련된 pool 쪽 옵션 값을 `false`로 선언하세요.
3. DataSource 관련 옵션 값을 `true`로 변경하세요. 기본값은 `false` 입니다.

whatap.conf
```
tomcat_ds_enabled=false  
weblogic_ds_enabled=false  

```

### ThreadPool 카운터[​](#threadpool-카운터 "ThreadPool 카운터에 대한 직접 링크")

ThreadPool 카운터는 JMX Mbean 정보를 통해 수집됩니다. Tomcat과 같이 사용 사례가 많은 경우라면 문제없지만 특정 환경에서는 이 지표가 수집되지 않을 수 있습니다.

수집을 위해서 추가 설정이 필요합니다. 관련 설정은   다음과 같습니다.

whatap.conf
```
jmx_threadpool_objectname=Catalina:type=ThreadPool,name="http-bio-8080"  
// JMX ThreadPool MBean 이름을 설정합니다.  
jmx_threadpool_atter_activecount=connectionCount  
// activecount 수치를 나타내는 attribute를 설정합니다.  
jmx_threadpool_atter_queuesize=maxThreads  
// maxThreads 수치를 나타내는 attribute를 설정합니다.  

```
JMX ThreadPool ObjectName 및 AttributeName 과 같은 Mbean 명은 JMX 모니터링 도구를 통해 확인하거나 각 WAS 별 Mbean 문서를 참고합니다.

노트사용 중인 WAS, 프레임워크 관련 [문서](https://www.ibm.com/support/knowledgecenter/ko/SS7K4U_liberty/com.ibm.websphere.wlp.zseries.doc/ae/rwlp_mon_threadpool.html)를 참고해 Mbean 정보를 확인하세요.

#### Jconsole 사용 시[​](#jconsole-사용-시 "Jconsole 사용 시에 대한 직접 링크")

* **ObjectName** : Catalina

**type** : ThreadPool

**name** : "http-bio-8080"

![](https://img.whatap.io/media/agent_java/data/threadpool_jmx01.png)
* **ActiveName** : connectionCount

**QueueName** : maxThreads

![](https://img.whatap.io/media/agent_java/data/threadpool_jmx02.png)

#### 결과 확인[​](#결과-확인 "결과 확인에 대한 직접 링크")

설정이 정상적으로 되면 카운터에서 다음과 같이 데이터를 조회할 수 있습니다.

![성능 카운터 - 정상 상태](https://img.whatap.io/media/agent_java/data/threadpool_counter.png)

Apdex[​](#apdex "Apdex에 대한 직접 링크")
----------------------------------

![](https://img.whatap.io/media/agent_php/data/tinified/apdex.png)

Apdex(Appliccation Performance Index)는 개방형 표준을 따르는 애플리케이션 성능지표입니다. Apdex는 응답시간에 기반하며 전체 요청 중 만족과 허용 건 비율로 수치화합니다. 대시보드에 Apdex 그래프가 추가되었습니다.

Apdex는 사용자 만족도에 대한 지표로 활용할 수 있으며, 0 ~ 1 사이의 값을 갖습니다.


> (만족 횟수 + (허용 횟수 \* 0.5)) / 전체 요청 수



| 상태 | 설명 |
| --- | --- |
| 만족 (Satisfied, **S**) | 업무처리에 전혀 문제가 없음 ≤ 1.2초 (만족 **S** 기본값) |
| 허용 (Tolerating, **T**) | 사용자가 지연을 느끼나 업무처리는 가능함 ≤ 4.8초 (만족 **S** \* 4) |
| 불만 (Frustrated, **F**) | 업무처리가 불가능함 > 4.8초 (허용 **T** 초과 및 오류) |

* **whatap.apdex\_time** millisecond

기본값 `1200`

만족 **S** 기본값은 에이전트 설정 메뉴에서 변경할 수 있습니다.
