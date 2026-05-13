> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/fr.md)

Le nœud `CLIP Vision Encode` est un nœud d'encodage d'image dans ComfyUI, utilisé pour convertir les images d'entrée en vecteurs de caractéristiques visuelles via le modèle CLIP Vision. Ce nœud constitue un pont important entre la compréhension d'image et de texte, et est largement utilisé dans divers flux de travail de génération et de traitement d'images par IA.

**Fonctionnalité du nœud**

- **Extraction de caractéristiques d'image** : Convertit les images d'entrée en vecteurs de caractéristiques haute dimension
- **Passerelle multimodale** : Fournit une base pour le traitement conjoint d'images et de texte
- **Génération conditionnelle** : Fournit des conditions visuelles pour la génération conditionnelle basée sur l'image

## Entrées

| Nom du paramètre | Type de données | Description                                                      |
| ---------------- | --------------- | ---------------------------------------------------------------- |
| `clip_vision`    | CLIP_VISION     | Modèle de vision CLIP, généralement chargé via le nœud CLIPVisionLoader |
| `image`          | IMAGE           | L'image d'entrée à encoder                                       |
| `crop`           | Menu déroulant  | Méthode de recadrage de l'image, options : center (recadrage centré), none (pas de recadrage) |

## Sorties

| Nom de la sortie        | Type de données      | Description                |
| ----------------------- | -------------------- | -------------------------- |
| CLIP_VISION_OUTPUT      | CLIP_VISION_OUTPUT   | Caractéristiques visuelles encodées |

Cet objet de sortie contient :

- `last_hidden_state` : Le dernier état caché
- `image_embeds` : Vecteur d'incorporation d'image
- `penultimate_hidden_states` : L'avant-dernier état caché
- `mm_projected` : Résultat de projection multimodale (si disponible)