import random
import sys

print("Quiz time! Scriptet styrs av kortkommandon. 'y' för facit 'n' för att ta bort strukturen från listan eller 'c' för att recentrera på punkten. 'f' för statistik.")

layoutManager = slicer.app.layoutManager()
layoutManager.layoutLogic().GetLayoutNode().AddLayoutDescription(customLayoutId, customLayout)

def clear_all_markers():
    # Get all fiducial nodes in the scene
    fiducial_nodes = slicer.util.getNodesByClass("vtkMRMLMarkupsFiducialNode")

    # Remove each fiducial node from the scene
    for node in fiducial_nodes:
        scene.RemoveNode(node)

# Get the MRML scene
scene = slicer.mrmlScene

clear_all_markers()

error_structures = []

exvivo = slicer.util.getNode("Ex_vivo 500")
invivo = slicer.util.getNode("In vivo 7T 500M")
bigbrain = slicer.util.getNode("Big brain 400 ljus")

# Enable slice intersections
sliceDisplayNodes = slicer.util.getNodesByClass("vtkMRMLSliceDisplayNode")
for sliceDisplayNode in sliceDisplayNodes:
  sliceDisplayNode.SetIntersectingSlicesVisibility(1)

# Get a vtkMRMLNodeCollection containing all the nodes in the scene
node_collection = scene.GetNodes()

# Define slice views
layoutManager = slicer.app.layoutManager()
red = layoutManager.sliceWidget("Red")
green = layoutManager.sliceWidget("Green")
yellow = layoutManager.sliceWidget("Yellow")
redLogic = red.sliceLogic()
greenLogic = green.sliceLogic()
yellowLogic = yellow.sliceLogic()

Ventriculus_lateralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
putamen = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')

# Set the positions of nodes
#28-04-2023
Ventriculus_lateralis.AddControlPoint(9, -11.4, 23)
putamen.AddControlPoint(24.7232,-0.6141,11.6539)

# Define a dictionary that maps nodes to their names
node_names = {
    Ventriculus_lateralis: 'Ventriculus Lateralis',
    putamen: 'Putamen'
}

# Convert the collection to a Python list of nodes
my_nodes = [Ventriculus_lateralis,
putamen
]

bigbrain_list = [putamen]
invivo_list = [Ventriculus_lateralis]
exvivo_list = []

redlist = [putamen]

# Define a function to prompt the user to identify the structure associated with a given node
def quiz_node(node):
    global right, wrong
    # Sets only the current node to be visible
    for n in my_nodes:
        if n == node:
            # Change slice position
            redLogic.SetSliceOffset(node.GetNthControlPointPositionVector(0)[2])
            greenLogic.SetSliceOffset(node.GetNthControlPointPositionVector(0)[1])
            yellowLogic.SetSliceOffset(node.GetNthControlPointPositionVector(0)[0])
            n.SetDisplayVisibility(True)
        else:
            n.SetDisplayVisibility(False)
    # Prompt the user to identify the structure associated with the node
    user_input = ''
    while user_input not in ['y', 'n']:
        try:
            user_input = input("Vilken struktur är markerad? ")
        except EOFError:
            user_input = 'y'
        # Check user input
        if user_input == 'y':
            print(str(node_names[node]))
            right_wrong = input('Fick du rätt? (y/n) ')
            if right_wrong == 'y':
                right += 1
                print("Mäktigt.")
            if right_wrong == 'n':
                wrong += 1
                error_structures.append(node)
                print("Snart finns även den här strukturen i din hippocampus. Försök igen!")
            else:
                pass
        elif user_input == 'c':
            # Change slice position
            redLogic.SetSliceOffset(node.GetNthControlPointPositionVector(0)[2])
            greenLogic.SetSliceOffset(node.GetNthControlPointPositionVector(0)[1])
            yellowLogic.SetSliceOffset(node.GetNthControlPointPositionVector(0)[0])
            n.SetDisplayVisibility(True)
        elif user_input == 'f':
            # Gives statistics on current quiz run
            if right+wrong == 0:
                print("Du måste svara på någon struktur innan du kan få ut statistik!")
            else:
                print(str(right) + " rätt")
                print(str(wrong) + " fel")
                print(str(round(100*(right/(right+wrong)),1))+"%")
                print("Strukturer du svarat fel på: ")
                for error in error_structures:
                    print(str(node_names[error]))
        elif user_input == 'n':
            # Removes node from list
            if len(my_nodes) == 1:
                print("Listan är nu tom!")
            else:
                my_nodes.remove(node)
                scene.RemoveNode(node)
                print(node_names[node]+" borttagen.")
                print(str(len(my_nodes))+" strukturer kvar i listan.")

right = 0
wrong = 0
def main():
    while True:
        # Select a random node from the list of nodes
        node = random.choice(my_nodes)
        # Changes view based on node
        if node in bigbrain_list:
            slicer.util.setSliceViewerLayers(background=bigbrain)
        if node in invivo_list:
            slicer.util.setSliceViewerLayers(background=invivo)
        if node in exvivo_list:
            slicer.util.setSliceViewerLayers(background=exvivo)
        if node in horizontal_list:
            layoutManager.setLayout(6)
        if node in sagittal_list:
            layoutManager.setLayout(7)
        if node in coronal_list:
            layoutManager.setLayout(8)
        if node in horizontal_sagital_list:
            layoutManager.setLayout(29)
        else:
            layoutManager.setLayout(0)
        # Quiz the user on the structure associated with the node
        quiz_node(node)

if __name__ == "__main__":
  #Run as main program
  main()
