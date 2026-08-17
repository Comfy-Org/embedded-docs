# Charger LoRA (Bypass) (Pour le débogage)

Le nœud `LoraLoaderBypass` applique un LoRA (Low-Rank Adaptation) à un modèle de diffusion et à un modèle CLIP dans un mode de contournement spécial. Contrairement à un chargeur LoRA standard, il ne modifie pas définitivement les poids du modèle de base. Au lieu de cela, il ajoute l'effet du LoRA au passage avant normal du modèle, ce qui est utile pour l'entraînement ou lorsque l'on travaille avec des modèles dont les poids sont déchargés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel le LoRA sera appliqué. | MODEL | Oui | N/A |
| `clip` | Le modèle CLIP auquel le LoRA sera appliqué. | CLIP | Oui | N/A |
| `lora_name` | Le nom du fichier LoRA à appliquer. Les options sont chargées depuis le dossier `loras`. | COMBO | Oui | Liste des fichiers LoRA disponibles |
| `strength_model` | Force de modification du modèle de diffusion. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 |
| `strength_clip` | Force de modification du modèle CLIP. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 |

**Remarque :** Si `strength_model` et `strength_clip` sont tous deux définis sur 0, le nœud renvoie les entrées `model` et `clip` originales et non modifiées, sans traitement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle de diffusion avec le LoRA appliqué en mode de contournement. | MODEL |
| `CLIP` | Le modèle CLIP avec le LoRA appliqué en mode de contournement. | CLIP |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/fr.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
