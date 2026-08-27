# Charger un Jeu de Données Images et Textes depuis un Dossier

Ce nœud charge un ensemble de paires image-légende texte depuis un dossier sélectionné et les retourne sous forme de liste. Il prend en charge les images PNG, JPG, JPEG et WEBP, et pour chaque image, il recherche une légende dans un fichier `.txt` portant le même nom de base. Le nœud prend également en charge la structure de dossiers kohya-ss/sd-scripts, où un nom de sous-dossier commençant par un nombre (par exemple `10_cats`) répète les images contenues dans ce sous-dossier autant de fois dans la sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder` | Le dossier à partir duquel charger les images et les légendes texte. | COMBO | Oui | Sous-dossiers du répertoire d’entrée de ComfyUI (chargés dynamiquement) |

**Remarque :** Le dossier sélectionné doit être un sous-dossier du répertoire d’entrée de ComfyUI. Le nœud attend un fichier de légende `.txt` par image : pour chaque fichier image (`.png`, `.jpg`, `.jpeg`, `.webp`), il recherche un fichier `.txt` portant le même nom de base dans le même emplacement et utilise son contenu, après suppression des espaces de début et de fin, comme légende. Si aucun fichier de légende n’est trouvé, une chaîne vide est utilisée. Le nœud prend également en charge la structure de dossiers kohya-ss/sd-scripts : les sous-dossiers dont le nom commence par un nombre suivi d’un trait de soulignement (par exemple `5_cats`) répètent les images qu’ils contiennent ce nombre de fois dans la liste de sortie finale. Si le dossier sélectionné ne contient aucune image valide, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Liste des images chargées. Les images sont converties en RVB et normalisées dans la plage flottante 0–1. | IMAGE |
| `texts` | Liste des légendes texte, une pour chaque image chargée. Les légendes sont le contenu, après suppression des espaces de début et de fin, du fichier `.txt` correspondant, ou une chaîne vide si aucun fichier de légende n’existe. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/fr.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
