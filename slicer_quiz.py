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

exvivo = slicer.util.getNode("Ex_vivo 500")
invivo = slicer.util.getNode("In vivo 7T 500M")
bigbrain = slicer.util.getNode("Big brain 400 ljus")

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

# Creates fiducial nodes
Ventriculus_lateralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
Corpus_callosum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
Hippocampus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
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
nucleus_caudatus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
putamen = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
thalamus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
capsula_interna = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
capsula_externa = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
capsula_extrema = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
ventriculus_quartus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
globus_pallidus_externa = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
globus_pallidus_interna = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')

# Set the positions of nodes
#28-04-2023
Ventriculus_lateralis.AddControlPoint(9, -11.4, 23)
Corpus_callosum.AddControlPoint(0.0357, -10.7357, 24.7500)
Hippocampus.AddControlPoint(-23.25, -11.41, -19.19)
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
#29-04-2023
nucleus_caudatus.AddControlPoint(11.6773,11.2457,11.6539)
putamen.AddControlPoint(24.7232,-0.6141,11.6539)
thalamus.AddControlPoint(9.3054,-18.4039,11.4804)
capsula_interna.AddControlPoint(16.4213,10.6528,5.9804)
capsula_externa.AddControlPoint(29.0020,5.6287,4.4804)
capsula_extrema.AddControlPoint(31.0476,7.5464,1.2135)
ventriculus_quartus.AddControlPoint(0.329,-38.710,-20.382)
globus_pallidus_externa.AddControlPoint(15.7509,4.3509,-3.3735)
globus_pallidus_interna.AddControlPoint(17.0080,-3.8205,-3.3735)

# Define a dictionary that maps nodes to their names
node_names = {
    Ventriculus_lateralis: 'Ventriculus Lateralis',
    Corpus_callosum: 'Corpus Callosum',
    Hippocampus: 'Hippocampus',
    Nervus_opticus: 'Nervus Opticus',
    Dura_mater: 'Dura mater',
    cerebellum: 'Cerebellum',
    pons: 'Pons',
    chiasma_opticus: 'Chiasma Opticus',
    tractus_opticus: 'Tractus Opticus',
    tentorium_cerebelli: 'Tentorium Cerebelli',
    n_trochlearis: 'N. trochlearis',
    a_carotisinterna: 'A. Carotis interna',
    a_vertebralis: 'A. vertebralis',
    a_basilaris: 'A. basilaris',
    a_cerebriposterior: 'A. cerebri posterior',
    sinus_transversus: 'Sinus transversus',
    n_trigeminus: 'N. trigeminus',
    n_vestibulocochlearis: 'N. vestibulocochlearis',
    n_fascialis: 'N. fascialis',
    nucleus_caudatus: 'Nucleus caudatus',
    putamen: 'Putamen',
    thalamus: 'Thalamus',
    capsula_interna: 'Capsula interna',
    capsula_externa: 'Capsula externa',
    capsula_extrema: 'Capsula extrema',
    ventriculus_quartus: 'Ventriculus quartus',
    globus_pallidus_externa: 'Globus Pallidus Externa',
    globus_pallidus_interna: 'Globus Pallidus Interna'
}

invivo_allviews_list = [Ventriculus_lateralis,
Hippocampus,
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
n_fascialis,
nucleus_caudatus,
putamen,
thalamus,
capsula_interna,
capsula_externa,
capsula_extrema,
ventriculus_quartus]

exvivo_allviews_list = [globus_pallidus_externa,
globus_pallidus_interna]

bigbrain_allviews_list = [Corpus_callosum]

# Convert the collection to a Python list of nodes
my_nodes = bigbrain_allviews_list + invivo_allviews_list + exvivo_allviews_list

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
        else:
            user_input = 'y'
right = 0
wrong = 0
def main():
    while True:
        # Select a random node from the list of nodes
        node = random.choice(my_nodes)
        # Changes view based on node
        if node in invivo_allviews_list:
            slicer.util.setSliceViewerLayers(background=invivo)
        if node in exvivo_allviews_list:
            slicer.util.setSliceViewerLayers(background=exvivo)
        if node in bigbrain_allviews_list:
            slicer.util.setSliceViewerLayers(background=bigbrain)
        #if node in horizontal_list:
        #    layoutManager.setLayout(6)
        #if node in sagittal_list:
        #    layoutManager.setLayout(7)
        #if node in coronal_list:
        #    layoutManager.setLayout(8)
        #if node in horizontal_sagital_list:
        #    layoutManager.setLayout(29)
        else:
            layoutManager.setLayout(0)
        # Quiz the user on the structure associated with the node
        quiz_node(node)

if __name__ == "__main__":
  #Run as main program
  main()
