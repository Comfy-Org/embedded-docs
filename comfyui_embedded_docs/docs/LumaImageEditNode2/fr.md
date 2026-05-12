> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Ce nœud modifie une image existante à l'aide d'une invite textuelle, propulsé par le modèle Luma UNI-1. Il prend une image source et une description de la modification souhaitée, puis génère une nouvelle version éditée de l'image.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `source` | IMAGE | Oui | - | Image source à modifier. |
| `prompt` | STRING | Oui | 1–6000 caractères | Description de la modification souhaitée. Par défaut : "" (chaîne vide). |
| `model` | MODEL | Oui | `"uni-1"`<br>`"uni-1-max"` | Modèle à utiliser pour la modification. |
| `seed` | INT | Oui | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 0. |

**Contraintes des paramètres :**
- Le `prompt` doit contenir entre 1 et 6000 caractères.
- Le paramètre `model` est une liste déroulante dynamique qui, lorsqu'elle est définie sur `"uni-1"` ou `"uni-1-max"`, fournit des sous-paramètres supplémentaires (tels que `style`, `web_search` et `image_ref`). Le sous-paramètre `image_ref` accepte un maximum de 8 références d'image.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | L'image modifiée générée par le modèle Luma UNI-1. |