설치 문제 해결
========

방화벽 설정 확인[​](#방화벽-설정-확인 "방화벽 설정 확인에 대한 직접 링크")
----------------------------------------------

와탭의 데이터 수집 서버에 대한 TCP 아웃바운드 정책을 설정하지 않으면 모니터링 정보를 전송할 수 없습니다. **방화벽 차단**을 **해제**하세요.

`telnet` 명령을 사용해 "Connected to `IP`"를 확인하세요.


```
$ telnet 52.193.60.176 6600  
Trying 52.193.60.176...  
Connected to 52.193.60.176.  
Escape character is '^]'.  

```
노트수집 서버 정보는 [와탭 모니터링 서비스](https://service.whatap.io/)에서 해당 프로젝트를 선택한 다음 ***관리*** > ***에이전트 설치*** 메뉴에서 확인할 수 있습니다.

SpringBoot 2.2 버전 이상, Tomcat JMX가 off 상태[​](#springboot-22-버전-이상-tomcat-jmx가-off-상태 "SpringBoot 2.2 버전 이상, Tomcat JMX가 off 상태에 대한 직접 링크")
-----------------------------------------------------------------------------------------------------------------------------------------

SpringBoot 2.2 버전 이상에서 Embedded Tomcat을 사용하는 경우 기본값으로 JMX 관련 기능이 동작하지 않습니다. 이 경우 JMX 기능을 활성화하세요. [관련 링크](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-2.2-Release-Notes#jmx-now-disabled-by-default)

application.properties
```
spring.jmx.enabled=true  
server.tomcat.mbeanregistry.enabled=true # tomcat embedded인 경우 #  

```
application.yml
```
spring:  
  jmx:  
    enabled: true  
server:  
  tomcat:  
    mbeanregistry:  
      enabled: true #tomcat embedded인 경우  

```
OSGI 프레임워크 사용 애플리케이션 서버의 경우[​](#osgi-프레임워크-사용-애플리케이션-서버의-경우 "OSGI 프레임워크 사용 애플리케이션 서버의 경우에 대한 직접 링크")
----------------------------------------------------------------------------------------------------

OSGI 프레임워크 구조의 애플리케이션 서버인 경우 JVM 옵션에 에이전트 패키지 prefix(whatap)를 등록하세요.

Jboss EAP 6.0 버전 이상, Jboss AS 7.0 버전 이상, Wildfly 8.0 버전 이상, IBM WebSphere AS 7.0 버전 이상 등이 해당합니다.

### JBoss AS, Wildfly, JBoss EAP 6.0 이상[​](#jboss-as-wildfly-jboss-eap-60-이상 "JBoss AS, Wildfly, JBoss EAP 6.0 이상에 대한 직접 링크")

다음 파일에 prefix를 등록하세요.

$JBOSS\_HOME/bin/standalone.conf(domain.conf)
```
-Djboss.modules.system.pkgs=whatap  

```
![JBOSS EAP 7.0](https://img.whatap.io/media/agent_java/install/410.png)

### WebSphere[​](#websphere "WebSphere에 대한 직접 링크")

JVM 옵션으로 다음 내용을 추 가하세요.


```
-Dcom.ibm.ws.classloader.server.alwaysAllowedPackages=whatap  

```
* 기본값으로 '\*'로 지정된 경우 별도 설정이 필요 없습니다.
* 설정 위치는 [WebSphere](/java/add-jvm-opt/websphere)를 참조합니다.

*security.policy* 권한을 다음과 같이 추가하세요.

$WEBSPHERE\_HOME/properties/server.policy || $WEBSPHERE\_PROFILE\_HOME/properties/server.policy
```
grant codeBase "file:$WHATAP_HOME/-"  
{  
   permission java.security.AllPermission;  
};  

```
Log Manager 관련 에러[​](#log-manager-관련-에러 "Log Manager 관련 에러에 대한 직접 링크")
----------------------------------------------------------------------

JBoss AS 7.0 버전 이상, JBoss EAP 6.0 버전 이상에서 Log Manager 관련 에러가 발생한다면 JVM 옵션을 추가합니다.

* `-Djava.util.logging.manager` 항목에 Log Manager package 명을 설정하세요.
* `-Xbootclassloader` 항목에 JBoss Log Manager JAR file을 설정하세요.

(JBoss\_Path)/bin/standalone.conf(domain.conf)
```
# Specify the exact Java VM executable to use.  
#  
if [ "x$JBOSS_MODULES_SYSTEM_PKGS" = "x" ]; then  
    JBOSS_MODULES_SYSTEM_PKGS="org.jboss.byteman,org.jboss.logmanager,whatap"  
fi  
  
...  
# Specify options to pass to the Java VM.  
#  
if [ "x$JAVA_OPTS" = "x" ]; then  
    JAVA_OPTS="-Xms1303m -Xmx1303m -Djava.net.preferIPv4Stack=true"  
    JAVA_OPTS="$JAVA_OPTS -Djboss.modules.system.pkgs=$JBOSS_MODULES_SYSTEM_PKGS -Djava.awt.headless=true"  
    JAVA_OPTS="$JAVA_OPTS -Djava.util.logging.manager=org.jboss.logmanager.LogManager -Xbootclasspath/p:/home/vagrant/EAP-7.0.0/modules/system/layers/base/org/jboss/logmanager/main/jboss-logmanager-2.0.3.Final-redhat-1.jar"  
else  
    echo "JAVA_OPTS already set in environment; overriding default settings with values: $JAVA_OPTS"  
fi  

```
MBeanServerBuilder 에러가 발생하는 경우[​](#mbeanserverbuilder-에러가-발생하는-경우 "MBeanServerBuilder 에러가 발생하는 경우에 대한 직접 링크")
-------------------------------------------------------------------------------------------------------------

JBoss 5.0 버전 이하에서 MBeanServerBuilder 관련 에러가 출력된 경우 JVM 옵션을 추가하세요.

(JBoss\_Path)/bin/run.conf
```
# Specify options to pass to the Java VM.  
#  
if [ "x$JAVA_OPTS" = "x" ]; then  
   JAVA_OPTS="-Xms128m -Xmx512m -XX:MaxPermSize=256m -Dorg.jboss.resolver.warning=true -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000"  
   JAVA_OPTS="$JAVA_OPTS -Djboss.platform.mbeanserver"  
fi  

```
Permission 오류가 발생하는 경우[​](#permission-오류가-발생하는-경우 "Permission 오류가 발생하는 경우에 대한 직접 링크")
-------------------------------------------------------------------------------------

Java Security Policy 관련 오류가 발생하면 *$JAVA\_HOME/jre/lib/security/java.policy* 파일에 권한 설정을 추가하세요.

모든 권한을 일괄 적용하려면 다음과 같이 *java.policy* 파일에 설정을 추가하세요.

$JAVA\_HOME/jre/lib/security/java.policy
```
grant {  
   permission java.security.AllPermission;  
};  

```
### java.io.FilePermission 오류가 발생하는 경우[​](#javaiofilepermission-오류가-발생하는-경우 "java.io.FilePermission 오류가 발생하는 경우에 대한 직접 링크")

![java.io.FilePermision error](/assets/images/troubleshooting-permission-error-4d8210609932d8b7a2d2121045758cd9.png)

다음과 같이 *java.policy* 파일에 설정을 추가하세요.

$JAVA\_HOME/jre/lib/security/java.policy
```
grant {  
   ...  
   permission java.io.FilePermission {오류 메시지에서 확인된 패키지 경로}, "read"  
};  

```
### java.util.PropertyPermission 오류가 발생하는 경우[​](#javautilpropertypermission-오류가-발생하는-경우 "java.util.PropertyPermission 오류가 발생하는 경우에 대한 직접 링크")

다음과 같이 *java.policy* 파일에 설정을 추가하세요.

$JAVA\_HOME/jre/lib/security/java.policy
```
grant {  
   ...  
   permission java.util.PropertyPermission {오류 메시지에서 확인된 패키지 경로}, "read"  
};  

```
Sigar library를 로딩하지 못하는 경우[​](#sigar-library를-로딩하지-못하는-경우 "Sigar library를 로딩하지 못하는 경우에 대한 직접 링크")
-------------------------------------------------------------------------------------------------

*$WHATAP\_HOME/lib1/\*.so* 파일에 실행 권한이 있는지 확인하세요. 권한이 없다면 실행 권한을 부여하세요.


```
$ sudo chmod +x *.so  

```
AIX 7에서 *$WHATAP\_HOME/lib1* 하위에 *libsigar-ppc64-aix-7.so* 파일이 없어 오류가 발생한 경우 파일을 복사하세요.

![Sigar library error on AIX 7](/assets/images/troubleshooting-sigar-error-4d8210609932d8b7a2d2121045758cd9.png)


```
$ cp libsigar-ppc64-aix-5.so libsigar-ppc64-aix-7.so  

```
