# Enregistrer l'ensemble d'images et de textes dans un dossier

Enregistrer Image-Texte (dans un dossier) est un nœud de sortie qui enregistre un jeu de données d’images et de légendes textuelles appariées dans un dossier du répertoire de sortie de ComfyUI. Chaque image est enregistrée sous forme de fichier PNG, et lorsque des légendes sont fournies, un fichier TXT correspondant portant le même nom de base est créé pour chaque image. Cela est utile pour constituer des jeux de données organisés d’images générées et de leurs descriptions.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Liste des images à enregistrer. | IMAGE | Oui | - |
| `texts` | Liste des légendes textuelles à enregistrer. Cette entrée est facultative. | STRING | Non | - |
| `folder_name` | Nom du dossier dans lequel enregistrer les images (dans le répertoire de sortie). (par défaut : « dataset ») | STRING | Oui | - |
| `filename_prefix` | Préfixe des noms de fichiers des images enregistrées. (par défaut : « image ») | STRING | Oui | - |
| `mode` | Indique s’il faut écraser les fichiers existants ou incrémenter les noms de fichiers pour éviter l’écrasement. (par défaut : « overwrite ») | COMBO | Oui | « overwrite »<br>« increment » |

**Remarque :** L’entrée `images` est une liste. L’entrée `texts` est facultative ; si elle est fournie, elle doit être une liste de légendes textuelles. Les légendes sont appariées aux images dans l’ordre, et chaque légende est enregistrée sous forme de fichier `.txt` en UTF-8 portant le même nom de base que l’image correspondante (par exemple, `image_00000.txt` pour `image_00000.png`). S’il y a moins de légendes que d’images, les images restantes sont enregistrées sans légende ; toute légende supplémentaire est ignorée.

Les entrées avec des valeurs par défaut (`folder_name`, `filename_prefix`, `mode`) n’ont pas besoin d’être connectées ; leurs valeurs par défaut sont utilisées automatiquement.

Lorsque `mode` est défini sur `overwrite` (par défaut), les images sont enregistrées avec des noms comme `image_00000.png`, remplaçant tout fichier existant portant le même nom. Lorsque `mode` est défini sur `increment`, un compteur automatiquement incrémenté est ajouté aux noms de fichiers afin que les fichiers existants ne soient pas écrasés.

La valeur de `folder_name` doit correspondre à un emplacement situé dans le répertoire de sortie de ComfyUI. Les noms de dossier qui tentent de sortir du répertoire de sortie (par exemple, en utilisant `..`) sont rejetés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| - | Ce nœud n’a aucune sortie. Il enregistre les fichiers directement dans le système de fichiers. | - |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/fr.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
