# RenormCFG

Le nœud RenormCFG modifie le processus de guidance sans classifieur (CFG) dans les modèles de diffusion en appliquant une mise à l’échelle et une normalisation conditionnelles. Il ajuste le processus de débruitage en fonction de seuils de pas de temps spécifiés et de facteurs de renormalisation afin de contrôler l’influence des prédictions conditionnelles par rapport aux prédictions inconditionnelles pendant la génération d’images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer le CFG renormalisé | MODEL | Oui | - |
| `cfg_trunc` | Seuil de pas de temps pour l’application de la mise à l’échelle CFG. Lorsque le pas de temps actuel est inférieur à cette valeur, la mise à l’échelle CFG est appliquée ; sinon, seule la prédiction conditionnelle est utilisée (par défaut : 100.0) | FLOAT | Non | 0.0 - 100.0 |
| `renorm_cfg` | Facteur de renormalisation qui limite la norme maximale de la prédiction mise à l’échelle par CFG par rapport à la prédiction conditionnelle d’origine. Une valeur de 0.0 désactive la renormalisation (par défaut : 1.0) | FLOAT | Non | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la fonction CFG renormalisée appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/fr.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
