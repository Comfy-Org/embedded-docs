# LatentApplyOperationCFG

Le nœud **LatentApplyOperationCFG** applique une opération latente pour modifier le processus de guidage du conditionnement dans un modèle. Il fonctionne en interceptant les sorties de conditionnement pendant le processus d'échantillonnage par guidage sans classifieur (CFG) et en appliquant l'opération spécifiée aux représentations latentes avant qu'elles ne soient utilisées pour la génération.

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
**Source fingerprint (SHA-256):** `9fbcc9183abf89bb93e55263bb655e931549360c05a561f7dacae8723db62e52`
