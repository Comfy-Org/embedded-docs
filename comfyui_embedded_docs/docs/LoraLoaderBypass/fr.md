# Charger LoRA (Bypass) (Pour le débogage)

Le nœud LoraLoaderBypass applique un LoRA (Low-Rank Adaptation) à un modèle de diffusion et à un modèle CLIP dans un mode « bypass » spécial. Contrairement à un chargeur LoRA standard, cette méthode ne modifie pas de façon permanente les poids du modèle de base. Au lieu de cela, elle calcule le résultat en ajoutant la contribution du LoRA à la passe avant normale du modèle, ce qui est utile pour l'entraînement ou lorsque l'on travaille avec des modèles dont les poids sont déchargés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel le LoRA sera appliqué. | MODEL | Oui | - |
| `clip` | Le modèle CLIP auquel le LoRA sera appliqué. | CLIP | Oui | - |
| `lora_name` | Le nom du LoRA. Les fichiers LoRA disponibles sont chargés depuis le dossier `loras`. | COMBO | Oui | Liste des fichiers LoRA disponibles |
| `strength_model` | Dans quelle mesure modifier le modèle de diffusion. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 (pas : 0.01) |
| `strength_clip` | Dans quelle mesure modifier le modèle CLIP. Cette valeur peut être négative (par défaut : 1.0). | FLOAT | Oui | -100.0 à 100.0 (pas : 0.01) |

**Remarque :** Si `strength_model` et `strength_clip` sont tous deux définis sur 0, le nœud renvoie les entrées `model` et `clip` d'origine, non modifiées, sans traitement.

**Remarque :** Le fichier LoRA sélectionné est mis en cache après son premier chargement. Il n'est relu depuis le disque que lorsqu'un `lora_name` différent est choisi.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle de diffusion modifié. | MODEL |
| `CLIP` | Le modèle CLIP modifié. | CLIP |

**Remarque :** Ce nœud est marqué comme expérimental.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/fr.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
