# Enregistrer l’image (Avancé)

Le nœud **SaveImageAdvanced** enregistre des images dans votre répertoire de sortie ComfyUI avec un contrôle avancé sur le format de fichier, la profondeur de bits et l'espace colorimétrique. Il prend en charge l'enregistrement au format PNG ou EXR et peut intégrer des métadonnées de workflow dans les fichiers enregistrés.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Les images à enregistrer. | IMAGE | Oui | - |
| `filename_prefix` | Le préfixe du fichier à enregistrer. Peut inclure des jetons de formatage tels que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (défaut : « ComfyUI ») | STRING | Oui | - |
| `format` | Le format de fichier dans lequel enregistrer l'image. La sélection d'un format révèle des options supplémentaires pour ce format. | DYNAMIC_COMBO | Oui | `"png"`<br>`"exr"` |

### Entrées PNG

Ces entrées sont affichées lorsque `format` est défini sur `"png"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `bit_depth` | La profondeur de bits utilisée lors de l'enregistrement de l'image. (défaut : « 8-bit ») | COMBO | Oui (conditionnel) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | L'espace colorimétrique du tenseur d'entrée. (défaut : « sRGB ») | COMBO | Oui (conditionnel) | `"sRGB"` |

### Entrées EXR

Ces entrées sont affichées lorsque `format` est défini sur `"exr"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `bit_depth` | La profondeur de bits utilisée lors de l'enregistrement de l'image. (défaut : « 32-bit float ») | COMBO | Oui (conditionnel) | `"32-bit float"` |
| `input_color_space` | Espace colorimétrique du tenseur d'entrée. Le fichier EXR est toujours écrit en linéaire de scène dans le gamut correspondant. (défaut : « sRGB ») | COMBO | Oui (conditionnel) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Remarques sur les dépendances des paramètres et le comportement des fichiers :**

- `bit_depth` et `input_color_space` n'apparaissent que lorsque leur paramètre parent `format` est sélectionné.
- Pour le format PNG, seules les profondeurs de bits `"8-bit"` et `"16-bit"` sont disponibles, ainsi que le seul espace colorimétrique `"sRGB"`. La sélection de l'espace colorimétrique ne modifie pas les pixels PNG — les fichiers PNG sont toujours enregistrés en tant qu'images encodées sRGB.
- Pour le format EXR, seule la profondeur de bits `"32-bit float"` est disponible, avec les espaces colorimétriques `"sRGB"`, `"HDR"` ou `"linear"`.
- Le paramètre `input_color_space` pour EXR détermine comment le tenseur d'entrée est interprété avant l'enregistrement :
  - `"sRGB"` — l'entrée est encodée sRGB Rec.709 ; l'EOTF sRGB inverse est appliquée.
  - `"HDR"` — l'entrée est encodée HLG Rec.2020 (BT.2100) ; l'OETF HLG inverse est appliquée pour obtenir une lumière linéaire de scène.
  - `"linear"` — l'entrée est déjà en linéaire de scène (primaires Rec.709) ; écrite telle quelle. Utilisez ceci pour la sortie d'un moteur de rendu / compositeur.
- Les métadonnées de workflow (prompt et informations PNG supplémentaires) sont intégrées dans les fichiers PNG et EXR enregistrés, sauf si l'écriture des métadonnées est désactivée avec l'argument de ligne de commande `--disable-metadata`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images qui ont été enregistrées (les mêmes images transmises à l'entrée `images`). Le résultat de l'interface du nœud comprend une liste des fichiers enregistrés, chacun avec son nom de fichier, son sous-dossier et son type (« output »). | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/fr.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
