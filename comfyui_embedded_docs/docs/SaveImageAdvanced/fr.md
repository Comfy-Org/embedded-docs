# Enregistrer l’image (Avancé)

Le nœud **Save Image (Advanced)** enregistre les images d’entrée dans votre répertoire de sortie ComfyUI avec un contrôle avancé sur le format de fichier, la profondeur de bits et l’espace colorimétrique. Il prend en charge l’enregistrement en fichiers PNG ou EXR et peut intégrer les métadonnées du workflow dans les fichiers enregistrés.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images à enregistrer. | IMAGE | Oui | - |
| `préfixe_nom_fichier` | Le préfixe pour le fichier à enregistrer. Peut inclure des jetons de formatage tels que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (défaut : « ComfyUI ») | STRING | Oui | - |
| `format` | Le format de fichier dans lequel enregistrer l’image. La sélection d’un format révèle des options supplémentaires pour ce format. | DYNAMIC_COMBO | Oui | `"png"`<br>`"exr"` |

### Entrées PNG

Ces options apparaissent lorsque `format` est défini sur `"png"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits pour le fichier PNG enregistré. (défaut : « 8-bit ») | COMBO | Oui (conditionnel) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Espace colorimétrique du tenseur d’entrée. Seul le sRGB est disponible pour le format PNG. (défaut : « sRGB ») | COMBO | Oui (conditionnel) | `"sRGB"` |

### Entrées EXR

Ces options apparaissent lorsque `format` est défini sur `"exr"`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `bit_depth` | La profondeur de bits pour le fichier EXR enregistré. (défaut : « 32-bit float ») | COMBO | Oui (conditionnel) | `"32-bit float"` |
| `input_color_space` | Espace colorimétrique du tenseur d’entrée. L’EXR est toujours écrit en scène-linéaire dans le gamut correspondant.<br>`"sRGB"` — l’entrée est encodée en sRGB Rec.709 ; l’EOTF sRGB inverse est appliquée.<br>`"HDR"` — l’entrée est encodée en HLG Rec.2020 (BT.2100) ; l’OETF HLG inverse est appliquée pour obtenir une lumière scène-linéaire.<br>`"linear"` — l’entrée est déjà scène-linéaire (primaires Rec.709) ; écrite telle quelle. Utilisez ce mode pour une sortie de moteur de rendu ou de composite. (défaut : « sRGB ») | COMBO | Oui (conditionnel) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notes sur les dépendances des paramètres :**
- Les paramètres `bit_depth` et `input_color_space` ne sont disponibles que lorsqu’un `format` spécifique est sélectionné.
- Pour le format PNG, seules les profondeurs de bits « 8-bit » et « 16-bit » sont disponibles, et uniquement l’espace colorimétrique « sRGB ».
- Pour le format EXR, seule la profondeur de bits « 32-bit float » est disponible, avec les espaces colorimétriques « sRGB », « HDR » ou « linear ».
- Les images doivent avoir 1 (niveaux de gris), 3 (RGB) ou 4 (RGBA) canaux ; les autres nombres de canaux ne sont pas pris en charge et génèrent une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Les images d’entrée, transmises sans modification. La sortie UI du nœud fournit une liste des images enregistrées, chacune contenant le nom de fichier, le sous-dossier et le type (« output »). | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
