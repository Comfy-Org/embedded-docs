# HeyGen Video 1.0 Reference to Video

Générez une vidéo avec un dialogue et un son synchronisés à partir d'un prompt textuel avec HeyGen Video 1.0, éventuellement guidée par des éléments de référence connectés. Les images de personnes, de produits ou de lieux, les vidéos à réutiliser et les clips audio qui fournissent une voix peuvent tous servir de références. Mentionnez chaque référence dans le prompt sous la forme @Image1, @Video1 ou @Audio1, numérotées par type dans l'ordre où les entrées sont connectées : ces balises sont réécrites dans les libellés attendus par HeyGen, et une balise qui pointe vers une référence non connectée déclenche une erreur. Sans aucune image ni vidéo de référence, le nœud s'exécute comme une génération texte-vers-vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Version du modèle utilisée pour la génération. (par défaut : `"heygen-video-1"`) | DYNAMIC_COMBO | Oui | `"heygen-video-1"` |
| `prompt` | Description de la vidéo, y compris tout dialogue. Référez-vous aux références connectées sous la forme @Image1, @Video1, @Audio1, numérotées par type dans l'ordre des entrées. (par défaut : chaîne vide) | STRING | Oui | 1 à 32000 caractères |
| `duration` | Durée de la vidéo de sortie en secondes. (par défaut : 5) | INT | Oui | 5 à 15 |
| `resolution` | Résolution de sortie. (par défaut : `"768p"`) | COMBO | Oui | `"768p"`<br>`"480p"` |
| `aspect_ratio` | Rapport d'aspect de sortie. `"auto"` correspond à 16:9 lorsqu'aucune référence n'est connectée ; sinon, il suit la première image de référence, ou la première vidéo de référence lorsqu'aucune image n'est connectée. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Graine pour la génération. Les résultats peuvent encore varier entre les exécutions avec la même graine. (par défaut : 42) | INT | Oui | 0 à 4294967295 |
| `reference_images` | Emplacement extensible : images de personnes, de produits ou de lieux à utiliser dans la vidéo (`image_1` ... `image_9`) ; référencez-les sous la forme @Image1, @Image2, ... Chaque entrée doit contenir exactement une image, et chaque image doit avoir un rapport d'aspect compris entre 1:4 et 4:1. | IMAGE | Non | 0 à 9 images |
| `reference_videos` | Emplacement extensible : vidéos à utiliser comme références (`video_1` ... `video_3`) ; référencez-les sous la forme @Video1, @Video2, ... | VIDEO | Non | 0 à 3 vidéos |
| `reference_audios` | Emplacement extensible : clips audio tels qu'une voix pour un locuteur (`audio_1` ... `audio_3`) ; référencez-les sous la forme @Audio1, @Audio2, ... Nécessite au moins une image ou une vidéo de référence. Une référence vocale nécessite quelques secondes de parole claire, et les clips de moins d'environ 2 secondes sont généralement ignorés. | AUDIO | Non | 0 à 3 clips audio |

### Contraintes des paramètres

- **Limite de références :** au maximum 12 références au total entre `reference_images`, `reference_videos` et `reference_audios` ; en connecter davantage déclenche une erreur.
- **L'audio nécessite une image ou une vidéo :** l'audio de référence est rejeté lorsqu'aucune image de référence et aucune vidéo de référence ne sont connectées.
- **Règles relatives aux images de référence :** chaque entrée `reference_images` doit contenir exactement une image (un lot est rejeté), et chaque image doit avoir un rapport d'aspect compris entre 1:4 et 4:1.
- **Balises de prompt :** `@ImageN`, `@VideoN` et `@AudioN` sont mises en correspondance sans tenir compte de la casse. Le numéro ne doit pas dépasser le nombre de références connectées de ce type, et le prompt doit être non vide après suppression des espaces blancs.
- **Mode :** avec au moins une image ou une vidéo de référence, la requête est une exécution référence-vers-vidéo ; sans aucune, il s'agit d'une exécution texte-vers-vidéo simple.
- **Graine :** la graine détermine uniquement si le nœud se réexécute ; les résultats ne sont pas reproductibles avec la même graine.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec un dialogue et un son synchronisés. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `44de381703821043aa1399e58c9132f9b6a2b0ac5dbf47197dffed0438ea7ad7`
