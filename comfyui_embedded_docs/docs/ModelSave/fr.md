# ModèleEnregistrer

Le nœud ModelSave enregistre un MODEL dans le stockage de votre ordinateur sous forme de fichier checkpoint `.safetensors`. Il écrit le fichier dans le répertoire de sortie de ComfyUI en utilisant le préfixe de nom de fichier que vous fournissez, et intègre les informations de prompt du workflow et les métadonnées du modèle dans le fichier enregistré lorsqu'elles sont disponibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à enregistrer sur le disque | MODEL | Oui | - |
| `filename_prefix` | Préfixe du nom de fichier et du chemin pour le fichier de modèle enregistré (par défaut : « diffusion_models/ComfyUI ») | STRING | Oui | - |
| `prompt` | Informations de prompt du workflow (fournies automatiquement) | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées de workflow supplémentaires (fournies automatiquement) | EXTRA_PNGINFO | Non | - |

Remarque : Le nom de fichier enregistré est construit à partir de la valeur `filename_prefix`, suivie d'un compteur à cinq chiffres (par exemple, `diffusion_models/ComfyUI_00001_.safetensors`). Si un fichier avec le même préfixe existe déjà, le compteur est incrémenté afin que le nouveau fichier obtienne un nom unique. Lorsqu'ils sont disponibles, le prompt du workflow, les métadonnées supplémentaires et les informations d'architecture du modèle (par exemple Stable Diffusion XL, SDXL Refiner, Stable Video Diffusion ou Stable Diffusion 3) sont intégrés dans le fichier enregistré. Si l'enregistrement des métadonnées est désactivé via les paramètres de ligne de commande de ComfyUI, le prompt et les métadonnées supplémentaires ne sont pas écrits dans le fichier.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *None* | Ce nœud ne renvoie aucune valeur de sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/fr.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
