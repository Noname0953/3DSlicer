import random
import sys

print("Markera den efterfrågade strukturen. När du är nöjd med din markering trycker du 'f' för facit. Tryck 's' för statistik.")

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

# Define a list of structure lists
my_nodes = [
    ['A. basilaris', 2.117, -13.342, -36.126, 'invivo'],
    ['A. carotis interna', -18.5652, -7.1370, -40.5675, 'invivo'],
    ['A. cerebelli inferior anterior',-2.557,-15.766,-34.401,'invivo'],
    ['A. cerebelli inferior posterior',-8.730,-39.024,-43.589,'invivo'],
    ['A. cerebelli superior',8.870,-8.599,-20.914,'invivo'],
    ['A. cerebri anterior',3.994,4.618,-10.281,'invivo'],
    ['A. cerebri media',-22.975,0.085,-8.562,'invivo'],
    ['A. cerebri posterior',-6.432,-7.957,-13.319,'invivo'],
    ['A. communicans anterior',0.647,11.978,-13.922,'invivo'],
    ['A. communicans posterior',-9.190,-2.305,-17.512,'invivo'],
    ['A. vertebralis',-7.2983,-37.9725,-51.7110,'invivo'],
    ['Amygdala',-21.2982,-2.5985,-15.9190,'bigbrain'],
    ['Foramen Magendie eller Apertura mediana ventriculi quarti',1.864,-48.538,-49.338,'invivo'],
    ['Aqueductus cerebri/mesencephali',0.169,-31.340,-5.577,'invivo'],
    ['Capsula extrema',34.902,7.800,0.502,'exvivo'],
    ['Capsula externa',31.966,7.800,0.418,'exvivo'],
    ['Capsula interna',16.4213,10.6528,5.9804,'invivo'],
    ['Chiasma Opticum',-0.3038,5.3050,-13.6747,'invivo'],
    ['Colliculus inferior',5.196,-36.707,-8.114,'invivo'],
    ['Colliculus superior',5.196,-32.695,-2.031,'invivo'],
    ['Commisura anterior',0,0,0,'invivo'],
    ['Confluens sinuum',-10.347,-89.269,-28.472,'invivo'],
    ['Corpus callosum rostrum',0.500,15.640,6.846,'invivo'],
    ['Corpus callosum corpus/truncus',0.500,-5.327,25.224,'invivo'],
    ['Corpus callosum genu',0.500,21.852,15.647,'invivo'],
    ['Corpus callosum splenium',0.500,-36.130,9.823,'invivo'],
    ['Corpus geniculatum laterale',-23.736,-22.850,-5.674,'bigbrain'],
    ['Corpus geniculatum mediale',-15.848,-25.698,-5.674,'bigbrain'],
    ['Corpus mamillare',-2.746,-8.524,-14.707,'exvivo'],
    ['Cortex orbitofrontalis',5.099,42.016,-22.294,'exvivo'],
    ['Cortex piriformis',-20.447,-4.560,-13.944,'invivo'],
    ['Crus cerebri',-17.680,-18.261,-13.051,'exvivo'],
    ['Dura mater',-10.3420,36.0077,61.3329,'invivo'],
    ['Fissura longitudinalis cerebri',-1.467,30.546,38.912,'invivo'],
    ['Flocculus',-6.856,-52.550,-31.737,'invivo'],
    ['Foramen interventriculare eller Foramen Monroi',3.628,-3.473,5.976,'invivo'],
    ['Globus Pallidus Externa',21.616,-1.234,-1.774,'exvivo'],
    ['Globus Pallidus Interna',17.0080,-3.8205,-3.3735,'exvivo'],
    ['Gyrus temporalis transversus',-51.313,-18.486,7.458,'bigbrain'],
    ['Gyrus angularis',-39.391,-69.268,46.773,'exvivo'],
    ['Gyrus cinguli',-5.245,-4.321,35.217,'exvivo'],
    ['Gyrus frontalis inferior',-51.080,-1.339,25.231,'exvivo'],
    ['Gyrus frontalis medius',-32.673,11.790,48.564,'exvivo'],
    ['Gyrus frontalis superior',-12.732,34.249,48.564,'exvivo'],
    ['Gyrus parahippocampalis',-24.318,-23.765,-21.301,'exvivo'],
    ['Gyrus postcentralis',-49.9681,-17.7000,60.9956,'exvivo'],
    ['Gyrus precentralis',-37.6719,-16.2534,68.9521,'exvivo'],
    ['Sulcus parietooccipitalis',-8.986,-82.441,32.071,'exvivo'],
    ['Hippocampus',-23.944,-14.091,-18.506,'bigbrain'],
    ['Sulcus precentralis',-45.376,-17.422,47.042,'exvivo'],
    ['Sulcus centralis',-39.8418,-19.4748,49.4234,'exvivo'],
    ['Sulcus postcentralis',-58.688,-39.187,40.463,'exvivo'],
    ['Gyrus supramarginalis',-60.547,-40.301,26.786,'exvivo'],
    ['Gyrus temporalis superior',-61.047,-38.165,13.463,'exvivo'],
    ['Gyrus temporalis media',-62.110,-26.572,-9.658,'exvivo'],
    ['Gyrus temporalis inferior',-60.748,-43.785,-14.662,'exvivo'],
    ['Hypothalamus',0.080,0.211,-11.460,'invivo'],
    ['Infundibulum',0.580,1.823,-15.124,'invivo'],
    ['Lobus cerebelli anterior',10.973,-53.935,-16.900,'invivo'],
    ['Lobus cerebelli posterior',19.782,-75.532,-37.940,'invivo'],
    ['Medulla oblongata',1.030,-40.093,-52.135,'invivo'],
    ['Nervus fascialis',17.827,-28.288,-35.711,'invivo'],
    ['Nervus opticus',21.252,32.909,-19.435,'invivo'],
    ['Nervus trigeminus',-17.3793,-24.3338,-25.2110,'invivo'],
    ['Nervus trochlearis',11.2952,-36.2650,-10.1671,'invivo'],
    ['Nervus vestibulocochlearis',20.1049,-30.4617,-36.2110,'invivo'],
    ['Nucleus caudatus cauda',25.532,-36.829,6.423,'invivo'],
    ['Nucleus caudatus corpus',-16.076,3.638,16.684,'invivo'],
    ['Nucleus caudatus caput',-9.950,9.921,4.173,'invivo'],
    ['Nucleus ruber',-5.604,-19.104,-10.645,'bigbrain'],
    ['Nucleus olivaris eller Oliva',5.090,-37.300,-54.174,'exvivo'],
    ['Pedunculus cerebellaris inferior',9.747,-42.201,-38.788,'exvivo'],
    ['Pedunculus cerebellaris medius',16.123,-34.786,-34.702,'exvivo'],
    ['Pedunculus cerebellaris superior',-4.838,-41.456,-25.656,'exvivo'],
    ['Planum temporale',-49.939,-32.159,8.181,'exvivo'],
    ['Pons',0.0339,-25.9000,-27.6748,'invivo'],
    ['Putamen',28.345,-0.614,-3.021,'invivo'],
    ['Pyramis Medullae Oblongatae', -3.903,-34.181,-53.877,'exvivo'],
    ['Septum pellucidum',-0.043,12.008,10.522,'exvivo'],
    ['Sinus cavernosus',-1.626,-66.076,-7.615,'invivo'],
    ['Sinus sagittalis superior',-1.031,-73.862,54.061,'invivo'],
    ['Sinus transversus',-54.325,-44.213,-34.315,'invivo'],
    ['Substantia nigra',-6.939,-16.970,-17.106,'bibgrain'],
    ['Sulcus calcarinus',-3.839,-78.273,6.529,'bigbrain'],
    ['Sulcus lateralis',-52.838,0,0,'bigbrain'],
    ['Thalamus',9.3054,-18.4039,11.4804,'invivo'],
    ['Tonsilla',-5.316,-51.792,-39.754,'invivo'],
    ['Ventriculus lateralis',9, -11.4, 23,'invivo'],
    ['Cerebellum',0.5339,-54.6794,-27.6747,'invivo'],
    ['Tractus opticus',-9.5054,-3.8966,-9.1747,'invivo'],
    ['Tentorium cerebelli',-9.5054, -63.7734,-9.2014,'invivo'],
    ['Sinus transversus',-15.9745,-90.0629,-32.9464,'invivo'],
    ['Ventriculus quartus',0.329,-41.764,-25.818,'invivo']
    ]

