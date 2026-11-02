# MiniMax H3 Max Reframe Video

Ce nœud adapte une vidéo à un nouveau rapport d'aspect en l'ajustant sur un nouveau canevas et en générant les zones environnantes. La synchronisation et le son de la vidéo source sont conservés. Utilisez-le pour transformer un clip paysage en vertical, ou inversement, sans rogner le sujet hors du cadre.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | "MiniMax H3 Max" |

### Entrées MiniMax H3 Max

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo source à recadrer, d'une durée de 0,5 à 300 secondes. | VIDEO | Oui | 0.5 à 300 secondes |
| `aspect_ratio` | Rapport d'aspect du canevas de sortie (par défaut : « 9:16 »). | COMBO | Oui | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9"<br>"9:21" |
| `resolution` | Résolution de la vidéo de sortie (par défaut : « 768P »). | COMBO | Oui | "480P"<br>"768P"<br>"1080P" |
| `prompt` | Indication facultative pour les zones environnantes générées. | STRING | Oui | 0 à 50000 caractères |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo recadrée selon le rapport d'aspect sélectionné. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`
