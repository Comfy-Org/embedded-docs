# Enregistrer les poids LoRA

Le nœud SaveLoRA enregistre un modèle LoRA (Low-Rank Adaptation) dans un fichier. Il prend un modèle LoRA en entrée et l'écrit dans un fichier `.safetensors` dans le répertoire de sortie. Vous pouvez spécifier un préfixe de nom de fichier et un nombre d'étapes facultatif à inclure dans le nom final du fichier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `lora` | Le modèle LoRA à enregistrer. N'utilisez pas le modèle avec des couches LoRA. | LORA_MODEL | Oui | N/A |
| `prefix` | Le préfixe à utiliser pour le fichier LoRA enregistré (par défaut : "loras/ComfyUI_trained_lora"). | STRING | Oui | N/A |
| `steps` | Facultatif : Le nombre d'étapes pour lequel le LoRA a été entraîné, utilisé pour nommer le fichier enregistré. | INT | Non | N/A |

**Remarque :** L'entrée `lora` doit être un modèle LoRA pur. Ne fournissez pas un modèle de base auquel des couches LoRA ont été appliquées.


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *None* | Ce nœud ne produit aucune donnée vers le workflow. Il s'agit d'un nœud de sortie qui enregistre un fichier sur le disque. | N/A |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/fr.md)

---
**Source fingerprint (SHA-256):** `e68a449d741c908f23fc1585d848254d78c310ad19efbd139c33c9ddef3145c7`
