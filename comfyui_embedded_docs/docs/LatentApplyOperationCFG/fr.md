# LatentApplyOperationCFG

Le nœud LatentApplyOperationCFG applique une opération latente pour modifier le processus de guidage du conditionnement dans un modèle. Il fonctionne en interceptant les sorties de conditionnement pendant le processus d'échantillonnage du guidage sans classificateur (CFG) et en appliquant l'opération spécifiée aux représentations latentes avant leur utilisation pour la génération. Lorsque l'échantillonneur produit deux sorties de conditionnement, l'opération est appliquée à la différence entre elles, puis la seconde sortie est rajoutée au résultat.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel l'opération CFG sera appliquée | MODEL | Oui | - |
| `operation` | L'opération latente à appliquer pendant le processus d'échantillonnage CFG | LATENT_OPERATION | Oui | - |

Note : Ce nœud est marqué comme expérimental. L'opération est appliquée aux sorties de conditionnement du modèle pendant le processus d'échantillonnage CFG. Lorsque deux sorties de conditionnement sont présentes, l'opération est appliquée à la différence entre la première et la seconde sortie, puis la seconde sortie est rajoutée. Lorsqu'une seule sortie de conditionnement est présente, l'opération lui est appliquée directement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'opération CFG appliquée à son processus d'échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/fr.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
