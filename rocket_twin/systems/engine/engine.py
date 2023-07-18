from cosapp.base import System
import numpy as np

class Engine(System):
    """Simple model of an engine.

    Inputs
    ------
    force_command: float,
        External control, which inputs the % of the maximum force the engine outputs

    Outputs
    ------
    weight [kg]: float,
        weight
    cg [m]: float,
        position of the center of gravity
    force [N]: float,
        thrust force
    """

    def setup(self):

        self.add_inward("isp", 20.0, desc="Specific impulsion in vacuum", unit="s")
        self.add_inward("w_out", 0.0, desc="Fuel consumption rate", unit="kg/s")
        self.add_inward("g_0", 10.0, desc="Gravity at Earth's surface", unit="m/s**2")
        self.add_inward("t0", self.time, desc="Engine start time")

        self.add_outward("weight", 1.0, desc="weight", unit="kg")
        self.add_outward("cg", 1.0, desc="Center of Gravity", unit="m")
        self.add_outward("force", 1.0, desc="Thrust force", unit="N")

    def compute(self):

        self.force = self.isp * self.w_out * self.g_0 * np.heaviside(self.time - self.t0 - 0.11, 0.)
