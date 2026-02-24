> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/fr.md)

Ce nœud utilise le modèle Kling 3.0 pour générer une vidéo. Il crée la vidéo à partir d'une description textuelle, d'une durée spécifiée et de deux images fournies : une image de départ et une image de fin. Le nœud peut également générer une bande-son accompagnant la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | La description textuelle qui guide la génération de la vidéo. Doit contenir entre 1 et 2500 caractères. |
| `duration` | INT | Non | 3 à 15 | La durée de la vidéo en secondes (par défaut : 5). |
| `first_frame` | IMAGE | Oui | N/A | L'image de départ pour la vidéo. Doit mesurer au moins 300x300 pixels et avoir un rapport d'aspect compris entre 1:2,5 et 2,5:1. |
| `end_frame` | IMAGE | Oui | N/A | L'image de fin pour la vidéo. Doit mesurer au moins 300x300 pixels et avoir un rapport d'aspect compris entre 1:2,5 et 2,5:1. |
| `generate_audio` | BOOLEAN | Non | N/A | Contrôle si une bande-son doit être générée pour la vidéo (par défaut : True). |
| `model` | COMBO | Non | `"kling-v3"` | Modèle et paramètres de génération. La sélection de cette option révèle un paramètre imbriqué `resolution`. |
| `model.resolution` | COMBO | Non | `"1080p"`<br>`"720p"` | La résolution de la vidéo générée. Ce paramètre n'est disponible que lorsque `model` est défini sur `"kling-v3"`. |
| `seed` | INT | Non | 0 à 2147483647 | Un nombre utilisé pour contrôler si le nœud doit être réexécuté. Les résultats sont non déterministes quelle que soit la valeur du `seed` (par défaut : 0). |

**Note :** Les images `first_frame` et `end_frame` doivent respecter les exigences de taille minimale et de rapport d'aspect spécifiées pour que le nœud fonctionne correctement.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |
