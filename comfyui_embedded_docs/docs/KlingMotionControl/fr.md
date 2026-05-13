> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/fr.md)

Voici la traduction en français de la documentation du nœud Kling Motion Control :

Le nœud Kling Motion Control génère une vidéo en appliquant les mouvements, expressions et déplacements de caméra d'une vidéo de référence à un personnage défini par une image de référence et un prompt textuel. Il permet de contrôler si l'orientation finale du personnage provient de la vidéo de référence ou de l'image de référence.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | N/A | Description textuelle de la vidéo souhaitée. Longueur maximale de 2500 caractères. |
| `reference_image` | IMAGE | Oui | N/A | Image du personnage à animer. Dimensions minimales de 340x340 pixels. Le rapport hauteur/largeur doit être compris entre 1:2,5 et 2,5:1. |
| `reference_video` | VIDEO | Oui | N/A | Vidéo de référence de mouvement utilisée pour piloter les mouvements et expressions du personnage. Dimensions minimales de 340x340 pixels, dimensions maximales de 3850x3850 pixels. Les limites de durée dépendent du paramètre `character_orientation`. |
| `keep_original_sound` | BOOLEAN | Non | N/A | Détermine si l'audio original de la vidéo de référence est conservé dans la sortie. Par défaut : `True`. |
| `character_orientation` | COMBO | Non | `"video"`<br>`"image"` | Contrôle la provenance de l'orientation/du visage du personnage. `"video"` : les mouvements, expressions, déplacements de caméra et l'orientation suivent la vidéo de référence de mouvement (autres détails via le prompt). `"image"` : les mouvements et expressions suivent toujours la vidéo de référence de mouvement, mais l'orientation du personnage correspond à l'image de référence (caméra/autres détails via le prompt). |
| `mode` | COMBO | Non | `"pro"`<br>`"std"` | Mode de génération à utiliser. |
| `model` | COMBO | Non | `"kling-v3"`<br>`"kling-v2-6"` | Version du modèle Kling à utiliser. Par défaut : `"kling-v2-6"`. |

**Contraintes :**

* La durée de `reference_video` doit être comprise entre 3 et 30 secondes lorsque `character_orientation` est défini sur `"video"`.
* La durée de `reference_video` doit être comprise entre 3 et 10 secondes lorsque `character_orientation` est défini sur `"image"`.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée avec le personnage effectuant le mouvement de la vidéo de référence. |

---
**Source fingerprint (SHA-256):** `4159b10496e85ae93f522865494e9bc99ba08bda00df1601bca2314e61fb32df`
