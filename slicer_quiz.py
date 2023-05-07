import random
import sys

print("Quiz time! Scriptet styrs av kortkommandon. 'y' för facit, 'd' för att ta bort strukturen från listan eller 'c' för att recentrera på punkten. 'f' för statistik.")

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
a_basilaris = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_carotisinterna = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_cerebelli_inferior_anterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_cerebelli_inferior_posterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_cerebelli_superior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_cerebri_anterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_cerebri_media = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_cerebri_posterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_communicans_anterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_communicans_posterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
a_vertebralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
amygdala = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
foramen_magendie = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
aqueductus_cerebri = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
capsula_extrema = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
capsula_externa = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
capsula_interna = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
chiasma_opticum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
colliculus_inferior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
colliculus_superior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
commisura_anterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
confluens_sinuum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
corpus_callosum_rostrum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
corpus_callosum_corpus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
corpus_callosum_genu = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
corpus_callosum_splenium = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
corpus_geniculatum_laterale = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
corpus_geniculatum_mediale = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
corpus_mamillare = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
cortex_orbitofrontalis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
cortex_piriformis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
crus_cerebri = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
dura_mater = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
fissura_longitudinalis_cerebi = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
flocculus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
foramen_interventriculare = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
globus_pallidus_externa = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
globus_pallidus_interna = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')


hippocampus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')


Ventriculus_lateralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
Nervus_opticus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
cerebellum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
pons = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
tractus_opticus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
tentorium_cerebelli = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_trochlearis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
sinus_transversus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_trigeminus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_vestibulocochlearis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
n_fascialis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nucleus_caudatus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
putamen = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
thalamus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
ventriculus_quartus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')

# Set the positions of nodes
a_basilaris.AddControlPoint(2.117,-13.342,-36.126)
a_carotisinterna.AddControlPoint(-18.5652,-7.1370,-40.5675)
a_cerebelli_inferior_anterior.AddControlPoint(-2.557,-15.766,-34.401)
a_cerebelli_inferior_posterior.AddControlPoint(-8.730,-39.024,-43.589)
a_cerebelli_superior.AddControlPoint(8.870,-8.599,-20.914)
a_cerebri_anterior.AddControlPoint(3.994,4.618,-10.281)
a_cerebri_media.AddControlPoint(-22.975,0.085,-8.562)
a_cerebri_posterior.AddControlPoint(-6.432,-7.957,-13.319)
a_communicans_anterior.AddControlPoint(0.647,11.978,-13.922)
a_communicans_posterior.AddControlPoint(-9.190,-2.305,-17.512)
a_vertebralis.AddControlPoint(-7.2983,-37.9725,-51.7110)
amygdala.AddControlPoint(-25.540,-14.891,-11.279)
foramen_magendie.AddControlPoint(1.864,-48.538,-49.338)
aqueductus_cerebri.AddControlPoint(0.169,-31.340,-5.577)
capsula_extrema.AddControlPoint(34.902,7.800,0.502)
capsula_externa.AddControlPoint(31.966,7.800,0.418)
capsula_interna.AddControlPoint(16.4213,10.6528,5.9804)
chiasma_opticum.AddControlPoint(-0.3038,5.3050,-13.6747)
colliculus_inferior.AddControlPoint(5.196,-36.707,-8.114)
colliculus_superior.AddControlPoint(5.196,-32.695,-2.031)
commisura_anterior.AddControlPoint(0,0,0)
confluens_sinuum.AddControlPoint(-10.347,-89.269,-28.472)
corpus_callosum_rostrum.AddControlPoint(0.500,15.640,6.846)
corpus_callosum_corpus.AddControlPoint(0.500,-5.327,25.224)
corpus_callosum_genu.AddControlPoint(0.500,21.852,15.647)
corpus_callosum_splenium.AddControlPoint(0.500,-36.130,9.823)
corpus_geniculatum_laterale.AddControlPoint(-23.736,-22.850,-5.674)
corpus_geniculatum_mediale.AddControlPoint(-15.848,-25.698,-5.674)
corpus_mamillare.AddControlPoint(-2.746,-8.524,-14.707)
cortex_orbitofrontalis.AddControlPoint(5.099,42.016,-22.294)
cortex_piriformis.AddControlPoint(-20.447,-4.560,-13.944)
crus_cerebri.AddControlPoint(-17.680,-18.261,-13.051)
dura_mater.AddControlPoint(-10.3420,36.0077,61.3329)
fissura_longitudinalis_cerebi.AddControlPoint(-1.467,30.546,38.912)
flocculus.AddControlPoint(-6.856,-52.550,-31.737)
foramen_interventriculare.AddControlPoint(3.628,-3.473,5.976)
globus_pallidus_externa.AddControlPoint(21.616,-1.234,-1.774)
globus_pallidus_interna.AddControlPoint(17.0080,-3.8205,-3.3735)


