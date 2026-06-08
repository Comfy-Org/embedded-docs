Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/en.md)

Ce nœud génère une vidéo en créant des transitions entre plusieurs images clés. Il part d'une image initiale et anime une séquence d'images finales et de prompts définis par l'utilisateur, produisant un fichier vidéo unique en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle Vidu à utiliser pour la génération vidéo. | COMBO | Oui | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `image_de_départ` | L'image de départ. Le rapport hauteur/largeur doit être compris entre 1:4 et 4:1. | IMAGE | Oui | - |
| `graine` | Une valeur de graine pour la génération de nombres aléatoires, garantissant des résultats reproductibles (par défaut : 1). | INT | Non | 0 à 2147483647 |
| `résolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `images` | Nombre de transitions d'images clés (2-9). La sélection d'une valeur révèle dynamiquement les entrées requises pour chaque image. | DYNAMICCOMBO | Oui | `"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` |

**Entrées d'images (révélées dynamiquement) :**
Lorsque vous sélectionnez une valeur pour `frames` (par exemple, "3"), le nœud affiche un ensemble correspondant d'entrées requises pour chaque transition. Pour chaque image `i` de 1 au nombre sélectionné, vous devez fournir :

* `end_image{i}` (IMAGE) : L'image cible pour cette transition. Le rapport hauteur/largeur doit être compris entre 1:4 et 4:1.
* `prompt{i}` (STRING) : Une description textuelle guidant la transition vers cette image (2000 caractères maximum).
* `duration{i}` (INT) : La durée en secondes pour ce segment de transition spécifique.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré contenant toutes les transitions animées. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `02ddbb1e041b6d9e6654ab6c3cc25f4c2e5bc1545d84a30624608edc85e51f96`
