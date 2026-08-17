# QwenImageDiffsynthControlnet

Le nœud `QwenImageDiffsynthControlnet` applique un patch de réseau de contrôle de synthèse de diffusion pour modifier le comportement d’un modèle de base. Il utilise une image d’entrée et un masque optionnel pour guider le processus de génération du modèle avec une force ajustable, créant ainsi un modèle patché qui intègre l’influence du réseau de contrôle pour une synthèse d’image plus contrôlée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de base à patcher avec le réseau de contrôle | MODEL | Oui | - |
| `model_patch` | Le modèle de patch du réseau de contrôle à appliquer au modèle de base | MODEL_PATCH | Oui | - |
| `vae` | Le VAE (autoencodeur variationnel) utilisé dans le processus de diffusion | VAE | Oui | - |
| `image` | L’image d’entrée utilisée pour guider le réseau de contrôle (seuls les canaux RVB sont utilisés) | IMAGE | Oui | - |
| `strength` | La force de l’influence du réseau de contrôle (défaut : 1,0) | FLOAT | Oui | -10,0 à 10,0 (pas : 0,01) |
| `mask` | Masque optionnel définissant les zones où le réseau de contrôle doit être appliqué (inversé en interne) | MASK | Non | - |

**Remarque :** Lorsqu’un masque est fourni, il est automatiquement inversé (1,0 - masque) et redimensionné pour correspondre aux dimensions attendues par le traitement du réseau de contrôle. Lorsque le patch du modèle est de type ZImage Control, le patch est appliqué à la fois au raffineur de bruit et aux blocs doubles ; pour un réseau de contrôle DiffSynth standard, seul le patch du bloc double est appliqué.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de réseau de contrôle de synthèse de diffusion appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
