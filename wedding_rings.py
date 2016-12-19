import bpy

# based on http://yzahk.in/3D-printable-ring-Blender-add-on


SIZES = {
    'Aeva' : 18.75,
    'Mym'  : 20.75,
}
    


def units(n):
    #return n/1000
    return n


def ring_generator(wearer, thickness=5, segments=128):
    diameter = SIZES[wearer]
    
    bpy.ops.mesh.primitive_circle_add(
        vertices=segments, 
        radius=units(diameter)/2,
        enter_editmode=False, 
    )
    ob = bpy.context.active_object
    ob.name = "{0}'s Ring".format(wearer)
    me = ob.data
    me.name = ob.name + 'Mesh'
    
    bpy.ops.object.mode_set( mode   = 'EDIT'   )
    bpy.ops.mesh.select_mode( type  = 'VERT'   )
    bpy.ops.mesh.select_all( action = 'SELECT' )

    bpy.ops.mesh.extrude_region_move(
        TRANSFORM_OT_translate={"value":(0, 0, units(thickness))}
    )

    bpy.ops.object.mode_set( mode = 'OBJECT' )
    
    bpy.ops.object.modifier_add(type = 'SOLIDIFY')
    ob.modifiers['Solidify'].thickness = units(2)
    
    #bpy.ops.object.modifier_add(type = 'BEVEL')
    #ob.modifiers['Bevel'].width = 1
    #ob.modifiers['Bevel'].segments = 1

    bpy.ops.object.modifier_add(type = "SUBSURF")
    ob.modifiers['Subsurf'].levels = 2
    ob.modifiers['Subsurf'].render_levels = 2
    
    return ob


ring_generator('Aeva')
ring_generator('Mym')
