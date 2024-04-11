Scale In에서 에이전트 자동 삭제
=====================

Auto Scale 환경에서 에이전트 이름을 자동 부여하면 Scale Out이 발생할 경우 운영자 개입이 필요 없습니다. 시스템을 자동으로 확장합니다. 반면 Scale In이 발생하면 시스템이 정상적인 Shut down으로 인식해야 합니다.

에이전트 자동 삭제를 위해 와탭 서버는 자바 에이전트로부터 메시지를 받아야 합니다. 에이전트는 `${WHATAP_HOME}`에 Java 프로세스의 *whatap\_`{java-process-pid}`.shutdown* 파일이 나타나면 **SILENT\_SHUTDOWN** 이벤트를 와탭 서버에 전송합니다. 전송은 5초 이내로 완료합니다.

**SILENT\_SHUTDOWN** 이벤트를 와탭 서버에 전송하고 1분 이내에 에이전트가 셧다운 되면 와탭 서버는 목록에서 해당 Java 에이전트를 바로 제거합니다. inactive 이벤트도 발생시키지 않습니다.

노트Tomcat의 경우 *shutdown.sh* 파일에 설정할 수 있습니다.


```
touch $WHATAP_HOME/whatap_{java-process-pid}.shutdown  

```
