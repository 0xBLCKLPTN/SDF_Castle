import moderngl_window as mglw
import moderngl

class App(mglw.WindowConfig):
    window_size: tuple[int, int] = 600, 600
    resource_dir: str = 'programs'

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.quad = mglw.geometry.quad_fs()
        self.program = self.load_program(vertex_shader='vertex.glsl', fragment_shader='fragment.glsl')

        # uniforms
        self.program['u_resolution'] = self.window_size

    def on_render(self, time, frame_time):
        self.ctx.clear()
        self.quad.render(self.program)

    def on_mouse_position_event(self, x, y, dx, dy):
        self.program['u_mouse'] = (x, y)
        return super().on_mouse_position_event(x, y, dx, dy)

if __name__ == '__main__':
    mglw.run_window_config(App)
