Spring Boot
===========

Spring Boot를 사용하는 애플리케이션 서버 환경에서 JVM 옵션을 추가하는 방법을 확인하세요.

JVM 옵션 추가[​](#jvm-옵션-추가 "JVM 옵션 추가에 대한 직접 링크")
----------------------------------------------

* Java 17 버전 이상의 경우 reflection 관련 JVM 옵션 추가로 애플리케이션을 기동할 수 있습니다.


```
# Java 17 이상만 지원  
java -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -Dwhatap.oname={Agent_Name} --add-opens=java.base/java.lang=ALL-UNNAMED -jar {application.jar}  

```
* 시작 스크립트에 JVM 옵션으로 `-javaagent`를 추가하세요.


```
java -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -jar {application.jar}  

```

JVM 옵션을 추가한 다음 사용하는 Spring Boot의 버전과 에이전트 버전에 맞춰 적합한 에이전트 설정을 진행하세요.

Spring Boot 3[​](#spring-boot-3 "Spring Boot 3에 대한 직접 링크")
----------------------------------------------------------

### Spring Boot 3.0.0 버전 이상[​](#spring-boot-300-버전-이상 "Spring Boot 3.0.0 버전 이상에 대한 직접 링크")

* Java 에이전트 v2.2.9 버전 이상(*whatap.agent-2.2.9.jar*)

whatap.conf
```
weaving=spring-boot-3.0  

```
* Java 에이전트 v2.2.5 버전 이상(*whatap.agent-2.2.5.jar*)

whatap.conf
```
weaving=spring-boot-3.0,tomcat10  

```
* Java 에이전트 v2.2.4 버전 이하(*whatap.agent-2.2.4.jar*)


	+ `jakarta.servlet.http.HttpServlet` 추적(동기 방식)
	
	whatap.conf
	```
	weaving=tomcat10  
	
	```
	+ WebClient 추적(비동기 방식)
	
	whatap.conf
	```
	weaving=webflux-6.0  
	
	```

Spring Boot 2[​](#spring-boot-2 "Spring Boot 2에 대한 직접 링크")
----------------------------------------------------------

### Spring Boot 2.7.0 버전 이상[​](#spring-boot-270-버전-이상 "Spring Boot 2.7.0 버전 이상에 대한 직접 링크")

* Java 에이전트 v2.2.9 버전 이상(*whatap.agent-2.2.9.jar*)

whatap.conf
```
weaving=spring-boot-2.7  

```
* Java 에이전트 v2.2.5 버전 이상(*whatap.agent-2.2.5.jar*)

whatap.conf
```
weaving=spring-boot-2.7,tomcat9  

```
* Java 에이전트 v2.2.4 버전 이하(*whatap.agent-2.2.4.jar*)

WebClient 추적(비동기 방식)

whatap.conf
```
weaving=webflux-5.3  

```

### Spring Boot 2.5.0 버전 이상[​](#spring-boot-250-버전-이상 "Spring Boot 2.5.0 버전 이상에 대한 직접 링크")

* Java 에이전트 v2.2.9 버전 이상(*whatap.agent-2.2.9.jar*)

whatap.conf
```
weaving=spring-boot-2.5  

```
* Java 에이전트 v2.2.5 버전 이상(*whatap.agent-2.2.5.jar*)

whatap.conf
```
weaving=spring-boot-2.5,tomcat9  

```
* Java 에이전트 v2.2.4 버전 이하(*whatap.agent-2.2.4.jar*)

WebClient 추적(비동기 방식)

whatap.conf
```
weaving=webflux-5.3  

```

힙 히스토그램 조회[​](#힙-히스토그램-조회 "힙 히스토그램 조회에 대한 직접 링크")
-------------------------------------------------

와탭의 Java 모니터링에서는 JVM 메모리에 올라가 있는 Heap 점유 객체 현황(힙 메모리상의 객체별 사이즈)을 조회할 수 있는 기능을 기본으로 제공합니다. 애플리케이션 > 인스턴스 성능 분석 메뉴에서 힙 히스토그램 탭을 선택하세요.

Java 6 ~ 8 버전에서는 JVM 옵션 없이 기본 지원하지만, 일부 Java 버전에 따라 다음과 같이 JVM 옵션을 적용해야 합니다.

* Java 9 ~ Java 15 버전


```
-Djdk.attach.allowAttachSelf=true  

```
example
```
java -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -Djdk.attach.allowAttachSelf=true -jar {application.jar}  

```
* Java 16 버전 이상


```
-Djdk.attach.allowAttachSelf=true  
--add-opens=jdk.attach/sun.tools.attach=ALL-UNNAMED  

```
example
```
java -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -Djdk.attach.allowAttachSelf=true --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=jdk.attach/sun.tools.attach=ALL-UNNAMED -jar {application.jar}  

```

노트Java 5 버전 이하, IBM Java는 지원하지 않습니다.

모니터링 시작하기[​](#모니터링-시작하기 "모니터링 시작하기에 대한 직접 링크")
----------------------------------------------

모든 설정을 완료한 다음 애플리케이션 서버를 다시 시작하면 에이전트가 정보를 수집하기 시작합니다. [다음 문서](/java/install-check)를 확인하세요.

