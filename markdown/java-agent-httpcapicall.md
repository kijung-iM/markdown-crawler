HTTPC, API Call
===============

HTTP 외부 호출과 API 호출 관련 데이터를 수집, 분석을 위한 자바(Java) 에이전트의 옵션 설정 방법을 안내합니다. TOO SLOW 에러 처리 및 CPU와 메모리 사용량 추적, 호출 시점의 스택 트레이스 기록, URL 정규화 등 세밀한 모니터링을 위한 다양한 옵션을 제공합니다. 이를 통해 개발자는 애플리케이션의 외부 의존성을 효율적으로 관리하고 성능 문제를 식별할 수 있습니다.

* **profile\_error\_httpc\_time\_max** Int

기본값 `10000`

HTTPC 수행 시간이 지정한 값을 초과하면 TOO SLOW 에러로 처리합니다. `0`으로 설정하면 에러 처리하지 않습니다.
* **profile\_httpc\_resource\_enabled** Boolean

기본값 `false`

트레이스에서 HTTP Call 스텝을 수집할 때 해당 스텝에서 사용한 CPU와 메모리 사용량을 추적합니다.
* **profile\_position\_httpc** Boolean

기본값 `false`

HTTPC가 수행하는 시점의 StackTrace를 기록합니다.
* **trace\_httpc\_normalize\_enabled** Boolean

기본값 `true`

트랜잭션 내 HTTPC URL을 파싱해 정규화하는 기능을 활성화합니다.
* **trace\_httpc\_normalize\_urls** String

정규화할 HTTPC URL 패턴을 설정합니다. 호출 URL 패턴을 파싱해 패스 파라미터를 제거합니다.

노트예시, `/a/{v}/b`라고 선언하면 `a/123/b` → `a/{v}/b`로 치환합니다. 여러 개를 등록할 때는 쉼표(,)를 구분자로 사용합니다. 치환 패턴 정리 후 보완이 필요합니다.
* **hook\_httpc\_patterns** String

HTTP outbound 호출을 수행하는 `full package 클래스명`.`메소드`를 설정합니다. HTTP Call을 수행하는 메소드(method)의 전체 경로(full path)를 등록해 사용합니다. 등록 후 클래스 재정의(class redefine)를 하거나 에이전트를 재시작해야 합니다.

whatap.conf
```
hook_httpc_patterns=io.home.test.baseapp.app.post.service.HookHttpcService.*  

```
노트
	+ 클래스를 여러 개 등록하려면 쉼표(,)를 구분자로 사용하세요.
	+ 와일드 카드는 별표(\*)만 사용할 수 있으며 정규식은 사용할 수 없습니다.
