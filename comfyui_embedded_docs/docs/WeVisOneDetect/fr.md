# WeVisOne-VL Detect

WeVisOne-VL Detect trouve des objets dans une image à partir d'un prompt textuel et retourne des boîtes, des masques alpha, des points ou la réponse propre au modèle, selon la tâche choisie. Il couvre la détection et la segmentation à vocabulaire ouvert, les expressions référentielles, le pointage, le comptage et la localisation OCR, et exécute un prompt par image du lot.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `clip` | L'encodeur de texte WeVisOne-VL qui charge le checkpoint. | CLIP | Oui | - |
| `image` | L'image ou le lot d'images à parcourir. | IMAGE | Oui | - |
| `task` | Ce que le nœud doit retourner. La segmentation retourne des boîtes plus des masques alpha ; detection, referring, ocr et ocr_grounding retournent des boîtes ; point et count_point retournent des points ; count_box compte avec des boîtes ; visual_prompt trouve les objets similaires aux boîtes de référence dans `bboxes` ; freeform envoie la requête inchangée et retourne uniquement du texte (par défaut : "segmentation"). | COMBO | Oui | `"segmentation"`<br>`"detection"`<br>`"referring"`<br>`"point"`<br>`"count_box"`<br>`"count_point"`<br>`"ocr"`<br>`"ocr_grounding"`<br>`"visual_prompt"`<br>`"freeform"` |
| `query` | Ce qu'il faut rechercher, en langage naturel (par exemple « la tasse rouge »). `detection` et `point` lisent un libellé par ligne, `count_box` et `count_point` comptent le sujet que vous nommez, `ocr_grounding` recherche ce texte exact, `visual_prompt` utilise plutôt `bboxes`, et `freeform` l'envoie comme prompt complet. `ocr` l'ignore. | STRING | Oui | - |
| `bboxes` | Boîtes de référence que `visual_prompt` utilise comme exemples de l'objet à trouver. | BOUNDING_BOX | Non | - |
| `individual_masks` | Retourner un masque alpha par boîte détectée dans la sortie `bboxes`, trame par trame, au lieu d'un masque combiné par trame (par défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `max_length` | Nombre maximal de tokens que le modèle peut générer pour sa réponse (par défaut : 4096). | INT | Oui | 1 à 32768 |

**Remarque :** Les masques alpha ne sont remplis que lorsque le modèle répond avec des références d'objets, ce que demande la tâche `segmentation`. Les autres tâches retournent des boîtes, des points ou du texte avec un masque alpha vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `masks` | Masques alpha des objets correspondants, un par trame par défaut ou un par boîte avec `individual_masks`. | MASK |
| `bboxes` | Boîtes trouvées dans chaque image, stockées sous la forme `x`, `y`, `width`, `height` et `label`. | BOUNDING_BOX |
| `points` | Points au format JSON en pixels, de la forme `[{"x", "y", "label", "frame"}]`, remplis par les tâches `point` et `count_point`. | STRING |
| `text` | Réponse brute du modèle, une ligne par image. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeVisOneDetect/fr.md)

---
**Source fingerprint (SHA-256):** `0cef1dfcab790e145ace51401a84cdc10282835330cda5a3770f5b20a32d475e`
