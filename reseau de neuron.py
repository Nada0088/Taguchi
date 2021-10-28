#mon reseau de neurone ase sur Faster RCNN
#Conguration du Model
model {
faster_rcnn {
num_classes : 7
image_resizer {
keep_aspect_ratio_resizer {
min_dimension : 300
max_dimension : 600
}
}
#inception v2 plus rapide il extrait depuis layer Mixed_4e avec strid= 16 pixels
#resize and crop maps a 14*14
feature_extractor {
type : 'faster_rcnn_inception_v2'

#denir à quel point on veux approfondir la convolution pour extraire les fonction-
nalités

rst_stage_features_stride : 16
}
rst_stage_anchor_generator {
grid_anchor_generator {
# la taille de l anchor de base
height : 256
width : 256
#C est le taux de sous-échantillonnage du réseau vgg16
height_stride : 16
width_stride : 16
#aspect_ratios c est largeurs sur hauteur
scales : [0.25, 0.5,0.75, 1.0, 1.5, 2.0]  
  aspect_ratios : [0.5, 1.0, 2.0, 2.5, 3.0]
}
}
#La régularisation du poids fournit une approche permettant de réduire
#la sur adaptation d un modèle du CNN sur les données d entraînement
#et d améliorer les performances du modèle sur de nouvelles données, telles que l
ensemble de tests de maintien
#la régularisation L2 regles logistiques et le model de réseaux de neurones
#Il existe deux paramètres de régularisation courants :L1 s appelle Lasso et L2 s
appelle Ridge
#Ils ont utilisé la perte L1 au lieu de la perte L2 car les valeurs de la tête de régression
prévue
#de la RPN ne sont pas bornées. La perte de régression est également appliquée aux
boîtes englobantes qui ont une étiquette positive
#Un modèle avec des poids élevés est plus complexe qu un modèle avec des poids
plus petits
rst_stage_box_predictor_conv_hyperparams {
op : CONV
regularizer {
l2_regularizer {
weight : 0.0005
}
}
#Les initialisations dénissent la manière de dénir les poids aléatoires initiaux
initializer {
#Le but de l'utilisation de la normale tronquée est de surmonter la saturation des
fonctions
#temporelles comme sigmoïde (où si la valeur est trop grande / petite, le neurone
arrête d'apprendre).
truncated_normal_initializer {
#Écart type des valeurs aléatoires à générer.
stddev : 0.01
}
}
}
#rst_stage_nms_score_threshold seuil de score pour la suppression non max pour
#le réseau de proposition de région (RPN). Cette valeur devrait être dans 0, 1
#car elle est appliquée directement après une transformation softmax.
#La valeur recommandée pour Faster R-CNN est 0.
rst_stage_nms_score_threshold : 0.0
rst_stage_nms_iou_threshold : 0.6
#nbr de box qui peut existe apr nms
rst_stage_max_proposals : 100

#Les modèles de détection dénissent généralement un poids de perte pour la clas-
sication et l objectivité.

#Cette fonction met à jour les poids de sorte que le rapport entre le poids de clas-
sication et le poids

#de localisation soit le rapport fourni. De manière arbitraire, le poids de localisation
est déni sur 1.0.
rst_stage_localization_loss_weight : 2.0
rst_stage_objectness_loss_weight : 1.0
#14*14 pour inception v2
initial_crop_size : 14
maxpool_kernel_size : 2
maxpool_stride : 2
#box predector pour les détecteurs d objets sont des classes
#qui prennent en entrée une carte de caractéristiques d image
#de haut niveau et produisent deux prédictions,
#1 un emplacement de case de codage tenseur et
#2 une classe de codage tenseur pour chaque case.
#Ces composants sont directement transmis aux fonctions de perte dans nos modèles
de détection.

#Ces modules sont séparés du modèle principal car les mêmes architectures de pré-
dicteurs de boîtes sont partagées entre plusieurs modèles.

#mask box predictor pour chaque ancre, une prédiction distincte est eectuée pour
chaque classe.
#Outre la prédiction de boîtes et de classes, cette classe permet également de prévoir
des masques
#et des points-clés dans des boîtes de détection. Actuellement, ce prédicteur de case
établit des prédictions par classe.
#c a d que chaque ancre fait une prédiction de boîte distincte pour chaque classe.
second_stage_box_predictor {
mask_rcnn_box_predictor {
use_dropout : true
dropout_keep_probability : 0.8
fc_hyperparams {
op : FC
regularizer {
l2_regularizer {
weight : 0.0
}
}
initializer {
variance_scaling_initializer {
factor : 1.0
uniform : true
mode : FAN_AVG
}
}
}
}
}
second_stage_post_processing {
batch_non_max_suppression {
score_threshold : 0.0
iou_threshold : 0.6
max_detections_per_class : 80
max_total_detections : 300
}
score_converter : SOFTMAX
}
second_stage_localization_loss_weight : 2.0
second_stage_classication_loss_weight : 1.0
}
}
# qui décide des paramètres a utiliser pour entraîner les paramètres du modèles
#(paramètres SGD, valeurs de prétraitement de l extracteur de caractéristiques).
train_cong {
batch_size : 1
optimizer {
momentum_optimizer : {
learning_rate : {
manual_step_learning_rate {
initial_learning_rate : 0.0003
schedule {
step : 50000
learning_rate : .00003
}
schedule {
step : 900000
learning_rate : .000003
}
}
}
momentum_optimizer_value : 0.9
}
use_moving_average : false
}
gradient_clipping_by_norm : 10.0
# chemin d'accès au point contrôle pré-existant
ne_tune_checkpoint : "/home/nada/Desktop/training/my_models/Faster_inc_v2
]
#valeur booléenne si false : le point de contrôle est celui d une classication sinon
detection.
from_detection_checkpoint : true
num_steps : 30000
}
#qui détermines quel ensemble de métriques seront rapporte pour l'évaluation.
eval_cong {

#le nombre de lots (batchs)(actuellement de taille 1) utilise pour un cycle d'évalua-
tion

#et correspond souvent a la taille totale du jeu de donnée d'évaluation
num_examples : 119
#limiter le processus de l evaluation a 20 evaluations
max_evals : 20
#les métriques a exécuter lors de l évaluation default pascalvoc
}
#data base de l apprentissage.
train_input_cong {
tf_record_input_reader {
input_path : "/home/nada/Desktop/training/my_models/Faster_inc_v2
]
}
label_map_path : "/home/nada/Desktop/training/my_models/Faster_inc_v2
]
}
#data base d évaluation.
eval_input_cong {
  tf_record_input_reader {
input_path : "/home/nada/Desktop/training/my_models/Faster_inc_v2
]
}
label_map_path : "/home/nada/Desktop/training/my_models/Faster_inc_v2
]
shue : false
num_readers : 1
}
  
