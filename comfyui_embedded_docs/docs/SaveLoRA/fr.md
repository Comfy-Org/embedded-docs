> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `lora` | MODEL | Oui | N/A | Le modèle LoRA à sauvegarder. Ne pas utiliser le modèle avec les couches LoRA appliquées. |
| `prefix` | STRING | Oui | N/A | Le préfixe à utiliser pour le fichier LoRA sauvegardé (par défaut : "loras/ComfyUI_trained_lora"). |
| `steps` | INT | Non | N/A | Optionnel : Le nombre d'étapes d'entraînement du LoRA, utilisé pour nommer le fichier sauvegardé. |

**Note :** L'entrée `lora` doit être un modèle LoRA pur. Ne fournissez pas un modèle de base auquel des couches LoRA ont été appliquées.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| *Aucune* | N/A | Ce nœud ne renvoie aucune donnée dans le flux de travail. C'est un nœud de sortie qui enregistre un fichier sur le disque. |
