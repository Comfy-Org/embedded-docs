> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Une description textuelle de la vidéo souhaitée. La longueur maximale est de 2500 caractères. |
| `reference_image` | IMAGE | Oui | N/A | Une image du personnage à animer. Les dimensions minimales sont de 340x340 pixels. Le rapport d'aspect doit être compris entre 1:2,5 et 2,5:1. |
| `reference_video` | VIDEO | Oui | N/A | Une vidéo de référence de mouvement utilisée pour piloter les mouvements et les expressions du personnage. Les dimensions minimales sont de 340x340 pixels, les dimensions maximales sont de 3850x3850 pixels. Les limites de durée dépendent du paramètre `character_orientation`. |
| `keep_original_sound` | BOOLEAN | Non | N/A | Détermine si l'audio original de la vidéo de référence est conservé dans la sortie. La valeur par défaut est `True`. |
| `character_orientation` | COMBO | Non | `"video"`<br>`"image"` | Contrôle la source de l'orientation/du sens du regard du personnage. `"video"` : les mouvements, expressions, mouvements de caméra et l'orientation suivent la vidéo de référence de mouvement. `"image"` : les mouvements et expressions suivent la vidéo de référence de mouvement, mais l'orientation du personnage correspond à celle de l'image de référence. |
| `mode` | COMBO | Non | `"pro"`<br>`"std"` | Le mode de génération à utiliser. |

**Contraintes :**

* La durée de la `reference_video` doit être comprise entre 3 et 30 secondes lorsque `character_orientation` est défini sur `"video"`.
* La durée de la `reference_video` doit être comprise entre 3 et 10 secondes lorsque `character_orientation` est défini sur `"image"`.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | La vidéo générée avec le personnage exécutant le mouvement de la vidéo de référence. |
