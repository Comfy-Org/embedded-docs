> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/fr.md)

Le nœud PerpNegGuider crée un système de guidage pour contrôler la génération d'images à l'aide d'un conditionnement négatif perpendiculaire. Il prend en entrée des conditionnements positif, négatif et vide, puis applique un algorithme de guidage spécialisé pour orienter le processus de génération. Ce nœud est conçu pour des tests expérimentaux et offre un contrôle précis de la force de guidage et de l'échelle négative.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle à utiliser pour la génération du guidage |
| `positive` | CONDITIONING | Oui | - | Le conditionnement positif qui oriente la génération vers le contenu souhaité |
| `négative` | CONDITIONING | Oui | - | Le conditionnement négatif qui éloigne la génération du contenu indésirable |
| `conditionnement vide` | CONDITIONING | Oui | - | Le conditionnement vide ou neutre utilisé comme référence de base |
| `cfg` | FLOAT | Oui | 0,0 - 100,0 | L'échelle de guidage sans classifieur qui contrôle l'influence du conditionnement sur la génération (par défaut : 8,0) |
| `échelle nég` | FLOAT | Oui | 0,0 - 100,0 | Le facteur d'échelle négative qui ajuste la force du conditionnement négatif (par défaut : 1,0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `guider` | GUIDER | Un système de guidage configuré, prêt à être utilisé dans le pipeline de génération |

---
**Source fingerprint (SHA-256):** `efd3f78d461ade9d16885923875bacffb5afeafcbe32fc2d207598e0efe3a8c6`
