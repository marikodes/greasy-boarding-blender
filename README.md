# greasy-boarding-blender
blender add-on for storyboarding w/ grease pencil

## Credits
https://medium.com/geekculture/creating-a-custom-panel-with-blenders-python-api-b9602d890663 \
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

## Development

I created this project as a part of the hackathon WildHacks 2023 for the Entertainment and Arts track. I am interested in working in the animation industry as a pipeline technical director. 
TDs take care of the artists by making sure they have the tools they need to do their work efficiently and effectively.
I wanted to use this hackathon to create a project similiar to the work I see myself doing as a TD. I came into the hackathon knowing I wanted to create some kind of add on for blender, but I wanted it to address an unmet need. 
I watched some videos to understand how different artists use blender (videos linked below, and I thought to do something involving storyboarding and blender's grease pencil(GP) feature. 
Basically, I wanted to make it easier to do perspective for storyboards in blender. Instead of having to create a room layout from scratch, 
I wanted something that would set up a basic room layout from an imported top down svg image. I wanted it to have different extrusion settings for walls vs furnature, 
as well as something to easily enable drawing over the 3d setup with GP. Normally, to enable GP, you have to first add a GP object and then go to draw mode. 
I thought that it would increase speed by removing the extra clicking to add a GP object with a button.

## Video Inspiration
https://www.youtube.com/watch?v=2BERE-IytcU \
https://www.youtube.com/watch?v=XrJctA2_Ixc 

## Features
-Using imported SVG, extrudes walls and furniture for basic perspective \
-Efficiently enables drawing over 3D layout with grease pencil with one click 


## Blender API references
https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html \
https://docs.blender.org/api/current/info_overview.html 
