Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

## Aperçu

Ce nœud génère une courte vidéo à partir d’une image de départ unique en utilisant le modèle HappyHorse. Vous fournissez une première image (première trame) et une description textuelle du mouvement et de la scène souhaités, et le nœud crée une vidéo qui se poursuit à partir de cette image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle HappyHorse à utiliser pour la génération vidéo. | COMBO | Oui | `"happyhorse-1.0-i2v"` |
| `model.prompt` | Description des éléments et des caractéristiques visuelles. Prend en charge l’anglais et le chinois. (par défaut : "") | STRING | Non | N/A |
| `model.resolution` | La résolution de la vidéo de sortie. (par défaut : "720P") | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.duration` | La durée de la vidéo générée en secondes. (par défaut : 5) | INT | Oui | 3 à 15 |
| `première image` | Image de la première trame. Le rapport hauteur/largeur de la sortie est dérivé de cette image. | IMAGE | Oui | N/A |
| `graine` | Graine à utiliser pour la génération. (par défaut : 0) | INT | Non | 0 à 2147483647 |
| `filigrane` | Indique s’il faut ajouter un filigrane indiquant une génération par IA au résultat. (par défaut : Faux) | BOOLEAN | Non | Vrai / Faux |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/fr.md)

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
