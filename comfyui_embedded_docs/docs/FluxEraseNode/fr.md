# Flux Effacer l'image

Supprime l'objet masqué d'une image et reconstruit l'arrière-plan. Peignez le masque sur ce que vous souhaitez effacer, et le nœud comble la zone avec un contenu d'arrière-plan plausible.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `mask` | Les zones blanches sont supprimées ; les zones noires sont préservées | MASK | Oui | - |
| `dilate_pixels` | Élargit les limites du masque pour garantir une couverture nette des bords de l'objet (par défaut : 10) | INT | Oui | 0 à 25 |
| `graine` | La graine aléatoire utilisée pour générer le bruit (par défaut : 0) | INT | Non | 0 à 2147483647 |

**Remarque :** L'image d'entrée doit mesurer au moins 256x256 pixels dans les deux dimensions. Le masque est automatiquement redimensionné pour correspondre aux dimensions de l'image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image résultante avec l'objet masqué supprimé et l'arrière-plan reconstruit | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/fr.md)

---
**Source fingerprint (SHA-256):** `70cf3223bc1ba0528cf99e84f073bd7a1bbcc26164cef99f4deb1645038fbf11`
