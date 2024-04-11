AES 256 암호화
===========

와탭 애플리케이션 에이전트는 수집한 데이터를 암호화해 서버로 전송합니다. 이를 위해 XOR(Exclusive-OR) 연산과 고급 암호화 표준(Advanced Encryption Standard, 이하 AES) 암호화를 사용하며, 평문을 128비트 단위로 나누어 암복호화를 수행합니다. 256비트까지 확장해 보안을 강화할 수 있습니다.

기본적으로 Java Cryptography Extension(이하 JCE)은 128비트를 지원합니다. AES 256비트를 적용하려면 JCE를 업데이트해야 합니다.

기본 환경에서 AES 256 적용 시 다음과 같이 오류가 발생합니다.


```
Unsupported keysize or algorithm parameters.  
##혹은,  
Illegal key size or default parameters.  

```
1. 다음 링크에서 버전에 맞는 파일을 다운로드하세요.

노트**자바 버전 별 JCE 다운로드 링크**


	* [JAVA 8](https://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)
	* [JAVA 7](http://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html)
	* [JAVA 6](http://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html)
	* [JAVA 5](http://www.oracle.com/technetwork/java/javasebusiness/downloads/java-archive-downloads-java-plat-419418.html#jce_policy-1.5.0-oth-JPR)
	* [JAVA 1.42](http://www.oracle.com/technetwork/java/javasebusiness/downloads/java-archive-downloads-java-plat-419418.html#7503-jce-1.4.2-oth-JPR)
2. *`$JAVA_HOME`/jre/lib/security* 경로에 파일을 덮어쓰기하세요.
3. JCE를 적용했다면 *`${WHATAP_HOME}`/whatap.conf* 파일에 다음 설정을 추가하세요.

whatap.conf
```
cypher_level=256  

```
4. 애플리케이션 서버를 다시 시작하면 ASE 256 암호화를 적용합니다.
