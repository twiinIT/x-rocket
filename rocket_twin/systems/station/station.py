from cosapp.base import System

from rocket_twin.systems import CosappController, Pipe, Rocket, Tank


class Station(System):
    """A space station composed by a rocket, a tank and a pipe connecting them.

    Inputs
    ------
    model_path: string,
        the path to the .mo file, if any
    model_name: string
        the .fmu file name

    Outputs
    ------
    """

    def setup(self):
        self.add_child(CosappController("controller"))
        self.add_child(Tank("g_tank"))
        self.add_child(Pipe("pipe"))
        self.add_child(Rocket("rocket"))

        self.connect(self.g_tank.outwards, self.pipe.inwards, {"w_out": "w_in"})
        self.connect(self.pipe.outwards, self.rocket.inwards, {"w_out": "w_in"})

        self.connect(self.controller.outwards, self.g_tank.inwards, {"wg": "w_command"})
        self.connect(
            self.controller.outwards,
            self.rocket.inwards,
            {"wr": "w_command", "f": "force_command"},
        )

        self.g_tank.weight_max = 10.0
