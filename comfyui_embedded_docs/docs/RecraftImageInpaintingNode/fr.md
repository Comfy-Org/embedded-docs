# Recraft Image Inpainting

Ce nœud modifie des zones spécifiques d'une image en fonction d'une invite textuelle et d'un masque. Il utilise l'API Recraft pour éditer intelligemment uniquement les régions masquées tout en conservant le reste de l'image inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à modifier | IMAGE | Oui | - |
| `mask` | Le masque définissant les zones de l'image à modifier | MASK | Oui | - |
| `invite` | Invite pour la génération d'image (par défaut : chaîne vide, longueur maximale : 1000 caractères) | STRING | Oui | - |
| `n` | Le nombre d'images à générer (par défaut : 1, minimum : 1, maximum : 6) | INT | Oui | 1-6 |
| `seed` | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Paramètre de style facultatif pour l'API Recraft. S'il n'est pas fourni, le style par défaut est "realistic_image" | STYLEV3 | Non | - |
| `invite négative` | Une description textuelle facultative des éléments indésirables sur une image (par défaut : chaîne vide) | STRING | Non | - |

*Remarque : Les paramètres `image` et `mask` doivent être fournis ensemble pour que l'opération d'incrustation fonctionne. Le masque sera automatiquement redimensionné pour correspondre aux dimensions de l'image. L'invite `prompt` est validée et a une longueur maximale de 1000 caractères.*

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | La ou les images modifiées générées en fonction de l'invite et du masque. Renvoie une image par image d'entrée multipliée par le paramètre `n` | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/fr.md)

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`
