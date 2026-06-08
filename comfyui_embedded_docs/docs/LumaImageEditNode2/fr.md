Voici la traduction de la documentation du nœud ComfyUI, en respectant vos consignes :

## Aperçu

Ce nœud modifie une image existante à l'aide d'une invite textuelle, propulsé par le modèle Luma UNI-1. Il prend une image source et une description de la modification souhaitée, puis génère une nouvelle version éditée de l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `source` | Image source à modifier. | IMAGE | Oui | - |
| `invite` | Description de la modification souhaitée. Par défaut : "" (chaîne vide). | STRING | Oui | 1–6000 caractères |
| `modèle` | Modèle à utiliser pour la modification. | MODEL | Oui | `"uni-1"`<br>`"uni-1-max"` |
| `graine` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. | INT | Oui | 0 à 2147483647 |

**Contraintes des paramètres :**
- Le `prompt` doit avoir une longueur comprise entre 1 et 6000 caractères.
- Le paramètre `model` est une liste déroulante dynamique qui, lorsqu'il est défini sur `"uni-1"` ou `"uni-1-max"`, fournit des sous-paramètres supplémentaires (tels que `style`, `web_search` et `image_ref`). Le sous-paramètre `image_ref` accepte un maximum de 8 références d'images.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image modifiée générée par le modèle Luma UNI-1. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/fr.md)

---
**Source fingerprint (SHA-256):** `7026e3ce818b0a9710624bd071fc2049950290f89c7d0365ff44236e9ad5eaed`
