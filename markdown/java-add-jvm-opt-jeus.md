JEUS
====

JVM 옵션 추가[​](#jvm-옵션-추가 "JVM 옵션 추가에 대한 직접 링크")
----------------------------------------------

JEUS 애플리케이션 서버 환경에서 Java 모니터링 에이전트를 효과적으로 사용하기 위해 필요한 JVM 옵션을 추가하는 방법을 안내합니다.

1. JEUS 버전에 따른 시작 옵션의 설정 파일의 경로를 참고해 `-javaagent` 옵션을 추가하세요.


	* JEUS 7
	* JEUS 6$JEUS\_HOME/domains/jeus\_domain/config.xml
```
<domain>  
    <servers>  
        <server>  
            <name>server1</name>  
            <jvm-config>  
                <jvm-option>  
                    -Xmx1024m -XX:MaxPermSize=128m  
                    -javaagent:/whatap/whatap.agent-X.Y.Z.jar  
                </jvm-option>  
            </jvm-config>  
        </server>  
    </servers>  
    ...  
</domain>  

```
$JEUS\_HOME/config/$hostname/JEUSMain.xml
```
<node>  
    <name>node01</name>  
    <engine-container1>  
        <name>container1</name>  
        ...  
        <command-option>-Xmx1024m -XX:MaxPermSize=128m  
            -javaagent:/whatap/whatap.agent-#.#.#.jar  
        </command-option>  
        ...  
    </engine-container1>  
</node>  

```
2. 애플리케이션 서버를 다시 시작하세요.


```
jdown && jboot  

```
3. 애플리케이션 서버 로그 파일과 에이전트 로그 파일을 통해 에이전트가 정상 작동하는지, 에러가 발생하지 않았는지 확인하세요. 로그 파일의 위치는 다음을 참고하세요.


	* 에이전트: *$WHATAP\_HOME/logs/whatap-`{SERVER_NAME}`-`{DATE}`.log*
	* JEUS 7: *$JEUS\_HOME/domains/$HOST\_NAME/servers/$NODE\_NAME/logs/JeusServer.log*
	* JEUS 6: *$JEUS\_HOME/logs/$NODE\_NAME/JeusServer.log*
4. 에이전트가 애플리케이션 서버의 종류와 서비스 컨테이너 명을 인식했는지 확인하세요.

노트[와탭 모니터링 서비스](https://service.whatap.io/)에 로그인한 다음 프로젝트를 선택하세요. 애플리케이션 > 인스턴스 성능 분석 메뉴를 선택한 다음 실행 환경 변수 탭을 선택하세요. ***whatap.name***과 ***whatap.type*** 항목을 확인하세요. ***whatap.name*** 항목의 마지막 요소가 컨테이너 이름이어야 합니다. ***whatap.type*** 항목에는 애플리케이션 서버의 종류가 명시되어야 합니다.

![Boot Environment](https://img.whatap.io/media/agent_java/install/380.png)

노트Java 17 버전 이상의 경우 reflection 관련한 다음 옵션을 추가하세요.


```
  
--add-opens=java.base/java.lang=ALL-UNNAMED  
  

```
힙 히스토그램 조회[​](#힙-히스토그램-조회 "힙 히스토그램 조회에 대한 직접 링크")
-------------------------------------------------

와탭의 Java 모니터링에서는 JVM 메모리에 올라가 있는 Heap 점유 객체 현황(힙 메모리상의 객체별 사이즈)을 조회할 수 있는 기능을 기본으로 제공합니다. 애플리케이션 > 인스턴스 성능 분석 메뉴에서 힙 히스토그램 탭을 선택하세요.

Java 6 ~ 8 버전에서는 JVM 옵션 없 이 기본 지원하지만, 일부 Java 버전에 따라 다음과 같이 JVM 옵션을 적용해야 합니다.

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

