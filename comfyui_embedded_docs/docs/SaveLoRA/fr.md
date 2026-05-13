> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/fr.md)

Le nœud SaveLoRA enregistre un modèle LoRA (Low-Rank Adaptation) dans un fichier. Il prend un modèle LoRA en entrée et l'écrit dans un fichier `.safetensors` dans le répertoire de sortie. Vous pouvez spécifier un préfixe de nom de fichier et un nombre d'étapes facultatif à inclure dans le nom final du fichier.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `lora` | LORA_MODEL | Oui | N/A | Le modèle LoRA à enregistrer. N'utilisez pas le modèle avec des couches LoRA. |
| `prefix` | STRING | Oui | N/A | Le préfixe à utiliser pour le fichier LoRA enregistré (par défaut : "loras/ComfyUI_trained_lora"). |
| `steps` | INT | Non | N/A | Facultatif : Le nombre d'étapes pour lequel le LoRA a été entraîné, utilisé pour nommer le fichier enregistré. |

**Remarque :** L'entrée `lora` doit être un modèle LoRA pur. Ne fournissez pas un modèle de base auquel des couches LoRA ont été appliquées.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| *Aucun* | N/A | Ce nœud ne produit aucune donnée vers le workflow. Il s'agit d'un nœud de sortie qui enregistre un fichier sur le disque. |

---
**Source fingerprint (SHA-256):** `e68a449d741c908f23fc1585d848254d78c310ad19efbd139c33c9ddef3145c7`
