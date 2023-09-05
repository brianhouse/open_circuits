# Inkscape
 
Inkscape is a free vector graphics editor for GNU/Linux, Windows and macOS. You can download Inkscape [here](https://inkscape.org/release/inkscape-1.2.2/) Simple designs (geometric shapes, text, clipart) can all be done on the Glowforge webpage and may not need Inkscape. 

A video tutorial can be found [here](https://drive.google.com/file/d/1h6DkFrqTs8azBbxr2fY-hahtvEaqBuQK/view?usp=drive_link), which you can follow as you read the instructions.


## Set Up

1. Open Inkscape, The default options work great for most projects, Click New Document in the bottom right
2. Click `File`, Click `Document Properties`, Under `Display>Format`: Change the format to inches in., Change `Display units` to inches `in.`, Change `Width & Height` to dimensions of your laser cut material (Clear acrylic sheet is 20"X12")
3. In the same tab as before click `Grids` (to the right of Display), Click `New`, Make sure `Enabled`, `Visible`, and `Snap to visible grid lines only` are all checked. Change `Grid units` to inches `in`. Set `Spacing X` and `Spacing Y` to 0.25 (You can change this to suit your project, the smaller the spacing the more gridlines you will have) You can exit out of this tab now

## Creation

Understand what you are planning on creating. You should know the answers to these questions: What are you making? How big will it be? What parts will be cut/engraved/scored?

Click the `View Objects` button in the top dashboard. A tab will pop open to the right, click the `Add Layer` button and 3 layers. Name one layer cut, one engrave, and one score. When working on your project be sure to be conscious of which layer you are working on to make sure that all engraved, cut, and scored objects are on their respective layer.
Begin creating!

## Formatting
Once you have finished your drawing: Go to your Cut layer. Select all objects on this layer only: press Ctrl+ A (Win) or Command+ A (Mac). Click the `Fill and Stroke button`. A tab will pop open to the right, click `Fill` then click the X (`no paint`) under `Fill` so the objects become "hollow", this ensures that Beamzilla only cuts the perimeter of the objects. Next, click `Stroke Paint` and then the solid blue square, `Flat color`. Next, click `Stroke Style` and change the width unit to inches `in`. and change the width to 0.001. DON'T WORRY your work didn't just disappear it's still there the outline is just super thin!

If you want your engraved objects to be engraved as a filled solid shape: Go to your Engrave layer. Select all objects on this layer only: press Ctrl+ A (Win) or Command+ A (Mac). Click the `Fill and Stroke` button. A tab will pop open to the right, click `Fill` then the solid blue square, `Flat color` (you can do any color). Next, click `Stroke Paint` and then the solid blue square, `Flat color`. Next, click `Stroke Style` and change the width unit to inches `in`. and change the width to 0.001. Repeat for your Score layer.

If you want any objects on your engrave or score layer to be engraved/scored as lines rather than solid fill: Go to the respective layer (engrave or score). Select all the objects you wish to be made lines. Click the `Fill and Stroke` button. A tab will pop open to the right, click `Fill` then click the X (no paint). Next, click `Stroke Paint` and then the solid blue square, Flat color. Next, click `Stroke Style` and change the width unit to inches in. and change the width to 0.001

Select all objects on all layers: press Ctrl+Alt+A (Win) or Command+Option+A (Mac). Then click `Path`, then `Object to Path`. (Beamzilla can only read Paths so all objects must be converted)

Once you have completed all these steps you are ready to save your file! Go to `File>Save as`, save the file as an "Inkscape SVG (*.svg)"

_You are now ready for Beamzilla!_


