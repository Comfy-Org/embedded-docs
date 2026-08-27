# Enregistrer les poids LoRA

Le nœud SaveLoRA enregistre un modèle LoRA (adaptation de bas rang) dans un fichier. Il prend un modèle LoRA en entrée et l'écrit dans un fichier `.safetensors` dans le répertoire de sortie. Vous pouvez spécifier un préfixe de nom de fichier et un nombre d'étapes facultatif à inclure dans le nom final du fichier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `lora` | Le modèle LoRA à enregistrer. N'utilisez pas le modèle avec des couches LoRA. | LORA_MODEL | Oui | N/A |
| `prefix` | Le préfixe à utiliser pour le fichier LoRA enregistré (par défaut : « loras/ComfyUI_trained_lora »). | STRING | Oui | N/A |
| `steps` | Facultatif : le nombre d'étapes pendant lesquelles le LoRA a été entraîné, utilisé pour nommer le fichier enregistré. | INT | Non | N/A |

**Remarque :** L'entrée `lora` doit être un modèle LoRA pur. Ne fournissez pas un modèle de base auquel des couches LoRA ont été appliquées.

**Remarque :** Le fichier est enregistré dans le répertoire de sortie de ComfyUI avec une extension `.safetensors`. Le nom du fichier est construit à partir du `prefix` et d'un compteur complété par des zéros (5 chiffres) pour éviter d'écraser les fichiers existants. Lorsque `steps` est fourni, le nombre d'étapes est également inclus dans le nom du fichier (par exemple, `1000_steps` pour 1000 étapes).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *None* | Ce nœud ne produit aucune donnée pour le flux de travail. C'est un nœud de sortie qui enregistre un fichier sur le disque. | N/A |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/fr.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
