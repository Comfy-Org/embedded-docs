> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/fr.md)

Le nœud TrainLoraNode crée et entraîne un modèle LoRA (Low-Rank Adaptation) sur un modèle de diffusion en utilisant des latents et des données de conditionnement fournies. Il vous permet de fine-tuner un modèle avec des paramètres d'entraînement, des optimiseurs et des fonctions de perte personnalisés. Le nœud retourne le modèle entraîné avec LoRA appliqué, les poids LoRA, les métriques de perte d'entraînement et le nombre total d'étapes d'entraînement effectuées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle sur lequel entraîner le LoRA. |
| `latents` | LATENT | Oui | - | Les latents à utiliser pour l'entraînement, servent de jeu de données/d'entrée du modèle. |
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif à utiliser pour l'entraînement. |
| `batch_size` | INT | Oui | 1-10000 | La taille de lot à utiliser pour l'entraînement (défaut : 1). |
| `grad_accumulation_steps` | INT | Oui | 1-1024 | Le nombre d'étapes d'accumulation de gradient à utiliser pour l'entraînement (défaut : 1). |
| `steps` | INT | Oui | 1-100000 | Le nombre d'étapes pour entraîner le LoRA (défaut : 16). |
| `learning_rate` | FLOAT | Oui | 0.0000001-1.0 | Le taux d'apprentissage à utiliser pour l'entraînement (défaut : 0.0005). |
| `rank` | INT | Oui | 1-128 | Le rang des couches LoRA (défaut : 8). |
| `optimizer` | COMBO | Oui | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | L'optimiseur à utiliser pour l'entraînement (défaut : "AdamW"). |
| `loss_function` | COMBO | Oui | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | La fonction de perte à utiliser pour l'entraînement (défaut : "MSE"). |
| `seed` | INT | Oui | 0-18446744073709551615 | La graine à utiliser pour l'entraînement (utilisée dans le générateur pour l'initialisation des poids LoRA et l'échantillonnage du bruit) (défaut : 0). |
| `training_dtype` | COMBO | Oui | "bf16"<br>"fp32" | Le type de données à utiliser pour l'entraînement (défaut : "bf16"). |
| `lora_dtype` | COMBO | Oui | "bf16"<br>"fp32" | Le type de données à utiliser pour le LoRA (défaut : "bf16"). |
| `algorithm` | COMBO | Oui | Options multiples disponibles | L'algorithme à utiliser pour l'entraînement. |
| `gradient_checkpointing` | BOOLEAN | Oui | - | Utiliser le gradient checkpointing pour l'entraînement (défaut : True). |
| `existing_lora` | COMBO | Oui | Options multiples disponibles | Le LoRA existant auquel s'ajouter. Définir sur None pour un nouveau LoRA (défaut : "[None]"). |

**Note :** Le nombre d'entrées de conditionnement positif doit correspondre au nombre d'images latentes. Si un seul conditionnement positif est fourni avec plusieurs images, il sera automatiquement répété pour toutes les images.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model_with_lora` | MODEL | Le modèle original avec le LoRA entraîné appliqué. |
| `lora` | LORA_MODEL | Les poids LoRA entraînés qui peuvent être sauvegardés ou appliqués à d'autres modèles. |
| `loss` | LOSS_MAP | Un dictionnaire contenant les valeurs de perte d'entraînement au fil du temps. |
| `steps` | INT | Le nombre total d'étapes d'entraînement effectuées (incluant toute étape précédente d'un LoRA existant). |
