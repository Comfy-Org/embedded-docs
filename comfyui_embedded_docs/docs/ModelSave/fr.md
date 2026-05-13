> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/fr.md)

Le nœud ModelSave enregistre les modèles entraînés ou modifiés sur le stockage de votre ordinateur. Il prend un modèle en entrée et l'écrit dans un fichier avec le nom de fichier que vous spécifiez. Cela vous permet de conserver votre travail et de réutiliser les modèles dans de futurs projets.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle à enregistrer sur le disque |
| `préfixe_fichier` | STRING | Oui | - | Le préfixe du nom de fichier et du chemin pour le fichier de modèle enregistré (par défaut : "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | Non | - | Informations sur l'invite du workflow (fournies automatiquement) |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Métadonnées supplémentaires du workflow (fournies automatiquement) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| *Aucun* | - | Ce nœud ne renvoie aucune valeur de sortie |

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
