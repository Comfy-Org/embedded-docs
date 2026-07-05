# Render Splat

Rendu d'un splat gaussien sous forme d'image à l'aide d'un rastériseur EWA anisotrope avec des splats elliptiques orientés, anti-crénelage et rendu avant-arrière trié par profondeur. La caméra provient d'une entrée `camera_info`, ou vous pouvez la laisser vide pour un cadrage automatique du splat. Définissez un nombre d'images supérieur à 1 pour un lot d'images en rotation destiné à un nœud Vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat` | Les données du splat gaussien à rendre | SPLAT | Oui | - |
| `largeur` | Largeur de l'image de sortie (par défaut : 1024) | INT | Oui | 64 à 2048 (pas : 8) |
| `hauteur` | Hauteur de l'image de sortie (par défaut : 1024) | INT | Oui | 64 à 2048 (pas : 8) |
| `images` | Nombre d'images à rendre. -1, 0 ou 1 produit une seule image fixe. Les valeurs supérieures à 1 créent une animation rotative où la caméra orbite sur un tour complet de 360 degrés. Les valeurs négatives orbitent dans la direction opposée (par défaut : 1) | INT | Oui | -240 à 240 |
| `échelle_splat` | Multiplicateur de l'empreinte projetée de chaque splat. Les valeurs faibles produisent des points plus nets, les valeurs élevées produisent des surfaces plus douces et plus pleines (par défaut : 1.0) | FLOAT | Oui | 0.1 à 5.0 (pas : 0.05) |
| `accentuer` | Contrôle la netteté des splats qui se chevauchent. Une valeur de 1.0 donne un mélange physiquement correct. Les valeurs supérieures à 1.0 orientent chaque pixel vers son splat dominant (le plus proche) pour une texture plus nette sans réduire la taille des splats ni créer d'espaces vides (par défaut : 2.0) | FLOAT | Oui | 1.0 à 8.0 (pas : 0.5) |
| `ombrage_phare` | Ombrage diffus provenant d'une lumière à la position de la caméra, utilisant les normales des surfels du splat. Assombrit les surfaces qui s'éloignent de la vue pour révéler la forme et la courbure. 0 donne un albédo plat, 1 donne l'ombrage le plus fort (par défaut : 0.0) | FLOAT | Oui | 0.0 à 3.0 (pas : 0.05) |
| `seuil_opacité` | Supprime les gaussiennes dont l'opacité est inférieure à ce seuil, ce qui élimine les éléments flottants faibles (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `style_rendu` | Ce que montre la sortie d'image. Options : color (rendu couleur complet), clay (ombrage à albédo neutre), depth (objets proches apparaissent lumineux), normal (carte normale OpenGL) (par défaut : "color") | COMBO | Oui | "color"<br>"clay"<br>"depth"<br>"normal" |
| `arrière-plan` | Couleur d'arrière-plan unie pour le rendu (par défaut : #000000) | COLOR | Oui | - |
| `image_fond` | Fond optionnel composé derrière le splat. Remplace la couleur d'arrière-plan unie. Redimensionné à la taille du rendu. Un lot d'images est utilisé par image, une seule image est utilisée pour toutes les images. Fonctionne uniquement avec les styles de rendu color et clay | IMAGE | Non | - |
| `camera_info` | Caméra pour effectuer le rendu. Peut provenir d'un nœud Load3D, Preview3D ou Create Camera Info. Si vide, le splat est automatiquement cadré depuis une vue 3/4 par défaut | CAMERA_3D | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image rendue du splat gaussien | IMAGE |
| `mask` | Le masque alpha du splat rendu | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderSplat/fr.md)

---
**Source fingerprint (SHA-256):** `038bd9fb032f347ecda665c03719a64b0cf907599b701606f5cf6d0606d19d98`
