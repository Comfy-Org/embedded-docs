# Charger un Jeu de Données Images et Textes depuis un Dossier

Ce nœud charge un ensemble de paires d’images et de légendes textuelles depuis un dossier spécifié et les retourne sous forme de liste. Formats pris en charge : PNG, JPG, JPEG, WEBP. Pour chaque fichier image, le nœud recherche automatiquement un fichier `.txt` correspondant portant le même nom de base pour l’utiliser comme légende. Le nœud prend également en charge une structure de dossiers où les noms de sous-dossiers commencent par un préfixe numérique (tel que `10_folder_name`), ce qui entraîne la répétition des images contenues dans ce sous-dossier autant de fois dans la sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder` | Le dossier à partir duquel charger les images et les légendes textuelles. Les options disponibles sont les sous-répertoires du répertoire d’entrée de ComfyUI. | COMBO | Oui | *Dynamiquement chargé depuis `folder_paths.get_input_subfolders()`* |

**Note :** Le nœud attend une structure de fichiers spécifique. Pour chaque fichier image (`.png`, `.jpg`, `.jpeg`, `.webp`), il recherchera un fichier `.txt` portant le même nom pour l’utiliser comme légende. Si le fichier de légende n’est pas trouvé, une chaîne vide est utilisée. Le nœud prend également en charge une structure spéciale où le nom d’un sous-dossier commence par un nombre suivi d’un tiret bas (par exemple, `5_cats`), ce qui entraîne la répétition de toutes les images de ce sous-dossier autant de fois dans la liste de sortie finale. Le dossier sélectionné doit se trouver dans le répertoire d’entrée de ComfyUI ; les noms de dossiers qui pointent en dehors de celui-ci sont rejetés.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Une liste de tenseurs d’images chargés. | IMAGE |
| `texts` | Une liste de légendes textuelles correspondant à chaque image chargée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
