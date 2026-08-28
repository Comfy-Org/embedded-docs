# MaskPreview

Le nœud MaskPreview affiche un aperçu visuel des données de masque directement dans l'interface ComfyUI, sans les enregistrer dans le répertoire de sortie. Cela vous permet d'inspecter les valeurs exactes du masque à n'importe quel point de votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mask` | Les données de masque à prévisualiser | MASK | Oui | - |
| `filename_prefix` | Préfixe pour le nom de fichier de l'aperçu (par défaut : "ComfyUI") | STRING | Non | - |
| `prompt` | Informations de prompt pour les métadonnées (fournies automatiquement) | PROMPT | Non | - |
| `extra_pnginfo` | Informations PNG supplémentaires pour les métadonnées (fournies automatiquement) | EXTRA_PNGINFO | Non | - |

Les entrées `prompt` et `extra_pnginfo` sont masquées et sont fournies automatiquement par le système ComfyUI ; vous n'avez pas besoin de les connecter manuellement.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mask` | Les données de masque qui ont été prévisualisées, renvoyées inchangées pour une utilisation ultérieure dans le flux de travail | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/fr.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
