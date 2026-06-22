# Sauvegarder Point de Contrôle

Le nœud `Save Checkpoint` est conçu pour sauvegarder un modèle Stable Diffusion complet (incluant les composants UNet, CLIP et VAE) sous la forme d'un fichier de point de contrôle au format **.safetensors**.

Le nœud Save Checkpoint est principalement utilisé dans les workflows de fusion de modèles. Après avoir créé un nouveau modèle fusionné via des nœuds tels que `ModelMergeSimple`, `ModelMergeBlocks`, etc., vous pouvez utiliser ce nœud pour enregistrer le résultat sous la forme d'un fichier de point de contrôle réutilisable.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le paramètre model représente le modèle principal dont l'état doit être sauvegardé. Il est essentiel pour capturer l'état actuel du modèle en vue d'une restauration ou d'une analyse ultérieure. | MODEL |
| `clip` | Le paramètre clip est destiné au modèle CLIP associé au modèle principal, permettant de sauvegarder son état en même temps que le modèle principal. | CLIP |
| `vae` | Le paramètre vae est destiné au modèle d'autoencodeur variationnel (VAE), permettant de sauvegarder son état pour une utilisation ou une analyse future, en même temps que le modèle principal et le CLIP. | VAE |
| `préfixe_nom_fichier` | Ce paramètre spécifie le préfixe du nom de fichier sous lequel le point de contrôle sera sauvegardé. | STRING |

De plus, le nœud dispose de deux entrées cachées pour les métadonnées :

**prompt (PROMPT)** : Informations sur le prompt du workflow
**extra_pnginfo (EXTRA_PNGINFO)** : Informations PNG supplémentaires

## Sorties

Ce nœud produira un fichier de point de contrôle, et le chemin du fichier de sortie correspondant est le répertoire `output/checkpoints/`

## Compatibilité d'architecture

- Actuellement entièrement pris en charge : SDXL, SD3, SVD et autres architectures principales, voir le [code source](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- Prise en charge de base : Les autres architectures peuvent être sauvegardées mais sans informations de métadonnées standardisées

## Liens connexes

Code source associé : [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointSave/fr.md)
