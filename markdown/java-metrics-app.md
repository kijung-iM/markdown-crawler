애플리케이션 지표
=========

홈 화면 > 프로젝트 선택 > 분석 > 메트릭스 조회

메트릭스 조회 메뉴에서 검색할 수 있는 메트릭스 지표입니다.

### app\_active\_stat[​](#app_active_stat "app_active_stat에 대한 직접 링크")



---

액티브 트랜잭션 구간 지표입니다.

* 수집 간격 : 5초
* 통계 데이터 : 5분, 1시간

#### Tags[​](#tags "Tags에 대한 직접 링크")



| 태그명 | 설명 | 비고 |
| --- | --- | --- |
| container | 컨테이너 이름 | 고유값 |
| containerKey | 컨테이너 키값 | 고유값 |
| host\_ip | Host IP | 고유값 |
| okindName | 애플리케이션 종류명 | - |
| oname | 에이전트 이름 | 고유값 |
| onodeName | 애플리케이션 노드명 | - |
| pid | 애플리케이션 PID | - |
| type | 애플리케이션 유형 | 언어 이름 |

#### Fields[​](#fields "Fields에 대한 직접 링크")



| 필드명 | 단위 | 설명 | 비고 |
| --- | --- | --- | --- |
| dbc | 건수 | Database Connection을 수행 중인 트랜잭션 건수 | - |
| httpc | 건수 | HTTP Call을 수행 중인 트랜잭션 건수 | - |
| method | 건수 | Method 로직 수행 중인 트랜잭션 건수 | - |
| socket | 건수 | Socket 연결 수행 중인 트랜잭션 건수 | - |
| sql | 건수 | SQL 쿼리를 수행 중인 트랜잭션 건수 | - |

### app\_counter[​](#app_counter "app_counter에 대한 직접 링크")



---

트랜잭션 지표입니다.

* 수집 간격 : 5초
* 통계 데이터 : 5분, 1시간

#### Tags[​](#tags-1 "Tags에 대한 직접 링크")



| 태그명 | 설명 | 비고 |
| --- | --- | --- |
| alias | 애플리케이션 별칭 | 고유값 |
| container | 컨테이너 이름 | 고유값 |
| containerKey | 컨테이너 키 값 | 고유값 |
| host\_ip | Host IP | 고유값 |
| okindName | 애플리케이션 종류명 | - |
| oname | 에이전트 이름 | 고유값 |
| onodeName | 애플리케이션 노드명 | - |
| pid | 애플리케이션 PID | - |
| type | 애플리케이션 유형 | 언어 이름 |

#### Fields[​](#fields-1 "Fields에 대한 직접 링크")



| 필드명 | 단위 | 설명 | 비고 |
| --- | --- | --- | --- |
| active\_tx\_0 | 건수 | 3초 이하 구간 트랜잭션 수 | - |
| active\_tx\_3 | 건수 | 3초 초과 8초 이하 구간 트랜잭션 수 | - |
| active\_tx\_8 | 건수 | 8초 초과 구간 트랜잭션 수 | - |
| active\_tx\_count | 건수 | 수행 중인 전체 트랜잭션 수 | - |
| apdex\_satisfied | 건수 | APDEX 만족 수 | - |
| apdex\_tolerated | 건수 | APDEX 허용 수 | - |
| apdex\_total | 건수 | APDEX 트랜잭션 총 수 | - |
| arrival\_rate | 퍼센트 | 트랜잭션 요청률 | - |
| httpc\_count | 건수 | HTTP 외부 호출 수 | - |
| httpc\_error | 건수 | HTTP 외부 호출 에러 수 | - |
| httpc\_time | 밀리 세컨드 | HTTP 외부 호출 평균 시간 | - |
| metering | 코어 | 애플리케이션이 작동 중인 호스트의 코어 수 | 컨테이너의 경우 limit cpu |
| resp\_time | 밀리 세컨드 | 평균 응답 시간 | - |
| sql\_count | 건수 | 실행 완료된 SQL 건수 | - |
| sql\_error | 건수 | SQL 에러 건수 | - |
| sql\_fetch\_count | 건수 | SQL Fetch 건수 | - |
| sql\_fetch\_time | 밀리 세컨드 | SQL Fetch 수행 시간 | - |
| sql\_time | 밀리 세컨드 | SQL 평균 수행 시간 | - |
| tps | 건수 | 초당 트랜잭션 처리 수 | - |
| tx\_count | 건수 | 트랜잭션 처리 건 수 | - |
| tx\_dbc\_time | 밀리 세컨드 | DB 평균 연결 시간 | - |
| tx\_error | 건수 | 트랜잭션 에러 건수 | - |
| tx\_httpc\_time | 밀리 세컨드 | HTTP 호출 평균 시간 | - |
| tx\_sql\_time | 밀리 세컨드 | 트랜잭션별 SQL 수행시간의 합에 대한 평균 | - |
| tx\_time | 밀리 세컨드 | 트랜잭션 수행 시간 | - |

