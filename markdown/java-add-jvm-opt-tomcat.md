Tomcat
======

환경 변수 추가[​](#환경-변수-추가 "환경 변수 추가에 대한 직접 링크")
-------------------------------------------

Tomcat 애플리케이션 서버 환경에서 Java 모니터링 에이전트를 효과적으로 사용하기 위해 필요한 JVM 옵션을 추가하는 방법을 안내합니다. 사용하는 운영체제에 맞게 설정하세요.

### Linux[​](#linux "Linux에 대한 직접 링크")

*catalina.sh* 파일 상단에 `JAVA_OPTS` 환경 변수를 추가하세요.

{Tomcat\_PATH}/bin/catalina.sh
```
########## WHATAP START ############  
WHATAP_HOME=/whatap  
WHATAP_JAR=`ls ${WHATAP_HOME}/whatap.agent-*.jar | sort -V | tail -1`  
JAVA_OPTS="${JAVA_OPTS} -javaagent:${WHATAP_JAR} "  
########## WHATAP END ############  

```
노트`ls ${WHATAP_HOME}/whatap.agent-*.jar | sort -V | tail -1` 항목은 향후 에이전트 업데이트를 진행할 경우 최신 와탭 에이전트를 적용하기 위해서입니다.

### Windows[​](#windows "Windows에 대한 직접 링크")

* *setup.bat* 파일을 통해 실행하는 경우

*catalina.bat* 파일 상단에 `JAVA_OPT` 환경 변수를 추가하세요.

{Tomcat\_PATH}/bin/catalina.bat
```
rem ########## WHATAP START ############  
set WHATAP_HOME=C:\whatap  
for /f %%f in ('dir /b /on "%WHATAP_HOME%\whatap.agent-*.jar"') do set last=%%f  
set WHATAP_JAR=%last%  
set WHATAP_OPTS=-javaagent:%WHATAP_HOME%\%WHATAP_JAR%  
  
if "x%JAVA_OPTS%"=="x" goto setWhatap  
  
set JAVA_OPTS_TMP=%JAVA_OPTS:"=%  
if not "x%JAVA_OPTS_TMP:whatap=%"=="x%JAVA_OPTS_TMP%" goto endWhatap  
  
:setWhatap  
set JAVA_OPTS=%JAVA_OPTS% %WHATAP_OPTS%  
  
:endWhatap  
rem ########## WHATAP END ############  

```
* Tomcat을 Windows 인스톨러로 설치한 경우


	1. ***시작*** > ***Apache Tomcat `X.Y.Z.`*** > ***Configure Tomcat***을 선택하세요.
	2. ***Java*** 탭을 선택하세요.
	3. ***Java Options*** 텍스트 박스에 `-javaagent` 옵션을 추가하세요.
```
-javaagent:{와탭 설치 경로}/whatap.agent-X.Y.Z.jar  

```
![Apache Tomcat](https://img.whatap.io/media/images/tomcat-win.png)

### Java 17 버전 이상[​](#java-17-버전-이상 "Java 17 버전 이상에 대한 직접 링크")

Java 17 버전 이상의 경우 reflection 관련한 다음 옵션을 추가하세요.


```
  
--add-opens=java.base/java.lang=ALL-UNNAMED  
  

```
힙 히스토그램 조회[​](#힙-히스토그램-조회 "힙 히스토그램 조회에 대한 직접 링크")
-------------------------------------------------

와탭의 Java 모니터링에서는 JVM 메모리에 올라가 있는 Heap 점유 객체 현황(힙 메모리상의 객체별 사이즈)을 조회할 수 있는 기능을 기본으로 제공합니다. 애플리케이션 > 인스턴스 성능 분석 메뉴에서 힙 히스토그램  탭을 선택하세요.

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

