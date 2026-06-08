Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

## Aperçu

Détecte les visages dans une image et identifie 468 points de repère faciaux (points clés) sur chaque visage à l'aide des modèles BlazeFace et FaceMesh de MediaPipe. Il calcule également les coefficients de mélange de formes ARKit-52 pour l'analyse des expressions faciales. Le nœud peut traiter plusieurs images par lot et produit à la fois les données des points de repère et les boîtes englobantes pour chaque visage détecté.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `face_detection_model` | Le modèle de détection de visage MediaPipe à utiliser pour la détection des points de repère. | FACE_DETECTION_MODEL | Oui |  |
| `image` | L'image d'entrée ou le lot d'images dans lequel détecter des visages. | IMAGE | Oui |  |
| `detector_variant` | Portée du détecteur de visage. `"short"` est optimisé pour les visages rapprochés (à moins d'environ 2 m de la caméra) ; `"full"` couvre les visages plus éloignés/plus petits (jusqu'à environ 5 m) mais est plus lent. `"both"` exécute les deux détecteurs et conserve celui qui a trouvé le plus de visages par image (coût de détection environ 2x). Par défaut : `"short"`. | COMBO | Oui | `"short"`<br>`"full"`<br>`"both"` |
| `num_faces` | Nombre maximum de visages à retourner par image. 0 signifie aucune limite (retourner tous les visages détectés). Par défaut : 1. | INT | Oui | 0 à 16 |
| `min_confidence` | Seuil de score BlazeFace. Des valeurs plus faibles aident à détecter les petits visages ou les visages partiellement masqués. Par défaut : 0,5. | FLOAT | Non | 0,00 à 1,00 |
| `missing_frame_fallback` | Comportement par image lorsque la détection échoue dans un lot. `"empty"` laisse l'image sans visage. `"previous"` copie la détection réussie la plus récente. `"interpolate"` interpole linéairement les points de repère/boîtes englobantes/formes de mélange entre les images réussies encadrantes. Multi-visage : apparie les visages entre les images par un algorithme glouton du plus proche voisin du centre de la boîte englobante. Par défaut : `"empty"`. | COMBO | Non | `"empty"`<br>`"previous"`<br>`"interpolate"` |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `bboxes` | Une sortie structurée contenant les résultats de détection de visage par image, incluant 468 points de repère faciaux, les coefficients de mélange de formes ARKit-52, les matrices de transformation et les ensembles de connexions pour la visualisation du maillage. | FACE_LANDMARKS |
| `bboxes` | Une liste de boîtes englobantes pour chaque visage détecté, avec les coordonnées (x, y, largeur, hauteur), l'étiquette "face" et le score de confiance. Une liste par image d'entrée. | BOUNDING_BOX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceLandmarker/fr.md)

---
**Source fingerprint (SHA-256):** `f60ed6201288a59d65d62cc98c12f227a353870c36decea8da81a063cfdf2bba`
