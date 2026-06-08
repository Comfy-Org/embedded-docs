Le nœud TrainLoraNode crée et entraîne un modèle LoRA (Adaptation de Bas Rang) sur un modèle de diffusion en utilisant des latents et des données de conditionnement fournis. Il permet d'affiner un modèle avec des paramètres d'entraînement personnalisés, des optimiseurs et des fonctions de perte. Le nœud produit les poids LoRA entraînés, une carte de l'historique des pertes et le nombre total d'étapes d'entraînement effectuées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle sur lequel entraîner le LoRA. | MODEL | Oui | - |
| `latents` | Les latents à utiliser pour l'entraînement, servant d'ensemble de données/d'entrée du modèle. | LATENT | Oui | - |
| `positif` | Le conditionnement positif à utiliser pour l'entraînement. | CONDITIONING | Oui | - |
| `taille_du_lot` | La taille du lot à utiliser pour l'entraînement (par défaut : 1). | INT | Oui | 1-10000 |
| `étapes_accumulation_gradient` | Le nombre d'étapes d'accumulation de gradient à utiliser pour l'entraînement (par défaut : 1). | INT | Oui | 1-1024 |
| `étapes` | Le nombre d'étapes pour lesquelles entraîner le LoRA (par défaut : 16). | INT | Oui | 1-100000 |
| `taux_apprentissage` | Le taux d'apprentissage à utiliser pour l'entraînement (par défaut : 0.0005). | FLOAT | Oui | 0.0000001-1.0 |
| `rang` | Le rang des couches LoRA (par défaut : 8). | INT | Oui | 1-128 |
| `optimiseur` | L'optimiseur à utiliser pour l'entraînement (par défaut : "AdamW"). | COMBO | Oui | "AdamW"<br>"Adam"<br>"SGD"<br>"RMSprop" |
| `fonction_perte` | La fonction de perte à utiliser pour l'entraînement (par défaut : "MSE"). | COMBO | Oui | "MSE"<br>"L1"<br>"Huber"<br>"SmoothL1" |
| `graine` | La graine à utiliser pour l'entraînement (utilisée dans le générateur pour l'initialisation des poids LoRA et l'échantillonnage du bruit) (par défaut : 0). | INT | Oui | 0-18446744073709551615 |
| `type_données_entraînement` | Le type de données à utiliser pour l'entraînement. 'none' préserve le type de données de calcul natif du modèle au lieu de le remplacer. Pour les modèles fp16, GradScaler est automatiquement activé (par défaut : "bf16"). | COMBO | Oui | "bf16"<br>"fp32"<br>"none" |
| `type_données_lora` | Le type de données à utiliser pour le LoRA (par défaut : "bf16"). | COMBO | Oui | "bf16"<br>"fp32" |
| `quantized_backward` | Lors de l'utilisation de `type_données_entraînement` 'none' et de l'entraînement sur un modèle quantifié, effectue la rétropropagation avec multiplication matricielle quantifiée lorsqu'elle est activée (par défaut : False). | BOOLEAN | Oui | - |
| `algorithme` | L'algorithme à utiliser pour l'entraînement. | COMBO | Oui | Plusieurs options disponibles |
| `point de contrôle de gradient` | Utiliser le point de contrôle de gradient pour l'entraînement (par défaut : True). | BOOLEAN | Oui | - |
| `checkpoint_depth` | Niveau de profondeur pour le point de contrôle de gradient (par défaut : 1). | INT | Oui | 1-5 |
| `offloading` | Décharger les poids du modèle vers le CPU pendant l'entraînement pour économiser la mémoire GPU (par défaut : False). | BOOLEAN | Oui | - |
| `lora_existant` | Le LoRA existant auquel ajouter. Définir sur Aucun pour un nouveau LoRA (par défaut : "[None]"). | COMBO | Oui | Plusieurs options disponibles |
| `bucket_mode` | Activer le mode de compartiment de résolution. Lorsqu'il est activé, attend des latents pré-compartimentés du nœud ResolutionBucket (par défaut : False). | BOOLEAN | Oui | - |
| `bypass_mode` | Activer le mode de contournement pour l'entraînement. Lorsqu'il est activé, les adaptateurs sont appliqués via des crochets avant au lieu de la modification des poids. Utile pour les modèles quantifiés où les poids ne peuvent pas être modifiés directement (par défaut : False). | BOOLEAN | Oui | - |

**Remarque :** Le nombre d'entrées de conditionnement positif doit correspondre au nombre d'images latentes. Si un seul conditionnement positif est fourni avec plusieurs images, il sera automatiquement répété pour toutes les images.

**Remarque sur `training_dtype` :** Lorsqu'il est défini sur "none", le type de données de calcul natif du modèle est préservé. Pour les modèles fp16, GradScaler est automatiquement activé pour éviter un sous-écoulement lors du calcul du gradient. Si `fp16_accumulation` est également activé (via les indicateurs `--fast`), cette combinaison peut être numériquement instable et peut provoquer des valeurs NaN.

**Remarque sur `quantized_backward` :** Ce paramètre n'est pertinent que lorsque `training_dtype` est défini sur "none" et que le modèle est un modèle quantifié. Il active la multiplication matricielle quantifiée pendant la passe arrière.

**Remarque sur `bypass_mode` :** Lorsqu'il est activé, les adaptateurs sont appliqués via des crochets avant au lieu de modifier directement les poids du modèle. Ceci est particulièrement utile pour les modèles quantifiés où les poids ne peuvent pas être modifiés directement.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `carte_de_perte` | Les poids LoRA entraînés qui peuvent être sauvegardés ou appliqués à d'autres modèles. | LORA_MODEL |
| `étapes` | Un dictionnaire contenant les valeurs de perte d'entraînement au fil du temps. | LOSS_MAP |
| `étapes` | Le nombre total d'étapes d'entraînement effectuées (y compris les étapes précédentes du LoRA existant). | INT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrainLoraNode/fr.md)

---
**Source fingerprint (SHA-256):** `df315ef416ff3ce81e6a526af2c4e5115980e6c35830825967e7189d4f8541d8`
