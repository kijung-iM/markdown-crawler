Resin
=====

JVM 옵션 추가[​](#jvm-옵션-추가 "JVM 옵션 추가에 대한 직접 링크")
----------------------------------------------

Resin을 사용하는 애플리케이션 서버 환경에서 JVM 옵션을 추가하는 방법을 확인하세요. Java 버전에 따라 적용해야할 JVM 옵션이 다를 수 있습니다. 사용자의 환경에 맞는 JVM 옵션을 적용하세요. 옵션을 적용한 다음 애플리케이션 서버를 다시 시작하세요.

* 옵션 1: *resin.properties* 파일에 `jvm_args` 속성을 사용해 `javaagent` 인수를 추가하세요.
* 옵션 2: `conf/resin.conf` 또는 `conf/resin.xml` 파일에 `<jvm-args>` 섹션을 추가해 `-javaagent` 인수를 설정하세요.

노트* 애플리케이션 서버 로그 파일과 에이전트 로그 파일을 통해 에이전트가 정상 작동하는지, 에러가 발생하지 않았는지 확인하세요. 로그 파일의 위치는 다음을 확인하세요.


	+ 에이전트: *$WHATAP\_HOME/logs/whatap-`{SERVER_NAME}`-`{DATE}`.log*
	+ RESIN 4.x: *$RESIN\_HOME/log/jvm-app-#.log*
* 에이전트가 정상 작동하지 않거나 에러가 발생한다면 [다음 문서](/java/install-check)를 확인하세요.
### Java 6 ~ 8 버전[​](#java-6--8-버전 "Java 6 ~ 8 버전에 대한 직접 링크")

resin.properties
```
jvm_args : -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar  

```
resin.conf | resin.xml
```
<jvmarg>-javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar</jvm-arg>  

```
### Java 9 ~ 15 버전[​](#java-9--15-버전 "Java 9 ~ 15 버전에 대한 직접 링크")

resin.properties
```
jvm_args : -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -Djdk.attach.allowAttachSelf=true  

```
resin.conf | resin.xml
```
<jvmarg>-javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar</jvm-arg>  
<jvmarg>-Djdk.attach.allowAttachSelf=true</jvm-arg>  

```
### Java 16 버전 이상[​](#java-16-버전-이상 "Java 16 버전 이상에 대한 직접 링크")

resin.properties
```
jvm_args : -javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar -Djdk.attach.allowAttachSelf=true --add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=jdk.attach/sun.tools.attach=ALL-UNNAMED  

```
resin.conf | resin.xml
```
<jvmarg>-javaagent:{WHATAP_HOME}/whatap.agent-X.Y.Z.jar</jvm-arg>  
<jvmarg>-Djdk.attach.allowAttachSelf=true</jvm-arg>  
<jvmarg>--add-opens=java.base/java.lang=ALL-UNNAMED</jvm-arg> {/* Java 17 or later */}  
<jvmarg>--add-opens=jdk.attach/sun.tools.attach=ALL-UNNAMED</jvm-arg>  

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

