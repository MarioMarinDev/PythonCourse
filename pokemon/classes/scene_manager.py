
class SceneManager:
    def __init__(self, scenes, scene_active=""):
        self.scenes = scenes
        self.scene_active = scene_active

    def control(self):
        if self.scene_active in self.scenes:
            scene = self.scenes[self.scene_active]
            scene.control_objects()
            scene.render_objects()
            if scene.action_data is not None:
                self.control_action(scene.action_data)
                scene.action_data = None

    def control_action(self, action_data):
        if action_data["action"] == "scene_change":
            self.scene_active = action_data["value"]
