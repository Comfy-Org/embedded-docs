> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/fr.md)

Le nœud MaskPreview génère un aperçu visuel d'un masque en le convertissant en format image 3 canaux et en le sauvegardant comme fichier temporaire. Il prend un masque en entrée et le reformate dans un format adapté à l'affichage d'image, puis sauvegarde le résultat dans le répertoire temporaire avec un préfixe de nom de fichier aléatoire. Cela permet aux utilisateurs d'inspecter visuellement les données de masque pendant l'exécution du flux de travail.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `mask` | MASK | Oui | - | Les données de masque à visualiser et convertir en format image |
| `filename_prefix` | STRING | Non | - | Préfixe pour le nom de fichier de sortie (par défaut : "ComfyUI") |
| `prompt` | PROMPT | Non | - | Informations de prompt pour les métadonnées (fournies automatiquement) |
| `extra_pnginfo` | EXTRA_PNGINFO | Non | - | Informations PNG supplémentaires pour les métadonnées (fournies automatiquement) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `ui` | DICT | Contient les informations de l'image d'aperçu et les métadonnées pour l'affichage |