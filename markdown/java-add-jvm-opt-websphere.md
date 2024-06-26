WebSphere
=========

JVM 옵션 추가[​](#jvm-옵션-추가 "JVM 옵션 추가에 대한 직접 링크")
----------------------------------------------

WebSphere 애플리케이션 서버 환경에서 Java 모니터링 에이전트를 효과적으로 사용하기 위해 필요한 JVM 옵션을 추가하는 방법을 안내합니다. JVM 옵션을 추가하려면 관리 콘솔(Admin console)로 접속하세요.

1. 웹브라우저에서 관리 콘솔에 로그인하세요.
2. ***Environment*** > ***Virtual Hosts*** > ***default host*** > ***Host Aliases*** 항목을 선택한 다음 에이전트를 설치할 서버의 포트 번호를 확인하세요.

![WebSphere port](https://img.whatap.io/media/agent_java/install/330.png)
3. ***Servers*** > ***Server Types*** > ***Websphere application servers*** 항목으로 이동한 다음 에이전트를 설치할 서버를 선택하세요.

![WebSpherer application servers](https://img.whatap.io/media/agent_java/install/300.png)
4. 선택한 서버 화면에서 ***Configuration*** 탭을 선택하고 ***Server Infrastructure*** 섹션의 ***Java and Process Management*** > ***Process definition*** 메뉴를 선택하세요.

![WebSphere Configuration](https://img.whatap.io/media/agent_java/install/310.png)
5. 오른쪽 메뉴에서 ***Additional Properties*** > ***Java Virtual Machine*** 메뉴를 선택하세요.
6. ***Configuration*** 탭에서 ***Generic JVM arguments*** 텍스트 박스에 `-javaagent`와 `-Dwhatap.port`를 추가하세요.


```
-javaagent:/whatap/whatap.agent-X.Y.Z.jar  
-Dwhatap.port={포트번호} ## 2번 항목 포트 번호 ##  

```
![Add JVM arguments](https://img.whatap.io/media/agent_java/install/340.png)

노트Java 17 버전 이상의 경우 reflection 관련한 다음 옵션을 추가하세요.


```
  
--add-opens=java.base/java.lang=ALL-UNNAMED  
  

```
힙 히스토그램 조회[​](#힙-히스토그램-조회 "힙 히스토그램 조회에 대한 직접 링크")
-------------------------------------------------

와탭의 Java 모니터링에서는 JVM 메모리에 올라가 있는 Heap 점유 객체 현황(힙   메모리상의 객체별 사이즈)을 조회할 수 있는 기능을 기본으로 제공합니다. 애플리케이션 > 인스턴스 성능 분석 메뉴에서 힙 히스토그램 탭을 선택하세요.

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

