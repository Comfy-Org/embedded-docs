# Enregistrer Image

Le nœud SaveImage enregistre les images d'entrée sous forme de fichiers PNG dans votre répertoire de sortie ComfyUI. Il peut intégrer des métadonnées de workflow, telles que le prompt, dans chaque fichier enregistré, et il renvoie les images inchangées afin qu'elles puissent toujours être utilisées par d'autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images à enregistrer. | IMAGE | Oui | - |
| `préfixe_du_nom_de_fichier` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant de nœuds (par défaut : "ComfyUI"). | STRING | Oui | - |

Le nœud reçoit également deux entrées masquées, `prompt` et `extra_pnginfo`, qui sont automatiquement renseignées par ComfyUI avec le prompt du workflow et les informations PNG supplémentaires. Lorsque les métadonnées sont activées, ces informations sont intégrées sous forme de métadonnées textuelles dans chaque fichier PNG enregistré.

Le nom de fichier de chaque image enregistrée est construit à partir de `filename_prefix`, d'un emplacement optionnel `%batch_num%` qui est remplacé par la position de l'image dans le lot, et d'un compteur à cinq chiffres, par exemple `ComfyUI_00001_.png`. Les images sont écrites avec un niveau de compression PNG de 4.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Les images d'entrée d'origine, renvoyées inchangées après avoir été enregistrées sur le disque. | IMAGE |
| `ui` | Un résultat uniquement destiné à l'interface utilisateur contenant la liste des fichiers image enregistrés (nom de fichier, sous-dossier et type) pour affichage dans le front-end. | UI_RESULT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/fr.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
