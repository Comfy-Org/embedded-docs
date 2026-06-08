# Post-Process SeedVR2 Output

Ce nœud aligne l'image générée avec l'image redimensionnée d'origine et applique une correction colorimétrique optionnelle. Il prend la sortie d'un processus de suréchantillonnage SeedVR2 et l'ajuste pour correspondre aux couleurs et aux dimensions de l'image de référence originale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L'image générée à traiter. | IMAGE | Oui | - |
| `original_resized_images` | L'image originale redimensionnée avant prétraitement, utilisée comme référence. | IMAGE | Oui | - |
| `color_correction_method` | Méthode pour faire correspondre les couleurs de l'image générée à l'image originale. lab : transfert des couleurs dans l'espace CIELAB, préservant les détails (le plus fidèle). wavelet : transfert des basses fréquences de couleur, conservant les hautes fréquences du suréchantillonnage. adain : correspondance moyenne/écart-type par canal (le plus rapide, teinte globale). none : ignorer le transfert de couleur (alignement géométrique uniquement). (par défaut : "lab") | COMBO | Oui | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Remarque :** Les entrées `images` et `original_resized_images` doivent avoir des dimensions correspondantes. Si l'image originale possède un canal alpha (4 canaux), celui-ci sera préservé et appliqué à la sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image traitée avec la correction colorimétrique appliquée et les dimensions alignées sur l'image de référence. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/fr.md)

---
**Source fingerprint (SHA-256):** `befbe8ccd591c8064a07ae4bb8df853c7ce10f3de83ebfa9214755c22faf28b0`
