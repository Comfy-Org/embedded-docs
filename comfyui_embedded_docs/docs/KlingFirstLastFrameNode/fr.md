# Kling 3.0 Première-Dernière-Image en Vidéo

Ce nœud utilise le modèle Kling 3.0 pour générer une vidéo. Il crée la vidéo à partir d'une invite textuelle, d'une durée spécifiée et de deux images fournies : une image de début et une image de fin. Le nœud peut également générer un fichier audio d'accompagnement pour la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | La description textuelle qui guide la génération de la vidéo. Doit contenir entre 1 et 2500 caractères. | STRING | Oui | N/A |
| `durée` | La durée de la vidéo en secondes (valeur par défaut : 5). | INT | Non | 3 à 15 |
| `première image` | L'image de départ de la vidéo. Doit mesurer au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1. | IMAGE | Oui | N/A |
| `dernière image` | L'image de fin de la vidéo. Doit mesurer au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2,5 et 2,5:1. | IMAGE | Oui | N/A |
| `générer l'audio` | Contrôle la génération d'un fichier audio pour la vidéo (valeur par défaut : True). | BOOLEAN | Non | N/A |
| `modèle` | Paramètres du modèle et de génération. La sélection de cette option révèle un paramètre `resolution` imbriqué. | COMBO | Non | `"kling-v3"` |
| `model.resolution` | La résolution de la vidéo générée. Ce paramètre n'est disponible que lorsque le `modèle` est défini sur `"kling-v3"` (valeur par défaut : `"1080p"`). | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `seed` | Un nombre utilisé pour contrôler la réexécution du nœud. Les résultats ne sont pas déterministes, quelle que soit la valeur de la graine (valeur par défaut : 0). | INT | Non | 0 à 2147483647 |

**Remarque :** Les images `first_frame` et `end_frame` doivent respecter les exigences de taille minimale et de rapport hauteur/largeur spécifiées pour que le nœud fonctionne correctement.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `5c904fec35b2bb41cf521263b1b06fd36ba227400b4cec24e79a4e80618e4bae`
