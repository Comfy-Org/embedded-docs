> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/fr.md)

Ce nœud enregistre une liste d'images dans un dossier spécifié au sein du répertoire de sortie de ComfyUI. Il prend plusieurs images en entrée et les écrit sur le disque avec un préfixe de nom de fichier personnalisable.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Oui | N/A | Liste des images à enregistrer. |
| `folder_name` | STRING | Non | N/A | Nom du dossier dans lequel enregistrer les images (à l'intérieur du répertoire de sortie). La valeur par défaut est "dataset". |
| `filename_prefix` | STRING | Non | N/A | Préfixe pour les noms de fichiers des images enregistrées. La valeur par défaut est "image". |

**Note :** L'entrée `images` est une liste, ce qui signifie qu'elle peut recevoir et traiter plusieurs images à la fois. Les paramètres `folder_name` et `filename_prefix` sont des valeurs scalaires ; si une liste est connectée, seule la première valeur de cette liste sera utilisée.

## Sorties

Ce nœud ne possède aucune sortie. C'est un nœud de sortie qui effectue une opération d'enregistrement sur le système de fichiers.
