> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/fr.md)

# SaveImageAdvanced

Le nœud **SaveImageAdvanced** enregistre des images dans votre répertoire de sortie ComfyUI avec un contrôle avancé sur le format de fichier, la profondeur de bits et l'espace colorimétrique. Il prend en charge l'enregistrement au format PNG ou EXR et peut intégrer les métadonnées du workflow dans les fichiers sauvegardés.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `images` | IMAGE | Oui | - | Les images à enregistrer. |
| `préfixe_nom_fichier` | STRING | Oui | - | Le préfixe pour le fichier à enregistrer. Peut inclure des jetons de formatage tels que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%`. (par défaut : "ComfyUI") |
| `format` | COMBO | Oui | `"png"`<br>`"exr"` | Le format de fichier dans lequel enregistrer l'image. La sélection d'un format révèle des options supplémentaires pour ce format. |
| `bit_depth` | COMBO | Oui (conditionnel) | Pour PNG : `"8-bit"`<br>`"16-bit"`<br>Pour EXR : `"32-bit float"` | La profondeur de bits pour le format sélectionné. Ce paramètre apparaît lorsqu'un format est choisi. (par défaut : "8-bit" pour PNG, "32-bit float" pour EXR) |
| `input_color_space` | COMBO | Oui (conditionnel) | Pour PNG : `"sRGB"`<br>Pour EXR : `"sRGB"`<br>`"HDR"`<br>`"linear"` | Espace colorimétrique du tenseur d'entrée. Pour PNG, seul sRGB est disponible. Pour EXR, l'image est toujours écrite en lumière scène-linéaire dans le gamut correspondant. (par défaut : "sRGB") |

**Remarques sur les dépendances des paramètres :**
- Les paramètres `bit_depth` et `input_color_space` ne sont disponibles que lorsqu'un `format` spécifique est sélectionné.
- Pour le format PNG, seules les profondeurs de bits "8-bit" et "16-bit" sont disponibles, et uniquement l'espace colorimétrique "sRGB".
- Pour le format EXR, seule la profondeur de bits "32-bit float" est disponible, avec les espaces colorimétriques "sRGB", "HDR" ou "linear".
- Le paramètre `input_color_space` pour EXR détermine comment le tenseur d'entrée est interprété :
  - `"sRGB"` — l'entrée est en Rec.709 encodé sRGB ; l'EOTF sRGB inverse est appliquée.
  - `"HDR"` — l'entrée est en Rec.2020 (BT.2100) encodé HLG ; l'OETF HLG inverse est appliquée pour obtenir une lumière scène-linéaire.
  - `"linear"` — l'entrée est déjà scène-linéaire (primaires Rec.709) ; écrite sans modification. Utilisez cette option pour les sorties de rendu/composition.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `images` | IMAGE | Une liste des résultats d'images enregistrées, contenant chacun le nom du fichier, le sous-dossier et le type ("output"). Cette sortie est utilisée à des fins d'affichage dans l'interface utilisateur. |

---
**Source fingerprint (SHA-256):** `61e52bab8c28437cf648e4790823c15dbe0f758478635b0bd8b5cce785421fe5`
