# HitPaw Amélioration Générale d’Image

Ce nœud améliore les images basse résolution en les agrandissant en super-résolution, en supprimant les artefacts et le bruit. Il utilise une API externe pour traiter l'image et peut automatiquement ajuster la taille d'entrée afin de rester dans les limites de traitement. La taille de sortie maximale autorisée est de 32 mégapixels.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle d'amélioration à utiliser. Le modèle `generative_portrait` est optimisé pour les portraits, tandis que `generative` est un modèle polyvalent. | COMBO | Oui | `"generative_portrait"`<br>`"generative"` |
| `image` | L'image d'entrée à améliorer. | IMAGE | Oui | - |
| `facteur_d’agrandissement` | Le facteur par lequel agrandir les dimensions de l'image. Un facteur de 1 signifie aucun agrandissement, 2 double les dimensions, et 4 les quadruple. | COMBO | Oui | `1`<br>`2`<br>`4` |
| `réduction_automatique` | Réduire automatiquement l'image d'entrée si la sortie dépasse la limite. (par défaut : `False`) | BOOLEAN | Non | - |

**Remarque :** Le nœud génère une erreur si la taille de sortie calculée (largeur d'entrée × facteur d'agrandissement × hauteur d'entrée × facteur d'agrandissement) dépasse 32 000 000 pixels (32 MP) et que `auto_downscale` est désactivé. Lorsque `auto_downscale` est activé, le nœud réduit automatiquement la taille de l'image d'entrée ou le facteur d'agrandissement (ou les deux) afin que la sortie respecte la limite de 32 MP.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image de sortie améliorée et agrandie. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
