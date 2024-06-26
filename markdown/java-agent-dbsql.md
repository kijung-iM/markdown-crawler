DB, SQL
=======

데이터베이스 및 SQL 성능 데이터 수집을 위한 자바(Java) 에이전트의 다양한 옵션을 안내합니다. DBCP, Hikari, Tomcat 등 다양한 DB 연결 풀(Connection Pool) 정보 추적 및 SQL 실행 세부 사항을 기록할 수 있습니다. 또한, SQL 파라미터 정보 기록, DB 연결 누수 추적 등 성능 최적화에 필수적인 정보 수집 옵션을 제공합니다.

* **dbcp\_pool\_enabled** Boolean

기본값 `true`

JMX를 사용하지 않고 DBCP의 DB Connection 정보를 추적하기 위해 사용합니다.
* **hikari\_pool\_enabled** Boolean

기본값 `false`

JMX를 사용하지 않고 hikari pool의 DB Connection 정보를 추적하기 위해 사용합니다.
* **tomcat\_ds\_enabled** Boolean

기본값 `false`

JMX를 사용해 Tomcat DB Connection Pool 정보를 추적하는 기능을 활성화합니다.
* **tomcat\_pool\_enabled** Boolean

기본값 `true`

JMX를 사용하지 않고 Tomcat DB Connection Pool 정보를 추적하는 기능을 활성화합니다.
* **weblogic\_ds\_enabled** Boolean

기본값 `false`

JMX를 사용해 Weblogic DB Connection Pool 정보를 추적하는 기능을 활성화합니다.
* **weblogic\_pool\_enabled** Boolean

기본값 `true`

JMX를 사용하지 않고 Weblogic DB Connection Pool 정보를 추적하는 기능을 활성화합니다.
* **jeus\_pool\_enabled** Boolean

기본값 `true`

JMX를 사용하지 않고 JEUS DB Connection Pool 정보를 추적하는 기능을 활성화합니다.
* **profile\_connection\_open\_enabled** Boolean

기본값 `true`

트레이스 내역에 DBConnection 오픈 정보를 기록합니다.
* **profile\_dbc\_close** Boolean

기본값 `false`

