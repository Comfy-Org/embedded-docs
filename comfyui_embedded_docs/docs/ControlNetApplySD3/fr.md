# Appliquer Controlnet avec VAE

Ce nœud applique le guidage ControlNet au conditionnement de Stable Diffusion 3. Il prend en entrée les conditionnements positif et négatif ainsi qu'un modèle ControlNet et une image, puis applique le guidage de contrôle avec des paramètres de force et de timing ajustables pour influencer le processus de génération.

**Remarque :** Ce nœud a été marqué comme obsolète et pourrait être supprimé dans les versions futures.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif auquel appliquer le guidage ControlNet | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif auquel appliquer le guidage ControlNet | CONDITIONING | Oui | - |
| `control_net` | Le modèle ControlNet à utiliser pour le guidage | CONTROL_NET | Oui | - |
| `vae` | Le modèle VAE utilisé dans le processus | VAE | Oui | - |
| `image` | L'image d'entrée que ControlNet utilisera comme guidage | IMAGE | Oui | - |
| `strength` | La force de l'effet ControlNet (par défaut : 1.0). Lorsqu'elle est définie sur 0.0, le nœud ignore l'application de ControlNet et renvoie le conditionnement inchangé. | FLOAT | Oui | 0.0 - 10.0 |
| `start_percent` | Le point de départ du processus de génération où ControlNet commence à s'appliquer (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `end_percent` | Le point de fin du processus de génération où ControlNet cesse de s'appliquer (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

**Remarque :** Lorsque `strength` est définie sur 0.0, aucun guidage ControlNet n'est appliqué et le conditionnement d'entrée est transmis tel quel aux deux sorties.

**Remarque :** Si le même conditionnement est réutilisé ailleurs et contient déjà des informations de contrôle, le nouveau ControlNet est lié après le précédent, ce qui permet d'appliquer plusieurs ControlNets en séquence.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif modifié avec le guidage ControlNet appliqué | CONDITIONING |
| `negative` | Le conditionnement négatif modifié avec le guidage ControlNet appliqué | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/fr.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
