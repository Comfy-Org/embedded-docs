> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/fr.md)

Le nœud SaveLoRA enregistre les modèles LoRA (Low-Rank Adaptation) dans votre répertoire de sortie. Il prend un modèle LoRA en entrée et crée un fichier safetensors avec un nom de fichier généré automatiquement. Vous pouvez personnaliser le préfixe du nom de fichier et optionnellement inclure le nombre d'étapes d'entraînement dans le nom du fichier pour une meilleure organisation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `lora` | LORA_MODEL | Oui | - | Le modèle LoRA à sauvegarder. Ne pas utiliser le modèle avec les couches LoRA. |
| `prefix` | STRING | Oui | - | Le préfixe à utiliser pour le fichier LoRA sauvegardé (par défaut : "loras/ComfyUI_trained_lora"). |
| `steps` | INT | Non | - | Optionnel : Le nombre d'étapes pour lesquelles le LoRA a été entraîné, utilisé pour nommer le fichier sauvegardé. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| *Aucune* | - | Ce nœud ne retourne aucune sortie mais sauvegarde le modèle LoRA dans le répertoire de sortie. |
