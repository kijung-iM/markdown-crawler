CPU/메모리/디스크 사용량 수집
==================

Java 에이전트가 CPU, 메모리, 디스크 사용량을 수집하는 방법을 안내합니다. 자바(Java)의 JMX 라이브러리를 기본적으로 활용하며, 필요에 따라 Linux의 proc 디렉터리나 oshi, sigar 라이브러리를 통한 성능 지표 수집 방법을 확인할 수 있습니다.

* **linux\_proc\_stat\_enabled** Boolean

기본값 `false`

CPU, 메모리, 디스크 사용량을 Linux의 *proc* 디렉터리에서 수집할지 여부를 설정합니다.
* **oshi\_enabled** Boolean `Java Agent v2.1.0 or later`

기본값 `false`

CPU, 메모리, 디스크 사용량을 측정할 때 oshi 라이브러리 사용 여부를 설정합니다.
* **oshi\_netstat\_enabled** Boolean `Java Agent v2.2.31 or later`

기본값 `false`

netstat 지표 수집 여부를 설정합니다. Maximum Transmission Unit(MTU) 지표가 추가됩니다.
* **sigar\_enabled** Boolean

CPU, 메모리, 디스크 사용량을 측정할 때 sigar 라이브러리 사용 여부를 설정합니다.

노트whatap.agent.2.1.0 버전 미만에서 기본값은 `true`이며, whatap.agent.2.1.0 버전 이상에서는 기본값이 `false`입니다.
