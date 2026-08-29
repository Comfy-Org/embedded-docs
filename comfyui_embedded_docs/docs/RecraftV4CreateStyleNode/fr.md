# Recraft V4 Create Style

Ce nœud crée un style Recraft V4 réutilisable à partir de 1 à 10 images de référence. L'identifiant de style retourné fonctionne avec tous les modèles Recraft V4 et V4.1 du même type de sortie et peut être réutilisé dans les étapes ultérieures de génération d'images. La taille totale de toutes les images de référence est limitée à 10 Mo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Type de sortie pour lequel le style est créé : recraftv4_styles pour les images raster, recraftv4_styles_vector pour SVG. | COMBO | Oui | "recraftv4_styles"<br>"recraftv4_styles_vector" |
| `images` | Images de référence définissant le style. Des références similaires affinent la correspondance, des références variées l'élargissent. Emplacement extensible : connectez 1 à 10 images (`image_1` à `image_10`). | IMAGE | Oui | 1 à 10 images |

### Remarques

- Au moins une image de référence est requise ; le nœud génère une erreur si aucune n'est fournie.
- Au maximum 10 images de référence sont autorisées.
- La taille totale encodée de toutes les images de référence ne doit pas dépasser 10 Mo ; le nœud génère une erreur si la limite est dépassée.
- Chaque image de référence est réduite à une taille maximale de 2048×2048 pixels et encodée en WebP avant d'être envoyée à l'API Recraft.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `style_id` | Identifiant unique du style créé, utilisable avec tous les modèles Recraft V4 et V4.1 du même type de sortie. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/fr.md)

---
**Source fingerprint (SHA-256):** `63b31ff08d5cfe7c0d4de6987f2ee5a34bd491237ed0fb4c93c225e33b7cede3`
