"""
Example showing how to create particle explosions via the GPU.
"""
from array import array
from dataclasses import dataclass
import arcade
import arcade.gl

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "GPU Particle Explosion"


@dataclass
class Burst:
    """Track for each burst."""

    buffer: arcade.gl.Buffer
    vao: arcade.gl.Geometry


class MyWindow(arcade.Window):
    """Main window"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.burst_list = []

        # Program to visualize the points
        self.program = self.ctx.load_program(
            vertex_shader="vertex_shader_v1.glsl",
            fragment_shader="fragment_shader.glsl",
        )

        self.ctx.enable_only()

    def on_draw(self):
        """Draw everything"""
        self.clear()

    def on_update(self, dt):
        """Update everything"""
        pass

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        """User clicks mouse"""
        pass


if __name__ == "__main__":
    window = MyWindow()
    window.center_window()
    arcade.run()
