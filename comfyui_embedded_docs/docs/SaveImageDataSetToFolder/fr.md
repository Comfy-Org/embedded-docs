# Enregistrer l'ensemble d'images dans un dossier

Ce nœud enregistre une liste d'images dans un dossier spécifié à l'intérieur du répertoire de sortie de ComfyUI. Il écrit chaque image sur le disque sous forme de fichier PNG en utilisant un préfixe de nom de fichier configurable. Ce nœud est obsolète et remplacé par les nœuds Save Image existants, où le dossier cible peut être indiqué dans le préfixe du nom de fichier.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `images` | Liste des images à enregistrer. | IMAGE | Oui | N/A |
| `folder_name` | Nom du dossier dans lequel enregistrer les images (dans le répertoire de sortie). Valeur par défaut : "dataset". | STRING | Non | N/A |
| `filename_prefix` | Préfixe des noms de fichiers des images enregistrées. Valeur par défaut : "image". Paramètre avancé. | STRING | Non | N/A |
| `mode` | Indique s'il faut écraser les fichiers existants ou incrémenter les noms de fichiers pour éviter l'écrasement. Valeur par défaut : "overwrite". | COMBO | Non | "overwrite"<br>"increment" |

**Remarques :**

- L'entrée `images` est une liste, plusieurs images peuvent donc être enregistrées en une seule exécution.
- Les paramètres `folder_name`, `filename_prefix` et `mode` sont des valeurs scalaires ; si une liste est connectée, seule la première valeur de cette liste est utilisée.
- Le `folder_name` doit correspondre à un emplacement situé dans le répertoire de sortie de ComfyUI. Les valeurs qui sortent du répertoire de sortie (par exemple, les chemins contenant `..` ou les chemins absolus, les lettres de lecteur ou les échappements par lien symbolique) sont rejetées avec une erreur.
- En mode "overwrite", les fichiers sont enregistrés sous la forme `{prefix}_00000.png`, `{prefix}_00001.png`, etc., en remplaçant tout fichier existant. En mode "increment", un compteur est inséré dans le nom de fichier afin que les fichiers existants ne soient pas écrasés.
- Seule la sortie PNG est prise en charge.

## Sorties

Ce nœud n'a aucune sortie. C'est un nœud de sortie qui effectue une opération d'enregistrement dans le système de fichiers.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/fr.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
