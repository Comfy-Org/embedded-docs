Ce nœud charge un ensemble de données d'images et leurs légendes textuelles correspondantes à partir d'un dossier spécifié. Il recherche les fichiers image et cherche automatiquement les fichiers `.txt` correspondants portant le même nom de base pour les utiliser comme légendes. Le nœud prend également en charge une structure de dossiers spécifique où les sous-dossiers peuvent être nommés avec un préfixe numérique (comme `10_nom_dossier`) pour indiquer que les images qu'ils contiennent doivent être répétées plusieurs fois dans la sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder` | Le dossier à partir duquel charger les images. Les options disponibles sont les sous-répertoires du répertoire d'entrée de ComfyUI. | COMBO | Oui | *Chargé dynamiquement depuis `folder_paths.get_input_subfolders()`* |

**Remarque :** Le nœud s'attend à une structure de fichiers spécifique. Pour chaque fichier image (`.png`, `.jpg`, `.jpeg`, `.webp`), il recherchera un fichier `.txt` portant le même nom pour l'utiliser comme légende. Si aucun fichier de légende n'est trouvé, une chaîne vide est utilisée. Le nœud prend également en charge une structure spéciale où le nom d'un sous-dossier commence par un nombre suivi d'un trait de soulignement (par exemple, `5_chats`), ce qui entraînera la répétition de toutes les images de ce sous-dossier autant de fois dans la liste de sortie finale.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Une liste de tenseurs d'images chargées. | IMAGE |
| `texts` | Une liste de légendes textuelles correspondant à chaque image chargée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `e176f35118f08ea397c63f5b6f347d9cdb3dc1a08db7ad7a5cc8255e1526e6ca`
