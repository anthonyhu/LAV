import carla

from leaderboard.autoagents.autonomous_agent import AutonomousAgent, Track

def get_entry_point():
    return 'MILEAgent'

class MILEAgent(AutonomousAgent):
    def sensors(self):
        return [
            {'type': 'sensor.speedometer', 'id': 'EGO'},
            {'type': 'sensor.other.gnss', 'x': 0., 'y': 0., 'z': 2.4, 'id': 'GPS'},
            {'type': 'sensor.other.imu',  'x': 0., 'y': 0., 'z': 2.4, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,'sensor_tick': 0.05, 'id': 'IMU'},
            {'type': 'sensor.camera.rgb', 'x': 1.5, 'y': 0.0, 'z': 2.4, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0, 'width': 256, 'height': 288, 'fov': 64, 'id': 'RGB_0'}
        ]

    def setup(self, path_to_conf_file):
        self.track = Track.SENSORS
        # TODO Load config and model

    def destroy(self):
        # TODO clean up the agent
        pass

    def run_step(self, input_data, timestamp):
        return carla.VehicleControl(steer=0.0, throttle=0.0, brake=0.0)