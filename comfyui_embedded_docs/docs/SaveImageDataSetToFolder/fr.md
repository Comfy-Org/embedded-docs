# Enregistrer l'ensemble d'images dans un dossier

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/en.md)

Ce nœud enregistre une liste d'images dans un dossier spécifié à l'intérieur du répertoire de sortie de ComfyUI. Il prend plusieurs images en entrée et les écrit sur le disque avec un préfixe de nom de fichier personnalisable.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Liste d'images à enregistrer. | IMAGE | Oui | N/A |
| `folder_name` | Nom du dossier dans lequel enregistrer les images (à l'intérieur du répertoire de sortie). La valeur par défaut est "dataset". | STRING | Non | N/A |
| `filename_prefix` | Préfixe pour les noms de fichiers des images enregistrées. La valeur par défaut est "image". | STRING | Non | N/A |

**Remarque :** L'entrée `images` est une liste, ce qui signifie qu'elle peut recevoir et traiter plusieurs images à la fois. Les paramètres `folder_name` et `filename_prefix` sont des valeurs scalaires ; si une liste est connectée, seule la première valeur de cette liste sera utilisée.

## Sorties

Ce nœud n'a aucune sortie. Il s'agit d'un nœud de sortie qui effectue une opération d'enregistrement sur le système de fichiers.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/fr.md)

---
**Source fingerprint (SHA-256):** `65c7905caa8ff2811054bec2830c1359d0c441b5d93f50bc4d0bf10645046556`
