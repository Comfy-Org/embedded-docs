> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/fr.md)

Le nœud CFGGuider crée un système de guidage pour contrôler le processus d'échantillonnage lors de la génération d'images. Il prend un modèle ainsi que des conditionnements positifs et négatifs, puis applique une échelle de guidage sans classifieur pour orienter la génération vers le contenu souhaité tout en évitant les éléments indésirables. Ce nœud produit un objet guideur qui peut être utilisé par les nœuds d'échantillonnage pour contrôler la direction de la génération d'images.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle à utiliser pour le guidage |
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif qui guide la génération vers le contenu souhaité |
| `négative` | CONDITIONING | Oui | - | Le conditionnement négatif qui éloigne la génération du contenu indésirable |
| `cfg` | FLOAT | Oui | 0.0 à 100.0 | L'échelle de guidage sans classifieur qui contrôle l'intensité de l'influence du conditionnement sur la génération (par défaut : 8.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `GUIDER` | GUIDER | Un objet guideur pouvant être transmis aux nœuds d'échantillonnage pour contrôler le processus de génération |

---
**Source fingerprint (SHA-256):** `80c1f733dc26717c5762655404b9c36b53bb9059ceb6a8531ef1a853e2fe2380`
