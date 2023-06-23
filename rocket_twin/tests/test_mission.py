from rocket_twin.drivers.mission import Mission
from rocket_twin.systems import Ground
import numpy as np

class TestMission:

    def test_run_once(self):

        sys = Ground('sys')
        sys.g_tank.w_p = sys.g_tank.w_max
        sys.rocket.tank.w_p = 0.
        flux_in = 3.
        flux_out = 3.
        dt = 0.1

        sys.add_driver(Mission('mission', flux_in=flux_in, flux_out=flux_out, dt=dt, owner=sys))

        sys.run_drivers()

        data = sys.drivers['mission'].data
        data = data.drop(["Section", "Status", "Error code"], axis=1)

        np.testing.assert_allclose(sys.rocket.a, 40., atol=10**(-10))
        np.testing.assert_allclose(sys.rocket.tank.w_p, 0., atol=10**(-10))
        np.testing.assert_allclose(sys.g_tank.w_p, 0., atol=10**(-10))


test_mission = TestMission()
test_mission.test_run_once()
print("Mission complete!")
