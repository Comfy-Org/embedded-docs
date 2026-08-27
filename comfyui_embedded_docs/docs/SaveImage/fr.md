# Enregistrer Image

Le nœud SaveImage enregistre les images d'entrée en tant que fichiers PNG dans votre répertoire de sortie ComfyUI. Il peut intégrer des métadonnées de workflow, telles que le prompt, dans chaque fichier enregistré, et il renvoie les images inchangées afin qu'elles puissent encore être utilisées par d'autres nœuds.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images à enregistrer. | IMAGE | Oui | - |
| `préfixe_du_nom_de_fichier` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant de nœuds (défaut : "ComfyUI"). | STRING | Oui | - |

Le nœud reçoit également deux entrées cachées, `prompt` et `extra_pnginfo`, qui sont automatiquement remplies par ComfyUI avec le prompt du workflow et les informations PNG supplémentaires. Lorsque les métadonnées sont activées, ces informations sont intégrées en tant que métadonnées textuelles dans chaque fichier PNG enregistré.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Les images d'entrée d'origine, renvoyées inchangées après avoir été enregistrées sur le disque. | IMAGE |
| `ui` | Un résultat réservé à l'interface contenant la liste des fichiers image enregistrés (nom de fichier, sous-dossier et type) pour l'affichage dans l'interface. | UI_RESULT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/fr.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