hippocampus.AddControlPoint(-23.944,-14.091,-18.506)


Ventriculus_lateralis.AddControlPoint(9, -11.4, 23)
Nervus_opticus.AddControlPoint(21.0266, 32.9091, -20.211)
cerebellum.AddControlPoint(0.5339,-54.6794,-27.6747)
pons.AddControlPoint(0.0339,-25.9000,-27.6748)
tractus_opticus.AddControlPoint(-9.5054,-3.8966,-9.1747)
tentorium_cerebelli.AddControlPoint(-9.5054, -63.7734,-9.2014)
n_trochlearis.AddControlPoint(11.2952,-36.2650,-10.1671)
sinus_transversus.AddControlPoint(-15.9745,-90.0629,-32.9464)
n_trigeminus.AddControlPoint(-17.3793,-24.3338,-25.2110)
n_vestibulocochlearis.AddControlPoint(20.1049,-30.4617,-36.2110)
n_fascialis.AddControlPoint(18.0032,-28.1689,-35.7110)
#29-04-2023
nucleus_caudatus.AddControlPoint(11.6773,11.2457,11.6539)
putamen.AddControlPoint(24.7232,-0.6141,11.6539)
thalamus.AddControlPoint(9.3054,-18.4039,11.4804)
ventriculus_quartus.AddControlPoint(0.329,-41.764,-25.818)

