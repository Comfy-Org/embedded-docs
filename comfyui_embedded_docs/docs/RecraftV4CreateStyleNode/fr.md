# Recraft V4 Create Style

Ce nœud crée un style Recraft V4 réutilisable à partir de 1 à 10 images de référence. L'ID de style renvoyé fonctionne avec tous les modèles Recraft V4 et V4.1 du même type de sortie (raster ou vectoriel) et peut être réutilisé dans les étapes ultérieures de génération d'images. La taille totale de toutes les images de référence est limitée à 10 Mo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle pour lequel le style est créé. Standard et Pro partagent un même pool de styles : les styles raster fonctionnent avec tous les modèles raster Recraft V4 et V4.1, les styles vectoriels (*_vector) avec tous les modèles vectoriels V4 et V4.1. | COMBO | Oui | "recraftv4_styles"<br>"recraftv4_styles_vector"<br>"recraftv4_styles_pro"<br>"recraftv4_styles_pro_vector" |
| `images` | Images de référence définissant le style. Des références similaires affinent la correspondance, des références variées l'élargissent. Emplacement extensible : connectez 1 à 10 images (`image_1` à `image_10`). | IMAGE | Oui | 1 à 10 images |

### Remarques

- Au moins une image de référence est requise ; le nœud déclenche une erreur si aucune n'est fournie.
- Au maximum 10 images de référence sont autorisées ; le nœud déclenche une erreur si davantage sont fournies.
- La taille encodée totale de toutes les images de référence ne doit pas dépasser 10 Mo ; le nœud déclenche une erreur si la limite est dépassée.
- Chaque image de référence est réduite à 2048×2048 pixels au maximum et encodée en WebP avant d'être envoyée à l'API Recraft.
- Les modèles se terminant par `_vector` créent des styles vectoriels ; les autres options créent des styles raster. Les modèles Standard et Pro partagent les mêmes pools de styles au sein de chaque type de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `style_id` | Identifiant unique du style créé, utilisable avec tous les modèles Recraft V4 et V4.1 du même type de sortie. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/fr.md)

---
**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`
