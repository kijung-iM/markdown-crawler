WebLogic
========

JVM 옵션 추가[​](#jvm-옵션-추가 "JVM 옵션 추가에 대한 직접 링크")
----------------------------------------------

WebLogic 애플리케이션 서버 환경에서 Java 모니터링 에이전트를 효과적으로 사용하기 위해 필요한 JVM 옵션을 추가하는 방법을 안내합니다.

사용하는 운영체제를 확인 후 설정을 완료하세요.

* Linux
* Windows

{WebLogic\_Path}/user\_projects/domains/{User\_Domain}/bin/startWebLogic.sh
```
########## WHATAP START ############  
WHATAP_HOME=/path/to/whatap  
WHATAP_JAR=`ls ${WHATAP_HOME}/whatap.agent-*.jar | sort -V | tail -1`  
JAVA_OPTIONS="${JAVA_OPTIONS} -javaagent:${WHATAP_JAR} "  
########## WHATAP END ############  

```
{WebLogic\_Path}/user\_projects/domains/{User\_Domain}/bin/startWebLogic.bat
```
rem ########## WHATAP START ############  
set WHATAP_HOME=\path\to\whatap  
for /f %%f in ('dir /b /on "%WHATAP_HOME%\whatap.agent-*.jar"') do set last=%%f  
set WHATAP_JAR=%last%  
set WHATAP_OPTS=-javaagent:%WHATAP_HOME%\%WHATAP_JAR%  
if "x%JAVA_OPTIONS%"=="x" goto setWhatap  
set JAVA_OPTIONS_TMP=%JAVA_OPTIONS:"=%  
if not "x%JAVA_OPTIONS_TMP:whatap=%"=="x%JAVA_OPTIONS_TMP%" goto endWhatap  
:setWhatap  
set JAVA_OPTIONS=%JAVA_OPTIONS% %WHATAP_OPTS%  
:endWhatap  
rem ########## WHATAP END ############  

```
노트Java 17 버전 이상의 경우 reflection 관련한 다음 옵션을 추가하세요.


```
  
--add-opens=java.base/java.lang=ALL-UNNAMED  
  

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

