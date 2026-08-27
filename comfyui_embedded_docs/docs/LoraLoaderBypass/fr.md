# Charger LoRA (Bypass) (Pour le débogage)

Le nœud LoraLoaderBypass applique un LoRA (Adaptation de bas rang) à un modèle de diffusion et à un modèle CLIP dans un mode « bypass » spécial. Contrairement à un chargeur LoRA standard, cette méthode ne modifie pas de manière permanente les poids du modèle de base. Au lieu de cela, elle calcule la sortie en ajoutant l'effet du LoRA au passage normal du modèle, ce qui est utile pour l'entraînement ou pour travailler avec des modèles dont les poids sont déchargés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel le LoRA sera appliqué. | MODEL | Oui | - |
| `clip` | Le modèle CLIP auquel le LoRA sera appliqué. | CLIP | Oui | - |
| `lora_name` | Le nom du LoRA. Les fichiers LoRA disponibles sont chargés depuis le dossier `loras`. | COMBO | Oui | Liste des fichiers LoRA disponibles |
| `strength_model` | À quel point modifier le modèle de diffusion. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 (pas : 0.01) |
| `strength_clip` | À quel point modifier le modèle CLIP. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 (pas : 0.01) |

**Remarque :** Si `strength_model` et `strength_clip` sont tous deux définis à 0, le nœud renvoie les entrées `model` et `clip` d'origine, non modifiées, sans traitement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle de diffusion modifié. | MODEL |
| `CLIP` | Le modèle CLIP modifié. | CLIP |

**Remarque :** Ce nœud est marqué comme expérimental.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/fr.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