# Define a dictionary that maps nodes to their names
node_names = {
    a_basilaris: 'A. basilaris',
    a_carotisinterna: 'A. carotis interna',
    a_cerebelli_inferior_anterior: 'A. cerebelli inferior anterior',
    a_cerebelli_inferior_posterior: 'A. cerebelli inferior posterior',
    a_cerebelli_superior: 'A. cerebelli superior',
    a_cerebri_anterior: 'A. cerebri anterior',
    a_cerebri_media: 'A. cerebri media',
    a_cerebri_posterior: 'A. cerebri posterior',
    a_communicans_anterior: 'A. communicans posterior',
    a_communicans_posterior: 'A. communicans posterior',
    a_vertebralis: 'A. vertebralis',
    amygdala: 'Amygdala',
    foramen_magendie: 'Foramen Magendie eller Apertura mediana ventriculi quarti',
    aqueductus_cerebri: 'Aqueductus cerebri/mesencephali',
    capsula_extrema: 'Capsula extrema',
    capsula_externa: 'Capsula externa',
    capsula_interna: 'Capsula interna',
    chiasma_opticum: 'Chiasma Opticum',
    colliculus_inferior: 'Colliculus inferior',
    colliculus_superior: 'Colliculus superior',
    commisura_anterior: 'Commisura anterior',
    confluens_sinuum: 'Confluens sinuum',
    corpus_callosum_rostrum: 'Corpus callosum rostrum',
    corpus_callosum_corpus: 'Corpus callosum corpus/truncus',
    corpus_callosum_genu: 'Corpus callosum genu',
    corpus_callosum_splenium: 'Corpus callosum splenium',
    corpus_geniculatum_laterale: 'Corpus geniculatum laterale',
    corpus_geniculatum_mediale: 'Corpus geniculatum mediale',
    corpus_mamillare: 'Corpus mamillare',
    cortex_orbitofrontalis: 'Cortex orbitofrontalis',
    cortex_piriformis: 'Cortex piriformis',
    crus_cerebri: 'Crus cerebri',
    dura_mater: 'Dura mater',
    fissura_longitudinalis_cerebi: 'Fissura longitudinalis cerebri',
    flocculus: 'Flocculus',
    foramen_interventriculare: 'Foramen interventriculare eller Foramen Monroi',
    globus_pallidus_externa: 'Globus Pallidus Externa',
    globus_pallidus_interna: 'Globus Pallidus Interna',


    hippocampus: 'Hippocampus',


    Ventriculus_lateralis: 'Ventriculus Lateralis',
    Nervus_opticus: 'Nervus Opticus',
    cerebellum: 'Cerebellum',
    pons: 'Pons',
    tractus_opticus: 'Tractus Opticus',
    tentorium_cerebelli: 'Tentorium Cerebelli',
    n_trochlearis: 'N. trochlearis',
    sinus_transversus: 'Sinus transversus',
    n_trigeminus: 'N. trigeminus',
    n_vestibulocochlearis: 'N. vestibulocochlearis',
    n_fascialis: 'N. fascialis',
    nucleus_caudatus: 'Nucleus caudatus',
    putamen: 'Putamen',
    thalamus: 'Thalamus',
    ventriculus_quartus: 'Ventriculus quartus',
    globus_pallidus_externa: 'Globus pallidus externa',
    globus_pallidus_interna: 'Globus pallidus interna'
}

invivo_allviews_list = [a_basilaris,
                        a_carotisinterna,
                        a_cerebelli_inferior_anterior,
                        a_cerebelli_inferior_posterior,
                        a_cerebelli_superior,
                        a_cerebri_anterior,
                        a_cerebri_media,
                        a_cerebri_posterior,
                        a_communicans_anterior,
                        a_communicans_posterior,
                        a_vertebralis,
                        foramen_magendie,
                        aqueductus_cerebri,
                        capsula_interna,
                        chiasma_opticum,
                        colliculus_inferior,
                        colliculus_superior,
                        commisura_anterior,
                        confluens_sinuum,
                        corpus_callosum_rostrum,
                        corpus_callosum_corpus,
                        corpus_callosum_genu,
                        corpus_callosum_splenium,
                        cortex_piriformis,
                        dura_mater,
                        fissura_longitudinalis_cerebi,
                        flocculus,
                        foramen_interventriculare,



                        Ventriculus_lateralis,
                        Nervus_opticus,
                        cerebellum,
                        pons,
                        tractus_opticus,
                        tentorium_cerebelli,
                        n_trochlearis,
                        sinus_transversus,
                        n_trigeminus,
                        n_vestibulocochlearis,
                        n_fascialis,
                        nucleus_caudatus,
                        putamen,
                        thalamus,
                        ventriculus_quartus]

exvivo_allviews_list = [capsula_extrema,
                       capsula_externa,
                       corpus_mamillare,
                       cortex_orbitofrontalis,
                       crus_cerebri,
                       globus_pallidus_externa,
                       globus_pallidus_interna]

bigbrain_allviews_list = [amygdala,
                         hippocampus,
                         corpus_geniculatum_laterale,
                         corpus_geniculatum_mediale]

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
    while user_input not in ['y', 'n', 'c', 'd', 'f', 'q']:
        try:
            user_input = input("Vilken struktur är markerad? ")
        except EOFError:
            user_input = 'y'
        # Check user input
        if user_input == 'y':
            print(str(node_names[node]))
            right_wrong = input("Fick du rätt? (y/n) ")
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
        elif user_input == 'd':
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
