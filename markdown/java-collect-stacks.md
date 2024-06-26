트랜잭션 스텝 수집 방식
=============

애플리케이션 모니터링 에이전트는 선형 수집 방식과 환형 수집 방식을 제공합니다.

선형 수집[​](#선형-수집 "선형 수집에 대한 직접 링크")
----------------------------------

개별 트랜잭션 트레이스는 무한정 스텝을 수집할 수 없습니다. 트랜잭션별로 길이가 제한된 버퍼에 트레이스 스텝을 저장합니다. 각 트랜잭션은 최대로 수집할 수 있는 스텝의 수가 옵션으로 지정되어 있습니다.

* **profile\_step\_max\_count**

기본값 `1024`

최대로 수집 가능한 스텝 수입니다.
* **profile\_step\_normal\_count**

기본값 `800`

일반적으로 아무런 제약없이 수집되는 스텝 수입니다.
* **profile\_step\_heavy\_count**

기본값 `1000`

normal count를 초과한 경우 스텝은 응답시간이 느린 스텝과 액티브 스택 스텝만 수집합니다.
* **profile\_step\_heavy\_time**

기본값 `100`

heavy count 이내에서의 수집되는 스텝의 기준 시간은 `profile_step_heavy_time`입니다.

![step_buffer](https://img.whatap.io/media/agent_java/data/step_buffer.png)

수집되는 트레이스의 스텝 수가 heavy count를 초과하는 경우에는 액티브 스택만이 수집됩니다. 이 경우에도 최대 스텝 수는 `profile_step_max_count`를 넘지 않습니다.

환형 수집[​](#환형-수집 "환형 수집에 대한 직접 링크")
----------------------------------

선형 수집은 트레이스에서 앞부분을 수집하고 버퍼 사이즈를 넘으면 나중 내용을 버립니다. 반면 환형 수집은 앞부분의 스텝을 버리는 방식입니다.


```
circular_profile_enabled=true  

```
![circular_profile](https://img.whatap.io/media/agent_java/data/circular_profile.png)

버퍼 사이즈는 `profile_step_max_count`에 설정합니다.


```
profile_step_max_count=1024  

```
