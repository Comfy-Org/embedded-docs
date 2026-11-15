# Enregistrer l’image (Avancé)

Le nœud **Save Image (Advanced)** enregistre les images d’entrée dans votre répertoire de sortie ComfyUI avec un contrôle avancé du format de fichier, de la profondeur de bits et de l’espace colorimétrique. Il prend en charge l’enregistrement aux formats PNG, EXR ou AVIF (y compris AVIF animé) et peut intégrer les métadonnées du workflow dans les fichiers enregistrés.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images à enregistrer. | IMAGE | Oui | - |
| `filename_prefix` | Le préfixe du fichier à enregistrer. Peut inclure des jetons de mise en forme tels que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (par défaut : "ComfyUI") | STRING | Oui | - |
| `format` | Le format de fichier dans lequel enregistrer l’image. La sélection d’un format révèle des options supplémentaires pour ce format. | DYNAMIC_COMBO | Oui | `"png"`<br>`"exr"`<br>`"avif"` |

### Entrées PNG

Ces options apparaissent lorsque `format` est défini sur `"png"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits du fichier PNG enregistré. (par défaut : "8-bit") | COMBO | Oui (conditionnel) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espace colorimétrique du tenseur d’entrée. Seul sRGB est disponible pour le format PNG. (par défaut : "sRGB") | COMBO | Oui (conditionnel) | `"sRGB"` |
| `channels` | Quels canaux écrire dans le PNG. `"auto"` conserve les canaux d’entrée, grayscale convertit RGB en luminosité et supprime l’alpha, RGB enregistre la couleur sans alpha, et RGBA conserve l’alpha ou en ajoute un entièrement opaque. (par défaut : `"auto"`) | COMBO | Non | `"auto"`<br>`"grayscale (1 channel)"`<br>`"RGB (3 channels)"`<br>`"RGBA (4 channels)"` |

### Entrées EXR

Ces options apparaissent lorsque `format` est défini sur `"exr"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits du fichier EXR enregistré. (par défaut : "16-bit float") | COMBO | Oui (conditionnel) | `"16-bit float"`<br>`"32-bit float"` |
| `input_color_space` | Espace colorimétrique du tenseur d’entrée. L’EXR est toujours écrit en linéaire de scène dans le gamut correspondant.<br>`"sRGB"` — l’entrée est encodée sRGB Rec.709 ; l’EOTF sRGB inverse est appliquée.<br>`"HDR"` — l’entrée est encodée HLG Rec.2020 (BT.2100) ; l’OETF HLG inverse est appliquée pour obtenir une lumière linéaire de scène.<br>`"linear"` — l’entrée est déjà linéaire de scène (primaires Rec.709) ; elle est écrite sans modification. Utilisez ceci pour la sortie d’un moteur de rendu/compositeur.<br>`"linear ACEScg"` — l’entrée est déjà linéaire de scène ACEScg (AP1 / D60) ; elle est écrite sans modification avec les chromaticités ACEScg. (par défaut : "sRGB") | COMBO | Oui (conditionnel) | `"sRGB"`<br>`"HDR"`<br>`"linear"`<br>`"linear ACEScg"` |

### Entrées AVIF

Ces options apparaissent lorsque `format` est défini sur `"avif"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits du fichier AVIF enregistré. Auto utilise YUV420 8 bits pour sRGB et YUV420 10 bits pour HDR. (par défaut : "auto") | COMBO | Oui (conditionnel) | `"auto"`<br>`"8-bit YUV420"`<br>`"10-bit YUV420"` |
| `input_color_space` | Espace colorimétrique des images d’entrée. HDR sélectionne BT.2020/HLG et HDR PQ sélectionne BT.2020/PQ. (par défaut : "sRGB") | COMBO | Oui (conditionnel) | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |
| `crf` | Des valeurs plus faibles produisent une qualité plus élevée et des fichiers plus volumineux. (par défaut : 18) | INT | Oui (conditionnel) | 1 à 63 |
| `save_mode` | Le mode d’enregistrement du fichier AVIF. `"still images"` enregistre chaque image du lot comme un fichier image fixe distinct ; `"animated"` enregistre l’ensemble du lot comme un seul fichier AVIF animé et révèle `fps` et `loop_count`. (par défaut : "still images") | DYNAMIC_COMBO | Oui (conditionnel) | `"still images"`<br>`"animated"` |

### Options AVIF animées

Ces options apparaissent lorsque `save_mode` est défini sur `"animated"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `fps` | La fréquence d’images de l’animation. (par défaut : 6.0) | FLOAT | Oui (conditionnel) | 0.01 à 1000.0 |
| `loop_count` | Nombre de fois où l’animation est lue en boucle. 0 boucle indéfiniment. (par défaut : 0) | INT | Oui (conditionnel) | 0 à 1000 |

**Remarques sur les dépendances des paramètres :**
- Les paramètres spécifiques au format (`bit_depth`, `input_color_space`, et pour AVIF également `crf` et `save_mode`) ne sont disponibles que lorsqu’un `format` spécifique est sélectionné.
- Pour le format PNG, seules les profondeurs de bits "8-bit" et "16-bit" sont disponibles, et seul l’espace colorimétrique "sRGB" est disponible.
- Pour le format EXR, les profondeurs de bits "16-bit float" et "32-bit float" sont toutes deux disponibles, avec les espaces colorimétriques "sRGB", "HDR", "linear" ou "linear ACEScg". "16-bit float" est la valeur par défaut et produit des fichiers plus petits.
- Pour le format AVIF, `fps` et `loop_count` ne sont disponibles que lorsque `save_mode` est défini sur `"animated"`.
- Les images PNG et EXR doivent avoir 1 (grayscale), 3 (RGB) ou 4 (RGBA) canaux ; les autres nombres de canaux ne sont pas pris en charge et déclenchent une erreur.
- AVIF ne prend en charge que les images grayscale à 1 canal et RGB à 3 canaux ; les images RGBA (alpha) ne sont pas prises en charge et déclenchent une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Les images d’entrée, transmises sans modification. La sortie UI du nœud fournit une liste de résultats d’images enregistrées, chacun contenant le nom de fichier, le sous-dossier et le type ("output"). Pour un AVIF animé comportant plus d’une image, la sortie UI inclut également un indicateur `animated`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `4e8a92c5f1bba35bc4cdf8c858cc9a6fe57cf08436e2dc303d8204c726108216`