### app\_host\_resource[​](#app_host_resource "app_host_resource에 대한 직접 링크")



---

애플리케이션 서버 자원 지표입니다.

* 수집 간격 : 5초
* 통계 데이터 : 5분, 1시간

#### Tags[​](#tags-2 "Tags에 대한 직접 링크")



| 태그명 | 설명 | 비고 |
| --- | --- | --- |
| alias | 애플리케이션 별칭 | 고유값 |
| container | 컨테이너 이름 | 고유값 |
| containerKey | 컨테이너 키값 | 고유값 |
| host\_ip | Host IP | 고유값 |
| okindName | 애플리케이션 종류명 | - |
| oname | 에이전트 이름 | 고유값 |
| onodeName | 애플리케이션 노드명 | - |
| pid | 애플리케이션 PID | - |
| type | 애플리케이션 유형 | 언어 이름 |

#### Fields[​](#fields-2 "Fields에 대한 직접 링크")



| 필드명 | 단위 | 설명 | 비고 |
| --- | --- | --- | --- |
| cpu | 퍼센트 | 호스트 CPU 사용률 | - |
| cpu\_cores | 정수 | 호스트 CPU 코어 수 | - |
| cpu\_irq | 퍼센트 | 호스트 CPU IRQ 사용률 | - |
| cpu\_proc | 퍼센트 | 자바 프로세스 CPU 사용률 | - |
| cpu\_steal | 퍼센트 | 호스트 CPU Steal 사용률 | - |
| cpu\_sys | 퍼센트 | 호스트 CPU SYS 사용률 | - |
| cpu\_usr | 퍼센트 | 호스트 CPU USER 사용률 | - |
| cpu\_wait | 퍼센트 | 호스트 CPU WAIT 사용률 | - |
| disk | 퍼센트 | 루트 파일시스템 디스크 사용률 | JAVA는 설정으로 지정한 파일시스템 경로의 디스크 사용률 |
| mem | 퍼센트 | 호스트 메모리 사용률 | - |
| swap | 퍼센트 | 호스트 SWAP 사용률 | - |

### app\_proc\_counter[​](#app_proc_counter "app_proc_counter에 대한 직접 링크")



---

애플리케이션 프로세스 지표입니다.

* 수집 간격 : 5초
* 통계 데이터 : 5분, 1시간

#### Tags[​](#tags "Tags에 대한 직접 링크")



| 태그명 | 설명 | 비고 |
| --- | --- | --- |
| container | 컨테이너 이름 | 고유값 |
| containerKey | 컨테이너 키 값 | 고유값 |
| host\_ip | Host IP | 고유값 |
| okindName | 애플리케이션 종류명 | - |
| oname | 에이전트 이름 | 고유값 |
| onodeName | 애플리케이션 노드명 | - |
| pid | 애플리케이션 PID | - |
| type | 애플리케이션 유형 | 언어 이름 |

#### Fields[​](#fields "Fields에 대한 직접 링크")



| 필드명 | 단위 | 설명 | 비고 |
| --- | --- | --- | --- |
| cputime | 밀리 세컨드 | 트랜잭션 cpu 시간 | - |
| db\_num\_active | 정수 | DB Connection Pool Active 수 | - |
| db\_num\_idle | 정수 | DB Connection Pool Idel 수 | - |
| gc\_count | 회수 | GC 발생 회수 | - |
| gc\_oldgen\_count | 건수 | Old Generation GC 건수 | - |
| gc\_time | 밀리 세컨드 | GC 수행 시간 | - |
| heap\_max | 바이트 | 힙 최대량 | - |
| heap\_perm | 바이트 | Perm 사용량 | - |
| heap\_tot | 바이트 | 힙 총량 | - |
| heap\_use | 바이트 | 힙 사용량 | - |
| pending\_finalization | 정수 | GC 중 fianlize 수행을 위해 대기 중인 객체 수 | - |
| proc\_fd | 정수 | 프로세스 fd 사용수 | - |
| proc\_fd\_max |  정수 | 프로세스 fd 최대수 | - |
| thread\_count | 정수 | JVM 실행중인 스레드 수 | - |
| thread\_daemon | 정수 | JVM 데몬 스레드 수 | - |
| thread\_peak\_count | 정수 | JVM 최대 스레드 수 | - |
| thread\_total\_started | 정수 | JVM 실행 이후 총 start된 스레드 수 | - |

