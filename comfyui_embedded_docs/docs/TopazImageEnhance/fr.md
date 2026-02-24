> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/fr.md)

Le nœud Topaz Image Enhance offre un suréchantillonnage et une amélioration d'image de qualité industrielle. Il traite une seule image d'entrée en utilisant un modèle d'IA basé sur le cloud pour améliorer la qualité, les détails et la résolution. Le nœud propose un contrôle précis du processus d'amélioration, avec des options pour le guidage créatif, la mise au point sur le sujet et la préservation des visages.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"Reimagine"` | Le modèle d'IA à utiliser pour l'amélioration de l'image. |
| `image` | IMAGE | Oui | - | L'image d'entrée à améliorer. Une seule image est prise en charge. |
| `prompt` | STRING | Non | - | Une consigne textuelle optionnelle pour guider le suréchantillonnage créatif (par défaut : vide). |
| `subject_detection` | COMBO | Non | `"All"`<br>`"Foreground"`<br>`"Background"` | Contrôle la partie de l'image sur laquelle se concentre l'amélioration (par défaut : "All"). |
| `face_enhancement` | BOOLEAN | Non | - | Activez pour améliorer les visages s'ils sont présents dans l'image (par défaut : True). |
| `face_enhancement_creativity` | FLOAT | Non | 0.0 - 1.0 | Définit le niveau de créativité pour l'amélioration des visages (par défaut : 0.0). |
| `face_enhancement_strength` | FLOAT | Non | 0.0 - 1.0 | Contrôle la netteté des visages améliorés par rapport à l'arrière-plan (par défaut : 1.0). |
| `crop_to_fill` | BOOLEAN | Non | - | Par défaut, l'image est encadrée (letterbox) lorsque le rapport d'aspect de sortie diffère. Activez pour recadrer l'image afin de remplir les dimensions de sortie à la place (par défaut : False). |
| `output_width` | INT | Non | 0 - 32000 | La largeur souhaitée de l'image de sortie. Une valeur de 0 signifie qu'elle sera calculée automatiquement, généralement en fonction de la taille originale ou de la `output_height` si elle est spécifiée (par défaut : 0). |
| `output_height` | INT | Non | 0 - 32000 | La hauteur souhaitée de l'image de sortie. Une valeur de 0 signifie qu'elle sera calculée automatiquement, généralement en fonction de la taille originale ou de la `output_width` si elle est spécifiée (par défaut : 0). |
| `creativity` | INT | Non | 1 - 9 | Contrôle le niveau de créativité global de l'amélioration (par défaut : 3). |
| `face_preservation` | BOOLEAN | Non | - | Préserve l'identité faciale des sujets dans l'image (par défaut : True). |
| `color_preservation` | BOOLEAN | Non | - | Préserve les couleurs originales de l'image d'entrée (par défaut : True). |

**Note :** Ce nœud ne peut traiter qu'une seule image d'entrée. Fournir un lot de plusieurs images entraînera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | L'image de sortie améliorée. |
