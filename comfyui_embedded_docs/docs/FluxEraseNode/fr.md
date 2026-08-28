# Flux Effacer l'image

Supprime l'objet masqué d'une image et reconstruit l'arrière-plan. Peignez le masque sur ce que vous voulez effacer, et le nœud remplit la zone avec un contenu d'arrière-plan plausible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `mask` | Les zones blanches sont supprimées ; les zones noires sont conservées | MASK | Oui | - |
| `dilate_pixels` | Élargit les limites du masque pour garantir une couverture propre des bords de l'objet (par défaut : 10) | INT | Oui | 0 à 25 |
| `graine` | La graine aléatoire utilisée pour créer le bruit (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Remarque :** L'image d'entrée doit mesurer au moins 256x256 pixels dans les deux dimensions. Le masque est automatiquement redimensionné pour correspondre aux dimensions de l'image, et le canal alpha de l'image est supprimé avant le traitement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image résultante avec l'objet masqué supprimé et l'arrière-plan reconstruit | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/fr.md)

---
**Source fingerprint (SHA-256):** `124be59b9829aa9f865d7ec76cd68f7978e2010cd3a84f25742a1c17f2d70b76`
