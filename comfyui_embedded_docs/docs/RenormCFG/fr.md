# RenormCFG

Le nœud RenormCFG modifie le processus de guidage sans classifieur (CFG) dans les modèles de diffusion en appliquant une mise à l'échelle conditionnelle et une normalisation. Il ajuste le processus de débruitage en fonction d'un seuil de pas de temps spécifié et d'un facteur de renormalisation, contrôlant l'influence des prédictions conditionnelles par rapport aux prédictions inconditionnelles pendant la génération d'images. Le modèle résultant est renvoyé avec ce comportement CFG patché.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer le CFG renormalisé | MODEL | Oui | - |
| `cfg_trunc` | Seuil de pas de temps pour appliquer la mise à l'échelle CFG. Lorsque le pas de temps actuel est inférieur à cette valeur, la mise à l'échelle CFG et la renormalisation sont appliquées ; sinon, seule la prédiction conditionnelle est utilisée (valeur par défaut : 100.0) | FLOAT | Non | 0.0 - 100.0 (pas 0.01) |
| `renorm_cfg` | Facteur de renormalisation qui limite la norme maximale de la prédiction mise à l'échelle par CFG par rapport à la prédiction conditionnelle d'origine. Une valeur de 0.0 désactive la renormalisation (valeur par défaut : 1.0) | FLOAT | Non | 0.0 - 100.0 (pas 0.01) |

Remarque : `cfg_trunc` et `renorm_cfg` sont des paramètres avancés. La renormalisation ne prend effet que lorsque `renorm_cfg` est supérieur à 0.0 et que le pas de temps actuel est inférieur à `cfg_trunc` ; si la norme de la nouvelle prédiction est déjà inférieure au maximum calculé, aucun redimensionnement n'est effectué.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié auquel la fonction CFG renormalisée est appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenormCFG/fr.md)

---
**Source fingerprint (SHA-256):** `5925bdfe2d62ef7261d73cda661834102ae6600b1afe53f4093568a6e83ec2ab`
