Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Ce nœud applique le guidage ControlNet au conditionnement de Stable Diffusion 3. Il prend en entrée des conditionnements positifs et négatifs, ainsi qu'un modèle ControlNet et une image, puis applique le guidage de contrôle avec des paramètres de force et de temporisation ajustables pour influencer le processus de génération.

**Remarque :** Ce nœud a été marqué comme obsolète et pourrait être supprimé dans les versions futures.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | Le conditionnement positif auquel appliquer le guidage ControlNet | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif auquel appliquer le guidage ControlNet | CONDITIONING | Oui | - |
| `control_net` | Le modèle ControlNet à utiliser pour le guidage | CONTROL_NET | Oui | - |
| `vae` | Le modèle VAE utilisé dans le processus | VAE | Oui | - |
| `image` | L'image d'entrée que ControlNet utilisera comme guide | IMAGE | Oui | - |
| `strength` | La force de l'effet ControlNet (par défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |
| `start_percent` | Le point de départ dans le processus de génération où ControlNet commence à s'appliquer (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `end_percent` | Le point d'arrêt dans le processus de génération où ControlNet cesse de s'appliquer (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `negative` | Le conditionnement positif modifié avec le guidage ControlNet appliqué | CONDITIONING |
| `negative` | Le conditionnement négatif modifié avec le guidage ControlNet appliqué | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/fr.md)

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
