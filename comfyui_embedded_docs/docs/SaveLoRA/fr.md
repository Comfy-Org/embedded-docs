# Enregistrer les poids LoRA

Le nœud SaveLoRA enregistre un modèle LoRA (Low-Rank Adaptation) dans un fichier. Il écrit le modèle LoRA sous forme de fichier `.safetensors` dans le répertoire de sortie. Vous pouvez spécifier un préfixe de nom de fichier et un nombre d'étapes facultatif ; lorsqu'il est fourni, le nombre d'étapes est inclus dans le nom du fichier enregistré.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `lora` | Le modèle LoRA à enregistrer. N'utilisez pas le modèle avec des couches LoRA. | LORA_MODEL | Oui | N/A |
| `prefix` | Le préfixe à utiliser pour le fichier LoRA enregistré (par défaut : "loras/ComfyUI_trained_lora"). | STRING | Oui | N/A |
| `steps` | Facultatif : Le nombre d'étapes d'entraînement du LoRA, utilisé pour nommer le fichier enregistré. | INT | Non | N/A |

**Remarque :** L'entrée `lora` doit être un modèle LoRA pur. Ne fournissez pas un modèle de base auquel des couches LoRA ont été appliquées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| *None* | Ce nœud ne renvoie aucune donnée au workflow. C'est un nœud de sortie qui enregistre un fichier sur le disque. | N/A |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/fr.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
