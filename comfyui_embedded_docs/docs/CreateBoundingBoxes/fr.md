# Créer des boîtes englobantes

Ce nœud fournit une interface graphique pour dessiner des boîtes englobantes autour d'objets ou de zones de texte dans une image. Il produit les coordonnées des boîtes englobantes dans l'espace pixel, des données d'élément structurées compatibles avec le formatage des invites Ideogram, ainsi qu'une image de prévisualisation montrant les boîtes dessinées avec des étiquettes et des palettes de couleurs.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `arrière-plan` | Image facultative utilisée comme arrière-plan dans le canevas et la prévisualisation. | IMAGE | Non | - |
| `largeur` | Largeur du canevas et de la grille de pixels pour les boîtes englobantes (par défaut : 1024). | INT | Oui | 64 à 16384 (pas : 16) |
| `hauteur` | Hauteur du canevas et de la grille de pixels pour les boîtes englobantes (par défaut : 1024). | INT | Oui | 64 à 16384 (pas : 16) |
| `état_éditeur` | Dessinez les boîtes englobantes et définissez le type, le texte, la description et la palette de couleurs de chaque boîte. Commencez par l'élément d'arrière-plan en premier et l'avant-plan en dernier. | BOUNDING_BOXES | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `aperçu` | Une image RVB montrant le canevas avec toutes les boîtes englobantes rendues, incluant les étiquettes, les échantillons de palette de couleurs et le texte descriptif. | IMAGE |
| `boîtes_englobantes` | Une liste de boîtes englobantes en coordonnées pixels, chaque boîte contenant les valeurs x, y, largeur et hauteur. | BOUNDING_BOX |
| `éléments` | Un tableau structuré d'objets élément, chacun contenant le type, les coordonnées de la boîte englobante (normalisées de 0 à 1000), le texte (pour le type texte), la description et la palette de couleurs. | ARRAY |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/fr.md)

---
**Source fingerprint (SHA-256):** `a63939f13edc6c6507590a390dcd6d0a3321febb5831baab1655d9952228612c`
