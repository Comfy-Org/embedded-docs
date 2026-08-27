# Post-traitement de la sortie SeedVR2

Ce nœud aligne l'image générée avec l'image redimensionnée d'origine et applique une correction des couleurs facultative. Il prend la sortie d'un processus d'upscaling SeedVR2 et l'ajuste pour qu'elle corresponde aux couleurs et aux dimensions de l'image de référence d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L'image générée à traiter. | IMAGE | Oui | - |
| `original_resized_images` | L'image redimensionnée d'origine avant le pré-traitement, utilisée comme référence. | IMAGE | Oui | - |
| `color_correction_method` | Méthode pour faire correspondre les couleurs de l'image générée à celles de l'image originale. lab : transfert des couleurs dans l'espace CIELAB, en préservant les détails (le plus fidèle). wavelet : transfert des couleurs basse fréquence, en conservant les détails haute fréquence agrandis. adain : correspondance moyenne/écart-type par canal (le plus rapide, teinte globale). none : ignorer le transfert de couleur (alignement géométrique uniquement). (défaut : "lab") | COMBO | Oui | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Remarque :** Les deux entrées peuvent être des tenseurs 4-D (batch, hauteur, largeur, canaux) ou 5-D (batch, images, hauteur, largeur, canaux). Le nœud recadre les deux à la plus petite taille de batch, nombre d'images, hauteur et largeur, elles n'ont donc pas besoin de correspondre exactement. La hauteur et la largeur de sortie sont arrondies vers le bas à des nombres pairs. Si l'image de référence possède un canal alpha (4 canaux), ce canal alpha est préservé et appliqué à la sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image alignée et corrigée des couleurs. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/fr.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
