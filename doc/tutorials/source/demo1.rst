A minimal scene
===============

This is a minimal example of a scene with one camera, two point lights
and a sphere that has a material assigned.

.. image:: pics/demo1_screenshot.jpg

Here is the :download:`script <../../../demos/demo1.py>`::

    ######################################################################
    # A simple static scene: a camera, two point lights and a sphere.
    ######################################################################

    TargetCamera(
        pos    = (3,2,2),
        target = (0,0,0)
    )

    GLPointLight(
        pos       = (3, -1, 2),
        diffuse   = (1, 0.7, 0.2)
    )

    GLPointLight(
        pos       = (-5, 3, 0),
        diffuse   = (0.2, 0.2, 0.5),
        intensity = 3.0
    )

    Sphere(
        name      = "My Sphere",
        radius    = 1.0,
        material  = GLMaterial(
                       diffuse = (0.7, 1, 0.7)
                   )
    )