redLogic.SetSliceOffset(0)
greenLogic.SetSliceOffset(0)
yellowLogic.SetSliceOffset(0)

# Define a function to prompt the user to identify the structure associated with a given node
def quiz_node(node):
    base_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
    user_input = ''
    # Prompt the user to identify the structure associated with the node
    if len(my_nodes) == 0:
        print("Inga strukturer kvar.")
    while user_input not in ['y', 'n', 'c', 'd', 'f', 'q']:
        try:
            user_input = input(node[0] + " ")
        except EOFError:
            user_input = ''
        # Check user input
        if user_input == 'f':
            base_node.AddControlPoint(node[1],node[2],node[3])
            redLogic.SetSliceOffset(base_node.GetNthControlPointPositionVector(0)[2])
            greenLogic.SetSliceOffset(base_node.GetNthControlPointPositionVector(0)[1])
            yellowLogic.SetSliceOffset(base_node.GetNthControlPointPositionVector(0)[0])
            right_wrong = input("Fick du rätt? (y/n) ")
            redLogic.SetSliceOffset(0)
            greenLogic.SetSliceOffset(0)
            yellowLogic.SetSliceOffset(0)
            if right_wrong == 'y':
                global right
                right += 1
                print("Snyggt! Tar bort strukturen från listan.")
                scene.RemoveNode(base_node)
                my_nodes.remove(node)
            if right_wrong == 'n':
                global wrong
                wrong += 1
                print("Strukturen kommer vara kvar i listan tills du får rätt.")
                scene.RemoveNode(base_node)
        elif user_input == 's':
            if right + wrong == 0:
                print("Du måste svara på någon struktur innan du kan få ut statistik.")
            else:
                print(str(len(my_nodes)) + " strukturer kvar.")
                print(str(right) + " rätt.")
                print(str(wrong) + " fel.")
        else:
            #Unmark this code for search function when testing new structures
            #for n in my_nodes:
            #    if user_input.lower() == n[0].lower():
            #        base_node.AddControlPoint(n[1],n[2],n[3])
            #        redLogic.SetSliceOffset(base_node.GetNthControlPointPositionVector(0)[2])
            #        greenLogic.SetSliceOffset(base_node.GetNthControlPointPositionVector(0)[1])
            #        yellowLogic.SetSliceOffset(base_node.GetNthControlPointPositionVector(0)[0])
            print("'f' för facit. 's' för statistik.")

right = 0
wrong = 0

def main():
    while True:
        # Select a random node from the list of nodes
        node = random.choice(my_nodes)
        # Changes view based on node
        if node[4] == 'invivo' :
            slicer.util.setSliceViewerLayers(background=invivo)
        if node[4] == 'exvivo':
            slicer.util.setSliceViewerLayers(background=exvivo)
        if node[4] == 'bigbrain':
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
