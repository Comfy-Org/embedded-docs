# Video Deflicker

Retire le scintillement temporel d'une vidéo traitée, afin que chaque image conserve ses propres détails tout en suivant le mouvement de ses voisines. Il est destiné aux séquences qui pulsent après avoir été agrandies ou traitées image par image : connectez le modèle de flux optique et les images scintillantes, et éventuellement une copie stable de la source comme guide.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modèle de flux optique issu du nœud Load Optical Flow Model (torchvision RAFT-large). | OPTICAL_FLOW | Oui | - |
| `images` | Images scintillantes à stabiliser, par exemple une vidéo qui a été agrandie ou traitée image par image. | IMAGE | Oui | - |
| `guide` | Images sources stables dont suivre le mouvement, à n'importe quelle résolution. Par défaut : `images`, ce qui retire moins de scintillement. Ses différences entre images consécutives, après compensation du mouvement, pondèrent aussi le lissage : si le guide change d'une manière que le flux n'explique pas, le lissage diminue même lorsque l'estimation du mouvement est correcte. | IMAGE | Non | - |
| `strength` | Force avec laquelle chaque image suit ses voisines (par défaut : 1.0). Des valeurs plus élevées retirent davantage de scintillement et adoucissent davantage les détails fins ; 0 renvoie les images inchangées. | FLOAT | Oui | 0.0 à 100.0 (pas : 0.1) |
| `direction` | Direction du passage. `bidirectional` moyenne un passage avant et un passage arrière, ce qui évite d'être en retard sur le mouvement ; `forward` exécute un seul passage. (par défaut : `bidirectional`) | COMBO | Oui | `"bidirectional"`<br>`"forward"` |
| `threshold` | Les changements supérieurs à cette valeur entre une image et son voisin compensé en mouvement sont traités comme réels et moins lissés (par défaut : 0.1). 0 lisse tous les changements de la même manière. | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

**Notes :**

- Le flux optique est calculé sur une copie réduite du guide, il n’a donc pas besoin d’avoir la taille de `images` ; les pixels du guide ne sont pas mélangés à la sortie.
- Les images au-delà du plus court de `images` et `guide` ne sont pas traitées. Si `guide` est plus courte, les images restantes sont renvoyées inchangées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | Images sans scintillement, avec la même taille et le même nombre d'images que `images`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoDeflicker/fr.md)

---
**Source fingerprint (SHA-256):** `d9937a67b0ac33ef3b326017e7d7990474705917902f1097cfeb06d9f83322a1`
