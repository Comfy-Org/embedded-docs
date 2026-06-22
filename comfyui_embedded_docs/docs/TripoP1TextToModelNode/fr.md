# Tripo P1 : Texte vers Modèle

Voici la traduction en français de la documentation technique du nœud ComfyUI, en respectant les règles établies :

---

## Aperçu

Ce nœud génère un modèle 3D à partir d'une description textuelle en utilisant l'API Tripo P1. Il est optimisé pour créer des maillages low-poly prêts pour le jeu, avec une topologie stable, ce qui le rend adapté aux applications temps réel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | La description textuelle du modèle 3D que vous souhaitez générer. | STRING | Oui | Jusqu'à 1024 caractères |
| `invite négative` | Une description textuelle de ce que vous ne voulez pas voir dans le modèle généré. | STRING | Non | Jusqu'à 255 caractères |
| `mode de sortie` | Contrôle les paramètres de qualité et de texture du modèle de sortie. Ce paramètre est un dictionnaire avec les clés suivantes :<br><br>`texture_quality` : STRING, Plage : `"standard"`<br>`pbr` : BOOLEAN, défaut : True<br>`texture` : BOOLEAN, défaut : True<br>`subdivision` : INT, défaut : 0, Plage : 0 à 2<br>`texture_size` : INT, défaut : 2048, Plage : 512 à 4096 (doit être une puissance de 2)<br>`texture_format` : STRING, Plage : `"png"`<br>`texture_clean` : BOOLEAN, défaut : False<br>`texture_seamless` : BOOLEAN, défaut : False<br><br>Valeur par défaut : `{"texture_quality": "standard", "pbr": True, "texture": True, "subdivision": 0, "texture_size": 2048, "texture_format": "png", "texture_clean": False, "texture_seamless": False}` | DICT | Oui | Voir description |
| `graine d'image` | Une valeur de graine pour la génération d'image, utilisée pour contrôler l'aléatoire. Valeur par défaut : 42. | INT | Non |  |
| `limite de faces` | Le nombre maximum de faces pour le maillage généré. Une valeur de -1 signifie aucune limite. Valeur par défaut : -1. | INT | Non |  |
| `graine du modèle` | Une valeur de graine pour la génération du modèle, utilisée pour contrôler l'aléatoire. | INT | Non |  |
| `taille automatique` | Si activé, le nœud déterminera automatiquement la taille optimale du modèle. Valeur par défaut : False. | BOOLEAN | Non |  |
| `exporter UV` | Si activé, le modèle inclura des coordonnées UV pour le mappage de texture. Valeur par défaut : True. | BOOLEAN | Non |  |
| `compresser la géométrie` | Si activé, la géométrie sera compressée pour réduire la taille du fichier. Valeur par défaut : False. | BOOLEAN | Non |  |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `ID de tâche modèle` | Le chemin d'accès au fichier du modèle 3D généré (uniquement pour la rétrocompatibilité). | STRING |
| `GLB` | L'identifiant unique de la tâche pour la demande de génération du modèle. | MODEL_TASK_ID |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/fr.md)

---
**Source fingerprint (SHA-256):** `154e75209d65c823d5681b74cd12fe7b2ed37d7b94bf51cac86f343c68f85722`
