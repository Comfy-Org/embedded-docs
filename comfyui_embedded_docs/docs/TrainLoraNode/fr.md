> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/fr.md)

Le nœud TrainLoraNode crée et entraîne un modèle LoRA (Adaptation de Bas Rang) sur un modèle de diffusion en utilisant des latents et des données de conditionnement fournis. Il permet d'affiner un modèle avec des paramètres d'entraînement personnalisés, des optimiseurs et des fonctions de perte. Le nœud produit les poids LoRA entraînés, un historique des pertes et le nombre total d'étapes d'entraînement effectuées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle sur lequel entraîner le LoRA. |
| `latents` | LATENT | Oui | - | Les latents à utiliser pour l'entraînement, servant de jeu de données/d'entrée pour le modèle. |
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif à utiliser pour l'entraînement. |
| `batch_size` | INT | Oui | 1-10000 | La taille du lot à utiliser pour l'entraînement (par défaut : 1). |
| `grad_accumulation_steps` | INT | Oui | 1-1024 | Le nombre d'étapes d'accumulation de gradient à utiliser pour l'entraînement (par défaut : 1). |
| `steps` | INT | Oui | 1-100000 | Le nombre d'étapes pour lesquelles entraîner le LoRA (par défaut : 16). |
| `learning_rate` | FLOAT | Oui | 0.0000001-1.0 | Le taux d'apprentissage à utiliser pour l'entraînement (par défaut : 0.0005). |
| `rank` | INT | Oui | 1-128 | Le rang des couches LoRA (par défaut : 8). |
| `optimizer` | COMBO | Oui | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" | L'optimiseur à utiliser pour l'entraînement (par défaut : "AdamW"). |
| `loss_function` | COMBO | Oui | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" | La fonction de perte à utiliser pour l'entraînement (par défaut : "MSE"). |
| `seed` | INT | Oui | 0-18446744073709551615 | La graine à utiliser pour l'entraînement (utilisée dans le générateur pour l'initialisation des poids LoRA et l'échantillonnage du bruit) (par défaut : 0). |
| `training_dtype` | COMBO | Oui | "bf16"<br>"fp32"<br>"none" | Le type de données à utiliser pour l'entraînement. 'none' préserve le type de données de calcul natif du modèle au lieu de le remplacer. Pour les modèles fp16, GradScaler est automatiquement activé (par défaut : "bf16"). |
| `lora_dtype` | COMBO | Oui | "bf16"<br>"fp32" | Le type de données à utiliser pour le LoRA (par défaut : "bf16"). |
| `quantized_backward` | BOOLEAN | Oui | - | Lors de l'utilisation de training_dtype 'none' et de l'entraînement sur un modèle quantifié, effectue la rétropropagation avec multiplication matricielle quantifiée lorsqu'activé (par défaut : False). |
| `algorithm` | COMBO | Oui | Plusieurs options disponibles | L'algorithme à utiliser pour l'entraînement. |
| `gradient_checkpointing` | BOOLEAN | Oui | - | Utiliser le point de contrôle de gradient pour l'entraînement (par défaut : True). |
| `checkpoint_depth` | INT | Oui | 1-5 | Niveau de profondeur pour le point de contrôle de gradient (par défaut : 1). |
| `offloading` | BOOLEAN | Oui | - | Décharger les poids du modèle vers le CPU pendant l'entraînement pour économiser la mémoire GPU (par défaut : False). |
| `existing_lora` | COMBO | Oui | Plusieurs options disponibles | Le LoRA existant auquel ajouter. Définir sur None pour un nouveau LoRA (par défaut : "[None]"). |
| `bucket_mode` | BOOLEAN | Oui | - | Activer le mode de compartiment de résolution. Lorsqu'activé, attend des latents pré-compartimentés du nœud ResolutionBucket (par défaut : False). |
| `bypass_mode` | BOOLEAN | Oui | - | Activer le mode de contournement pour l'entraînement. Lorsqu'activé, les adaptateurs sont appliqués via des crochets avant au lieu de la modification des poids. Utile pour les modèles quantifiés où les poids ne peuvent pas être directement modifiés (par défaut : False). |

**Remarque :** Le nombre d'entrées de conditionnement positif doit correspondre au nombre d'images latentes. Si un seul conditionnement positif est fourni avec plusieurs images, il sera automatiquement répété pour toutes les images.

**Remarque sur `training_dtype` :** Lorsqu'il est défini sur "none", le type de données de calcul natif du modèle est préservé. Pour les modèles fp16, GradScaler est automatiquement activé pour éviter un sous-dépassement lors du calcul du gradient. Si `fp16_accumulation` est également activé (via les indicateurs `--fast`), cette combinaison peut être numériquement instable et peut provoquer des valeurs NaN.

**Remarque sur `quantized_backward` :** Ce paramètre n'est pertinent que lorsque `training_dtype` est défini sur "none" et que le modèle est un modèle quantifié. Il active la multiplication matricielle quantifiée pendant la passe arrière.

**Remarque sur `bypass_mode` :** Lorsqu'il est activé, les adaptateurs sont appliqués via des crochets avant au lieu de modifier directement les poids du modèle. Ceci est particulièrement utile pour les modèles quantifiés où les poids ne peuvent pas être directement modifiés.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `lora` | LORA_MODEL | Les poids LoRA entraînés qui peuvent être sauvegardés ou appliqués à d'autres modèles. |
| `loss_map` | LOSS_MAP | Un dictionnaire contenant les valeurs de perte d'entraînement au fil du temps. |
| `steps` | INT | Le nombre total d'étapes d'entraînement effectuées (y compris les étapes précédentes d'un LoRA existant). |