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
gyrus_temporalis_transversus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_angularis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_cinguli = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_frontalis_inferior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_frontalis_medius = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_frontalis_superior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_parahippocampalis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_postcentralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_precentralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
sulcus_parietooccipitalis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
hippocampus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
sulcus_precentralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
sulcus_centralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
sulcus_postcentralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_supramarginalis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_temporalis_superior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_temporalis_media = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
gyrus_temporalis_inferior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
hypothalamus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
infundibulum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
lobus_cerebelli_anterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
lobus_cerebelli_posterior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
medulla_oblongata = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nervus_fascialis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nervus_opticus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nervus_trigeminus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nervus_trochlearis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nervus_vestibulocochlearis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nucleus_caudatus_cauda = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nucleus_caudatus_corpus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nucleus_caudatus_caput = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nucleus_ruber = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
nucleus_olivaris = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
pedunculus_cerebellaris_inferior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
pedunculus_cerebellaris_medius = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
pedunculus_cerebellaris_superior = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')


Ventriculus_lateralis = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
cerebellum = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
pons = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
tractus_opticus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
tentorium_cerebelli = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
sinus_transversus = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsFiducialNode', ' ')
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
gyrus_temporalis_transversus.AddControlPoint(-51.313,-18.486,7.458)
gyrus_angularis.AddControlPoint(-39.391,-69.268,46.773)
gyrus_cinguli.AddControlPoint(-5.245,-4.321,35.217)
gyrus_frontalis_inferior.AddControlPoint(-51.080,-1.339,25.231)
gyrus_frontalis_medius.AddControlPoint(-32.673,11.790,48.564)
gyrus_frontalis_superior.AddControlPoint(-12.732,34.249,48.564)
gyrus_parahippocampalis.AddControlPoint(-24.318,-23.765,-21.301)
gyrus_postcentralis.AddControlPoint(-57.458,-32.516,39.861)
gyrus_precentralis.AddControlPoint(-45.376,-25.636,53.236)
sulcus_parietooccipitalis.AddControlPoint(-8.986,-82.441,32.071)
hippocampus.AddControlPoint(-23.944,-14.091,-18.506)
sulcus_precentralis.AddControlPoint(-45.376,-17.422,47.042)
sulcus_centralis.AddControlPoint(-51.615,-29.405,49.985)
sulcus_postcentralis.AddControlPoint(-58.688,-39.187,40.463)
gyrus_supramarginalis.AddControlPoint(-60.547,-40.301,26.786)
gyrus_temporalis_superior.AddControlPoint(-61.047,-38.165,13.463)
gyrus_temporalis_media.AddControlPoint(-62.110,-26.572,-9.658)
gyrus_temporalis_inferior.AddControlPoint(-60.748,-43.785,-14.662)
hypothalamus.AddControlPoint(0.080,0.211,-11.460)
infundibulum.AddControlPoint(0.580,1.823,-15.124)
lobus_cerebelli_anterior.AddControlPoint(10.973,-53.935,-16.900)
lobus_cerebelli_posterior.AddControlPoint(19.782,-75.532,-37.940)
medulla_oblongata.AddControlPoint(1.030,-40.093,-52.135)
nervus_fascialis.AddControlPoint(17.827,-28.288,-35.711)
nervus_opticus.AddControlPoint(21.252,32.909,-19.435)
nervus_trigeminus.AddControlPoint(-17.3793,-24.3338,-25.2110)
nervus_trochlearis.AddControlPoint(11.2952,-36.2650,-10.1671)
nervus_vestibulocochlearis.AddControlPoint(20.1049,-30.4617,-36.2110)
nucleus_caudatus_cauda.AddControlPoint(25.532,-36.829,6.423)
nucleus_caudatus_corpus.AddControlPoint(-16.076,3.638,16.684)
nucleus_caudatus_caput.AddControlPoint( -9.950,9.921,4.173)
nucleus_ruber.AddControlPoint(-5.604,-19.104,-10.645)
nucleus_olivaris.AddControlPoint(5.090,-37.300,-54.174)
pedunculus_cerebellaris_inferior.AddControlPoint(9.747,-42.201,-38.788)
pedunculus_cerebellaris_medius.AddControlPoint(16.123,-34.786,-34.702)
pedunculus_cerebellaris_superior.AddControlPoint(-4.838,-41.456,-25.656)


