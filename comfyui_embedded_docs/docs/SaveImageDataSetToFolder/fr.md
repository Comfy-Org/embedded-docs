# Enregistrer l'ensemble d'images dans un dossier

Ce nœud enregistre une liste d'images sous forme de fichiers PNG dans un dossier spécifié à l'intérieur du répertoire de sortie de ComfyUI. Il est obsolète : il est redondant et remplacé par les nœuds Save Image existants, où le dossier cible peut être spécifié dans le préfixe du nom de fichier. Le nœud écrit chaque image reçue sur le disque à l'aide d'un préfixe de nom de fichier personnalisable, et peut soit écraser les fichiers existants, soit générer des noms de fichiers incrémentés pour éviter l'écrasement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Liste d'images à enregistrer. | IMAGE | Oui | N/A |
| `folder_name` | Nom du dossier dans lequel enregistrer les images (à l'intérieur du répertoire de sortie). La valeur par défaut est "dataset". | STRING | Non | N/A |
| `filename_prefix` | Préfixe pour les noms de fichiers des images enregistrées. La valeur par défaut est "image". | STRING | Non | N/A |
| `mode` | Indique s'il faut écraser les fichiers existants ou incrémenter les noms de fichiers pour éviter l'écrasement. La valeur par défaut est "overwrite". | COMBO | Non | "overwrite"<br>"increment" |

**Remarque :** L'entrée `images` est une liste, ce qui signifie qu'elle peut recevoir et traiter plusieurs images à la fois. Toutes les entrées sont reçues sous forme de listes ; pour `folder_name`, `filename_prefix` et `mode`, seule la première valeur de la liste connectée est utilisée. Le `folder_name` doit correspondre à un dossier situé dans le répertoire de sortie de ComfyUI — les noms de dossiers qui en sortent (par exemple en utilisant "..", un chemin absolu ou une lettre de lecteur) sont rejetés avec une erreur. Les images sont toujours enregistrées au format PNG. Le paramètre `filename_prefix` est une option avancée.

## Sorties

Ce nœud n'a aucune sortie de données. C'est un nœud de sortie qui effectue une opération de sauvegarde sur le système de fichiers.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/fr.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
