비동기 추적
======

자바(Java) 에이전트 설정을 통해 비동기 애플리케이션 활동을 추적하는 방법을 안내합니다. `CompletableFuture` 메소드 수집 방법과 사용자 애플리케이션에 해당 메소드를 hooking하는 방식을 포함합니다. 설정 예시와 함께 *whatap.conf* 파일에 추가해야 할 옵션을 제공하여 비동기 호출의 성능 모니터링을 강화할 수 있도록 지원합니다.

CompletableFuture[​](#completablefuture "CompletableFuture에 대한 직접 링크")
----------------------------------------------------------------------

Java 에이전트 설정을 통해 CompletableFuture 메소드를 수집할 수 있는 방법을 안내합니다.

### CompletableFuture 메서드 추가[​](#completablefuture-메서드-추가 "CompletableFuture 메서드 추가에 대한 직접 링크")

사용자  의 Java 애플리케이션 프로젝트에 에이전트로 hooking할 CompletableFuture 메소드를 추가하세요.

* 메서드 이름: `trace`로 통일
* ReturnType: `Supplier`, `Consumer`, `Runnable`, `Future`


```
package io.home.test.util;  
  
import java.util.concurrent.Future;  
import java.util.function.Consumer;  
import java.util.function.Supplier;  
  
public class W {  
    public static <T> Supplier<T> trace(Supplier<T> f) {  
        return f;  
    }  
    public static <T> Consumer<T> trace(Consumer<T> f) {  
        return f;  
    }  
    public static <T> Runnable trace(Runnable f) {  
        return f;  
    }  
    public static <T> Future<T> trace(Future<T> f) {  
        return f;  
    }  
}  

```
### 에이전트 설정 추가[​](#에이전트-설정-추가 "에이전트 설정 추가에 대한 직접 링크")

에이전트 설정을 위해 *whatap.conf* 파일에 다음 옵션을 추가하세요.

whatap.conf
```
hook_completablefuture_patterns=io.home.test.util.W.*  

```
노트* Context가 있는 경우 `trace` 메소드를 추가해 트랜잭션을 연결하세요.
* Context가 없는 경우 `hook_service_patterns` 옵션으로 서비스를 시작해야 합니다.
### 사용 예시[​](#사용-예시 "사용 예시에 대한 직접 링크")

* **원본**


```
public CompletableFuture<String> serviceATimeout() {  
    return CompletableFuture.supplyAsync(() -> {  
        RestTemplate restTemplate = new RestTemplate();  
        return restTemplate.getForObject("http://localhost:8081/api/serviceB/timeout", String.class);  
    });  
}  

```
* `io.home.test.util.W.trace()` 적용


```
// io.home.test.util.W.trace() 적용  
public CompletableFuture<String> serviceATimeout() {  
    return CompletableFuture.supplyAsync(W.trace(() -> {  
        RestTemplate restTemplate = new RestTemplate();  
        return restTemplate.getForObject("http://localhost:8081/api/serviceB/timeout", String.class);  
    }));  
}  

```
