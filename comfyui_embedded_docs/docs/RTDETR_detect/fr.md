# Détection RT-DETR

Le nœud RT-DETR Detect effectue la détection d'objets sur des images d'entrée à l'aide d'un modèle RT-DETR. Il identifie les objets, dessine des boîtes englobantes autour d'eux et les étiquette selon les classes du jeu de données COCO. Vous pouvez filtrer les résultats par score de confiance, classe d'objet et limiter le nombre total de détections.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle RT-DETR utilisé pour la détection d'objets. | MODEL | Oui | N/A |
| `image` | La ou les images d'entrée dans lesquelles détecter des objets. Le nœud traite les images par lots allant jusqu'à 32. | IMAGE | Oui | N/A |
| `threshold` | Le score de confiance minimum qu'une détection doit avoir pour être incluse dans les résultats (par défaut : 0,5). | FLOAT | Non | N/A |
| `class_name` | Filtre les détections par classe. Définir sur 'all' pour désactiver le filtrage (par défaut : "all"). | COMBO | Non | `"all"`<br>`"person"`<br>`"bicycle"`<br>`"car"`<br>`"motorcycle"`<br>`"airplane"`<br>`"bus"`<br>`"train"`<br>`"truck"`<br>`"boat"`<br>`"traffic light"`<br>`"fire hydrant"`<br>`"stop sign"`<br>`"parking meter"`<br>`"bench"`<br>`"bird"`<br>`"cat"`<br>`"dog"`<br>`"horse"`<br>`"sheep"`<br>`"cow"`<br>`"elephant"`<br>`"bear"`<br>`"zebra"`<br>`"giraffe"`<br>`"backpack"`<br>`"umbrella"`<br>`"handbag"`<br>`"tie"`<br>`"suitcase"`<br>`"frisbee"`<br>`"skis"`<br>`"snowboard"`<br>`"sports ball"`<br>`"kite"`<br>`"baseball bat"`<br>`"baseball glove"`<br>`"skateboard"`<br>`"surfboard"`<br>`"tennis racket"`<br>`"bottle"`<br>`"wine glass"`<br>`"cup"`<br>`"fork"`<br>`"knife"`<br>`"spoon"`<br>`"bowl"`<br>`"banana"`<br>`"apple"`<br>`"sandwich"`<br>`"orange"`<br>`"broccoli"`<br>`"carrot"`<br>`"hot dog"`<br>`"pizza"`<br>`"donut"`<br>`"cake"`<br>`"chair"`<br>`"couch"`<br>`"potted plant"`<br>`"bed"`<br>`"dining table"`<br>`"toilet"`<br>`"tv"`<br>`"laptop"`<br>`"mouse"`<br>`"remote"`<br>`"keyboard"`<br>`"cell phone"`<br>`"microwave"`<br>`"oven"`<br>`"toaster"`<br>`"sink"`<br>`"refrigerator"`<br>`"book"`<br>`"clock"`<br>`"vase"`<br>`"scissors"`<br>`"teddy bear"`<br>`"hair drier"`<br>`"toothbrush"` |
| `max_detections` | Nombre maximum de détections à retourner par image. Dans l'ordre décroissant du score de confiance (par défaut : 100). | INT | Non | N/A |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `bboxes` | Une liste de boîtes englobantes pour chaque image d'entrée. Chaque boîte contient les coordonnées (x, y, largeur, hauteur), une étiquette de classe et un score de confiance. | BOUNDINGBOX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RTDETR_detect/fr.md)

---
**Source fingerprint (SHA-256):** `0c32aa9e17b8ea81e52cb45df2a40f7c1faeb39fdf18dfc643d1d31ed0bfdefd`
