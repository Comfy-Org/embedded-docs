# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet applique un patch de réseau de contrôle de synthèse par diffusion à un modèle de base. Il utilise une image d'entrée et un masque facultatif pour guider le processus de génération du modèle avec une force réglable, produisant un modèle patché qui intègre l'influence du réseau de contrôle pour une synthèse d'image plus contrôlée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base à patcher avec le réseau de contrôle | MODEL | Oui | - |
| `correctif_modèle` | Le modèle de patch du réseau de contrôle à appliquer au modèle de base | MODEL_PATCH | Oui | - |
| `vae` | Le VAE (auto-encodeur variationnel) utilisé dans le processus de diffusion | VAE | Oui | - |
| `image` | L'image d'entrée utilisée pour guider le réseau de contrôle. Seuls les trois premiers canaux de couleur (RVB) sont utilisés ; tout canal supplémentaire est ignoré | IMAGE | Oui | - |
| `intensité` | La force de l'influence du réseau de contrôle (par défaut : 1.0) | FLOAT | Oui | -10.0 à 10.0 (pas de 0.01) |
| `masque` | Masque facultatif qui définit les zones où le réseau de contrôle doit être appliqué. Pour les patchs DiffSynth et Z-Image, le masque est inversé en interne avant utilisation | MASK | Non | - |
| `start_percent` | Le point dans le processus de débruitage, en tant que fraction du nombre total d'étapes d'échantillonnage, où le réseau de contrôle commence à prendre effet (par défaut : 0.0) | FLOAT | Non | 0.0 à 1.0 (pas de 0.001) |
| `end_percent` | Le point dans le processus de débruitage où le réseau de contrôle cesse de prendre effet (par défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 (pas de 0.001) |

**Remarque :** Les valeurs `start_percent` et `end_percent` limitent le réseau de contrôle à une fenêtre du processus de débruitage ; en dehors de cette fenêtre, le modèle est échantillonné sans le patch. Si `strength` est défini sur 0, le nœud renvoie le modèle de base inchangé. Lorsqu'un masque est fourni, il est inversé (1.0 - mask) et remodelé pour le Z-Image Control et les chemins DiffSynth standard, tandis qu'un patch Qwen Image 2.1 Fun ControlNet utilise le masque tel quel. Le nœud choisit son implémentation de patch interne à partir du patch de modèle chargé, de sorte que les mêmes entrées se comportent légèrement différemment pour Z-Image Control, Qwen Image 2.1 Fun ControlNet et les checkpoints DiffSynth standard. Ce nœud est marqué comme expérimental.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de réseau de contrôle de synthèse par diffusion appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `7be42c001c2937af7ca5c2d45aa8a529574aa9117b4740c62da822910041d231`
