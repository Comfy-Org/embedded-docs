# Post-traitement de la sortie SeedVR2

Ce nœud aligne l'image générée avec l'image redimensionnée d'origine et applique une éventuelle correction des couleurs. Il prend la sortie d'un processus de suréchantillonnage SeedVR2 et l'ajuste pour correspondre aux couleurs et aux dimensions de l'image de référence d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L'image générée à traiter. | IMAGE | Oui | - |
| `original_resized_images` | L'image redimensionnée d'origine avant le prétraitement, utilisée comme référence. | IMAGE | Oui | - |
| `color_correction_method` | Méthode pour aligner les couleurs de l'image générée sur celles de l'image d'origine. lab : transfert des couleurs dans l'espace CIELAB, en préservant les détails (le plus fidèle). wavelet : transfert des couleurs basse fréquence, en conservant les détails haute fréquence suréchantillonnés. adain : correspondance moyenne/écart-type par canal (le plus rapide, teinte globale). none : aucun transfert de couleur (uniquement l'alignement géométrique). (défaut : "lab") | COMBO | Oui | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Remarque :** La sortie est recadrée à la hauteur et à la largeur les plus petites entre l'image générée et l'image de référence, et les dimensions finales sont arrondies vers le bas à des nombres pairs. Si l'image de référence possède un canal alpha (4 canaux), celui-ci est préservé et appliqué à la sortie. Les deux entrées peuvent être des tenseurs d'image 4D ou 5D, et la sortie utilise la même dimensionnalité que l'image générée en entrée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image alignée et corrigée des couleurs. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/fr.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
