# Enregistrer Image

Le nœud SaveImage enregistre les images qu'il reçoit dans votre répertoire `ComfyUI/output`. Il enregistre chaque image sous forme de fichier PNG et peut intégrer des métadonnées de workflow, telles que le prompt, dans le fichier enregistré pour référence ultérieure.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images à enregistrer. | IMAGE | Oui | - |
| `filename_prefix` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant de nœuds (par défaut : "ComfyUI"). | STRING | Oui | - |
| `prompt` | Entrée cachée, fournie automatiquement par ComfyUI : les données du prompt intégrées comme métadonnées dans le fichier PNG enregistré. | PROMPT | Non | - |
| `extra_pnginfo` | Entrée cachée, fournie automatiquement par ComfyUI : des informations supplémentaires sur le workflow intégrées comme métadonnées dans le fichier PNG enregistré. | EXTRA_PNGINFO | Non | - |

Chaque image est enregistrée sous forme de fichier PNG. Dans le nom de fichier enregistré, `%batch_num%` dans le préfixe est remplacé par le numéro de lot de l'image, et un compteur complété de zéros est ajouté.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `images` | Les mêmes images qui ont été enregistrées, transmises pour pouvoir être utilisées par d'autres nœuds. | IMAGE |
| `ui` | Résultat d'interface contenant une liste des images enregistrées avec leurs noms de fichiers, sous-dossiers et type, affiché dans l'interface de ComfyUI. | UI_RESULT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/fr.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
