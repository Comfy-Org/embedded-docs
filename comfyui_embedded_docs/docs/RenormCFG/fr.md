Voici la traduction en français de la documentation du nœud RenormCFG :

Le nœud RenormCFG modifie le processus de guidage sans classifieur (CFG) dans les modèles de diffusion en appliquant une mise à l'échelle conditionnelle et une normalisation. Il ajuste le processus de débruitage en fonction de seuils de pas de temps spécifiés et de facteurs de renormalisation pour contrôler l'influence des prédictions conditionnelles par rapport aux prédictions inconditionnelles lors de la génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion auquel appliquer le CFG renormalisé | MODEL | Oui | - |
| `cfg_trunc` | Seuil de pas de temps pour l'application de la mise à l'échelle CFG. Lorsque le pas de temps actuel est inférieur à cette valeur, la mise à l'échelle CFG est appliquée ; sinon, seule la prédiction conditionnelle est utilisée (par défaut : 100,0) | FLOAT | Non | 0,0 - 100,0 |
| `renorm_cfg` | Facteur de renormalisation qui limite la norme maximale de la prédiction mise à l'échelle par CFG par rapport à la prédiction conditionnelle d'origine. Une valeur de 0,0 désactive la renormalisation (par défaut : 1,0) | FLOAT | Non | 0,0 - 100,0 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle modifié avec la fonction CFG renormalisée appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/fr.md)

---
**Source fingerprint (SHA-256):** `b59929606f7519574b7ad14a3caacee51e4f141dd6be3abb594217bcfdbc401e`
