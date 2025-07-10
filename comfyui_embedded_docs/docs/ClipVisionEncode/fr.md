Le nœud `CLIP Vision Encode` dans ComfyUI est un nœud d'encodage d'image, utilisé pour convertir les images d'entrée en vecteurs de caractéristiques visuelles à l'aide du modèle CLIP Vision. Ce nœud est un pont important entre la compréhension de l'image et du texte, et il est largement utilisé dans divers flux de travail de génération et de traitement d'images par IA.

**Fonctionnalité du nœud**

- **Extraction de caractéristiques d'image** : Convertit les images d'entrée en vecteurs de caractéristiques de haute dimension
- **Pont multimodal** : Fournit une base pour le traitement conjoint de l'image et du texte
- **Génération conditionnelle** : Fournit des conditions visuelles pour la génération conditionnelle basée sur l'image

## Entrées

| Nom du paramètre | Data Type   | Description                                                      |
|------------------|------------|------------------------------------------------------------------|
| `clip_vision`    | CLIP_VISION| Modèle CLIP vision, généralement chargé via le nœud CLIPVisionLoader |
| `image`          | IMAGE      | L'image d'entrée à encoder                                       |
| `crop`           | Dropdown   | Méthode de recadrage de l'image, options : center (recadrage centré), none (pas de recadrage) |

## Sorties

| Nom de sortie         | Data Type           | Description                |
|-----------------------|--------------------|----------------------------|
| SORTIE_CLIP_VISION    | CLIP_VISION_OUTPUT | Caractéristiques visuelles encodées |

Cet objet de sortie contient :

- `last_hidden_state` : Le dernier état caché
- `image_embeds` : Vecteur d'intégration de l'image
- `penultimate_hidden_states` : L'avant-dernier état caché
- `mm_projected` : Résultat de la projection multimodale (si disponible)
