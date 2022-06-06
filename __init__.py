bl_info = {
    'name': 'Comment Box',
    'category': 'Node',
    'author': 'Spectral Vectors',
    'version': (0, 0, 1),
    'blender': (2, 90, 0),
    'location': 'Node Editor',
    "description": "Frames around the selected nodes, requests name and color"
    }

import bpy

class NODE_OT_comment_box(bpy.types.Operator):
    bl_idname = "node.comment_box"
    bl_label = "Comment Box"
    bl_description = "Frames around the selected nodes, requests name and color"
    bl_options = {'REGISTER', 'UNDO'}
    bl_space_type = 'NODE_EDITOR'
    bl_context_mode = 'OBJECT'
    bl_property = 'comment_name'


    comment_name : bpy.props.StringProperty(
        name = 'Label -',
        default = 'Your Text Here',
    )

    comment_color : bpy.props.FloatVectorProperty(
        name = 'Color -',
        default = (0.8, 0.3, 0.3),
        min=0, max=1, step=1, precision=3,
        subtype='COLOR_GAMMA', size=3
    )


    @classmethod
    def poll(cls, context):
        return context.area.type == 'NODE_EDITOR'


    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


    def execute(self, context):

        nodes = context.selected_nodes
        selected = []
        for node in nodes:
            if node.select == True:
                selected.append(node)

        bpy.ops.node.add_node(type='NodeFrame')
        frame = context.active_node
        frame.label = self.comment_name
        frame.use_custom_color = True
        frame.color = self.comment_color

        for node in selected:
            node.parent = frame

        return {'FINISHED'}
    
def register():
    bpy.utils.register_class(NODE_OT_comment_box)
    
def unregister():
    bpy.utils.unregister_class(NODE_OT_comment_box)
    
if __name__ == "__main__":
    register()
