# MuJoCo Menagerie 모델

출처: https://github.com/google-deepmind/mujoco_menagerie (커밋 `eea4c7431b63da8278b0ff31638e0b0e941cec0e`, 2026-11-23)

| 폴더 | 모델 | 라이선스 |
|---|---|---|
| `universal_robots_ur5e/` | Universal Robots UR5e | `universal_robots_ur5e/LICENSE` (BSD-3-Clause) |
| `robotiq_2f85/` | Robotiq 2F-85 그리퍼 | `robotiq_2f85/LICENSE` (BSD-2-Clause) |

## 원본에서 바꾼 점

`universal_robots_ur5e/ur5e.xml`
- 화면용 메시를 OBJ에서 바이너리 STL로 바꿨다(31MB → 6MB, 모양은 같음). 재질 색은 XML의 `material`이 정한다.
- 원본 `home` 키프레임을 뺐다. 장면 전체의 `home` 키프레임은 `scenes/cocktail_bar.xml`에 있다.
- `wrist_3_link`의 `attachment_site` 자리에 `tool_mount` 바디를 두고 2F-85를 `<attach>`로 붙였다(이름 앞에 `gripper_`).
- 접촉 옵션을 그리퍼와 같게 맞췄다(`cone="elliptic" impratio="10"`).

`robotiq_2f85/` 는 원본 그대로다.
