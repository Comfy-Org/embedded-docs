# Creatify Boreal-H3 Reference to Video

Creatify Boreal-H3 Reference to Video génère une vidéo avec son guidée par des images, vidéos et audio de référence, en utilisant le modèle H3 post-entraîné de Creatify conçu pour les publicités vidéo. Nommez les références dans le prompt comme `@Image1`, `@Video1` et `@Audio1` pour contrôler ce que chacune apporte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible pour jusqu'à 9 images de référence (`image_1` ... `image_9`), référencées dans le prompt comme `@Image1` ... `@Image9` dans l'ordre de connexion. Au moins une image ou une vidéo est requise, et au plus 12 références au total. | IMAGE | Non | Jusqu'à 9 images |
| `reference_videos` | Emplacement extensible pour jusqu'à 3 vidéos de référence (`video_1` ... `video_3`), chacune d'une durée d'au moins 1 seconde. Leur son est réutilisé lorsque le prompt demande de le poursuivre ; une nouvelle ligne dans le prompt le remplace. Au plus 15 secondes de vidéo de référence sont facturées au total. | VIDEO | Non | Jusqu'à 3 vidéos |
| `reference_audios` | Emplacement extensible pour jusqu'à 3 clips de référence (`audio_1` ... `audio_3`). La parole guide la voix plutôt que les mots, et la musique instrumentale peut devenir la bande sonore. | AUDIO | Non | Jusqu'à 3 clips |
| `prompt` | Prompt texte qui décrit la vidéo et fait référence aux références connectées. Doit contenir au moins un caractère autre qu'un espace. | STRING | Oui | Tout texte non vide |
| `resolution` | Résolution de la vidéo de sortie (par défaut : `"768p"`). | COMBO | Oui | `"768p"`<br>`"1088p"`<br>`"2k"` |
| `aspect_ratio` | Rapport d'aspect de la vidéo de sortie. `"auto"` suit la première image de référence, ou la première vidéo de référence lorsqu'aucune image n'est connectée (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durée de la vidéo en secondes (par défaut : 5). Avec `"2k"`, le maximum est de 14 secondes. | INT | Oui | 1 à 15 (pas : 1) |
| `prompt_enhancement` | Comment Creatify réécrit le prompt avant le rendu : `"auto"` et `"ads"` le transforment en prompt de publicité vidéo et peuvent ajouter des répliques parlées, `"general"` le réécrit pour toute autre vidéo, `"none"` le rend tel quel (par défaut : `"auto"`). | COMBO | Oui | `"auto"`<br>`"ads"`<br>`"general"`<br>`"none"` |
| `seed` | La graine contrôle si le nœud est réexécuté. Creatify choisit son propre aléatoire, donc les mêmes entrées donnent la même vidéo uniquement lorsque `prompt_enhancement` est défini sur `"none"` (par défaut : 42). | INT | Oui | 0 à 2147483647 |

**Contraintes :** connectez au moins une image ou une vidéo de référence ; l'audio seul n'est pas accepté. Une balise de référence qui pointe au-delà du nombre de références connectées de ce type déclenche une erreur, tout comme plus de 12 références au total. Avec `"1088p"` et `"auto"` et aucune image de référence, le rapport d'aspect est repris de la première vidéo de référence.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec son. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyBorealH3ReferenceVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c6e60b83a8e02262fcbae7c04f4f379cf665a9e25b2fa00836047fe56d0fa064`
