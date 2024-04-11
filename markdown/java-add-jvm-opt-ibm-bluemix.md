IBM BlueMix
===========

에이전트 적용하기[​](#에이전트-적용하기 "에이전트 적용하기에 대한 직접 링크")
----------------------------------------------

**IBM BlueMix**를 이용해 배포할 경우 와탭 에이전트를 적용하는 방법입니다.

[IBM BlueMix](https://console.bluemix.net/docs/apps/index.html%E2%80%8B)는 컨테이너로 **WebSphere Liberty** 환경을 제공합니다. **Liberty**는 **WebSphere Application Server**와 다른 경량화 환경으로 **Spring Boot**가 동작하는 방식과 유사합니다.

노트**Platform as a Service**(**PaaS**) 환경에서는 배포 대상 애플리케이션에 와탭 에이전트의 설정을 포함해 배포합니다.

다음은 설정 환경 예제입니다. [가이드](https://cloud.ibm.com/docs)에 따른 환경을 구성할 경우 로컬 개발 환경에서 생성하는 파일들입니다.


```
whatap@vmwas01:/apps/bluemix/java-helloworld$ ls -alrt  
합계 64  
drwxrwxr-x 3 whatap whatap  4096 10월 29 13:13 ..  
-rw-rw-r-- 1 whatap whatap  1079 10월 29 13:13 .classpath  
-rw-rw-r-- 1 whatap whatap  1184 10월 29 13:13 .project  
-rw-rw-r-- 1 whatap whatap    39 10월 29 13:13 .gitignore  
-rw-rw-r-- 1 whatap whatap   151 10월 29 13:13 CONTRIBUTING.md  
drwxrwxr-x 2 whatap whatap  4096 10월 29 13:13 .settings  
-rw-rw-r-- 1 whatap whatap  2823 10월 29 13:13 pom.xml  
-rw-rw-r-- 1 whatap whatap   122 10월 29 13:13 manifest.yml  
-rw-rw-r-- 1 whatap whatap  3522 10월 29 13:13 README.md  
-rw-rw-r-- 1 whatap whatap 11323 10월 29 13:13 LICENSE  
drwxrwxr-x 3 whatap whatap  4096 10월 29 13:13 src  
drwxrwxr-x 2 whatap whatap  4096 10월 29 13:13 target  
drwxrwxr-x 8 whatap whatap  4096 10월 29 13:13 .git  
drwxrwxr-x 6 whatap whatap  4096 10월 29 15:26 .  

```
1. `${APP_HOME}`에서 *src/main/resources/whatap-agent/* 디렉터리를 생성하고 jar 파일, conf 파일을 복사하세요.


```
$ mkdir -p src/main/resources/whatap-agent/  
$ cp /apps/whatap/whatap.agent.tracer-1.5.4.jar src/main/resources/whatap-agent/  
$ cp /apps/whatap/whatap.conf src/main/resources/whatap-agent/  

```
2. *`${APP_HOME}`/manifest.yml* 파일에 옵션을 추가하세요. yml 파일이므로 공백, 들여쓰기 기준을 잘 맞춰 작성하세요.


```
---  
applications:  
- name: sample-java-helloworld  
random-route: true  
memory: 256M  
path: target/JavaHelloWorldApp.war  
# 여기서부터 추가합니다.  
env:  
    JAVA_OPTS: "-javaagent:/{APPLICATION_DIR}/WEB-INF/classes/whatap-agent/whatap.agent-X.Y.Z.jar -Dorg.osgi.framework.bootdelegation=whatap.* "  

```

노트Java 17 버전 이상의 경우 reflection 관련한 다음 옵션을 추가하세요.


```
  
--add-opens=java.base/java.lang=ALL-UNNAMED  
  

```
노트* *whatap.conf* 설정은 PaaS가 아닌 환경과 동일하게 적용합니다. 적용 후 에이전트 명 식별에 어려울 수 있으니 상황에 맞는 에이전트 명을 적용하세요.
* 에이전트 네이밍에 관한 자세한 내용은 [다음 문서](/java/agent-name)를 참조하세요.
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

