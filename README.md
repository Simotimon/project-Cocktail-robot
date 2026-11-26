# 칵테일 바 로봇팔 (MuJoCo 시뮬레이션)

작은 칵테일 바를 무인으로 운영하도록 칵테일 제조를 로봇팔이 맡아, 매번 같은 양으로 만들 수 있음을 MuJoCo 시뮬레이션으로 입증하는 팀프로젝트.

- 팀 차터: [docs/charter.md](docs/charter.md)
- 산출물 목록: [docs/register.md](docs/register.md)
- 문제 정의서: [docs/problem.md](docs/problem.md)
- 요구사항 명세: [docs/requirements.md](docs/requirements.md)
- 장면 구성표: [docs/scene.md](docs/scene.md)
- 시스템 구조·안전 개념: [docs/architecture.md](docs/architecture.md)

## 폴더

| 폴더 | 들어갈 것 |
|---|---|
| scenes/ | MuJoCo 장면 XML |
| src/ | 로봇 프로그램 |
| tests/ | 테스트 |
| docs/ | 산출물 문서 |
| logs/ | 실행 기록 |

## 환경

```
git clone https://github.com/Simotimon/project-Cocktail-robot.git
uv sync
uv run python -m mujoco.viewer --mjcf=scenes/cocktail_bar.xml   # 맥은 mjpython
```
