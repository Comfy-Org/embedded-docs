Le nœud `Sauvegarder Point de Contrôle` est conçu pour sauvegarder un modèle Stable Diffusion complet (y compris les composants UNet, CLIP et VAE) dans un fichier de point de contrôle au format **.safetensors**.

Ce nœud est principalement utilisé dans les flux de travail de fusion de modèles. Après avoir créé un nouveau modèle fusionné via des nœuds comme `ModelMergeSimple`, `ModelMergeBlocks`, etc., vous pouvez utiliser ce nœud pour sauvegarder le résultat comme un fichier de point de contrôle réutilisable.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|----------------|-------------|
| `modèle` | MODEL | Représente le modèle principal dont l'état doit être sauvegardé. Il est essentiel pour capturer l'état actuel du modèle pour une restauration ou une analyse future. |
| `clip` | CLIP | Les paramètres du modèle CLIP associé au modèle principal, permettant de sauvegarder son état aux côtés du modèle principal. |
| `vae` | VAE | Les paramètres du modèle Autoencodeur Variationnel (VAE), permettant de sauvegarder son état aux côtés du modèle principal et du CLIP pour une utilisation ou une analyse future. |
| `préfixe_nom_fichier` | STRING | Spécifie le préfixe pour le nom du fichier du point de contrôle à sauvegarder. |

De plus, le nœud possède deux entrées cachées pour les métadonnées :

**prompt (PROMPT)** : Informations sur le flux de travail
**extra_pnginfo (EXTRA_PNGINFO)** : Informations PNG supplémentaires

## Sorties

Ce nœud produira un fichier de point de contrôle, et le chemin de sortie correspondant est le répertoire `output/checkpoints/`

## Compatibilité des Architectures

- Actuellement entièrement supportées : SDXL, SD3, SVD et autres architectures principales, voir le [code source](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- Support basique : Les autres architectures peuvent être sauvegardées mais sans informations de métadonnées standardisées

## Liens Connexes

Code source associé : [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)
