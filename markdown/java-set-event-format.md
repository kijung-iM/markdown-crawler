이벤트 수신 포맷
=========

공용 알림 템플릿[​](#공용-알림-템플릿 "공용 알림 템플릿에 대한 직접 링크")
----------------------------------------------

공통 템플릿은 대부분의 경우 적용 가능합니다. 다양한 환경에서 동일한 포멧으로 알림을 받을 수 있습니다.

* Product Type : 애플리케이션, 데이터베이스, 쿠버네티스
* Event Type : 애플리케이션 알림, 데이터베이스 알림, 메트릭스 알림
* Event Channel : sms, mobile, 3rd party plugin , plugin

### 이벤트 제목[​](#이벤트-제목 "이벤트 제목에 대한 직접 링크")

Event title format
```
[Level][Platform][ProjectName][ApplicationName][EventTitle]  

```
Event title example
```
[Info][JAVA][애플리케이션 프로젝트][TC-0-1-8081][CRITICAL_HIGH_MEMORY]  

```
노트* ApplicationName을 설정하지 않은 경우 이벤트 제목에서 생략합니다.
* Platform은 다음 중 한 가지로 표시합니다.
	+ JAVA
	+ NODEJS
	+ PYTHON
	+ PHP
	+ DOTNET
	+ GO
	+ POSTGRESQL
	+ ORACLE
	+ MYSQL
	+ MSSQL
	+ BSM\_JAVA
	+ CLOUDWATCH
	+ TIBERO
	+ KUBERNETES
	+ KUBE\_NS
	+ URLCHECK
	+ URLCHECK\_ADMIN
	+ CUBRID
	+ ALTIBASE
	+ CLUSTER
	+ REDIS
	+ MONGODB
	+ VR
	+ RUM
### 이벤트 메시지[​](#이벤트-메시지 "이벤트 메시지에 대한 직접 링크")

이벤트 메시지에 포함할 수 있는 정보입니다. `optional`이 `false`인 경우 항상 메시지에 포함합니다. `optional`이 `true`인 경우 해당 데이터를 확인할 수 있으면 표시합니다.

Event message example
```
Project Name : 애플리케이션 프로젝트  
Project Code : 3  
Application Name : TC-0-1-8081  
Event Message : RECOVERED: Memory is too high. less than 10%  
Event ON Time : 2022-04-12 18:53:24 +0900  
Event OFF Time : 2022-04-12 18:53:24 +0900  
Alert Type : APPLICATION_MEMORY  
Metric Name : memory  
Metric Value : 20  
Metric Threshold : 10  
Stateful : true  

```
다음은 이벤트 메시지 구성 요소입니다.



| En | Ko | 지원되는 알림 타입 | 설명 |
| --- | --- | --- | --- |
| Project Name | 프로젝트 이름 | 전체 | - |
| Project Code | 프로젝트 Code | 전체 | - |
| Application Name | 에이전트 이름 | 전체(optional) | oname |
| Event Message | 이벤트 메시지 | 전체 | - |
| Alert Type | 이벤트 종류 | 전체 | 아래의 AlertType 종류 표 참고 |
| Event ON Time | 이벤트 발생 시간 | 전체 | 2022-04-13 10:40:49 +0900에서 +0900는 GMT를 의미합니다. |
| Event OFF Time | 이벤트 해제 시간 | 전체(optional) | 2022-04-13 10:40:49 +0900에서 +0900는 GMT를 의미합 니다. |
| Metric Name | 메트릭스 이름 | 전체(optional) | 이벤트 조건 판단에서 사용하는 메트릭스의 이름 |
| Metric Value | 메트릭스 값 | 전체(optional) | 메트릭스 값이 메트릭스 임계치를 넘으면 이벤트 발생 조건이 만족한 경우입니다. |
| Metric Threshold | 메트릭스 임계치 | 전체(optional) | 메트릭스 값이 메트릭스 임계치를 넘으면 이벤트 발생 조건이 만족한 경우입니다. |
| Stateful | 해결된 이벤트 알림 | 전체(optional) | 해결된 이벤트 알림 기능 사용 중이면 true, 아니면 false |
| Event Rule | 이벤트 발생 조건 | 메트릭스 알림 | - |
| Event Target Filter | 이벤트 대상 선택 | 메트릭스 알림 | 특정 대상에서 수집된 메트릭스에 대해서만 이벤트 조건을 확인합니다. |
| Repeat Count | 이벤트 반복 횟수 | 메트릭스 알림 | 이벤트 조건이 이벤트 반복 시간동안 이벤트 반복 횟수만큼 만족해야 이벤트가 발생됩니다. |
| Repeat Duration | 이벤트 반복 시간 | 메트릭스 알림 | 이벤트 조건이 이벤트 반복 시간동안 이벤트 반복 횟수만큼 만족해야 이벤트가 발생됩니다. |
| Receiver | 수신자 | 메트릭스 알림 | - |
| Query | MXQL 쿼리 | 복합 메트릭스 알림 | - |
| Rule | 이벤트 발생 조건 | 복합 메트릭스 알림 | - |
| Query Period | 쿼리 기간 | 복합 메트릭스 알림 | - |
| Query Interval | 쿼리 간격 | 복합 메트릭스 알림 | - |
| Silent Time | 무음 시간 | 복합 메트릭스 알림 | - |
| Query | URL | Exception 알림 | Exception을 발생시킨 요청의 URL |
| TXID | 트랜잭션 ID | Exception 알림 | - |
| Class | 에러 클래스 이름 | Exception 알림 | - |
| Log Message | 로그 메시지 | 서버 - 파일 로그 알림 | - |
| Log File | 로그 파일 경로 | 서버 - 파일 로그 알림 | - |
| IP | IP | 서버 알림 전체 | - |
| CPU | CPU | 서버 알림 전체 | 이벤트 발생 당시의 Snapshot |
| CPU\_load1 | CPU\_load1 | 서버 알림 전체 | 이벤트 발생 당시의 Snapshot |
| CPU\_loadPerCore | CPU\_loadPerCore | 서버 알림 전체 | 이벤트 발생 당시의 Snapshot |
| Memory | Memory | 서버 알림 전체 | 이벤트 발생 당시의 Snapshot |
| Swap | Swap | 서버 알림 전체 | 이벤트 발생 당시의 Snapshot |
| Disk Name | Used Percent | Free Size | IO Percent | 디스크 퍼포먼스 | 서버 알림 전체 | 이벤트 발생 당시의 Snapshot |
| Name | Bps | Pps | 트래픽 퍼포먼스 | 서버 알림 전체 | 이벤트 발생 당시의 Snapshot |
| Message | Time | Name | 처리내역 메시지 | 서버 알림 전체 | - |

노트* 해당 이벤트에서 제공할 수 있는 최대한 많은 정보를 보여줍니다.
* AlertType은 다음 중 한 가지로 표시합니다.



| AlertType | 설명 |
| --- | --- |
| APPLICATION\_CPU | 애플리케이션 CPU 알림 |
| APPLICATION\_MEMORY | 애플리케이션 MEMORY 알림 |
| APPLICATION\_DISK | 애플리케이션 DISK 알림 |
| APPLICATION\_ACTIVE\_TRANSACTION | 애플리케이션 액티브 트랜잭션 알림 |
| APPLICATION\_ERROR\_TRANSACTION | 애플리케이션 에러 트랜잭션 알림 |
| APPLICATION\_SLOW\_TRANSACTION | 애플리케이션 트랜잭션 응답시간 알림 |
| METRICS | 메트릭스 알림 |
| COMPOSITE\_METRICS | 복합 메트릭스 알림 |
| ANOMALY | 이상치 탐지 알림 |
| LOG\_REALTIME | 로그 실시간 알림 |
| COMPOSITE\_LOG | 복합 로그 알림 |
| SERVER\_REBOOT | 서버 - 재시작 알림 |
| SERVER\_NO\_DATA | 서버 - 미수신 알림 |
| SERVER\_PORT | 서버 - 포트 알림 |
| SERVER\_NETWORK\_IOPS | 서버 - 네트워크 IOPS 알림 |
| SERVER\_NETWORK\_BPS | 서버 - 네트워크 BPS 알림 |
| SERVER\_DISK\_IO | 서버 - 디스크 I/O 알림 |
| SERVER\_DISK\_QUOTA | 서버 - 디스크 사용량 알림 |
| SERVER\_DISK\_INODE | 서버 - inode 알림 |
| SERVER\_CPU | 서버 - CPU 알림 |
| SERVER\_MEMORY | 서버 - 메모리 알림 |
| SERVER\_CPU\_STEAL | 서버 - steal 알림 |
| SERVER\_MEMORY\_SWAP | 서버 - 스왑 알림 |
| SERVER\_LOG\_FILE | 서버 - 로그 파일 알림 |
| SERVER\_WINDOW\_EVENT | 서버 - 윈도우 이벤트 알림 |
| SERVER\_OFF | 서버 - 알림 OFF 알림 |
| SERVER\_ACKNOWLEDGE | 서버 - 처리내역 알림 |
| SERVER\_PROCESS\_COUNT | 서버 - 프로세스 수 알림 |
| SERVER\_PROCESS\_CPU | 서버 - 프로세스 CPU 알림 |
| SERVER\_PROCESS\_MEMORY | 서버 - 프로세스 메모리 알림 |
| SERVER\_PROCESS\_OFF | 서버 - 프로세스 알림 OFF 알림 |
| AGENT\_ACTIVE | 에이전트 활성화 알림 |
| AGENT\_INACTIVE | 에이전트 비활성화 알림 |
| AGENT\_REACTIVATED | 에이전트 재활성화 알림 |
| URL | URL 알림 |
| TOO\_MANY\_EVENT | 너무 많은 이벤트 발생 알림 |
| CLOUD\_WATCH | Cloud Watch 알림 |
| EXCEPTION | Exception 알림 |

애플리케이션 경고 알림[​](#애플리케이션-경고-알림 "애플리케이션 경고 알림에 대한 직접 링크")
-------------------------------------------------------

애플리케이션 알림은 Event Title, Event Message 모두 제공합니다. ***이벤트 상태가 해결되면 추가 알림*** 기능을 사용하는 경우 이벤트 발생 조건이 해제되면 Evnet Off Message가 전송됩니다.



| Event Type | Event Level | Event Title | Event Message | Event Off Message |
| --- | --- | --- | --- | --- |
| 애플리케이션 CPU | Warning | HIGH\_CPU | CPU is high. `${value}% (>= ${threshold}%)` | RECOVERED: CPU is high. less than `${threshold}%` |
| 애플리케이션 CPU | Critical | CRITICAL\_HIGH\_CPU | CPU is too high. `${value}% (>= ${threshold}%)` | RECOVERED: CPU is too high. less than `${threshold}%` |
| 애플리케이션 메모리 | Warning | HIGH\_MEMORY | Memory is high. `${value}% (>= ${threshold}%)` | RECOVERED: Memory is high. less than `${threshold}%` |
| 애플리케이션 메모리 | Critical | CRITICAL\_HIGH\_MEMORY | Memory is too high `${value}% (>= ${threshold}%)` | RECOVERED: Memory is too high. less than `${threshold}%` |
| 애플리케이션 디스크 | Warning | HIGH\_DISK | Disk is high `${value}% (>= ${threshold}%)` | RECOVERED: Disk id high. less than `${threshold}%` |
| 애플리케이션 디스크 | Critical | CRITICAL\_HIGH\_DISK | Disk is too high `${value}% (>= ${threshold}%)` | RECOVERED: Disk is too highf. less than `${threshold}%` |
| 정상 트랜잭션 | Warning | HIGH\_ACTIVE\_TRANSACTION | Active Transaction Count is over `${value} (>= ${threshold})` | RECOVERED: Active Transaction Count is less than `${threshold}` |
| 에러 트랜잭션 | Warning | HIGH\_ERROR\_TRANSACTION | Error Transaction Count is over `${threshold} (${value})` | RECOVERED: Error Transaction Count is less than `${threshold}` |
| 느린 트랜잭션 | Warning | TOO\_MANY\_SLOW\_TX | Too many delayed transactions `(${value}, above ${time} ms)` | RECOVERED: Too many delayed transactions. less than `${threshold}` |

