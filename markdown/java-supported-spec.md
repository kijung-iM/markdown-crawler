지원 환경
=====

Java 에이전트 지원 환경[​](#java-에이전트-지원-환경 "Java 에이전트 지원 환경에 대한 직접 링크")
----------------------------------------------------------------

에이전트를 설치하기 전에 JVM 애플리케이션 서버가 다음의 사양을 충족하는지 확인하세요.

Web Application Server (WAS) 뿐 아니라 데몬 및 배치 애플리케이션 등 JVM에서 동작하는 모든 애플리케이션에 적용할 수 있습니다. Java 1.6 미만은 [support@whatap.io](mailto:support@whatap.io)로 문의하거나 [다음 문서](/java/add-jvm-opt/java-under-ver)를 참조하세요.

* **지원 버전**



| 지원범위 | 환경 | OS | JVM 버전 |
| --- | --- | --- | --- |
| Fully support | Java | JVM으로 구동하는 모든 OS | Java 6 이상, Java 20 이하 |
| Limited support | Java | JVM으로 구 동하는 모든 OS | Java 1.5 이하 |
* **운영체제**


	+ HP-UX 11.x 32bit, 64bit
	+ Itanium 64bit
	+ Oracle Solaris 2.8, 2.9, 10, 11 32bit, 64bit
	+ x86 Intel Linux 32bit
	+ Red Hat Itanium 64bit
	+ Microsoft Windows 2000, XP, 2003, 2008, 7, 8노트JDK 6를 설치할 수 있는 모든 운영체제를 지원합니다.
* **애플리케이션 서버**


	+ BEA WebLogic 9.x, 10.x, 11.x, 12.x
	+ Tmaxsoft JEUS 6.x, 7.x
	+ SUN Application Server 8.x, 9.x
	+ Fujitsu Interstage 5.x, 6.x, 7.x
	+ Hitachi Cosminexus 7.x, 8.x, 9.x
	+ Apache Jakarta Tomcat 6.x, 7.x, 8.x, 9.x, 10.x
	+ Caucho Technology Resin 3.x, 4.x
	+ Red Hat JBoss Application Server 6.x, 7.x
	+ GlassFish 3.x, 4.x, 5.x노트이외 Java EE Spec을 준수하는 모든 애플리케이션 서버를 지원합니다. [다음 링크](https://www.oracle.com/technetwork/java/javaee/overview/compatibility-jsp-136984.html)를 참조하세요.
* **프레임워크** / **라이브러리**


	+ Spring Boot Project
	+ Netty, Akka HTTP 및 Play Framework 등 비동기 Framework
	+ Quarkus, Quarkus-reactive
	+ Mule Framework 3.9.5, Mule Framework 4.5노트이외 Java EE Spec을 준수하는 Application Server에서 동작하 는 모든 라이브러리를 지원합니다.
* **데이터베이스**


	+ Generic JDBC (any JDBC compliant driver)
	+ DB2 JDBC
	+ Derby JDBC
	+ H2 JDBC
	+ jTDS JDBC
	+ MariaDB JDBC
	+ Microsoft SQL Server JDBC
	+ MySQL mysql-connector-java
	+ Oracle ojdbc5, ojdbc6, ojdbc7, ojdbc8, ojdbc14
	+ Postgres JDBC
	+ Tibero
	+ Jedis Redis driver

애플리케이션 서버별 호환성 및 데이터 소스[​](#애플리케이션-서버별-호환성-및-데이터-소스 "애플리케이션 서버별 호환성 및 데이터 소스에 대한 직접 링크")
----------------------------------------------------------------------------------------

### Tomcat[​](#tomcat "Tomcat에 대한 직접 링크")

#### 호환성[​](#호환성 "호환성에 대한 직접 링크")



| WAS Ver. | Java SE 6 (jdk1.6.0) | Java SE 7 (jdk1.7.0\_80) | Java SE 8 (jdk1.8.0\_91) |
| --- | --- | --- | --- |
| Tomcat 6 | ✅ | ✅ | ✅ |
| Tomcat 7 | ✅ | ✅ | ✅ |
| Tomcat 8 | ❌ | ✅ | ✅ |
| Tomcat 9 | ❌ | ❌ | ✅ |



| WAS Ver. | OpenJDK 6 (1.6.0\_45) | OpenJDK 7 (1.7.0\_80) | OpenJDK 8 (1.8.0\_91) |
| --- | --- | --- | --- |
| Tomcat 6 | ✅ | ✅ | ✅ |
| Tomcat 7 | ✅ | ✅ | ✅ |
| Tomcat 8 | ❌ | ✅ | ✅ |
| Tomcat 9 | ❌ | ❌ | ✅ |



| WAS Ver. | ibm-java-x86\_64-60 | ibm-java-x86\_64-71 | ibm-java-x86\_64-80 |
| --- | --- | --- | --- |
| Tomcat 6 | ✅ | ✅ | ✅ |
| Tomcat 7 | ✅ | ✅ | ✅ |
| Tomcat 8 | ❌ | ✅ | ✅ |
| Tomcat 9 | ❌ | ❌ | ✅ |

#### DataSource[​](#datasource "DataSource에 대한 직접 링크")



| DB | JDBC Driver 파일명 | JDBC Ver. | JDK Ver. | 호환성 |
| --- | --- | --- | --- | --- |
| MySQL | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| MariaDB | mariadb-java-client-1.4.6.jar | 1.4.6 | JDK 1.7.0\_80 | ✅ |
| PostgreSQL | postgresql-9.4.1209.jre7.jar | 9.4.1209 | JDK 1.7.0\_80 | ✅ |
| Amazon Aurora | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| Oracle | ojdbc6-11.2.0.2.0.jar | 11.2.0.2.0 | JDK 1.7.0\_80 | ✅ |
| DB2 | db2jcc.jar, db2jcc\_license\_cu.jar | 1.4.2 | JDK 1.7.0\_80 | ✅ |

### JBoss[​](#jboss "JBoss에 대한 직접 링크")

#### 호환성[​](#호환성-1 "호환성에 대한 직접 링크")



| WAS Ver. | Java SE 6 (jdk1.6.0) | Java SE 7 (jdk1.7.0\_80) | Java SE 8 (jdk1.8.0\_91) |
| --- | --- | --- | --- |
| JBOSS EAP 7.0 (standalone) | ❌ | ❌ | ✅ |
| JBOSS EAP 6.1.1 (standalone) | ❌ | ✅ | ❌ |
| JBOSS EAP 6.2 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 6.3 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 6.4 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 7.0 (domain) | ❌ | ❌ | ✅ |
| JBOSS AS 5.1.0 (default) | ✅ | ✅ | ✅ |



| WAS Ver. | OpenJDK 6 (1.6.0\_45) | OpenJDK 7 (1.7.0\_80) | OpenJDK 8 (1.8.0\_91) |
| --- | --- | --- | --- |
| JBOSS EAP 7.0 (standalone) | ❌ | ❌ | ✅ |
| JBOSS EAP 6.1.1 (standalone) | ❌ | ✅ | ❌ |
| JBOSS EAP 6.2 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 6.3 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 6.4 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 7.0 (domain) | ❌ | ❌ | ✅ |
| JBOSS AS 5.1.0 (default) | ✅ | ✅ | ✅ |



| WAS Ver. | ibm-java-x86\_64-60 | ibm-java-x86\_64-71 | ibm-java-x86\_64-80 |
| --- | --- | --- | --- |
| JBOSS EAP 7.0 (standalone) | ❌ | ❌ | ✅ |
| JBOSS EAP 6.1.1 (standalone) | ❌ | ✅ | ❌ |
| JBOSS EAP 6.2 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 6.3 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 6.4 (standalone) | ❌ | ✅ | ✅ |
| JBOSS EAP 7.0 (domain) | - | - | - |
| JBOSS AS 5.1.0 (default) | ✅ | ✅ | ✅ |

#### DataSource[​](#datasource-1 "DataSource에 대한 직접 링크")



| DB | JDBC Driver 파일명 | JDBC Ver. | JDK Ver. | 호환성 |
| --- | --- | --- | --- | --- |
| MySQL | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| MariaDB | mariadb-java-client-1.4.6.jar | 1.4.6 | JDK 1.7.0\_80 | ✅ |
| PostgreSQL | postgresql-9.4.1209.jre7.jar | 9.4.1209 | JDK 1.7.0\_80 | ✅ |
| Amazon Aurora | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| Oracle | ojdbc6-11.2.0.2.0.jar | 11.2.0.2.0 | JDK 1.7.0\_80 | ✅ |
| DB2 | db2jcc.jar, db2jcc\_license\_cu.jar | 1.4.2 | JDK 1.7.0\_80 | ✅ |

### JEUS[​](#jeus "JEUS에 대한 직접 링크")

#### 호환성[​](#호환성-2 "호환성에  대한 직접 링크")



| WAS Ver. | Java SE 6 (jdk1.6.0) | Java SE 7 (jdk1.7.0\_80) | Java SE 8 (jdk1.8.0\_91) |
| --- | --- | --- | --- |
| JEUS 7 | ✅ | ✅ | ✅ |
| JEUS 6 | ✅ | ✅ | ✅ |



| WAS Ver. | OpenJDK 6 (1.6.0\_45) | OpenJDK 7 (1.7.0\_80) | OpenJDK 8 (1.8.0\_91) |
| --- | --- | --- | --- |
| JEUS 7 | ✅ | ✅ | ✅ |
| JEUS 6 | ✅ | ✅ | ✅ |



| WAS Ver. | ibm-java-x86\_64-60 | ibm-java-x86\_64-71 | ibm-java-x86\_64-80 |
| --- | --- | --- | --- |
| JEUS 7 | ✅ | ✅ | ✅ |
| JEUS 6 | ✅ | ✅ | ❌ |

#### DataSource[​](#datasource-2 "DataSource에 대한 직접 링크")



| DB | JDBC Driver 파일명 | JDBC Ver. | JDK Ver. | 호환성 |
| --- | --- | --- | --- | --- |
| MySQL | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| MariaDB | mariadb-java-client-1.4.6.jar | 1.4.6 | JDK 1.7.0\_80 | ✅ |
| PostgreSQL | postgresql-9.4.1209.jre7.jar | 9.4.1209 | JDK 1.7.0\_80 | ✅ |
| Amazon Aurora | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| Oracle | ojdbc6-11.2.0.2.0.jar | 11.2.0.2.0 | JDK 1.7.0\_80 | ✅ |
| DB2 | db2jcc.jar, db2jcc\_license\_cu.jar | 1.4.2 | JDK 1.7.0\_80 | ✅ |

### WebSphere[​](#websphere "WebSphere에 대한 직접 링크")

#### 호환성[​](#호환성-3 "호환성에 대한 직접 링크")



| WAS Ver. | ibm-java-x86\_64-60 |
| --- | --- |
| 8.5.5.10 | ✅ |

#### DataSource[​](#datasource-3 "DataSource에 대한 직접 링크")



| DB | JDBC Driver 파일명 | JDBC Ver. | JDK Ver. | 호환성 |
| --- | --- | --- | --- | --- |
| Mysql | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| Oracle | ojdbc6-11.2.0.2.0.jar | 11.2.0.2.0 | JDK 1.7.0\_80 | ✅ |

### JETTY[​](#jetty "JETTY에 대한 직접 링크")

#### 호환성[​](#호환성-4 "호환성에 대한 직접 링크")



| WAS Ver. | Java SE 6 (jdk1.6.0) | Java SE 7 (jdk1.7.0\_80) | Java SE 8 (jdk1.8.0\_91) |
| --- | --- | --- | --- |
| Jetty 8.1.21 | ❌ | ✅ | ✅ |
| Jetty 9.2.18 | ❌ | ✅ | ✅ |
| Jetty 9.3.12 | ❌ | ❌ | ✅ |



| WAS Ver. | ibm-java-x86\_64-60 | ibm-java-x86\_64-71 | ibm-java-x86\_64-80 |
| --- | --- | --- | --- |
| Jetty 8.1.21 | ❌ | ✅ | ✅ |
| Jetty 9.2.18 | ❌ | ✅ | ✅ |
| Jetty 9.3.12 | ❌ | ❌ | ✅ |

#### DataSource[​](#datasource-4 "DataSource에 대한 직접 링크")



| DB | JDBC Driver 파일명 | JDBC Ver. | JDK Ver. | 호환성 |
| --- | --- | --- | --- | --- |
| MySQL | mysql-connector-java-5.1.39-bin.jar | 5.1.39 | JDK 1.7.0\_80 | ✅ |
| Oracle | ojdbc6-11.2.0.2.0.jar | 11.2.0.2.0 | JDK 1.7.0\_80 | ✅ |

공통 지원 환경[​](#공통-지원-환경 "공통 지원 환경에 대한 직접 링크")
-------------------------------------------

### 브라우저 지원[​](#브라우저-지원 "브라우저 지원에 대한 직접 링크")

와탭 모니터링 서비스는 웹브라우저와 모바일 앱에서 이용할 수 있습니다.



| 브라우저 | 권장여부 | 지원버전 |
| --- | --- | --- |
| Google Chrome | ✅ | 84 이상 |
| Mozilla FireFox | ❌ | 최신 버전 |
| Edge | ❌ | 최신 버전 |
| Safari | ❌ | 최신 버전 |

노트* 브라우저 호환성과 성능을 이유로 Chrome 최신 버전 사용을 권장합니다.
* 사용자 인터페이스(User Interface, UI)는 HTML5 표준 기술로 구현하여 Internet Explorer는 지원하지 않습니다.
### 방화벽[​](#방화벽 "방화벽에 대한 직접 링크")

와탭 에이전트는 수집 서버 **TCP 6600** 포트로 접속 가능해야 합니다. 모니터링 대상과 가까운 수집 서버 주소를 허용하세요.

**출발지: 와탭 에이전트**



| 목적지 | 목적지 IP | 포트 |
| --- | --- | --- |
| 와탭 서울 수집 서버 | 13.124.11.223 / 13.209.172.35 | TCP 6600 |
| 와탭 도쿄 수집 서버 | 52.68.36.166 / 52.193.60.176 | TCP 6600 |
| 와탭 싱가포르 수집 서버 | 18.138.0.93 / 18.139.67.236 | TCP 6600 |
| 와탭 뭄바이 수집 서버 | 13.127.125.69 / 13.235.15.118 | TCP 6600 |
| 와탭 캘리포니아 수집 서버 | 52.8.223.130 / 52.8.239.99 | TCP 6600 |
| 와탭 프랑크프루트 수집 서버 | 3.125.142.162 / 3.127.76.140 | TCP 6600 |

에이전트에서 수집 서버로 직접 접속할 수 없다면 제공하는 Proxy 모듈을 이용해 경유하세요.

![Proxy](/img/proxy.png)

### 모바일 앱[​](#모바일-앱 "모바일 앱에 대한 직접 링크")

와탭 모바일 앱은 안드로이드와 iOS 환경을 지원합니다. 다음 링크로 이동하거나 QR 코 드를 스캔해 앱을 설치할 수 있습니다. 모바일 앱에 대한 자세한 설명은 [다음 문서](https://docs.whatap.io/mobile-app)를 참조하세요.



| [iOS](https://apps.apple.com/us/app/whatap-mobile/id6450067434) | [Android](https://play.google.com/store/apps/details?id=io.whatap.lion) |
| --- | --- |
| ![QR](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAJYAQMAAACEqAqfAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAC60lEQVR4nO3dQXLjIBCFYVSz8DJH8FF0NOloOoqPkKUXLjHTTQMN0aQqKZyRa/63wgI+ZQWIIDsEQgghJ841dtlKVXvhLX16SPnSd3rHwsLCwnqK9Qg1k3T9FeOaut7k2iwlubDLJ638Y7lOYcHCwsLCeg1rzjPAZFOF1dbKNfer1jV1umNhYWFh/aCVx/t+8b+X2QELCwsL619ZOt7H0rydAOI35g4sLCwsrJNYJXnuiMnSlBtpvr6fg4WFhYX1fatLu77XycCG9Ek2zrPVBgsLCwvrGdZxFlc7S+M11Duvn3TEwsLCwjqpdY01Oj2UclNpZ1d0MllkMpF5RJ8GLhXHwsLCwhpt5SW8ZU5d6402KS09LuXdujT7OVhYWFhYA63cXKLjvW6cv8Um5VB43YO5hT5YWFhYWCe3NHZhTl1DesfTH2wJZX0f3cGWw2cFLCwsLKwRluWSmufxfonHuZUOtgcT3ZMBFhYWFtZg6yqft1Qb3evxoYz3mkP873swWFhYWFjns7T5pW21Bn+jS9/1Xiq7uQMLCwsLa6yVm5dL+s7Pe3sjj5fy3lZiYWFhYZ3fstT9nHfnav96VlHz+X4OFhYWFtYYq/7rsy7hg/tuLL3R4jbky9PA7l4AxcLCwsJ6mmWjdn3nJ5b38Muye5IxXicA24PZXU8sLCwsrBewbDbo1vTWYpbymtt3VrcHg4WFhYU13NJRO7q03ymuXetv85Ts7WFzLCwsLKzB1kHq+UJdgm9S9hvna7C/ogYLCwsL6+yWv6LZXHPNnJvnDZpV1vTtxPJRx8LCwsIaYT1cv8mdY2kql8ayyrwH0zwrYGFhYWGNtebUyH4/ra7J2xzvwdyPz8FgYWFhYb2QdQs5ZQ8mRyrrSRcsLCwsrJ+zNNbLV2rWtKavWa0lFhYWFtYTrJI63tvXfge37J7sn5vRnXTZxMXCwsLCegWrS507ygWN/RDEQ9x76vnxnR8sLCwsrJEWIYSQ/yC/Ad628qx4qX+OAAAAAElFTkSuQmCC)iOS 12 버전 이상 | ![QR](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAJYAQMAAACEqAqfAAAABlBMVEX///8AAABVwtN+AAAACXBIWXMAAA7EAAAOxAGVKw4bAAADEUlEQVR4nO3bQW7jMAyFYQFZZDlH8FFyNPtoPoqPkGUXBTiRKFGk3RYoMIth8L/NjGzpc1eEKDulEEIIeWWVkO11aZGn3hvDU+rdW7z0iYWFhZXc2oulLn602fe4+F5nK615WXPZHQsLC+sNrKWtsNk21Cy+kO5zOGryEwsLC+v9rEe43fJHPtTSu6JDLCwsrDe2Tou1rrYt55j8mxqNhYWFlcayaOU8mtWG0meXOTzGk+YyLCwsLCxvhUzr5ouynWO6uz5YWFhYua1vc5t0mftVacPfBgsLC+s/t2Zd/ZybSndSuZfayofOvlzLLBYWFlZ+y42V7g22Zhn0PNZ03/os4+/AwsLCSmyVXhtD7CVO6XtMyxdbzllXsbCwsPJaI+6wsaaVyrXTLfF54XU3FhYWVn7LvuYZ+fq7x/rfUVetOT9OfxEWFhYWVpnduc4WsWZdrGTLHIbe3U45sbCwsBJba5tidTW8ptFLR3GFdG+L7mM3u5dyeT+EhYWFlc/SQup+PSPdOr3EuT5YL8XeHQsLCyunpbdlFNKtXQzfgJ/6bY0rs9fvhrCwsLCyWj/9puX09js058el38bCwsLKaO19Rd9UPnqDLX62td86+T5Zu4uFhYWV2NL0yjn7bfetzzGnzQfbMPbuWFhYWFhzth1c1ti3Pg99yhfD+s9ezr07FhYWVk6r1kaZe846+zlo6XdDniVsbmPvjoWFhZXZ6hm3rVnX9CeNPaaruudzACwsLKzM1ukXL5djTdtULvKcwxrfb2NhYWHltnoLvb0uLWMXOY8ie5ndrN+22JOwsLCwEluX1NnhNY3RY7FtKldfZrGwsLASW6uEhMqpdKirxW9Iz+eWWFhYWFjzaLLE2e5bHyvZ8yEf/u+IvTsWFhZWVssWnw4uax5+scb91Gbvw2/OAbCwsLDyWuKb9XG3ZSujle9rtZXHwsLCektLRoOtcaeeo/3uL8MDjYWFhZXaslzqathyKqxDGSeTP/buWFhYWGmskC1WzlVE/FfeVnX7k2ri7wyxsLCwMlqEEEL+Yf4Ckl7rw+cbI+wAAAAASUVORK5CYII=)Android 5.0 버전 이상 |