`profile_connection_open_enabled`의 값이 `true`인 경우에만 동작합니다. 트레이스 내역에 DBConnection 클로즈 정보를 기록합니다.
* **profile\_sql\_param\_enabled** Boolean[​](/java/agent-dbsql#profile-sql-param)

기본값 `false`

트레이스 내역에 SQL 파라미터 정보를 기록할 때 사용합니다. 파라미터는 별도 보안 키를 입력해야 조회할 수 있습니다.

노트
	+ **Java 에이전트 2.2.2 버전 이전**: 보안 키는 WAS 서버 *`${WHATAP_AGENT_HOME}`/paramkey.txt* 파일 내에 6자리로 작성합니다. *paramkey.txt* 파일이 존재하지 않는 경우 랜덤 값으로 자동 생성합니다.
	+ **Java 에이전트 2.2.2 버전 이후**: 보안 키는 WAS 서버 *`${WHATAP_AGENT_HOME}`/security.conf* 파일 내에 `paramkey` 키값을 확인하세요. *security.conf* 파일이 존재하지 않을 경우 `paramkey` 키값을 **WHATAP**으로 자동 생성합니다.
	+ 보안키 설정 파일에 대한 자세한 내용은 [다음 문서](/java/install-agent#security)를 참조하세요.
* **profile\_sql\_resource\_enabled** Boolean

기본값 `false`

트레이스에서 SQL을 수집할 때 해당 스텝에서 사용한 CPU와 메모리 사용량을 추적합니다.
* **profile\_update\_count** Boolean

기본값 `false`

`executeUpdate()` 메소드를 통해 SQL UPDATE 문을 수행한 경우 UPDATE 건수를 수집합니다.
* **custom\_pool\_classes** String

pre-define되지 않는 별도의 Connection Pool을 사용하는 경우 해당 클래스 명을 설정합니다.
* **ds\_update\_interval** MiliSeconds

기본값 `5000`

DB Connection 정보 Count   간격을 설정합니다.
* **profile\_position\_sql** Boolean

기본값 `false`

SQL을 수행하는 시점의 StackTrace를 기록합니다.
* **profile\_sql\_param\_length** Int

기본값 `40`

SQL 파라미터의 길이를 설정합니다.

노트최대값은 128이며 그 이상의 값을 입력하더라도 파라미터는 128까지 저장합니다.
* **trace\_dbc\_leak\_enabled** Boolean

기본값 `false`

DBConnection Leak을 추적하는 기능을 활성화합니다.

주의Connection Wrapper를 사용해 Leak을 추적하기에 운영 서비스에 영향을 미칠 수 있으므로 반드시 테스트 후 적용하세요.
* **trace\_dbc\_leak\_fullstack\_enabled** Boolean

기본값 `false`

DBConnection Leak이 감지되는 경우 해당 시점 StackTrace를 수집합니다.

주의피크 타임(Peak Time)에는 가급적 적용하지 마세요. 옵션을 적용하면 CPU 사용량이 다소 증가할 수 있습니다. 문제 해결 용도로만 한시적으로 적용할 것을 권고합니다.
* **trace\_sql\_normalize\_enabled** Boolean

기본값 `true`

SQL 문에서 리터럴 부분을 추출해 SQL 문을 정규화하는 기능을 활성화합니다.
* **profile\_error\_jdbc\_fetch\_max** Int

기본값 `10000`

SQL Fetch Count(`ResultSet.next()` 호출 건 수)가 설정한 값을 초과하면 TOO MANY Fetch 에러로 처리합니다. `0`으로 설정하면 에러 처리하지 않습니다.
* **profile\_error\_sql\_time\_max** Int

기본값 `30000`

SQL 수행 시간이 설정한 값을 초과하면 TOO SLOW 에러로 처리합니다. `0`으로 설정하는 경우 에러 처리를 하지 않습니 다.
* **hook\_connection\_open\_patterns** String

DB Connection Open 시 호출하는 메소드를 등록합니다. 미리 설정하지 않은 Connection Pool의 getConnection을 등록하는 것이 일반적입니다.

Example
```
hook_connection_open_patterns=mypool.ConPool.getConnection  

```
* **hook\_jdbc\_con\_classes** String

미등록한 JDBC Connection 클래스를 지정합니다.

Example
```
hook_jdbc_con_classes=mypool.ConPool  

```
* **hook\_jdbc\_pstmt\_classes** String

미등록한 jdbc PreparedStatement 클래스를 설정합니다. 생성자 파라미터에 SQL 문자열이 전달되는 구조여야 한다는 것을 주의하세요.

Example
```
hook_jdbc_pstmt_classes=org.apache.derby.impl.jdbc.EmbedPreparedStatement  

```
* **hook\_jdbc\_cstmt\_classes** String

미등록한 jdbc CallableStatement 클래스를 설정합니다.

Example
```
hook_jdbc_cstmt_classes=org.apache.derby.impl.jdbc.EmbedCallableStatement  

```
* **hook\_jdbc\_stmt\_classes** String

미등록한 JDBC Statement 클래스를 설정합니다.

Example
```
hook_jdbc_stmt_classes=org.apache.derby.impl.jdbc.EmbedStatement  

```
* **hook\_jdbc\_rs\_classes** String

미등록한 JDBC ResultSet 클래스를 설정합니다.

Example
```
hook_jdbc_rs_classes=org.apache.derby.impl.jdbc.EmbedResultSet  

```
* **hook\_jdbc\_wrapping\_driver\_patterns** String

DB2 드라이버처럼 난독 처리한 JDBC 드라이버는 `hook_jdbc_xxx` 옵션으로 직접 BCI가 어렵습니다. 이런 경우 Wrapper 방식으로 SQL를 추적할 수 있습니다. 이때 `Driver.connect`를 설정해 추적합니다.
* **debug\_dbc\_stack\_enabled** Boolean

기본값 `false`

DB Connection 시점의 StackTrace를 트레이스에 저장합니다. 애플리케이션에서 사용하는 Connection Pool 정보를 얻기 위해 사용합니다.
* **ignore\_sql\_hash\_set** String `Java Agent v2.2.4 or later`

해당 옵션에 입력한 SQL 해시값과 일치하는 SQL 문은 무시하도록 설정할 수 있습니다.
