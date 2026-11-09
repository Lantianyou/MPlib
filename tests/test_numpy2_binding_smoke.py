"""Regression for ArticulatedModel initialization with NumPy 2 bindings."""
from pathlib import Path
import unittest

import mplib
import numpy as np


class BindingSmokeTest(unittest.TestCase):
    def test_construct_panda_model(self):
        root = Path(__file__).resolve().parents[1] / "data/panda"
        planner = mplib.Planner(
            urdf=str(root / "panda.urdf"), srdf=str(root / "panda.srdf"),
            move_group="panda_hand",
        )
        self.assertEqual(len(planner.move_group_joint_indices), 7)
        self.assertTrue(np.isfinite(np.asarray(planner.joint_limits)).all())
        self.assertTrue(callable(planner.plan_qpos))
        self.assertTrue(callable(planner.plan_pose))


if __name__ == "__main__":
    unittest.main()
