# Génération d’image en vidéo Vidu Q3

Voici la traduction en français de la documentation du nœud Vidu Q3 Image-to-Video :

Le nœud de génération d'image vers vidéo Vidu Q3 crée une séquence vidéo à partir d'une image d'entrée. Il utilise un modèle Vidu Q3 pour animer l'image, éventuellement guidé par une invite textuelle, et produit un fichier vidéo en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Modèle à utiliser pour la génération vidéo. | COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.resolution` | Résolution de la vidéo de sortie. Les options disponibles dépendent du modèle sélectionné. | COMBO | Oui | `"720p"`<br>`"1080p"`<br>`"2K"` (viduq3-pro uniquement) |
| `model.duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 1 à 16 |
| `model.audio` | Lorsqu'activé, produit une vidéo avec son (incluant dialogues et effets sonores) (par défaut : False). | BOOLEAN | Oui | `True` / `False` |
| `image` | Image utilisée comme première image de la vidéo générée. | IMAGE | Oui | - |
| `invite` | Invite textuelle facultative pour la génération vidéo (2000 caractères maximum) (par défaut : vide). | STRING | Non | - |
| `graine` | Valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). | INT | Non | 0 à 2147483647 |

**Remarque :** L'`image` doit avoir un rapport hauteur/largeur compris entre 1:4 et 4:1 (portrait à paysage). Le `prompt` est facultatif mais ne peut pas dépasser 2000 caractères. Les options de `model.resolution` dépendent du `model` sélectionné : `"viduq3-pro"` prend en charge `"720p"`, `"1080p"` et `"2K"` ; `"viduq3-turbo"` prend en charge `"720p"` et `"1080p"`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `1dd3929860ee4a04b761014fd2cf7e9e32f9171d8b18fe1e93f27d0905ca04ee`
