> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/fr.md)

Ce nœud modifie des zones spécifiques d'une image en fonction d'une invite textuelle et d'un masque. Il utilise l'API Recraft pour éditer intelligemment uniquement les régions masquées tout en conservant le reste de l'image inchangé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | L'image d'entrée à modifier |
| `mask` | MASK | Oui | - | Le masque définissant les zones de l'image à modifier |
| `prompt` | STRING | Oui | - | Invite pour la génération d'image (par défaut : chaîne vide, longueur maximale : 1000 caractères) |
| `n` | INT | Oui | 1-6 | Le nombre d'images à générer (par défaut : 1, minimum : 1, maximum : 6) |
| `seed` | INT | Oui | 0-18446744073709551615 | Graine pour déterminer si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) |
| `recraft_style` | STYLEV3 | Non | - | Paramètre de style facultatif pour l'API Recraft. S'il n'est pas fourni, le style par défaut est "realistic_image" |
| `negative_prompt` | STRING | Non | - | Une description textuelle facultative des éléments indésirables sur une image (par défaut : chaîne vide) |

*Remarque : Les paramètres `image` et `mask` doivent être fournis ensemble pour que l'opération d'incrustation fonctionne. Le masque sera automatiquement redimensionné pour correspondre aux dimensions de l'image. L'invite `prompt` est validée et a une longueur maximale de 1000 caractères.*

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `image` | IMAGE | La ou les images modifiées générées en fonction de l'invite et du masque. Renvoie une image par image d'entrée multipliée par le paramètre `n` |

---
**Source fingerprint (SHA-256):** `3eb6505a19173d8e4ea4216348f9592fd996cdfe2f07a9e79ccec5f738a8fb93`
