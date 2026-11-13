# HeyGen Video 1.0 Référence vers vidéo

Générez une vidéo avec un dialogue et un son synchronisés à partir d’un prompt texte à l’aide de HeyGen Video 1.0, éventuellement guidé par du contenu de référence connecté. Les images de personnes, de produits ou de lieux, les vidéos à réutiliser et les clips audio fournissant une voix peuvent tous être utilisés comme références. Mentionnez chaque référence dans le prompt sous la forme @Image1, @Video1 ou @Audio1, numérotée par type dans l’ordre où les entrées sont connectées : ces balises sont réécrites en libellés attendus par HeyGen, et une balise qui pointe vers une référence non connectée déclenche une erreur. Sans aucune image ni vidéo de référence, le nœud s’exécute comme une génération texte-vers-vidéo.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Version du modèle utilisée pour la génération. (par défaut : `"heygen-video-1"`) | DYNAMIC_COMBO | Oui | `"heygen-video-1"` |
| `prompt` | Description de la vidéo, y compris tout dialogue. Faites référence aux références connectées sous la forme @Image1, @Video1, @Audio1, numérotées par type dans l’ordre des entrées. (par défaut : chaîne vide) | STRING | Oui | 1 à 16000 caractères |
| `duration` | Durée de la vidéo de sortie en secondes. Plus de 15 secondes n’est disponible que sans images ni vidéos de référence. (par défaut : 5) | INT | Oui | 5 à 30 |
| `resolution` | Résolution de sortie. 1080p et 2k nécessitent un rapport d’aspect 16:9 ou 9:16 ; `"auto"` fonctionne à ces résolutions uniquement sans références. (par défaut : `"768p"`) | COMBO | Oui | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `aspect_ratio` | Rapport d’aspect de sortie. `"auto"` vaut 16:9 lorsqu’aucune référence n’est connectée ; sinon, il suit la première image de référence, ou la première vidéo de référence lorsqu’aucune image n’est connectée. (par défaut : `"auto"`) | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Graine pour la génération. Les résultats peuvent encore varier entre les exécutions avec la même graine. (par défaut : 42) | INT | Oui | 0 à 4294967295 |
| `reference_images` | Emplacement extensible : images de personnes, de produits ou de lieux à utiliser dans la vidéo (`image_1` ... `image_9`) ; faites-y référence sous la forme @Image1, @Image2, ... Chaque entrée doit contenir exactement une image, et chaque image doit avoir un rapport d’aspect compris entre 1:4 et 4:1. | IMAGE | Non | 0 à 9 images |
| `reference_videos` | Emplacement extensible : vidéos à utiliser comme références (`video_1` ... `video_3`) ; faites-y référence sous la forme @Video1, @Video2, ... Au plus 15 secondes de séquence sont utilisées au total. | VIDEO | Non | 0 à 3 vidéos |
| `reference_audios` | Emplacement extensible : clips audio tels qu’une voix pour un locuteur (`audio_1` ... `audio_3`) ; faites-y référence sous la forme @Audio1, @Audio2, ... Nécessite au moins une image ou une vidéo de référence. Une référence vocale nécessite quelques secondes de parole claire, et les clips de moins de 2 secondes environ sont généralement ignorés. | AUDIO | Non | 0 à 3 clips audio |
| `auto_duration` | Lorsque cette option est activée, la durée de la vidéo suit le dialogue cité dans le prompt (8 à 30 secondes, ou 8 à 15 avec des images ou des vidéos de référence) et `duration` est ignoré. (par défaut : `"disabled"`) | COMBO | Non | `"disabled"`<br>`"enabled"` |

### Contraintes des paramètres

- **Limite de références :** au plus 15 références au total : jusqu’à 9 images, 3 vidéos et 3 clips audio. En connecter davantage déclenche une erreur.
- **L’audio nécessite une image ou une vidéo :** l’audio de référence est rejeté lorsqu’aucune image de référence ni aucune vidéo de référence n’est connectée.
- **Règles des images de référence :** chaque entrée `reference_images` doit contenir exactement une image (un lot est rejeté), et chaque image doit avoir un rapport d’aspect compris entre 1:4 et 4:1.
- **Balises de prompt :** `@ImageN`, `@VideoN` et `@AudioN` sont mises en correspondance sans tenir compte de la casse. Le numéro ne doit pas dépasser le nombre de références connectées de ce type, et le prompt doit être non vide après suppression des espaces.
- **Mode :** avec au moins une image ou une vidéo de référence, la requête est une exécution référence-vers-vidéo ; sans aucune, il s’agit d’une exécution texte-vers-vidéo simple.
- **Résolution 1080p et 2k :** `resolution` `"1080p"` ou `"2k"` nécessite `aspect_ratio` `"16:9"` ou `"9:16"` ; `"auto"` n’est accepté à ces résolutions que lorsqu’aucune image de référence ni aucune vidéo de référence n’est connectée.
- **Durée :** une durée supérieure à 15 secondes n’est disponible que sans images ni vidéos de référence, sauf si `auto_duration` est `"enabled"`.
- **Graine :** la graine détermine uniquement si le nœud est réexécuté ; les résultats ne sont pas reproductibles avec la même graine.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec dialogue et son synchronisés. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `415ffca1c385936e35bdb0451a23f03756e936b3b871d8d6a958da1ef8c56c36`
