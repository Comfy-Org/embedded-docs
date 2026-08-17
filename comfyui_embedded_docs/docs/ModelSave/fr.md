# ModèleEnregistrer

Le nœud ModelSave enregistre les modèles entraînés ou modifiés sur le stockage de votre ordinateur. Il prend un modèle en entrée et l'écrit dans un fichier de points de contrôle safetensors dans le dossier de sortie, en utilisant le préfixe de nom de fichier que vous spécifiez. Les informations de prompt du workflow et les métadonnées sont intégrées dans le fichier enregistré lorsqu'elles sont disponibles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à enregistrer sur le disque | MODEL | Oui | - |
| `filename_prefix` | Le préfixe du nom de fichier et du chemin pour le fichier de modèle enregistré (par défaut : "diffusion_models/ComfyUI"). Un compteur est ajouté au nom lors de l'enregistrement (par exemple, `ComfyUI_00000_.safetensors`). | STRING | Oui | - |
| `prompt` | Informations de prompt du workflow (fournies automatiquement) | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées supplémentaires du workflow (fournies automatiquement) | EXTRA_PNGINFO | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *Aucun* | Ce nœud ne renvoie aucune valeur de sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/fr.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
