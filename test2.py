# This example adds an action to the default double-click action on a markup
# and defines two new custom actions. It is done for all existing markups in the first 3D view.
#
# How to use:
# 1. Create markups nodes.
# 2. Run the script below.
# 3. Double-click on the markup -> this triggers toggleLabelVisibilty.
# 4. Hover the mouse over a markup then pressing `q` and `w` keys -> this triggers shrinkControlPoints and growControlPoints.

# Creates fiducial nodes
Ventriculus_lateralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'James')
putamen = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', 'Bond')

# Set the positions of nodes
#28-04-2023
Ventriculus_lateralis.AddControlPoint(9, -11.4, 23)
putamen.AddControlPoint(24.7232,-0.6141,11.6539)

Ventriculus_lateralis.GetDisplayNode().SetPointLabelsVisibility(True)
putamen.GetDisplayNode().SetPointLabelsVisibility(False)

# Define a dictionary that maps nodes to their names
node_names = {
    Ventriculus_lateralis: 'Ventriculus Lateralis',
    putamen: 'Putamen'
}

threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
markupsDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName('vtkMRMLMarkupsDisplayableManager')

def shrinkControlPoints(caller, eventId):
  markupsDisplayNode = caller
  markupsDisplayNode.SetGlyphScale(markupsDisplayNode.GetGlyphScale()/1.1)

def growControlPoints(caller, eventId):
  markupsDisplayNode = caller
  markupsDisplayNode.SetGlyphScale(markupsDisplayNode.GetGlyphScale()*1.1)

def toggleLabelVisibility(caller, eventId):
  markupsDisplayNode = caller
  markupsDisplayNode.SetPointLabelsVisibility(not markupsDisplayNode.GetPointLabelsVisibility())

observations = []  # store the observations so that later can be removed
markupsDisplayNodes = slicer.util.getNodesByClass("vtkMRMLMarkupsDisplayNode")
for markupsDisplayNode in markupsDisplayNodes:
  # Assign keyboard shortcut to trigger custom actions
  markupsWidget = markupsDisplayableManager.GetWidget(markupsDisplayNode)
  # Left double-click interaction event is translated to markupsWidget.WidgetEventAction by default,
  # therefore we don't need to add an event translation for that. We just add two keyboard event translation for two custom actions
  markupsWidget.SetKeyboardEventTranslation(markupsWidget.WidgetStateOnWidget, vtk.vtkEvent.NoModifier, '\0', 0, "q", markupsWidget.WidgetEventCustomAction1)
  markupsWidget.SetKeyboardEventTranslation(markupsWidget.WidgetStateOnWidget, vtk.vtkEvent.NoModifier, '\0', 0, "w", markupsWidget.WidgetEventCustomAction2)
  # Add observer to custom actions
  observations.append([markupsDisplayNode, markupsDisplayNode.AddObserver(markupsDisplayNode.ActionEvent, toggleLabelVisibility)])
  observations.append([markupsDisplayNode, markupsDisplayNode.AddObserver(markupsDisplayNode.CustomActionEvent1, shrinkControlPoints)])
  observations.append([markupsDisplayNode, markupsDisplayNode.AddObserver(markupsDisplayNode.CustomActionEvent2, growControlPoints)])

# Remove observations when custom actions are not needed anymore by uncommenting these lines:
for observedNode, observation in observations:
  observedNode.RemoveObserver(observation)
