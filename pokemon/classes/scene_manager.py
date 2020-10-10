
class SceneManager:
    def __init__(self, scenes, scene_active=""):
        self.scenes = scenes
        self.scene_active = scene_active

    def control(self):
        action_data = None
        if self.scene_active in self.scenes:
            scene = self.scenes[self.scene_active]
            scene.control_objects()
            scene.render_objects()
            if scene.action_data is not None:
                action_data = self.control_action(scene.action_data)
                scene.action_data = None
        return action_data

    def control_action(self, action_data):
        if action_data["action"] == "scene_change":
            self.scene_active = action_data["value"]
        elif action_data["action"] == "shutdown":
            return action_data
