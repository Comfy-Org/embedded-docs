Le nœud ModelSave enregistre les modèles entraînés ou modifiés sur le stockage de votre ordinateur. Il prend un modèle en entrée et l'écrit dans un fichier avec le nom de fichier que vous spécifiez. Cela vous permet de conserver votre travail et de réutiliser les modèles dans de futurs projets.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à enregistrer sur le disque | MODEL | Oui | - |
| `préfixe_fichier` | Le préfixe du nom de fichier et du chemin pour le fichier de modèle enregistré (par défaut : "diffusion_models/ComfyUI") | STRING | Oui | - |
| `prompt` | Informations sur l'invite du workflow (fournies automatiquement) | PROMPT | Non | - |
| `extra_pnginfo` | Métadonnées supplémentaires du workflow (fournies automatiquement) | EXTRA_PNGINFO | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| *Aucun* | Ce nœud ne renvoie aucune valeur de sortie | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/fr.md)

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
