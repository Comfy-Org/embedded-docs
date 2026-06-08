Le nœud Runway Text to Image génère des images à partir de descriptions textuelles en utilisant le modèle Gen 4 de Runway. Vous pouvez fournir une description textuelle et éventuellement inclure une image de référence pour guider le processus de génération d'image. Le nœud gère la communication avec l'API et renvoie l'image générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Description textuelle pour la génération (par défaut : "") | STRING | Oui | - |
| `ratio` | Format d'image pour l'image générée | COMBO | Oui | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" |
| `image_référence` | Image de référence optionnelle pour guider la génération | IMAGE | Non | - |

**Remarque :** L'image de référence ne doit pas dépasser 7999x7999 pixels et doit avoir un format d'image compris entre 0,5 et 2,0. Lorsqu'une image de référence est fournie, elle guide le processus de génération d'image.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L'image générée à partir de la description textuelle et de l'image de référence optionnelle | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `140f8e6b07216892d84f2d7fbc3afaf1c390e98ddedf27d4926032066a783f67`
