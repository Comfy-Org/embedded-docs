# GuideCFG

Le nœud CFGGuider crée un système de guidage pour contrôler le processus d'échantillonnage lors de la génération d'images. Il prend un modèle ainsi que des conditionnements positif et négatif, puis applique une échelle de guidage sans classifieur pour orienter la génération vers le contenu souhaité tout en évitant les éléments indésirables. Ce nœud produit un objet guider qui peut être utilisé par les nœuds d'échantillonnage pour contrôler la direction de génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à utiliser pour le guidage | MODEL | Oui | - |
| `positive` | Le conditionnement positif qui guide la génération vers le contenu souhaité | CONDITIONING | Oui | - |
| `negative` | Le conditionnement négatif qui éloigne la génération du contenu indésirable | CONDITIONING | Oui | - |
| `cfg` | L'échelle de guidage sans classifieur qui contrôle la force avec laquelle le conditionnement influence la génération (défaut : 8.0) | FLOAT | Oui | 0.0 à 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `GUIDER` | Un objet guider pouvant être transmis aux nœuds d'échantillonnage pour contrôler le processus de génération | GUIDER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGGuider/fr.md)

---
**Source fingerprint (SHA-256):** `73b57bfbb6d4fc083a8089bc0f786f82d03e0d7b2faeeb7a42b3d87e38047b9e`
