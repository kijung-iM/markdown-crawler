Docker
======

에이전트 적용하기[​](#에이전트-적  용하기 "에이전트 적용하기에 대한 직접 링크")
------------------------------------------------

기존 Docker 이미지를 바탕으로 와탭 에이전트 설정을 추가한 이미지를 빌드하세요.

노트이 문서에서는 Java 에이전트를 설치하는 경우만을 다룹니다. 와탭 쿠버네티스 모니터링과 함께 적용하는 경우 [다음 문서](/kubernetes/install-docker-java)를 참조하세요.

1. Docker 빌드 디렉터리를 생성하세요.


```
mkdir -p {Docker build dir}  

```
2. *whatap.conf* 파일을 생성하세요.


```
cat >{Docker build Dir}/whatap.conf <<EOL  
# 액세스 키를 입력하세요.  
license=XXXXXXXXXXXXXX-XXXXXXXXXXXXXX-XXXXXXXXXXXXXX   
# 수집 서버 IP 정보를 입력하세요.  
whatap.server.host=xx.xx.xx.xx/yy.yy.yy.yy   
EOL  

```
3. Dockerfile을 생성하세요.

이미지를 빌드할 경우 와탭 이미지에서 `-javaagent` 옵션에 적용할 jar 파일을 복사할 수 있습니다.


```
cat >/home/silver/whatap/docker/Dockerfile <<EOL  
FROM whatap/kube_mon as build  
## 실제 이미지 생성 (기존 이미지에 Whatap 추가)  
## $Image_Name(이미지명)  
FROM $Image_Name  
RUN mkdir -p /whatap  
COPY --from=build /data/agent/micro/whatap.agent-*.jar /whatap  
COPY ./whatap.conf /whatap/  
#...  
EOL  

```
4. `JAVA_OPT`에 다음 내용을 추가하세요.


```
WHATAP_HOME=/whatap  
WHATAP_JAR=ls ${WHATAP_HOME}/whatap.agent-*.jar | sort -V | tail -1  
export JAVA_OPTS="-javaagent:${WHATAP_JAR} "  

```
5. Docker를 빌드하세요.


```
cd docker  
docker build -t $Image_Name  

```

노트Java 17 버전 이상의 경우 reflection 관련한 다음 옵션을 추가하세요.


```
  
--add-opens=java.base/java.lang=ALL-UNNAMED  
  

```
노트Java 에이전트 파일 이름은 `Rename` 기능을 활용해 수정할 수 있습니다. Java 에이전트의 이름을 수정했다면 `JAVA_OPTS`에 새로운 Java 에이전트 이름을 등록하세요.

**Java 에이전트 이름 수정 방법 예시**


```
java -cp whatap.agent-X.Y.Z.jar whatap.agent.setup.Rename -from whatap.agent-X.Y.Z.jar -to whatap.agent.jar  

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

