# QwenImageDiffsynthControlnet

Voici la traduction en français de la documentation du nœud QwenImageDiffsynthControlnet :

Le nœud QwenImageDiffsynthControlnet applique un patch de réseau de contrôle de synthèse par diffusion pour modifier le comportement d'un modèle de base. Il utilise une image d'entrée et un masque optionnel pour guider le processus de génération du modèle avec une force ajustable, créant ainsi un modèle patché qui intègre l'influence du réseau de contrôle pour une synthèse d'image plus contrôlée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de base à patcher avec le réseau de contrôle | MODEL | Oui | - |
| `correctif_modèle` | Le patch du réseau de contrôle à appliquer au modèle de base | MODEL_PATCH | Oui | - |
| `vae` | L'AEV (Autoencodeur Variationnel) utilisé dans le processus de diffusion | VAE | Oui | - |
| `image` | L'image d'entrée utilisée pour guider le réseau de contrôle (seuls les canaux RVB sont utilisés) | IMAGE | Oui | - |
| `intensité` | La force de l'influence du réseau de contrôle (par défaut : 1,0) | FLOAT | Oui | -10,0 à 10,0 |
| `masque` | Masque optionnel qui définit les zones où le réseau de contrôle doit être appliqué (inversé en interne) | MASK | Non | - |

**Remarque :** Lorsqu'un masque est fourni, il est automatiquement inversé (1,0 - masque) et redimensionné pour correspondre aux dimensions attendues pour le traitement du réseau de contrôle. Le nœud utilise différentes méthodes de traitement interne selon que le patch du modèle est de type ZImage Control ou un réseau de contrôle DiffSynth standard.


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le patch de réseau de contrôle de synthèse par diffusion appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/fr.md)

---
**Source fingerprint (SHA-256):** `61833984d0b92be65fae72a894806572c0588dea74a295e8289d1194dee611bb`
