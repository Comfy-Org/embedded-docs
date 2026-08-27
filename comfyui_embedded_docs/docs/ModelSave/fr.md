# ModèleEnregistrer

Le nœud ModelSave enregistre un modèle sur le stockage de votre ordinateur sous forme de fichier de point de contrôle `.safetensors`. Il prend un modèle en entrée et l'écrit dans le répertoire de sortie en utilisant le préfixe de nom de fichier que vous spécifiez. Lorsqu'elles sont disponibles, il intègre également les informations du prompt du workflow et des métadonnées supplémentaires dans le fichier enregistré.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à enregistrer sur le disque | MODEL | Oui | - |
| `préfixe_fichier` | Le préfixe du nom de fichier et du chemin pour le fichier de modèle enregistré (par défaut : "diffusion_models/ComfyUI") | STRING | Oui | - |
| `prompt` | Informations du prompt du workflow (fournies automatiquement) | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées supplémentaires du workflow (fournies automatiquement) | EXTRA_PNGINFO | Non | - |

Note : Le nom de fichier enregistré est construit à partir de la valeur `filename_prefix` suivie d'un compteur à cinq chiffres (par exemple, `diffusion_models/ComfyUI_00001_.safetensors`). Si un fichier portant le même préfixe existe déjà, le compteur est incrémenté afin que le nouveau fichier obtienne un nom unique. Lorsqu'elles sont disponibles, les informations du prompt du workflow, les métadonnées supplémentaires et les informations sur l'architecture du modèle sont intégrées dans le fichier enregistré.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *None* | Ce nœud ne retourne aucune valeur de sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/fr.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
