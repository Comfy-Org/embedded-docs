> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/fr.md)

Le nœud Reve Image Edit vous permet de modifier une image existante en fonction d'une description textuelle. Il utilise l'API Reve pour interpréter vos instructions et appliquer les modifications demandées à l'image que vous fournissez.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image à modifier. |
| `edit_instruction` | STRING | Oui | - | Description textuelle de la manière de modifier l'image. Maximum 2560 caractères. |
| `model` | MODEL | Oui | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"`<br>`"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Version du modèle à utiliser pour l'édition. Les options incluent des versions de modèles spécifiques et des paramètres de rapport d'aspect. |
| `upscale` | COMBO | Non | `"disabled"`<br>`"enabled"` | Contrôle si l'image générée doit être suréchantillonnée (upscalée). |
| `upscale_factor` | FLOAT | Non | - | Le facteur par lequel suréchantillonner l'image lorsque l'upscaling est activé. |
| `remove_background` | BOOLEAN | Non | - | Contrôle si l'arrière-plan doit être supprimé de l'image générée. |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. (par défaut : 0) |

**Note :** Le paramètre `upscale_factor` n'est pertinent que lorsque le paramètre `upscale` est défini sur `"enabled"`.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image modifiée générée en fonction de l'instruction. |