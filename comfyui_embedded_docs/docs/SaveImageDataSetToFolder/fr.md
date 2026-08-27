# Enregistrer l'ensemble d'images dans un dossier

Ce nœud enregistre une liste d’images dans un dossier spécifié à l’intérieur du répertoire de sortie de ComfyUI. Il écrit chaque image sur le disque sous forme de fichier PNG en utilisant un préfixe de nom de fichier configurable. Ce nœud est obsolète et remplacé par les nœuds Save Image existants, où le dossier cible peut être spécifié dans le préfixe du nom de fichier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Liste des images à enregistrer. | IMAGE | Oui | N/A |
| `folder_name` | Nom du dossier dans lequel enregistrer les images (à l’intérieur du répertoire de sortie). Par défaut : « dataset ». | STRING | Non | N/A |
| `filename_prefix` | Préfixe pour les noms de fichiers des images enregistrées. Par défaut : « image ». Paramètre avancé. | STRING | Non | N/A |
| `mode` | Indique si les fichiers existants doivent être écrasés ou si les noms de fichiers doivent être incrémentés pour éviter tout écrasement. Par défaut : « overwrite ». | COMBO | Non | "overwrite"<br>"increment" |

**Remarques :**

- L’entrée `images` est une liste, donc plusieurs images peuvent être enregistrées en une seule exécution.
- Les paramètres `folder_name`, `filename_prefix` et `mode` sont des valeurs scalaires ; si une liste est connectée, seule la première valeur de cette liste est utilisée.
- Le paramètre `folder_name` doit correspondre à un emplacement situé à l’intérieur du répertoire de sortie de ComfyUI. Les valeurs qui sortent du répertoire de sortie (par exemple, les chemins contenant `..` ou les chemins absolus) sont rejetées avec une erreur.
- En mode « overwrite », les fichiers sont enregistrés sous les noms `{prefix}_00000.png`, `{prefix}_00001.png`, etc., en remplaçant les fichiers existants. En mode « increment », un compteur est inséré dans le nom de fichier afin que les fichiers existants ne soient pas écrasés.

## Sorties

Ce nœud n’a pas de sorties. C’est un nœud de sortie qui effectue une opération d’enregistrement sur le système de fichiers.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/fr.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
