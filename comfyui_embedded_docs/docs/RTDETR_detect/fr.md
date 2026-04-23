> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/fr.md)

Le nœud RT-DETR Detect effectue une détection d'objets sur les images d'entrée en utilisant un modèle RT-DETR. Il identifie les objets, dessine des boîtes englobantes autour d'eux et les étiquette selon les classes du jeu de données COCO. Vous pouvez filtrer les résultats par score de confiance, par classe d'objet et limiter le nombre total de détections.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | N/A | Le modèle RT-DETR utilisé pour la détection d'objets. |
| `image` | IMAGE | Oui | N/A | L'image ou les images d'entrée dans lesquelles détecter les objets. Le nœud traite les images par lots de jusqu'à 32. |
| `threshold` | FLOAT | Non | N/A | Le score de confiance minimum qu'une détection doit avoir pour être incluse dans les résultats (par défaut : 0.5). |
| `class_name` | COMBO | Non | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` | Filtre les détections par classe. Réglez sur 'all' pour désactiver le filtrage (par défaut : "all"). |
| `max_detections` | INT | Non | N/A | Nombre maximum de détections à retourner par image. Par ordre décroissant de score de confiance (par défaut : 100). |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `bboxes` | BOUNDINGBOX | Une liste de boîtes englobantes pour chaque image d'entrée. Chaque boîte contient des coordonnées (x, y, largeur, hauteur), un libellé de classe et un score de confiance. |