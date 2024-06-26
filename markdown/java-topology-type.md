유형별 토폴로지
========

유형별 토폴로지에 대해 알아보고 각 토폴로지에서 제공하는 기능을 설명합니다.

애플리케이션 토폴로지[​](#애플리케이션-토폴로지 "애플리케이션 토폴로지에 대한 직접 링크")
----------------------------------------------------

홈 화면 > 프로젝트 선택 > ***대시보드*** > ***애플리케이션 토폴로지***

![애플리케이션 토폴로지](/img/application_topology.png)

프로젝트 범위에 포함된 모든 애플리케이션의 호출 연관 정보를 표현합니다.

노트애플리케이션 노드를 더블 클릭하면 해당 애플리케이션의 ***인스턴스 토플로지*** 화면으로 전환합니다. 선택한 애플리케이션 중심의 토폴로지를 표현합니다.

그룹 토폴로지[​](#그룹-토폴로지 "그룹 토폴로지에 대한 직접 링크")
----------------------------------------

홈 화면 > 프로젝트 선택 > ***사이트맵*** > ***그룹 통계 토폴로지***

* 데이터베이스 호출 내역을 포함한 토폴로지의 경우 다음과 같이 데이터베이스 노드를 포함합니다.

![그룹 토폴로지](/img/group_topology_1.png)
* 타 프로젝트로부터 호출 내역이 존재하는 경우 타 프로젝트의 그룹 노드를 포함합니다.

![그룹 토폴로지 (타 프로젝트 그룹 노드 포함)](https://img.whatap.io/media/user_guide_application/topology/group_topology_2.png)
* 타 프로젝트 그룹 노드를 클릭하면 타 프로젝트의 토폴로지 정보를 함께 표시합니다.

![그룹 토폴로지 (타 프로젝트 그룹 클릭)](https://img.whatap.io/media/user_guide_application/topology/group_topology_with_other_project.png)

통합 토폴로지[​](#int-topology "통합 토폴로지에 대한 직접 링크")
---------------------------------------------

사용자가 복수 프로젝트에 대한 권한을 보유한다면 프로젝트 단위 토폴로지로 전체 상황을 조망하기 어려운 제약이 존재합니다. 이와 같은 경우 복수의 프  로젝트를 일괄 선택해 단일 토폴로지로 보기 위한 요구 사항을 총족하기 위한 기능입니다.

1. 와탭 모니터링 서비스 홈 화면에서 ***통합 APP.그룹 토폴로지*** 메뉴를 선택하세요.
2. 왼쪽 위에 ***프로젝트***를 선택하세요.

![프로젝트 선택](/img/uni-topology-select-project.png)
3. 토폴로지에 표현할 그룹 또는 프로젝트를 선택하세요.

토폴로지 화면의 중앙을 기준으로 프로젝트 단위의 클러스터를 형성하고 각 프로젝트에 포함된 그룹을 인접 위치에 군집시켜 표현합니다. 인접한 노드 사이의 간격을 조정하려면 상단의 노드 간격 관련 확대/축소(![확대축소 아이콘](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAN4AAABACAIAAAD6aV7TAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3hpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAwIDc5LjE3MWMyN2ZhYiwgMjAyMi8wOC8xNi0yMjozNTo0MSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDpiYzhmOTAxYS1jMWFlLTRlMGMtYjdjNS0yOTcyMjNlOTkxY2YiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MEVDNjY4NjU1MTA2MTFFRDk1NTBFNTZGQjUwMkEyQzYiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MEVDNjY4NjQ1MTA2MTFFRDk1NTBFNTZGQjUwMkEyQzYiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDI0LjAgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDpiNzI2OGNiZS0yZmFjLTRhZmYtOTljNS0zOTc1OWJhYTE3ZmQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6YmM4ZjkwMWEtYzFhZS00ZTBjLWI3YzUtMjk3MjIzZTk5MWNmIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+vhU6bgAABIJJREFUeNrsnL9PMkkYx1/8wSKwyg+TC7oE7ORIiFpoaCysvNJooZQWlnZW+geYmFhYmlgYjbXFFQatjHHrwyCRygQSTAgs6kZd/JF7wiTr3L7eq+cL83L4/RQbdpxldp/5MDPPymKrVCrfAGg+2hAC0Jx0vFlaLpdzuRwNqJqmGYaBMIG6I0mS1+v1eDzBYNDn831fwfb9hJ7JZFKpFGIHhBGLxSKRyDtqHh8fFwoFehGNRhVF8fv9brdb8Ilubm7SdmFhAe22ZLsMXddLpVI+n0+n07QbCATGx8f/dUKn8ZK8lGU5Ho+Hw2F8mkHjcNcIhUL9/f2qqpJ4pB8/drbx60s2j8NLIBKSjZSjF6QfSfiGmpT3sHkcXgLxdpJ4poRWNdmik9aXiBQQDxOPz3xe1dQ0jbaU9yBMQDxMPCahVU12/1J8Pg6AKR5/Ex3/DQJNCtQEUBMAqAmgJgBQE0BNAKAmAFATQE0A6kIHQvBx7u7u9vb2PndsIpFwOp2IIdRsCE9PT9ls9tPHIoCY0AHUBKAJJ/Rqtarrent7e09Pz49rXl9fPz8/u91uu90uYDn48PAgSZLL5ULvftFR8+LiYnV1lT2V92O2trao5vn5uYDrSSaT1NbBwQG6FhM6AFATQE0A/k9p0MvLS6lU4pObb7XbdcVi0Szs6uqidIfSo/v7e7OQ3dK7ubnha/r9/ra2OnwwDMOgdzZ3WbuUCfFtybLscDjQ2S2rJvX62tqapVDTNL5wdHR0Zmbm8PBQVVVLzT9rmLvLy8vvpvYfzMZ2d3cthX/VMHfn5uaGh4dbrOceHx9vb2/5EpfLJUlSo9tl90D4ku7ubn50IOx2+88///gf1LTZbHQSfGhIVhr5+JNggxNt+Zo0iNKISwNqZ2cn/271+Wx1dPBtUdSq1So1RM2ZhXy7LUM2m93e3uZLpqenx8bGGt3u0dHRyckJX7K4uLixscGXDA0NJRIJcWo6nc6VlRVz9+zsbGdnh+blpaUlS80/api76+vrV1dXU1NTdMZ1j9TvNczd/f3909PTkZER6qfWnu9ozqHL5Et6e3sFtKsoiqVdEsNSEgqFhE7ooKkgRWZnZ8W3O1LDUtiIM0GGDpoUqAmgJgBi1prhcHh+fv4j39igBMgwjL6+PgHXE4/HBwcHPR4PuvbrqinLMknwkZoDAwPCrue3GujXL63mF8ThcExOTn76WAQQajYKWr1MTEwgDkiDANQEAGoCADUB1AQAagKoCQDUBABqAqgJANQEUBOAX6Mme05U13UEBYiHicc/rPyqptfrpS3/IwgACIOJxyS0qsm+GZ7P5xEmIB4mHv94wquawWCQtul0+vLyEpECIiHlSDxTQquaPp8vFovRC1VVYScQ6SX7GSLSjyQ0y//xLfdIJFIsFguFQjKZjEajiqL4/f6f//EaAN7Me2h9SfM4Gy8DgQDpx1ewVSoVyzGZTCaVSiF2QBg0Xlq8fFtNolwu53I5+pOmaYZhIHag7kiSRPk45T20vuTn8XfUBOCXg/8GgSblbwEGAHlHocY5fjZ8AAAAAElFTkSuQmCC)) 버튼을 이용해 노드 간격을 조정할 수 있습니다.

노트* 대규모 환경의 경우 일반적으로 멀티 프로젝트로 구성합니다. 이를 토폴로지로 표현할 경우 개별 노드를 화면 전체에 균등 분포시키기 보다는 프로젝트 단위로 모아서 배치하는 것이 전체 규모를 파악하는데 용이합니다. 따라서 군집 단위를 선택하여 화면에 자동 배치합니다.
* 프로젝트, 데이터베이스, 외부 호스트, 애플리케이션 및 그룹을 호출하는 외부 모듈을 군집 단위로 합니다.
* 클러스터 구성은 프로젝트, 외부 모듈, 외부 호출, DB 호출 단위로 구성합니다.
인스턴스 토폴로지[​](#인스턴스-토폴로지 "인스턴스 토폴로지에 대한 직접 링크")
----------------------------------------------

홈 화면 > 프로젝트 선택 > ***사이트맵*** > ***인스턴스 토폴로지***

***인스턴스 토폴로지***는 애플리케이션 토폴로지와 동일한 데이터를 표현합니다. ***인스턴스 토폴로지***는 단일 애플리케이션을 대상으로 연관성을 지닌 애플리케이션, 외부 모듈, DB 및 외부 호출 노드와의 연관성을 표현합니다. 반면, ***애플리케이션 토폴로지***는 프로젝트에 포함된 전체 애플리케이션을 대상으로 합니다.

***애플리케이션 토폴로지***에 표현되는 정보가 너무 많아 애플리케이션 단위로 확인할 경우 ***인스턴스 토폴로지***를 이용하세요.

![인스턴스 토폴로지](/img/instance_topology.png)

Netstat 토폴로지[​](#netstat-토폴로지 "Netstat 토폴로지에 대한 직접 링크")
-------------------------------------------------------

홈 화면 > 프로젝트 선택 > ***사이트맵*** > ***Netstat 토폴로지***

프로젝트에 포함된 애플리케이션과 애플리케이션의 리스닝 정보, 아웃바운드 호출 정보를 노드로 표현합니다. 리스닝 포트와의 관계는 직선으로 아웃바운드 호출 정보와의 관계는 곡선으로 표현합니다.

![Netstat 토폴로지](/img/netstat-topology.png)

노트Netstat 토폴로지를 취득하는 과정은 에이전트의 부하를 유발하므로 자동 갱신 기능을 제공하지 않습니다. ![데이터 조회하기 아이콘](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAdCAYAAAAgqdWEAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAA3hpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDkuMC1jMDAwIDc5LjE3MWMyN2ZhYiwgMjAyMi8wOC8xNi0yMjozNTo0MSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iIHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD0ieG1wLmRpZDo5NGYxMDZkYi1mOWQ1LTRkNWItYjg1Mi01N2E4OWQ4N2NiODAiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6RkM0RjAyQzM1MTBFMTFFRDk1NTBFNTZGQjUwMkEyQzYiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6RkM0RjAyQzI1MTBFMTFFRDk1NTBFNTZGQjUwMkEyQzYiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIDI0LjAgKE1hY2ludG9zaCkiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDphMzM1ZWVmNC1mYjZhLTRkNzctOWI5MS0yZDViNTU2OTE4YTQiIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6OTRmMTA2ZGItZjlkNS00ZDViLWI4NTItNTdhODlkODdjYjgwIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+xFhE8QAAA2NJREFUeNrMl0tIVGEUx//fd2fm3nGaZHwkA+KjFylBWG5amG10GRGW9AKjRVFRCSJEQUPRokioNulCAhFsV2LiKogIwl7SoiyVsdJ8Vb5G5z3f1/luumk12lynw2WGy1zm/L7z+J9zmZRy4u1gIs/XEV78OC5g0xjostwSEojTR6mXw3fYcO3aok2y15/j83suL7rBgeI8bj4opfUwbOnAw5MCoOv5DVdAG8luvPR1RuqbCUSsAcTfluNmmA5J+MdFlA8Q2cZcjrhAWkz5Vf4VB3dQgUik15R/xcFV7mSaaZR/xcH/9U9SeRDbarpAUJ5HpgVkhO6X4pyZzZDjYogl1ghG04DpRYm5XxKHKm3YV26HywkMjAnc64nBPyxQULh6eUgahpOPnwGJBYrGk6sZ2LvDhukFIEhtWbWToa5Kx/nmEDpexFDs5dZGJhKTCISBRw1OE+Ts/RAePIubVWfYgYcXDbRecELjEh29CRR4Vt6lSR9hbFbi+G4NVWU2HL0dRHtXFN4sIN8D2DWJGl8IbwYTuFLrhJ2OGFuFbvGkW4+iUlvhwMB3gc6XceQVa9BtzJxluW6OGNVO0+MICjYwVJdwTAWkNTBqqAkHQyZ1y3xQQvw1TNUYcdDvs4t/ALLWUVfFLYqMjZ5iVDOfRhIo26TByABmCIovAdmpyySlsWKbRrUFvKKu8mRYBKPMlcnQ1B2lAgVaTuoI07rhnxCYmJMY9gtkehnqDxjo7o2i/wvdZzDruimXQt9PJ/a1h+E7ZmB7iw3NPREMEFRlqYb6/QZ0BzA+Q3pE7R+MSLh0tqJNYEWil0/6cas7ZgLcrHPi7imnOXVVeNueRjFFqWo8qMPjAk7fCUN4AbfBTMVOKYzqKFU7RTkMne/i6Hq/gHJS2zxKX983gbFRWgGoXlQdNdTocFOxn2kNmxEy7Cz1kVmW+CLaP9QM+kAR6hsF1uu0JRJYiIr8WlsEBqXrRLWOwuwohmhPUaKY1NwrOReYp293qlbJWFzS5gZku1R6JBykRUnOqQBHCk05tZNzDwlgMCrNhUlaVcBJAxGEqT1W6cxaGF9e+dJpy6svj9LgSTOL6V9x8K30vuT/IUwNSYcpv8q/4uDXjxj08gIM0ZxR4VqrlC37Un6Vf8XB/qd37d8CDAAmlWmEg71//QAAAABJRU5ErkJggg==) 버튼을 통해 사용자의 요청이 있는 경우 데이터를 조회합니다.

