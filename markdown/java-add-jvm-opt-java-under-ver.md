Java 1.6 버전 미만
==============

Java 1.6 버전 미만에서 와탭 에이전트를 적용할 수 있습니다. 하지만 일부 기능에 제약이 있습니다.

Java 1.5 버전[​](#java-15-버전 "Java 1.5 버전에 대한 직접 링크")
---------------------------------------------------

Java 1.5 버전은 `-javaagent` 옵션을 제공합니다. 다만 외부 스레드의 정보를 조회하는데 제약이 있어 일부 기능에 제약이 있습니다.

다음의 기능들은 동작하지 않습니다.

* 액티브 트랜잭션에서 실시간 트레이스
* 스택 분석 (탑 스택, 유니크 스택, 액티브 스택)
* 스레드 목록의 상세 스택

Java 1.4 버전[​](#java-14-버전 "Java 1.4 버전에 대한 직접 링크")
---------------------------------------------------

Java 1.4 버전은 `-javaagent` 옵션이 없습니다. 다른 방식으로 와탭 에이전트를 설치해야 합니다. 물론 *whatap.agent.jar* 파일은 Java 1.4 버전을 사용해야 합니다.


> whatap.java14.tracer-`X.Y.Z`.jar

### boot.jar 생성[​](#bootjar-생성 "boot.jar 생성에 대한 직접 링크")

*setup.sh* 파일을 이용해 *boot.jar* 파일을 생성하세요. 만약 [JAVA\_HOME]을 입력하지 않으면 현재 경로를 JDK의 위치를 자동으로 인식합니다.


```
$ setup.sh [JAVA_HOME]  

```
*setup.sh* 실행 결과: *whatap.java14.boot-`X.Y.Z`.jar*

### bootclasspath에 설치[​](#bootclasspath에-설치 "bootclasspath에 설치에 대한 직접 링크")

`bootclasspath` 옵션을 사용해 빌드된 jar와 tracer jar를 prepend로 추가하세요.


```
-Xbootclasspath/p:${WHATAP_HOME}/whatap.java14.boot-1.0.2.jar:${WHATAP_HOME}/whatap.java14.tracer-1.0.2.jar  

```
### 제약 사항[​](#제약-사항 "제약 사항에 대한 직접 링크")

jdk 1.4 버전에서는 다음의 기능들이 동작하지 않습니다.

* 액티브 트랜잭션에서 실시간 트래이스
* 스택 분석 (탑 스택, 유니크 스택, 액티브 스택)
* 컴포넌트 버전
* 스레드 목록, 힙히스토그램
* 로드된 클래스
* 오픈 소켓
* 에이전트 덤프
