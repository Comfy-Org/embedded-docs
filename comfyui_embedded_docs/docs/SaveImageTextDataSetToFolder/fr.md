# Enregistrer l'ensemble d'images et de textes dans un dossier

Save Image-Text (to Folder) enregistre un jeu de données composé de paires d'images et de légendes textuelles dans un dossier situé dans le répertoire de sortie de ComfyUI. Chaque image est écrite dans un fichier PNG, et sa légende correspondante est écrite dans un fichier TXT portant le même nom de base, de sorte que chaque image se retrouve associée à sa description.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `images` | Liste d'images à enregistrer. | IMAGE | Oui | - |
| `texts` | Liste de légendes texte à enregistrer. Cette entrée est facultative. | STRING | Non | - |
| `folder_name` | Nom du dossier dans lequel enregistrer les images (dans le répertoire de sortie). (par défaut : "dataset") | STRING | Oui | - |
| `filename_prefix` | Préfixe des noms de fichiers des images enregistrées. (par défaut : "image") | STRING | Oui | - |
| `mode` | Indique s'il faut écraser les fichiers existants ou incrémenter les noms de fichiers pour éviter l'écrasement. (par défaut : "overwrite") | COMBO | Oui | "overwrite"<br>"increment" |

**Remarque :** L'entrée `images` est une liste, et le nœud reçoit à la fois `images` et `texts` sous forme de listes. L'entrée `texts` est facultative ; si elle est fournie, elle doit être une liste de légendes texte et contenir le même nombre d'éléments que `images`. Chaque légende est enregistrée dans un fichier `.txt` correspondant à son image associée. En mode `overwrite`, les fichiers sont nommés `{filename_prefix}_{index}.png` et remplacent tout fichier existant portant le même nom. En mode `increment`, un compteur unique est ajouté aux noms de fichiers afin que les fichiers existants ne soient pas écrasés. Le `folder_name` doit pointer vers un chemin à l'intérieur du répertoire de sortie ; les noms de dossier qui tentent d'en sortir (par exemple avec `..`) sont rejetés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| - | Ce nœud ne renvoie aucune donnée. Il enregistre les fichiers directement dans le système de fichiers. | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/fr.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
