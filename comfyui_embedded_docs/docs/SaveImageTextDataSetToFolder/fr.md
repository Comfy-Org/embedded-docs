# Enregistrer l'ensemble d'images et de textes dans un dossier

Save Image-Text (to Folder) enregistre une liste d'images et leurs légendes textuelles correspondantes dans un dossier spécifié à l'intérieur du répertoire de sortie de ComfyUI. Pour chaque image enregistrée en fichier PNG, un fichier TXT correspondant portant le même nom de base est créé pour stocker sa légende, ce qui est utile pour créer des jeux de données organisés d'images générées associées à leurs descriptions.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Liste d'images à enregistrer. | IMAGE | Oui | - |
| `texts` | Liste de légendes textuelles à enregistrer. Cette entrée est facultative. | STRING | Non | - |
| `folder_name` | Nom du dossier dans lequel enregistrer les images (dans le répertoire de sortie). (défaut : "dataset") | STRING | Oui | - |
| `filename_prefix` | Préfixe pour les noms de fichiers des images enregistrées. (défaut : "image") | STRING | Oui | - |
| `mode` | Indique s'il faut écraser les fichiers existants ou incrémenter les noms de fichiers pour éviter tout écrasement. (défaut : "overwrite") | COMBO | Oui | "overwrite"<br>"increment" |

**Remarque :** L'entrée `images` est une liste. L'entrée `texts` est facultative ; si elle est fournie, elle doit être une liste de légendes textuelles et doit contenir le même nombre d'éléments que `images`. Chaque légende est enregistrée dans un fichier `.txt` correspondant à son image associée. En mode `overwrite`, les fichiers sont nommés `{filename_prefix}_{index}.png` et remplacent tout fichier existant portant le même nom. En mode `increment`, un compteur unique est ajouté aux noms de fichiers afin que les fichiers existants ne soient pas écrasés. Le `folder_name` doit correspondre à un chemin situé dans le répertoire de sortie ; les noms de dossier qui tentent d'en sortir (par exemple avec `..`) sont rejetés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| - | Ce nœud ne renvoie aucune donnée. Il enregistre les fichiers directement dans le système de fichiers. | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/fr.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
