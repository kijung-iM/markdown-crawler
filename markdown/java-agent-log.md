에이전트 로그 설정
==========

자바(Java) 애플리케이션 환경에서 발생하는 로그 데이터를 에이전트를 통해 관리하는 방법을 안내합니다. 로그 파일의 경로 및 이름 설정, 보관 기간 설정, 로그 모니터링, 사용자 정의 로그 추적 활성화 방법 등을 포함합니다. 로그 관리를 위한 다양한 설정 옵션을 제공해 시스템의 효율적인 로그 관리를 도와줍니다.

경로 및 이름 설정[​](#경로-및-이름-설정 "경로 및 이름 설정에 대한 직접 링크")
-------------------------------------------------

에이전트 로그의 경로와 이름은 *whatap.conf* 파일에 설정할 수 있습니다. `log_root`의 기본값으로 *`${WHATAP_HOME}`/logs* 경로를 사용합니다.

whatap.conf
```
log_root=System.getProperty("whatap.home", ".") + "/logs"  
log_name=whatap  

```
로그 관리 옵션[​](#로그-관리-옵션 "로그 관리 옵션에 대한 직접 링크")
-------------------------------------------

*whatap.conf* 파일에 로그 관련 옵션을 작성해 로그 내용을 관리할 수 있습니다.

whatap.conf
```
watchlog_enabled=true  
log_rotation_enabled=true  
log_oname_enabled=true  
log_keep_days=7  

```
* **watchlog\_enabled** Boolean

기본값 `false`

값이 `true`이면 로그 모니터링을 활성화합니다.
* **watchlog\_check\_interval** Int

기본값 `2000`

로그를 감시하는 간격입니다. 매 간격으로 로그 파일에 기록을 추가했는지 확인합니다.
* **watchlog\_read\_count** Int

기본값 `8`

로그를 읽는 최대 횟수입니다. 한 번에 `watchlog_buffer_size` 크기 만큼 읽습니다.
* **watchlog\_buffer\_size** Int

기본값 `131072(128k)`

로그를 한 번에 읽는 로그 사이즈입니다.
* **watchlog.LOGKEY**

하나의 로그 파일을 감시하기 위한 설정입니다. `file` 이름을 입력하고 감시한 `word` 여러 개를 쉼표(,)로 구분해 설정합니다. `check_interval` 간격으로 로그를 감시하다가 키워드를 발견하면 경고합니다. 한번 경고가 나가면 `silent` 만큼 경고를 멈춥니다.


	+ **watchlog.LOGKEY.enabled** Boolean 기본값 `true`
	+ **watchlog.LOGKEY.file** String
	+ **watchlog.LOGKEY.words** String
	+ **watchlog.LOGKEY.silent** Int 기본값 `10000`
	+ **watchlog.LOGKEY.check\_interval** Int 기본값 `1000`
* **log\_root** String

기본값 `${WHATAP_HOME}`/logs

에이전트 로그 경로를 설정합니다.
* **log\_datasource\_lookup\_enabled** Boolean

기본값 `true`

InitialContext Lookup 시 DataSource인 경우 로그를 기록하는 기능을 활성화합니다.
* **log\_rotation\_enabled** Boolean

기본값 `true`

에이전트 로그 파일을 날짜 별로 저장하는 기능을 활성화합니다. 로그 파일명은 *whatap-`yyyymmdd`.log* 형태로 저장합니다. 값이 `false`이면 로그 파일명은 *whatap.log* 형태로 저장합니다.
* **log\_keep\_days** Int

기본값 `7`

로그 파일 보관 기간을 설정합니다. `log_rotation_enabled` 값이 `true`인 경우에만 동작합니다.
* **log\_oname\_enabled** Boolean

기본값 `false`

값이 true이면 각 로그마다 에이전트 이름을 추가합니다.

![](/assets/images/java-agent-log-oname-9873bf818d3db89a259e9272d79a0d74.png)

로그싱크(LogSink)[​](#logsink "로그싱크(LogSink)에 대한 직접 링크")
----------------------------------------------------

whatap.agent-2.1.0 버전 이상부터는 애플리케이션 서버를 통합 모니터링하는 로그싱크(LogSink) 기능을 제공합니다.

주의LogSink 옵션은 whatap.agent-2.1.0 버전 이상에서 사용 가능합니다.

### 로그 모니터링 기능 활성화[​](#로그-모니터링-기능-활성화 "로그 모니터링 기능 활성화에 대한 직접 링크")

* **logsink\_enabled** Boolean

기본값 `false`

로그 모니터링 기능을 활성화합니다.
* **logsink\_trace\_enabled** Boolean

기본값 `false`

Log에 트랜잭션 ID를 삽입하여, 트랜잭션 트레이스의 로그 탭을 노출할지 여부를 지정합니다.

### 프레임워크 로그내용 수집[​](#프레임워크-로그내용-수집 "프레임워크 로그내용 수집에 대한 직접 링크")

프레임워크에서 수집하는 로그를 모니터링하려면 모듈에서 로그를 가로채기 위한 설정과 플러그인을 추가해야 합니다. 프레임워크에서 수집하는 로그의 기본 카테고리 이름을 'AppLog'로 설정합니다. 기본값은 `hooklog_enabled` 옵션의 설정과 동일합니다.

* **hooklog\_enabled** Boolean

기본값 `logsink_enabled`

로그 추적 활성화 여부를 설정합니다.

노트
	+ Java 에이전트 2.2.4 버전 이상에서는 애플리케이션의 재기동 없이 옵션의 변경 사항을 적용할 수 있습니다.
	+ Java 에이전트 2.2.4 버전 미만에서는 `hooklog_enabled` 값을 변경하면 재기동이 필요합니다. `hooklog_enabled` 기본값은 `logsink_enabled`입니다. 따라서 `logsink_enabled=true`로 설정하고 자바 애플리케이션을 재시작하면 `hooklog_enabled`는 `true`로 설정됩니다.
* **hooklog\_custom\_methods**

사용자 정의 로그를 등록합니다. 임의의 로그 프레임워크 내용을 전달합니다. 사이트에서 개별로 만든 로그 모듈의 로그를 추적할때 사용하세요.

Java
```
package io.home.test;  
  
public class MyLog {    
  public void customLog(String log) { ... }  
}  

```
whatap.conf
```
hooklog_custom_methods=io.home.test.MyLog.customLog  

```
