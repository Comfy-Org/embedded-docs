# Pruna P-Video-2 Pro Reference to Video

Générez une vidéo à partir d’un prompt guidé par des images, des vidéos et de l’audio de référence avec Pruna P-Video-2 Pro Reference to Video. Faites référence à chaque élément de référence par son numéro dans le prompt ; le modèle transfère son sujet, son style ou son mouvement dans le résultat.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle vidéo Pruna à utiliser. La sélection d’un modèle révèle ses entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"p-video-2-pro-reference"` |

### Entrées P-Video-2 Pro Reference

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model.images` | Emplacement extensible pour les images de référence (`image_1`, `image_2`, ...), référencées dans le prompt sous la forme `@Image1` à `@Image9` dans l’ordre de connexion. Jusqu’à 9 images, en comptant la première et la dernière image. | AUTOGROW | Non | 0 à 9 images |
| `model.videos` | Emplacement extensible pour les vidéos de référence (`video_1`, `video_2`, ...), référencées sous la forme `@Video1` à `@Video3`. Chaque vidéo dure de 2 à 15 secondes, à un maximum de 60 fps, pour un total de 15 secondes. Les vidéos au-dessus de 1080p sont réduites. | AUTOGROW | Non | 0 à 3 vidéos |
| `model.audios` | Emplacement extensible pour l’audio de référence (`audio_1`, `audio_2`, ...), référencé sous la forme `@Audio1` à `@Audio3`. Jusqu’à 15 secondes au total. | AUTOGROW | Non | 0 à 3 clips audio |
| `model.prompt` | Décrit la vidéo. Faites référence aux éléments de référence sous la forme `@Image1`, `@Video1` ou `@Audio1` (par défaut : vide). Jusqu’à 5000 caractères. | STRING | Oui | 1 à 5000 caractères |
| `model.first_frame` | Image à partir de laquelle la vidéo commence. Compte dans la limite de 9 images. | IMAGE | Non | - |
| `model.last_frame` | Image sur laquelle la vidéo se termine. Compte dans la limite de 9 images. | IMAGE | Non | - |
| `model.keep_audio` | Utilise l’audio connecté comme bande-son et génère la vidéo pour qu’elle corresponde (par défaut : False). Nécessite exactement un audio : un audio plus court est suivi d’un son généré, un audio plus long est coupé à la durée. | BOOLEAN | Oui | `True`<br>`False` |
| `model.duration` | Durée de la vidéo en secondes (par défaut : `"5"`). | COMBO | Oui | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"` |
| `model.resolution` | Résolution de sortie (par défaut : `"768p"`). Les résolutions 1080p, 2k et 4k effectuent une mise à l’échelle supérieure de la vidéo 768p générée. | COMBO | Oui | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `model.mode` | `"cost"` est moins coûteux, `"speed"` effectue le rendu plus rapidement (par défaut : `"speed"`). | COMBO | Oui | `"cost"`<br>`"speed"` |
| `model.aspect_ratio` | Rapport d’aspect de la vidéo de sortie (par défaut : `"16:9"`). `"adaptive"` utilise le rapport le plus courant parmi les références ; avec `enhance_prompt` activé, c’est le prompt réécrit qui choisit le rapport à la place. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `model.enhance_prompt` | Réécrit le prompt avec plus de détails avant la génération ; `"max"` est plus lent (par défaut : `"turbo"`). Laissez cette option activée lorsque le prompt fait référence aux références par leur numéro ; une première ou une dernière image utilise toujours `"turbo"`. Paramètre avancé. | COMBO | Oui | `"off"`<br>`"turbo"`<br>`"max"` |
| `model.seed` | Graine de génération (par défaut : 42). La même graine ne reproduit un résultat à l’identique que lorsque `model.enhance_prompt` est désactivé. | INT | Oui | 0 à 2147483647<br>Pas : 1 |

**Remarques :**

- Connectez au moins une image de référence, une vidéo de référence, une première image ou une dernière image ; sinon, le nœud s’arrête avec une erreur.
- 9 images sont autorisées, y compris les première et dernière images, et 12 références au total réparties entre images, images de début/fin, vidéos et audio.
- La vidéo de référence et l’audio de référence sont chacun limités à 15 secondes au total, et chaque vidéo de référence doit durer de 2 à 15 secondes, à un maximum de 60 fps.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaReferenceToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `d6e295b394984c924386ea6432532c7653b4512c646b1f86793be9b98583eef3`
