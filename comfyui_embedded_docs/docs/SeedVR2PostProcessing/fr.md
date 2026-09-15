# Post-traitement de la sortie SeedVR2

Ce nœud aligne l'image générée avec l'image redimensionnée originale et applique une correction colorimétrique facultative. Il prend la sortie d'un processus de mise à l'échelle SeedVR2 et l'ajuste pour correspondre aux couleurs et aux dimensions de l'image de référence originale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L'image générée à traiter. | IMAGE | Oui | - |
| `original_resized_images` | L'image redimensionnée originale avant prétraitement, utilisée comme référence. | IMAGE | Oui | - |
| `color_correction_method` | Méthode pour faire correspondre les couleurs de l'image générée à celles de l'image originale. lab : transfère la couleur dans l'espace CIELAB, en préservant les détails (la plus fidèle). wavelet : transfère la couleur basse fréquence, en conservant les détails haute fréquence de l'image mise à l'échelle. adain : fait correspondre la moyenne/écart-type par canal (la plus rapide, teinte globale). none : ignore le transfert de couleur (alignement géométrique uniquement). (par défaut : "lab") | COMBO | Oui | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Remarque :** Les deux entrées peuvent être des tenseurs 4-D (lot, hauteur, largeur, canaux) ou 5-D (lot, frames, hauteur, largeur, canaux). Le nœud recadre les deux au plus petit lot, au plus petit nombre de frames, à la plus petite hauteur et à la plus petite largeur, de sorte qu'elles n'ont pas besoin de correspondre exactement. Lorsqu'une méthode de correction colorimétrique autre que `none` est utilisée, l'image de référence est d'abord redimensionnée à la taille de sortie. La correction colorimétrique est traitée par blocs adaptés à la mémoire disponible, en réduisant la taille des blocs si la mémoire est insuffisante. La hauteur et la largeur de sortie sont arrondies à l'entier pair inférieur. Si l'image de référence possède un canal alpha (4 canaux), ce canal alpha est préservé et appliqué à la sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image alignée et corrigée colorimétriquement. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/fr.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
