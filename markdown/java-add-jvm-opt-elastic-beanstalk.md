Elastic Beanstalk
=================

에이전트 적용 하기[​](#에이전트-적용하기 "에이전트 적용하기에 대한 직접 링크")
-----------------------------------------------

**Elastic Beanstalk**를 이용해 배포할 경우 와탭 에이전트를 적용하는 방법입니다.

노트**Platform as a Service**(**PaaS**) 환경에서는 배포 대상 애플리케이션에 와탭 에이전트의 설정을 포함해 배포합니다.

1. Spring Boot 결과물을 jar로 배포할 경우 *.ebextensions*의 내용을 적용할 수 없습니다. 다음 파일들을 압축해 zip 형태로 배포하세요.


	* *.elasticbeanstalk/config.yml*: eb 명령을 실행하는 디렉터리 하위에 자동 생성
	* *.ebextensions/`{config_name}`.config*: eb 설정 파일
	* *Procfile*: JVM command line 옵션을 설정하기 위한 파일
	* *`{application}`.jar*: 실행할 applicaion.jar 파일
2. Service에 적용할 와탭 에이전트의 파일을 압축해 S3(혹은 다운로드할 수 있는 public 경로)에 업로드하세요.


	* *paramkey.txt*
	* *whatap.agent-2.0\_25.jar*
	* *whatap.conf*
```
# 디렉터리 압축하기  
zip -r whatap-agent.zip agent  

```
3. *.ebextension/`{config_name}`.config* 파일에 다운로드할 와탭 에이전트 경로를 입력하세요.

다운로드할 수 있도록 압축 파일 형태로 만들어 둔 경우 eb를 실행해 자동으로 다운로드한 다음 압축을 풉니다.


```
sources:  
  target directory:  
    S3경로  

```
Example
```
sources:  
  /home/webapp:  
    http://s3.ap-northeast-2.amazonaws.com/{bucket-name}/whatap-agent.zip  

```
4. 와탭 에이전트 옵션을 추가한 JVM command를 입력해 *Procfile*을 작성하세요.

Procfile
```
web: java -javaagent:${WHATAP_JAR_FILE_PATH} -Dwhatap.name=${WHATAP_NAME} -Dwhatap.okind=${WHATAP_OKIND_NAME} -Dwhatap.server.home=${APPLICAION_PATH} -Dwhatap.conf.path=${WHATAP_HOME} -jar ${APPLICAIONT}.jar  

```
Example
```
web: java -javaagent:/home/webapp/agent/whatap.agent-X.Y.Z.jar -Dwhatap.name=bootTest -Dwhatap.okind=test -Dwhatap.server.home=/var/app/current -Dwhatap.conf.path=/home/webapp/agent -jar whatap-boot-test.jar  

```
5. *Procfile* 파일과 *.ebextensions* 파일, *`{application}`.jar* 파일을 압축하세요.


```
zip -r {application}.zip Procfile .ebextensions/{application}.jar  

```
6. *.elasticbeanstalk/config.yml* 파일에 배포할 zip파일 경로를 추가하세요.


```
deploy:  
  artifact: /path/to/{application}.zip  

```
7. eb 배포 명령어를 실행하세요.


```
eb deploy  

```

노트Java 17 버전 이상의 경우 reflection 관련한 다음 옵션을 추가하세요.


```
  
--add-opens=java.base/java.lang=ALL-UNNAMED  
  

```
노트자세한 내용은 [AWS 가이드 문서](https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/Welcome.html)를 참조하세요.

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

