오픈소스 추적
=======

자바(Java) 애플리케이션에서 사용하는 프레임워크나 오픈소스 라이브러리를 에이전트를 통해 추적하는 설정 방법을 제공합니다. 이는 Java 에이전트 설정 파일(*whatap.conf*) 파일에 `weaving` 옵션을 추가하여 설정하며, 다양한 프레임워크 및 라이브러리 버전에 대응하는 방법을 안내합니다.

${WHATAP\_HOME}/whatap.conf
```
weaving=    

```
Java 에이전트를 통해 추적하고 있는 프레임워크 또는 오픈소스에 대한 설정 방법은 다음을 참조하세요.



| 프레임워크/오픈소스 | 버전 | 설정 | 에이전트 최소 버전 | 비고 |
| --- | --- | --- | --- | --- |
| apache-camel-cxf | camel-cxf-3.15 이상 | `weaving=camel-cxf-3.15` | [v2.2.27](../release-notes/java/java-2_2_27) | - |
| apache-camel-seda | camel-seda-2.22 이상 | `weaving=camel-seda-2.22` | [v2.2.20](../release-notes/java/java-2_2_20) | - |
| camel-seda-3.2 이상 | `weaving=camel-seda-3.2` | [v2.2.20](../release-notes/java/java-2_2_20) | - |
| db2 | db2-11.5 이상 | `weaving=db2-11.5` | [v2.2.18](../release-notes/java/java-2_2_18) | - |
| feign-client | feign-11 이상 | `weaving=feign-11` | [v2.2.6](../release-notes/java/java-2_2_6) | - |
| hystrix | hystrix-1.5 이상 | `weaving=hystrix-1.5` | [v2.0\_21](../release-notes/java/java-2_0#v20_21) | - |
| kafka | kafka-clients-2.4.0 이상 | `weaving=kafka-clients-2.4.0` | [v2.2.15](../release-notes/java/java-2_2_15) | - |
| reactor-kafka-1.3 이상 | `weaving=reactor-kafka-1.3` | [v2.2.5](../release-notes/java/java-2_2_5) | - |
| redis(jedis) | jedis-2.9.3 이상 | `weaving=jedis-2.9.3` | [v2.0\_33](../release-notes/java/java-2_0#v20_33) | - |
| jedis-3.2 이상 | `weaving=jedis-3.2` | [v2.0\_09](../release-notes/java/java-2_0#v20_09) | - |
| redis(lettuce) | lettuce-5.1 이상 | `weaving=lettuce-5.1` | [v2.2.7](../release-notes/java/java-2_2_7) | - |
| lettuce-6.2 이상 | `weaving=lettuce-6.2` | [v2.2.16](../release-notes/java/java-2_2_16) | - |
| mongodb, mongodb-reactive | mongodb-3.8.2 이상 | `weaving=mongodb-3.8.2` | [v2.2.11](../release-notes/java/java-2_2_11) | - |
| mongodb-4.0.3 이상 | `weaving=mongodb-4.0.3` | [v2.2.11](../release-notes/java/java-2_2_11) | - |
| mongodb-4.4 이상 | `weaving=mongodb-4.4` | [v2.2.11](../release-notes/java/java-2_2_11) | - |
| mongodb-4.8 이상 | `weaving=mongodb-4.8` | [v2.2.11](../release-notes/java/java-2_2_11) | - |
| mule framework | mule-3.9.5 이상 | `weaving=mule-3.9.5` | [v2.2.23](../release-notes/java/java-2_2_23) | - |
| mule-4.5 이상 | `weaving=mule-4.5` | [v2.2.23](../release-notes/java/java-2_2_23) | - |
| okhttp | okhttp-2.7 이상 | `weaving=okhttp-2.7` | [v2.0\_15](../release-notes/java/java-2_0#v20_15) | - |
| okhttp3 이상 | `weaving=okhttp3` | [v2.0\_15](../release-notes/java/java-2_0#v20_15) | - |
| okhttp3-4.4 | `weaving=okhttp3-4.4` | [v2.2.9](../release-notes/java/java-2_2_9) | - |
| quarkus, quarkus-reactive | quarkus-reactive-1.13 이상 | `weaving=quarkus-reactive-1.13` | [v2.2.19](../release-notes/java/java-2_2_19) | - |
| quarkus-reactive-2.10 이상 | `weaving=quarkus-reactive-2.10` | [v2.2.19](../release-notes/java/java-2_2_19) | - |
| rabbitmq | reactor-rabbitmq-1.2 이상 | `weaving=reactor-rabbitmq-1.2` | [v2.0\_06](../release-notes/java/java-2_0#v20_06) | - |
| retrofit | retrofit2-2.5 이상 | `weaving=retrofit-2.5` | - | (배포 예정) |
| ribbon | ribbon | `weaving=ribbon` | [v2.2.10](../release-notes/java/java-2_2_10) | - |
| spring-boot | spring-boot-2.1 이상 | `weaving=spring-boot-2.1` | [v2.2.23](../release-notes/java/java-2_2_23) | kafka-clients, r2dbc-mysql, spring-cloud-gateway, spring-webflux, tomcat9, undertow 포함 |
| spring-boot-2.5 이상 | `weaving=spring-boot-2.5` | [v2.2.9](../release-notes/java/java-2_2_9) | kafka-clients, r2dbc-mysql, redis(lettuce), spring-cloud-gateway, spring-webflux, tomcat9, undertow 포함 |
| spring-boot-2.7 이상 | `weaving=spring-boot-2.7` | [v2.2.9](../release-notes/java/java-2_2_9) | jasync-r2dbc-mysql, kafka-clients, r2dbc-mysql, redis(lettuce), spring-cloud-gateway, spring-webflux, tomcat9, undertow 포함 |
| spring-boot-3.0 이상 | `weaving=spring-boot-3.0` | [v2.2.9](../release-notes/java/java-2_2_9) | jasync-r2dbc-mysql, kafka-clients, r2dbc-mysql, redis(lettuce), spring-cloud-gateway,spring-webflux, tomcat10, undertow 포함 |
| tomcat | tomcat9 | `weaving=tomcat9` | [v2.2.5](../release-notes/java/java-2_2_5) | - |
| tomcat10 | `weaving=tomcat10` | [v2.2.5](../release-notes/java/java-2_2_5) | - |
| undertow | undertow-2.3 이상 | `weaving=undertow-2.3` | [v2.2.14](../release-notes/java/java-2_2_14) | - |

프레임워크나 오픈소스로 spring-boot-3.x, feign-client-11, okhttp3-4.4 사용 시 다음과 같이 옵션을 설정하세요.

whatap.conf
```
weaving=spring-boot-3.0,feign-11,okhttp3-4.4  

```