Ventriculus_lateralis.AddControlPoint(9, -11.4, 23)
cerebellum.AddControlPoint(0.5339,-54.6794,-27.6747)
pons.AddControlPoint(0.0339,-25.9000,-27.6748)
tractus_opticus.AddControlPoint(-9.5054,-3.8966,-9.1747)
tentorium_cerebelli.AddControlPoint(-9.5054, -63.7734,-9.2014)
sinus_transversus.AddControlPoint(-15.9745,-90.0629,-32.9464)
#29-04-2023
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
    gyrus_temporalis_transversus: 'Gyrus temporalis transversus',
    gyrus_angularis: 'Gyrus angularis',
    gyrus_cinguli: 'Gyrus cinguli',
    gyrus_frontalis_inferior: 'Gyrus frontalis inferior',
    gyrus_frontalis_medius: 'Gyrus frontalis medius',
    gyrus_frontalis_superior: 'Gyrus frontalis superior',
    gyrus_parahippocampalis: 'Gyrus parahippocampalis',
    gyrus_postcentralis: 'Gyrus postcentralis',
    gyrus_precentralis: 'Gyrus precentralis',
    sulcus_parietooccipitalis: 'Sulcus parietooccipitalis',
    hippocampus: 'Hippocampus',
    sulcus_precentralis: 'Sulcus precentralis',
    sulcus_centralis: 'Sulcus centralis',
    sulcus_postcentralis: 'Sulcus postcentralis',
    gyrus_supramarginalis: 'Gyrus supramarginalis',
    gyrus_temporalis_superior: 'Gyrus temporalis superior',
    gyrus_temporalis_media: 'Gyrus temporalis media',
    gyrus_temporalis_inferior: 'Gyrus temporalis inferior',
    hypothalamus: 'Hypothalamus',
    infundibulum: 'Infundibulum',
    lobus_cerebelli_anterior: 'Lobus cerebelli anterior',
    lobus_cerebelli_posterior: 'Lobus cerebelli posterior',
    medulla_oblongata: 'Medulla oblongata',
    nervus_fascialis: 'Nervus fascialis',
    nervus_opticus: 'Nervus opticus',
    nervus_trigeminus: 'Nervus trigeminus',
    nervus_trochlearis: 'Nervus trochlearis',
    nervus_vestibulocochlearis: 'Nervus vestibulocochlearis',
    nucleus_caudatus_cauda: 'Nucleus caudatus cauda',
    nucleus_caudatus_corpus: 'Nucleus caudatus corpus',
    nucleus_caudatus_caput: 'Nucleus caudatus caput',
    nucleus_ruber: 'Nucleus ruber',
    nucleus_olivaris: 'Nucleus olivaris eller Oliva',
    pedunculus_cerebellaris_inferior: 'Pedunculus cerebellaris inferior',
    pedunculus_cerebellaris_medius: 'Pedunculus cerebellaris medius',
    pedunculus_cerebellaris_superior: 'Pedunculus cerebellaris superior',


    Ventriculus_lateralis: 'Ventriculus Lateralis',
    cerebellum: 'Cerebellum',
    pons: 'Pons',
    tractus_opticus: 'Tractus Opticus',
    tentorium_cerebelli: 'Tentorium Cerebelli',
    sinus_transversus: 'Sinus transversus',
    putamen: 'Putamen',
    thalamus: 'Thalamus',
    ventriculus_quartus: 'Ventriculus quartus'
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
                        hypothalamus,
                        infundibulum,
                        lobus_cerebelli_anterior,
                        lobus_cerebelli_posterior,
                        medulla_oblongata,
                        nervus_fascialis,
                        nervus_opticus,
                        nervus_trigeminus,
                        nervus_trochlearis,
                        nervus_vestibulocochlearis,
                        nucleus_caudatus_cauda,
                        nucleus_caudatus_corpus,
                        nucleus_caudatus_caput,


                        Ventriculus_lateralis,
                        cerebellum,
                        pons,
                        tractus_opticus,
                        tentorium_cerebelli,
                        sinus_transversus,
                        putamen,
                        thalamus,
                        ventriculus_quartus]

exvivo_allviews_list = [capsula_extrema,
                       capsula_externa,
                       corpus_mamillare,
                       cortex_orbitofrontalis,
                       crus_cerebri,
                       globus_pallidus_externa,
                       globus_pallidus_interna,
                       gyrus_angularis,
                       gyrus_cinguli,
                       gyrus_frontalis_inferior,
                       gyrus_frontalis_medius,
                       gyrus_frontalis_superior,
                       gyrus_parahippocampalis,
                       gyrus_postcentralis,
                       gyrus_precentralis,
                       sulcus_parietooccipitalis,
                       sulcus_precentralis,
                       sulcus_centralis,
                       sulcus_postcentralis,
                       gyrus_supramarginalis,
                       gyrus_temporalis_superior,
                       gyrus_temporalis_media,
                       gyrus_temporalis_inferior,
                       nucleus_olivaris,
                       pedunculus_cerebellaris_inferior,
                       pedunculus_cerebellaris_medius,
                       pedunculus_cerebellaris_superior]

bigbrain_allviews_list = [amygdala,
                         hippocampus,
                         corpus_geniculatum_laterale,
                         corpus_geniculatum_mediale,
                         gyrus_temporalis_transversus,
                         nucleus_ruber]

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
