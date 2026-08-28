# Recraft Image Inpainting

Ce nœud modifie des zones spécifiques d'une image en fonction d'une invite textuelle et d'un masque. Il utilise l'API Recraft pour éditer intelligemment uniquement les régions masquées tout en laissant le reste de l'image inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à modifier | IMAGE | Oui | - |
| `mask` | Le masque définissant les zones de l'image à modifier | MASK | Oui | - |
| `invite` | Invite pour la génération d'image (par défaut : chaîne vide, longueur maximale : 1000 caractères) | STRING | Oui | - |
| `n` | Le nombre d'images à générer (par défaut : 1, minimum : 1, maximum : 6) | INT | Oui | 1-6 |
| `seed` | Graine pour déterminer si le nœud doit s'exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Paramètre de style facultatif pour l'API Recraft. S'il n'est pas fourni, le style par défaut est "realistic_image" | STYLEV3 | Non | - |
| `invite négative` | Description textuelle facultative des éléments indésirables sur une image (par défaut : chaîne vide) | STRING | Non | - |

*Remarque : `image` et `mask` doivent être fournis ensemble pour que l'opération d'inpainting fonctionne. Le masque est automatiquement redimensionné pour correspondre aux dimensions de l'image. L'invite `prompt` est validée et a une longueur maximale de 1000 caractères. Si un `style_id` provenant de la Infinite Style Library est utilisé, assurez-vous qu'il ne s'agit pas d'un style d'art vectoriel, car cela pourrait amener l'API à renvoyer des données SVG au lieu d'une image.*

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image ou les images modifiées générées à partir de l'invite et du masque. Renvoie une image par image d'entrée multipliée par le paramètre `n` | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/fr.md)

---
**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`
