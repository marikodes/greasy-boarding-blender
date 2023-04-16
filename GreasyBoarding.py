#add_on_script

#credits and helpful resources
#https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
#https://medium.com/geekculture/creating-a-custom-panel-with-blenders-python-api-b9602d890663
#https://b3d.interplanety.org/en/creating-custom-ui-panels-in-blender/
#https://www.youtube.com/watch?v=Zl2xuUyDLTc
#https://www.youtube.com/watch?v=udijKlIXSv4
#https://www.youtube.com/watch?v=3pbpIbTt15Y
#https://www.youtube.com/watch?v=uahfuypQQ04
#https://blender.stackexchange.com/questions/73145/when-declaring-a-panel-what-does-the-bl-context-value-need-to-be
#https://www.youtube.com/watch?v=Y67eCfiqJQU
#ui_panel Template within blender
#https://blender.stackexchange.com/questions/158775/having-trouble-creating-an-addon-with-multiple-modules
#https://en.wikibooks.org/wiki/Blender_3D:_Noob_to_Pro/Advanced_Tutorials/Python_Scripting/Addon_Anatomy#Invoking_Your_Operator
#https://blender3d-tutorials.com/blender-2-9-python-addon-programming-tutorial

bl_info = {
    # required
    'name': 'GreasyBoarding',
    'blender': (3, 5, 0),
    "location": "View3D > right-side panel > GreasyBoard",
    'category': 'Animation',
    # optional
    'version': (1, 0, 0),
    'author': 'Mariama Bah',
    'description': 'blender add-on for storyboarding w/ grease pencil',
    "wiki_url": 'https://github.com/marikodes/greasy-boarding-blender',
}

import bpy

class enable_GP(bpy.types.Operator):
    """Adds GP object to scene and toggles draw mode"""
    bl_idname = "object.enable_gp"
    bl_label = "Enable Grease Pencil"
    bl_options = {"UNDO"}
    
    def execute(self, context):
        bpy.ops.object.gpencil_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1), type='EMPTY')
        bpy.ops.gpencil.paintmode_toggle()
        bpy.context.scene.tool_settings.gpencil_stroke_placement_view3d = 'SURFACE'
        return {"FINISHED"}
    
    
    
class wall_Extrude(bpy.types.Operator):
    """Extrudes wall outline"""
    bl_idname = "mesh.extrude_wall"
    bl_label = "Extrude Wall"
    bl_options = {"UNDO"}
    
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 5), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        return {"FINISHED"}
    
class furniture_Extrude(bpy.types.Operator):
    """Extrudes furniture"""
    bl_idname = "mesh.extrude_furniture"
    bl_label = "Extrude Furniture"
    bl_options = {"UNDO"}
    
    def execute(self, context):
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 2), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        return {"FINISHED"}

        


class GreasyBoardingPanel(bpy.types.Panel):
    """Creates GB Menu in Edit Mode"""
    bl_label = "GB Menu"
    bl_idname = "greasy_boarding_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = "curve_edit"
    bl_category = "GreasyBoard"

    def draw(self, context):
        layout = self.layout

        scene = context.scene

        # Create two columns, by using a split layout.
        split = layout.split()


        col = split.column()
        col.label(text="Walls:")
        col.operator("mesh.extrude_wall")
        
        
        

        # Second column, aligned
        col = split.column(align=True)
        col.label(text="Furniture:")
        
        

        # Big render button
        layout.label(text="Enable Grease Pencil:")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("object.enable_gp")
        col.operator("mesh.extrude_furniture")

    


def register():
    bpy.utils.register_class(GreasyBoardingPanel)
    bpy.utils.register_class(enable_GP)
    bpy.utils.register_class(wall_Extrude)
    bpy.utils.register_class(furniture_Extrude)
    #important! You must register/unregister all classes or else buttons/sliders will
    #not appear!

def unregister():
    bpy.utils.unregister_class(GreasyBoardingPanel)
    bpy.utils.unregister_class(enable_GP)
    bpy.utils.unregister_class(wall_Extrude)
    bpy.utils.unregister_class(furniture_Extrude)


#if __name__ == "__main__":
#    #for testing only so I don't have to keep reinstalling
#    register()
##    
