Ce nœud se spécialise dans l'affinage de l'encodage des entrées textuelles en utilisant les modèles CLIP, améliorant le conditionnement pour les tâches génératives en incorporant des scores esthétiques et des dimensions.

## Types d'entrée de CLIPTextEncodeSDXLRefiner

| Paramètre | Comfy dtype | Description |
| --- | --- | --- |
| `clip` | `CLIP` | Une instance du modèle CLIP utilisée pour la tokenisation et l'encodage du texte, centrale pour générer le conditionnement. |
| `ascore` | `FLOAT` | Le paramètre de score esthétique influence la sortie de conditionnement en fournissant une mesure de la qualité esthétique. |
| `width` | `INT` | Spécifie la largeur du conditionnement de sortie, affectant les dimensions du contenu généré. |
| `height` | `INT` | Détermine la hauteur du conditionnement de sortie, influençant les dimensions du contenu généré. |
| `text` | `STRING` | L'entrée textuelle à encoder, servant de descripteur de contenu principal pour le conditionnement. |

## Types de sortie de CLIPTextEncodeSDXLRefiner

| Paramètre | Comfy dtype | Description |
| --- | --- | --- |
| `conditioning` | `CONDITIONING` | La sortie de conditionnement affinée, enrichie de scores esthétiques et de dimensions pour une génération de contenu améliorée. |
