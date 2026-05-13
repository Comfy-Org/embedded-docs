> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Ce nœud applique le guidage ControlNet au conditionnement de Stable Diffusion 3. Il prend en entrée des conditionnements positifs et négatifs, ainsi qu'un modèle ControlNet et une image, puis applique le guidage de contrôle avec des paramètres de force et de temporisation ajustables pour influencer le processus de génération.

**Remarque :** Ce nœud a été marqué comme obsolète et pourrait être supprimé dans les versions futures.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif auquel appliquer le guidage ControlNet |
| `negative` | CONDITIONING | Oui | - | Le conditionnement négatif auquel appliquer le guidage ControlNet |
| `control_net` | CONTROL_NET | Oui | - | Le modèle ControlNet à utiliser pour le guidage |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé dans le processus |
| `image` | IMAGE | Oui | - | L'image d'entrée que ControlNet utilisera comme guide |
| `strength` | FLOAT | Oui | 0.0 - 10.0 | La force de l'effet ControlNet (par défaut : 1.0) |
| `start_percent` | FLOAT | Oui | 0.0 - 1.0 | Le point de départ dans le processus de génération où ControlNet commence à s'appliquer (par défaut : 0.0) |
| `end_percent` | FLOAT | Oui | 0.0 - 1.0 | Le point d'arrêt dans le processus de génération où ControlNet cesse de s'appliquer (par défaut : 1.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `positive` | CONDITIONING | Le conditionnement positif modifié avec le guidage ControlNet appliqué |
| `negative` | CONDITIONING | Le conditionnement négatif modifié avec le guidage ControlNet appliqué |

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
