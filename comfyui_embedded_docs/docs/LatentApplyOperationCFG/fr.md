# LatentApplyOperationCFG

Le nœud LatentApplyOperationCFG applique une opération latente pour modifier le processus de guidage du conditionnement dans un modèle. Il fonctionne en interceptant les sorties de conditionnement pendant le processus d'échantillonnage par guidage sans classificateur (CFG) et en appliquant l'opération spécifiée aux représentations latentes avant qu'elles ne soient utilisées pour la génération.

Lorsque le modèle produit deux sorties de conditionnement (par exemple, un conditionnement positif et négatif), l'opération est appliquée à la différence entre les deux, puis le second conditionnement est rajouté. Lorsqu'il n'y a qu'une seule sortie de conditionnement, l'opération lui est appliquée directement. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel l'opération CFG sera appliquée | MODEL | Oui | - |
| `operation` | L'opération latente à appliquer pendant le processus d'échantillonnage CFG | LATENT_OPERATION | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'opération CFG appliquée à son processus d'échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/fr.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
