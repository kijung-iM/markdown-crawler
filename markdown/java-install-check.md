설치 점검 사항
========

에이전트를 설치한 다음 확인해야할 사항입니다. 만약 설치에 문제가 생겼다면 [다음 문서](/java/agent-troubleshooting)를 참조하세요.

WAS 다시 시작[​](#was-다시-시작 "WAS 다시 시작에 대한 직접 링크")
----------------------------------------------

애플리케이션 서버를 다시 시작하세요. 구동 로그에서 다음과 같은 와탭 캐릭터 로그가 보인다면 `JAVA_OPTS` 설정을 완료한 것입니다.


```
Nov 16, 2016 3:06:40 AM org.apache.catalina.startup.HostConfig deployDirectory  
INFO: Deployment of web application directory /var/lib/tomcat7/webapps/ROOT has finished in 577 ms  
Nov 16, 2016 3:06:40 AM org.apache.coyote.AbstractProtocol start  
INFO: Starting ProtocolHandler ["http-bio-8080"]  
Nov 16, 2016 3:06:40 AM org.apache.catalina.startup.Catalina start  
INFO: Server startup in 3984 ms  
_  	 ____       ______  
| | /| / / /  ___ /_  __/__ ____  
| |/ |/ / _ \/ _ `// / / _ `/ _ \  
|__/|__/_//_/\_,_//_/  \_,_/ .__/  
        	             /_/  
Just Tap, Always Monitoring  
WhaTap Agent version 0.3.9 20161115  

```
에이전트 연결 확인[​](#에이전트-연결-확인 "에이전트 연결 확인에 대한 직접 링크")
-------------------------------------------------

[와탭 모니터링 서비스](https://service.whatap.io)로 이동하세요. 로그인 후 프로젝트 목록에서 생성한 프로젝트를 선택하세요. ***애플리케이션 대시보드*** 화면에 연결한 서버의 정보가 나타나면 적용을 완료한 것입니다.

![애플리케이션 대시보드](/img/after-install-apm-dashboard.png)

노트* 에이전트 이름의 기본값은 `{type}-{ip2}-{ip3}-{port}`입니다.
* 에이전트의 이름을 변경하거나 속성을 추가하려면 [다음 문서](/java/agent-name)를 참조하세요.
