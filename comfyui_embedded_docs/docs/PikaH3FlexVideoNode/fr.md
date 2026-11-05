# Pika H3 Flex Video

Ce nœud génère une vidéo avec un audio synchronisé à partir d’un prompt texte, éventuellement ancrée par une première image, une dernière image, ou les deux. Pika H3 Flex est le modèle MiniMax H3 post-entraîné de Pika : il génère l’image et son son en une seule passe, et vous définissez la résolution, le ratio d’image et la durée. Sans image connectée, le nœud fonctionne en texte vers vidéo ; connecter une image le bascule en image vers vidéo.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Ce qui se passe dans la vidéo, y compris le son que vous souhaitez. Ne doit pas être vide. Par défaut : "" (chaîne vide). | STRING | Oui | 1 à 8000 caractères |
| `first_frame` | Image facultative utilisée comme image d’ouverture. La connecter lance le mode image vers vidéo au lieu de texte vers vidéo. | IMAGE | Non | - |
| `last_frame` | Image facultative utilisée comme image de clôture. Peut être utilisée avec `first_frame` ou seule. | IMAGE | Non | - |
| `resolution` | Résolution de sortie. `"1080p"` et au-delà sont rendus en 768p puis agrandis une fois. La même graine en 480p donne une vidéo différente. Par défaut : `"768p"`. | COMBO | Oui | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Ratio d’image de sortie. `"auto"` suit la première image connectée, sinon le prompt. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Durée du clip en secondes. La durée de sortie suit une grille d’images : 5 secondes donnent 124 images, soit environ 5,17 secondes. Par défaut : 5. | INT | Oui | 5 à 15 secondes |
| `rewrite_prompt` | Laisse Pika enrichir d’abord le prompt. La même graine donne alors une vidéo différente à chaque exécution. Par défaut : False. | BOOLEAN | Oui | true<br>false |
| `seed` | Graine d’échantillonnage. Avec `rewrite_prompt` désactivé, la même graine reproduit exactement la vidéo, bien qu’une exécution locale avec la même graine donne un résultat différent. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes :**

* Le prompt doit comporter entre 1 et 8000 caractères.
* La facturation dépend de la résolution sélectionnée et de la durée du clip, comptée par seconde de sortie.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | Le clip généré avec son audio synchronisé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `63a90fc5874ed861db3c0821e702cfcd1a14650f09459b242b4ec5e3ba5b0cd5`
