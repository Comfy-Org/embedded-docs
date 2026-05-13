> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/fr.md)

Le nœud MaskPreview enregistre les données de masque sous forme d'image d'aperçu dans votre répertoire de sortie ComfyUI, vous permettant d'inspecter visuellement les données de masque pendant l'exécution du workflow. Il convertit le masque d'entrée dans un format adapté à l'affichage d'image et l'enregistre avec un préfixe de nom de fichier configurable.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `mask` | MASK | Oui | - | Les données de masque à prévisualiser et à enregistrer sous forme d'image |
| `filename_prefix` | STRING | Non | - | Préfixe pour le nom du fichier de sortie (par défaut : "ComfyUI") |
| `prompt` | PROMPT | Non | - | Informations d'invite pour les métadonnées (fournies automatiquement) |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Informations PNG supplémentaires pour les métadonnées (fournies automatiquement) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `ui` | DICT | Contient les informations de l'image d'aperçu et les métadonnées pour l'affichage dans l'interface utilisateur |

---
**Source fingerprint (SHA-256):** `9f64adf4a0130368618fc1ca3655192686815ab10b4153f9552ef23149928e3f`
