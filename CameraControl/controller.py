import json, os

class motor_contorller:
    def __init__(self, path):
        self.path = path
        self.motor_control_json_file = os.path.join(self.path, 'motor_control_info.json')
        self.config_json_file = os.path.join(self.path, 'config.json')
        self.status = 0
        self.angle = '30'
        self.time = '1'
        self.direction = 1
        self.running = 0
        self.create_json_file()
    
    def create_json_file(self):
        if os.path.exists(self.motor_control_json_file):
            pass
        else:
            json_data = {'angle': self.angle,
                         'time': self.time,
                         'direction': self.direction, 
                         'status': self.status,
                         'running': self.running}
            with open(self.motor_control_json_file , 'w') as json_file:
                json.dump(json_data, json_file, indent=4)

    def get_motor_status(self):
        with open(self.motor_control_json_file, 'r') as json_file:
            return json.load(json_file)
    
    def set_motor_status(self, select_info):
        with open(self.motor_control_json_file , 'r') as json_file:
            json_data = json.load(json_file)
            json_data = select_info
        
        with open(self.motor_control_json_file , 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    def set_motor_progress(self, progress):
        with open(self.motor_control_json_file , 'r') as json_file:
            json_data = json.load(json_file)
            json_data['status'] =  progress
        
        with open(self.motor_control_json_file , 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    def set_motor_active(self, active):
        with open(self.motor_control_json_file , 'r') as json_file:
            json_data = json.load(json_file)
            json_data['running'] =  active
        
        with open(self.motor_control_json_file , 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    def get_config(self):
        with open(self.config_json_file,  mode='r', encoding='utf-8') as json_file:
            return json.load(json_file)

if __name__ == '__main__':
    controller = motor_contorller(os.getcwd())
    res = controller.get_config()
    print(res['time_table'])
