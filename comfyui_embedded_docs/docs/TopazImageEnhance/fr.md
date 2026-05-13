> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/fr.md)

Le nœud Topaz Image Enhance offre une mise à l'échelle et une amélioration d'image de qualité professionnelle. Il traite une seule image d'entrée à l'aide d'un modèle d'IA basé sur le cloud pour améliorer la qualité, les détails et la résolution. Le nœud permet un contrôle précis du processus d'amélioration, notamment des options pour l'orientation créative, la concentration sur le sujet et la préservation des visages.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"Reimagine"` | Le modèle d'IA à utiliser pour l'amélioration d'image. |
| `image` | IMAGE | Oui | - | L'image d'entrée à améliorer. Une seule image est prise en charge. |
| `prompt` | STRING | Non | - | Une invite textuelle facultative pour guider la mise à l'échelle créative (par défaut : vide). |
| `subject_detection` | COMBO | Non | `"All"`<br>`"Foreground"`<br>`"Background"` | Contrôle la partie de l'image sur laquelle l'amélioration se concentre (par défaut : "All"). |
| `face_enhancement` | BOOLEAN | Non | - | Activer pour améliorer les visages s'ils sont présents dans l'image (par défaut : True). |
| `face_enhancement_creativity` | FLOAT | Non | 0,0 - 1,0 | Définit le niveau de créativité pour l'amélioration des visages (par défaut : 0,0). |
| `face_enhancement_strength` | FLOAT | Non | 0,0 - 1,0 | Contrôle le degré de netteté des visages améliorés par rapport à l'arrière-plan (par défaut : 1,0). |
| `crop_to_fill` | BOOLEAN | Non | - | Par défaut, l'image est mise en boîte aux lettres lorsque le rapport hauteur/largeur de sortie diffère. Activez cette option pour recadrer l'image afin de remplir les dimensions de sortie (par défaut : False). |
| `output_width` | INT | Non | 0 - 32000 | La largeur souhaitée de l'image de sortie. Une valeur de 0 signifie qu'elle sera calculée automatiquement, généralement en fonction de la taille d'origine ou de la `output_height` si spécifiée (par défaut : 0). |
| `output_height` | INT | Non | 0 - 32000 | La hauteur souhaitée de l'image de sortie. Une valeur de 0 signifie qu'elle sera calculée automatiquement, généralement en fonction de la taille d'origine ou de la `output_width` si spécifiée (par défaut : 0). |
| `creativity` | INT | Non | 1 - 9 | Contrôle le niveau de créativité global de l'amélioration (par défaut : 3). |
| `face_preservation` | BOOLEAN | Non | - | Préserver l'identité faciale des sujets dans l'image (par défaut : True). |
| `color_preservation` | BOOLEAN | Non | - | Préserver les couleurs d'origine de l'image d'entrée (par défaut : True). |

**Remarque :** Ce nœud ne peut traiter qu'une seule image d'entrée. La fourniture d'un lot de plusieurs images entraînera une erreur.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image de sortie améliorée. |

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`
