Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/en.md)

Le nœud SaveLoRA enregistre les modèles LoRA (Low-Rank Adaptation) dans votre répertoire de sortie. Il prend un modèle LoRA en entrée et crée un fichier safetensors avec un nom de fichier généré automatiquement. Vous pouvez personnaliser le préfixe du nom de fichier et inclure éventuellement le nombre d'étapes d'entraînement dans le nom pour une meilleure organisation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `lora` | Le modèle LoRA à enregistrer. N'utilisez pas le modèle avec des couches LoRA. | LORA_MODEL | Oui | - |
| `prefix` | Le préfixe à utiliser pour le fichier LoRA enregistré (par défaut : "loras/ComfyUI_trained_lora"). | STRING | Oui | - |
| `steps` | Optionnel : Le nombre d'étapes pour lequel le LoRA a été entraîné, utilisé pour nommer le fichier enregistré. | INT | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *Aucun* | Ce nœud ne renvoie aucune sortie mais enregistre le modèle LoRA dans le répertoire de sortie. | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/fr.md)

---
**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`
