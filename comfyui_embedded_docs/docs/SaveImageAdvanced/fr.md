# Enregistrer l’image (Avancé)

Le nœud **Save Image (Advanced)** enregistre les images d'entrée dans votre répertoire de sortie ComfyUI avec un contrôle avancé du format de fichier, de la profondeur de bits et de l'espace colorimétrique. Il prend en charge l'enregistrement en fichiers PNG, EXR ou AVIF (y compris AVIF animé) et peut intégrer les métadonnées du workflow dans les fichiers enregistrés.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images à enregistrer. | IMAGE | Oui | - |
| `préfixe_nom_fichier` | Le préfixe pour le fichier à enregistrer. Peut inclure des jetons de formatage tels que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (par défaut : "ComfyUI") | STRING | Oui | - |
| `format` | Le format de fichier dans lequel enregistrer l'image. La sélection d'un format révèle des options supplémentaires pour ce format. | DYNAMIC_COMBO | Oui | `"png"`<br>`"exr"`<br>`"avif"` |

### Entrées PNG

Ces options apparaissent lorsque `format` est défini sur `"png"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits pour le fichier PNG enregistré. (par défaut : "8-bit") | COMBO | Oui (conditionnel) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espace colorimétrique du tenseur d'entrée. Seul sRGB est disponible pour le format PNG. (par défaut : "sRGB") | COMBO | Oui (conditionnel) | `"sRGB"` |

### Entrées EXR

Ces options apparaissent lorsque `format` est défini sur `"exr"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits pour le fichier EXR enregistré. (par défaut : "32-bit float") | COMBO | Oui (conditionnel) | `"32-bit float"` |
| `input_color_space` | Espace colorimétrique du tenseur d'entrée. L'EXR est toujours écrit en scène-linéaire dans la gamme correspondante.<br>`"sRGB"` — l'entrée est en Rec.709 codé sRGB ; l'EOTF sRGB inverse est appliquée.<br>`"HDR"` — l'entrée est en Rec.2020 (BT.2100) codé HLG ; l'OETF HLG inverse est appliquée pour obtenir une lumière scène-linéaire.<br>`"linear"` — l'entrée est déjà en scène-linéaire (primaires Rec.709) ; écrite telle quelle. Utilisez ceci pour la sortie de moteur de rendu/composition. (par défaut : "sRGB") | COMBO | Oui (conditionnel) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

### Entrées AVIF

Ces options apparaissent lorsque `format` est défini sur `"avif"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits pour le fichier AVIF enregistré. Auto utilise du YUV420 8 bits pour sRGB et du YUV420 10 bits pour HDR. (par défaut : "auto") | COMBO | Oui (conditionnel) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Espace colorimétrique des images d'entrée. HDR sélectionne BT.2020/HLG et HDR PQ sélectionne BT.2020/PQ. (par défaut : "sRGB") | COMBO | Oui (conditionnel) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Des valeurs plus faibles produisent une qualité supérieure et des fichiers plus volumineux. (par défaut : 18) | INT | Oui (conditionnel) | 1 à 63 |
| `save_mode` | Le mode d'enregistrement pour le fichier AVIF. `"still images"` enregistre chaque image du lot comme un fichier fixe distinct ; `"animated"` enregistre le lot entier comme un seul fichier AVIF animé et révèle `fps` et `loop_count`. (par défaut : "still images") | DYNAMIC_COMBO | Oui (conditionnel) | `"still images"`<br>`"animated"` |

### Options d'animation AVIF

Ces options apparaissent lorsque `save_mode` est défini sur `"animated"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `fps` | La fréquence d'images de l'animation. (par défaut : 6.0) | FLOAT | Oui (conditionnel) | 0.01 à 1000.0 |
| `loop_count` | Nombre de boucles de l'animation. 0 boucle indéfiniment. (par défaut : 0) | INT | Oui (conditionnel) | 0 à 1000 |

**Remarques sur les dépendances des paramètres :**
- Les paramètres spécifiques au format (`bit_depth`, `input_color_space`, et pour AVIF aussi `crf` et `save_mode`) ne sont disponibles que lorsqu'un `format` spécifique est sélectionné.
- Pour le format PNG, seules les profondeurs de bits "8-bit" et "16-bit" sont disponibles, et seul l'espace colorimétrique "sRGB".
- Pour le format EXR, seule la profondeur de bits "32-bit float" est disponible, avec les espaces colorimétriques "sRGB", "HDR" ou "linear".
- Pour le format AVIF, `fps` et `loop_count` ne sont disponibles que lorsque `save_mode` est défini sur `"animated"`.
- Les images PNG et EXR doivent avoir 1 (nuances de gris), 3 (RVB) ou 4 (RGBA) canaux ; les autres nombres de canaux ne sont pas pris en charge et génèrent une erreur.
- L'AVIF ne prend en charge que les images en nuances de gris à 1 canal et les images RVB à 3 canaux ; les images RGBA (alpha) ne sont pas prises en charge et génèrent une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Les images d'entrée, transmises tell quelles. La sortie UI du nœud fournit une liste des résultats d'images enregistrées, chacun contenant le nom de fichier, le sous-dossier et le type ("output"). | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `d3df3caca99d58d973d0bc2ff7c22c4626185d390ec2acf870d4014331c4c335`
