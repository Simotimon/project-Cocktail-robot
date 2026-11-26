"""D07 장면 구성표(docs/scene.md) 확인 테스트 — scenes/cocktail_bar.xml."""

from pathlib import Path

import mujoco
import numpy as np
import pytest

SCENE = Path(__file__).resolve().parents[1] / "scenes" / "cocktail_bar.xml"


@pytest.fixture(scope="module")
def model():
    return mujoco.MjModel.from_xml_path(str(SCENE))


def bodies(model, prefix):
    names = [model.body(i).name for i in range(model.nbody)]
    return [n for n in names if n.startswith(prefix)]


def test_bottles_count_and_mass(model):
    # 구성표: 병 7개, 각 1.2kg → 합 8.4kg
    bottles = bodies(model, "bottle_")
    assert len(bottles) == 7
    assert round(sum(model.body(n).mass[0] for n in bottles), 3) == 8.4


def test_cups_and_shaker(model):
    assert len(bodies(model, "cup_")) == 3
    assert {"shaker_tin", "shaker_lid", "shaker_device"} <= set(bodies(model, "shaker"))


def test_actuators_and_cameras(model):
    actuators = {model.actuator(i).name for i in range(model.nu)}
    assert {"rail", "shaker_device", "arm_gripper_fingers_actuator"} <= actuators
    assert len([a for a in actuators if a.startswith("arm_")]) == 7  # 팔 6 + 그리퍼 1
    cameras = {model.camera(i).name for i in range(model.ncam)}
    assert {"top_cam", "front_cam"} <= cameras


def test_scene_is_stable_from_home(model):
    # home 자세에서 2초 돌려도 물체가 튀거나 미끄러지지 않아야 한다(5mm 이내)
    data = mujoco.MjData(model)
    mujoco.mj_resetDataKeyframe(model, data, model.key("home").id)
    mujoco.mj_forward(model, data)
    movable = bodies(model, "bottle_") + bodies(model, "cup_") + ["shaker_tin", "shaker_lid"]
    start = {n: data.body(n).xpos.copy() for n in movable}
    for _ in range(int(2.0 / model.opt.timestep)):
        mujoco.mj_step(model, data)
    assert not np.isnan(data.qpos).any()
    for n in movable:
        assert np.linalg.norm(data.body(n).xpos - start[n]) < 0.005, n
