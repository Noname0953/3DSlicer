import random
import sys

print("Quiz time! Scriptet styrs av kortkommandon. 'y' för facit 'n' för att ta bort strukturen från listan eller 'c' för att recentrera på punkten. 'f' för statistik.")

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

# Get the list of volumes
volumes = slicer.mrmlScene.GetNodesByClass("vtkMRMLScalarVolumeNode")

# Choose the index of the volume you want to make active
index_of_volume_to_make_active = 0

# Set the active volume to the chosen volume
slicer.app.applicationLogic().GetSelectionNode().SetActiveVolumeID(volumes.GetItemAsObject(index_of_volume_to_make_active).GetID())

# Update the views
slicer.app.applicationLogic().PropagateVolumeSelection(0)

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

# Create a new fiducial node
Ventriculus_lateralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
Corpus_callosum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
Hippocampus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
Sulcus_lateralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode', ' ')
Nervus_opticus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
Dura_mater = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
cerebellum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
pons = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
chiasma_opticus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
tractus_opticus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
tentorium_cerebelli = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_trochlearis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_carotisinterna = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_vertebralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_basilaris = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_cerebriposterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
sinus_transversus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_trigeminus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_vestibulocochlearis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_fascialis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')

# Set the position of the new node
Ventriculus_lateralis.AddControlPoint(9, -11.4, 23)
Corpus_callosum.AddControlPoint(0, -11, 26)
Hippocampus.AddControlPoint(-23.25, -11.41, -19.19)
Sulcus_lateralis.AddControlPoint(-37, -20, 11.6)
Sulcus_lateralis.AddControlPoint(-63, -20, 11.6)
Nervus_opticus.AddControlPoint(21.0266, 32.9091, -20.211)
Dura_mater.AddControlPoint(-10.3420, 36.0077, 61.3329)
cerebellum.AddControlPoint(0.5339,-54.6794,-27.6747)
pons.AddControlPoint(0.0339,-25.9000,-27.6748)
chiasma_opticus.AddControlPoint(-0.3038,5.3050,-13.6747)
tractus_opticus.AddControlPoint(-9.5054,-3.8966,-9.1747)
tentorium_cerebelli.AddControlPoint(-9.5054, -63.7734,-9.2014)
n_trochlearis.AddControlPoint(11.2952,-36.2650,-10.1671)
a_carotisinterna.AddControlPoint(-18.5652,-7.1370,-40.5675)
a_vertebralis.AddControlPoint(-7.2983,-37.9725,-51.7110)
a_basilaris.AddControlPoint(-7.8913,-18.9968,-39.2110)
a_cerebriposterior.AddControlPoint(-9.8392,-8.8229,-13.6177)
sinus_transversus.AddControlPoint(-15.9745,-90.0629,-32.9464)
n_trigeminus.AddControlPoint(-17.3793,-24.3338,-25.2110)
n_vestibulocochlearis.AddControlPoint(20.1049,-30.4617,-36.2110)
n_fascialis.AddControlPoint(18.0032,-28.1689,-35.7110)

# Define a dictionary that maps nodes to their names
node_names = {
    Ventriculus_lateralis: 'Ventriculus Lateralis',
    Corpus_callosum: 'Corpus Callosum',
    Hippocampus: 'Hippocampus',
    Sulcus_lateralis: 'Sulcus Lateralis',
    Nervus_opticus: 'Nervus Opticus',
    Dura_mater: 'Dura mater',
    cerebellum: 'Cerebellum',
    pons: 'Pons',
    chiasma_opticus: 'Chiasma Opticus',
    tractus_opticus: 'Tractus Opticus',
    tentorium_cerebelli: 'Tentorium Cerebelli',
    n_trochlearis: 'N. trochlearis - kolla horizontalsnittet och zooma in på pons!',
    a_carotisinterna: 'A. Carotis interna',
    a_vertebralis: 'A. vertebralis',
    a_basilaris: 'A. basilaris',
    a_cerebriposterior: 'A. cerebri posterior',
    sinus_transversus: 'Sinus transversus',
    n_trigeminus: 'N. trigeminus',
    n_vestibulocochlearis: 'N. vestibulocochlearis',
    n_fascialis: 'N. fascialis'
}

# Convert the collection to a Python list of nodes
my_nodes = [Ventriculus_lateralis,
Corpus_callosum,
Hippocampus,
Sulcus_lateralis,
Nervus_opticus,
Dura_mater,
cerebellum,
pons,
chiasma_opticus,
tractus_opticus,
tentorium_cerebelli,
n_trochlearis,
a_carotisinterna,
a_vertebralis,
a_basilaris,
a_cerebriposterior,
sinus_transversus,
n_trigeminus,
n_vestibulocochlearis,
n_fascialis
]

# Define a function to prompt the user to identify the structure associated with a given node
def quiz_node(node):
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
                global right
                right += 1
                print("Mäktigt.")
            if right_wrong == 'n':
                global wrong
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
                print("Division med 0 inte tillåtet!")
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
        else:
            user_input = 'y'
# Main loop for the quiz
right = 0
wrong = 0
while True:
    # Select a random node from the list of nodes
    node = random.choice(my_nodes)
    # Quiz the user on the structure associated with the node
    quiz_node(node)
