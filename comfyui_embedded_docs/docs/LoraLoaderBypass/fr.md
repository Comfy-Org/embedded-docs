Le nœud LoraLoaderBypass applique un LoRA (Adaptation de Bas Rang) à un modèle de diffusion et à un modèle CLIP dans un mode spécial de « contournement » (bypass). Contrairement à un chargeur LoRA standard, cette méthode ne modifie pas de manière permanente les poids du modèle de base. Au lieu de cela, elle calcule la sortie en ajoutant l'effet du LoRA au passage avant normal du modèle, ce qui est utile pour l'entraînement ou lorsque l'on travaille avec des modèles dont les poids sont déchargés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel le LoRA sera appliqué. | MODEL | Oui | - |
| `clip` | Le modèle CLIP auquel le LoRA sera appliqué. | CLIP | Oui | - |
| `lora_name` | Le nom du fichier LoRA à appliquer. Les options sont chargées depuis le dossier `loras`. | COMBO | Oui | *Liste des fichiers LoRA disponibles* |
| `strength_model` | L'intensité de la modification du modèle de diffusion. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 |
| `strength_clip` | L'intensité de la modification du modèle CLIP. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 |

**Remarque :** Si `strength_model` et `strength_clip` sont tous deux définis sur 0, le nœud renverra les entrées `model` et `clip` originales et non modifiées, sans traitement.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle de diffusion avec le LoRA appliqué en mode contournement. | MODEL |
| `CLIP` | Le modèle CLIP avec le LoRA appliqué en mode contournement. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/fr.md)

---
**Source fingerprint (SHA-256):** `2642f4ed98457e5fd08e2103ffb9f2c02f11326590aadf0636fb7db51f484815`
