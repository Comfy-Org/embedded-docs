# Pika H3 Flex Reference to Video

Ce nœud génère ou modifie une vidéo avec un audio synchronisé, guidé par des images, des vidéos et des clips audio de référence. Pika H3 Flex est le modèle MiniMax H3 post-entraîné de Pika. Connectez des références et mentionnez-les dans le prompt sous la forme `@Image1`, `@Video1` ou `@Audio1` dans l'ordre de connexion. Au moins une image ou une vidéo de référence est requise, et un maximum de 12 références peuvent être connectées au total.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Jusqu'à 9 images, mentionnées dans le prompt sous la forme `@Image1` à `@Image9` dans l'ordre de connexion. Au moins une image ou une vidéo est requise. | AUTOGROW | Non | 0 à 9 images |
| `reference_videos` | Jusqu'à 3 clips, mentionnés dans le prompt sous la forme `@Video1` à `@Video3` dans l'ordre de connexion. Chaque clip doit durer de 2 à 15 secondes et les clips doivent totaliser 15 secondes ou moins. Facturés à la seconde. | AUTOGROW | Non | 0 à 3 vidéos |
| `reference_audios` | Jusqu'à 3 clips, mentionnés dans le prompt sous la forme `@Audio1` à `@Audio3`. Chaque clip doit durer de 2 à 15 secondes et les clips doivent totaliser 15 secondes ou moins. Lorsqu'ils sont copiés vers la sortie, les clips sont lus dans l'ordre de connexion, avant le son des vidéos connectées. | AUTOGROW | Non | 0 à 3 clips audio |
| `prompt` | Ce qu'il faut générer, ou la modification à apporter. Mentionnez les références sous la forme `@Image1`, `@Video1`, `@Audio1`, ou sous la forme `<Picture 1>`, `<Video 1>`, `<Audio 1>`. Ne doit pas être vide. Par défaut : "" (chaîne vide). | STRING | Oui | 1 à 8000 caractères |
| `reference_video_audio` | Copier le son des vidéos connectées vers la sortie. Désactivez cette option pour une nouvelle ambiance sonore ou pour un transfert de mouvement avec une nouvelle musique. Une tête parlante sans dialogue dans le prompt se voit alors attribuer une parole inventée. Par défaut : True. | BOOLEAN | Oui | true<br>false |
| `resolution` | Résolution de sortie. Les résolutions `"1080p"` et supérieures sont rendues en 768p puis agrandies une fois. La même graine en 480p donne une vidéo différente. Par défaut : `"768p"`. | COMBO | Oui | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Format d'image de sortie. `"auto"` suit une vidéo de référence, sinon le prompt. Les images de référence ne l'affectent pas. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Durée du clip en secondes. La durée de sortie suit une grille d'images : 5 secondes donnent 124 images, soit environ 5,17 secondes. Par défaut : 5. | INT | Oui | 5 à 15 secondes |
| `rewrite_prompt` | Laissez Pika développer d'abord le prompt. La même graine donne alors une vidéo différente à chaque exécution. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `seed` | Graine pour l'échantillonnage. Lorsque `rewrite_prompt` est désactivé, la même graine reproduit exactement la vidéo, bien qu'une exécution locale avec la même graine donne un résultat différent. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes :**

* Au moins une image ou une vidéo de référence est requise.
* Un maximum de 12 références peuvent être connectées au total, en comptant ensemble les images, les vidéos et les clips audio.
* Chaque vidéo de référence et chaque clip audio doivent durer de 2 à 15 secondes ; les vidéos doivent totaliser 15 secondes ou moins, et les clips audio 15 secondes ou moins.
* Le prompt doit contenir entre 1 et 8000 caractères.
* Référencer un emplacement non connecté, par exemple `@Image3` avec deux images fournies, déclenche une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le clip généré ou modifié avec son audio synchronisé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexReferenceVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c6d8700e3bb0c4ed7663aff55d477314af566568bd6db353fc21d6249ddd93bd`
