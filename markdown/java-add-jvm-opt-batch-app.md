배치 애플리케이션
=========

배치 애플리케이션에서 와탭 에이전트를 적용하는 방법입니다. 배치 애플리케이션은 WAS와는 다르게 애플리케이션이 실행과 중단을 반복하는 특성이 있습니다. 따라서 일반적인 웹 애플리케이션과 다르게 모니터링해야 합니다.

![Batch Application](/assets/images/batch-app-intro-fb3a58319b1862785aa2e91d0b1f9c89.png)

에이전트 다운로드[​](#에이전트-다운로드 "에이전트 다운로드에 대한 직접 링크")
----------------------------------------------

다음 명령어를 실행해 배치 애플리케이션 모니터링을 위한 에이전트를 다운로드할 수 있습니다.


```
wget https://api.whatap.io/agent/whatap.agent.batch.tar.gz  

```
배치 에이전트  파일 구성*whatap.agent.batch.tar.gz*

⎿ *whatap.agent-x.y.z.jar*: 자바 에이전트

⎿ *whatap.agent.batch.host-x.y.z.jar*: 배치 호스트(Batch Host) - 수집 서버로 데이터 전송

⎿ *whatap.conf*: 배치 호스트(Batch Host) 설정 파일(파일이 없는 경우 새로 생성하여 ***설정*** > ***에이전트 설치*** 메뉴의 `license`, `whatap.server.host` 항목을 추가하세요.)

⎿ *agent/whatap.agent.batch-x.y.z.jar*: 배치 에이전트 - 애플리케이션 데이터를 수집하여 배치 호스트로 전송

⎿ *agent/whatap.conf*: 배치 에이전트 설정 파일

에이전트 설정하기[​](#에이전트-설정하기 "에이전트 설정하기에 대한 직접 링크")
----------------------------------------------

### 배치 호스트(Batch Host) 설정[​](#배치-호스트batch-host-설정 "배치 호스트(Batch Host) 설정에 대한 직접 링크")

`license`, `whatap.server.host` 옵션값은 해당 프로젝트의 ***설정*** > ***에이전트 설치*** 메뉴에서 확인할 수 있습니다.

whatap.conf
```
# default setting  
license=  
whatap.server.host=  
  
# 스텝을 나누어서 전송  
split_trace_enabled=true  
  
# 하나의 트레이스에 표시할 최대 스텝 개수  
trace_step_max_count=1024  

```
### 배치 에이전트 설정[​](#배치-에이전트-설정 "배치 에이전트 설정에 대한 직접 링크")

agent/whatap.conf
```
# default setting  
net_udp_listen_ip=0.0.0.0  
net_udp_listen_port=6611  
  
# 배치 호스트와 통신 설정  
net_udp_listen_ip=0.0.0.0  
net_udp_listen_port=6611  
  
# 배치 잡에서 http call 최대 개수  
trace_httpc_limit=1000000  
  
# 배치 잡에서 sql 최대 개수  
trace_sql_limit=1000000  
  
# 엑티브 스택 표시 여부  
active_stack_enabled=true   
# 5회 이내  
active_stack_time1=5000  
# 5회 이후  
active_stack_time2=10000  
# 최초 스택 시작시간  
active_stack_start_wait_time=1000  

```
배치 잡(Batch Job) 실행하기[​](#배치-잡batch-job-실행하기 "배치 잡(Batch Job) 실행하기에 대한 직접 링크")
-----------------------------------------------------------------------------

배치 잡(Batch Job)을 하나의 트랜잭션 관점에서 모니터링해야 합니다. 그래서 와탭의 Java 에이전트는 Job 프로세스를 위한 Job 에이전트와 이 정보를 서버로 중계하기 위한 Host 에이전트로 분리된 두 개의 에이전트를 실행해야 합니다.

### 배치 호스트(Batch Host) 실행 명령어[​](#배치-호스트batch-host-실행-명령어 "배치 호스트(Batch Host) 실행 명령어에 대한 직접 링크")

Batch Host Agent
```
java -cp {BATCH_HOST_HOME}/whatap.agent.batch.host-x.y.z.jar;{BATCH_HOST_HOME}/whatap.agent-x.y.z.jar -Dwhatap.name=batch whatap.agent.batch.App  

```
Batch Host Agent, Java 17 or later
```
java --add-opens=java.base/java.lang=ALL-UNNAMED -cp {BATCH_HOST_HOME}/whatap.agent.batch.host-x.y.z.jar;{BATCH_HOST_HOME}/whatap.agent-x.y.z.jar -Dwhatap.name=batch whatap.agent.batch.App  

```
### 배치 에이전트(Batch Agent) 실행 명령어[​](#배치-에이전트batch-agent-실행-명령어 "배치 에이전트(Batch Agent) 실행 명령어에 대한 직접 링크")

Batch Agent
```
java -javaagent:{BATCH_AGENT_HOME}/whatap.agent.batch-x.y.z.jar -jar {APP_PATH}/batch-application.jar  

```
Batch Agent, Java 17 or later
```
java -javaagent:{BATCH_AGENT_HOME}/whatap.agent.batch-x.x.x.jar --add-opens=java.base/java.lang=ALL-UNNAMED -jar {APP_PATH}/batch-application.jar  

```
노트배치 잡(Batch Job) 에이전트와 배치 호스트(Batch Host) 에이전트는 배치 잡(Batch Job)을 수행하는 호스트와 같이 설치 및 실행하세요.

Time Limit 설정[​](#time-limit-설정 "Time Limit 설정에 대한 직접 링크")
----------------------------------------------------------

배치 잡(Batch Job) 에이전트와 배치 호스트(Batch Host) 에이전트 사이는 UDP를 이용해 통신합니다.

![Batch Job UDP](/assets/images/batch-app-udp-415098264f62073d1912a053f99fd5e1.png)

배치 잡(Batch Job)은 일반적으로 장시간 수행합니다. 수십초가 넘을 수도 있습니다. 따라서 배치 잡(Batch Job) 별로 `time_limit`의 값은 다를 수 있습니다. 배치 잡(Batch Job)이 실행되는 예상 처리 시간을 `time_limit` 옵션에 설정하세요.


```
time_limit=300000  
warning_time=70% of time_limit  
step_interval=5000  

```
액티브 이퀄라이저 컬러 설정[​](#액티브-이퀄라이저-컬러-설정 "액티브 이퀄라이저 컬러 설정에 대한 직접 링크")
----------------------------------------------------------------

배치 잡(Batch Job)의 실행 시간이 `time_limit`의 70%를 지나면 노란색으로 표시하고, `time_limit`을 초과하면 빨간색으로 표시하도록 다음과 같이 설정하세요.

whatap.conf
```
## 기대 종료시간의 70%  
yellow_time = time_limit * 0.7;  
## 기대 종료 시간을 초과  
red_time = time_limit;  

```
![Batch Job UDP](/img/batch-app-timelimit.png)

노트서버 운영자는 배치 잡(Batch Job)의 지연 여부를 실시간으로 확인하려면 `time_limit` 값을 적절하게 설정하세요.

액티브 스택 수집 간격 설정[​](#액티브-스택-수집-간격-설정 "액  티브 스택 수집 간격 설정에 대한 직접 링크")
------------------------------------------------------------------

배치 잡(Batch Job) 에이전트는 `step_interval` 옵션값의 간격으로 액티브 스택을 수집할 수 있습니다.


```
step_interval=5000  

```
배치 에이전트의 메트릭 지표 수집[​](#배치-에이전트의-메트릭-지표-수집 "배치 에이전트의 메트릭 지표 수집에 대한 직접 링크")
-------------------------------------------------------------------------

대시보드에는 배치 호스트(Batch Host)의 Heap Memory를 수집하고, 배치 애플리케이션의 성능 지표는 메트릭(TagCount: `batch_job_counter`)으로 수집합니다.

### `batch_job_counter`[​](#batch_job_counter "batch_job_counter에 대한 직접 링크")

* batch job: `pid`, `hostname`, `job_name`
* gc: `gc_count`, `gc_time_sum`, `gc_oldgen_count`
* heap: `heap_tot`, `heap_use`, `heap_max`, `heap_pending_final`, `heap_perm`
* cpu: `cputime`
* thread count: `thread_total_started`, `thread_count`, `thread_daemon`, `thread_peak_count`
