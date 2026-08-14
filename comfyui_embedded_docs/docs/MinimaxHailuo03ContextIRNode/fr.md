# MinimaxHailuo03ContextIRNode

Ce nœud utilise MiniMax H3 Context IR pour analyser votre description textuelle et tout média attaché, puis produit une invite vidéo structurée et plus robuste. L'invite renvoyée est conçue pour être connectée à l'entrée `prompt` d'un nœud vidéo MiniMax H3 ; si vous y attachez des médias, attachez les mêmes médias dans le même ordre, car l'invite améliorée fait référence aux médias par position.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour l'amélioration de l'invite. | COMBO | Oui | `"MiniMax H3"` |
| `prompt` | Description de la vidéo que vous souhaitez générer. Ne peut pas être vide. (défaut : `""`) | STRING | Oui | Texte libre |
| `duration` | Durée de la vidéo que vous souhaitez générer, en secondes (4-15). (défaut : 5) | INT | Oui | 4 à 15 |
| `ratio` | Ratio d'aspect de la vidéo que vous souhaitez générer. `"adaptive"` nécessite au moins une entrée image, vidéo ou audio. (défaut : `"adaptive"`) | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `reference_images` | Images de référence de sujet ou de style, désignées dans l'invite comme « Image 1 » à « Image 9 » dans l'ordre de connexion. Jusqu'à 9 images. | IMAGE | Non | 0 à 9 images |
| `reference_videos` | Vidéos de référence de mouvement ou de scène, désignées dans l'invite comme « Vidéo 1 » à « Vidéo 3 » dans l'ordre de connexion. Jusqu'à 3 vidéos, de 2 à 15 secondes chacune, 15 secondes au total. | VIDEO | Non | 0 à 3 vidéos |
| `reference_audios` | Références audio, désignées dans l'invite comme « Audio 1 » à « Audio 3 » dans l'ordre de connexion. Jusqu'à 3 clips, de 2 à 15 secondes chacun, 15 secondes au total. Ne peut pas être utilisé sans une image ou une vidéo de référence. | AUDIO | Non | 0 à 3 clips |
| `first_frame` | Première image de la vidéo que vous souhaitez générer. Ne peut pas être combinée avec des médias de référence. | IMAGE | Non | Image unique |
| `last_frame` | Dernière image de la vidéo que vous souhaitez générer. Ne peut pas être combinée avec des médias de référence. | IMAGE | Non | Image unique |

### Contraintes des paramètres

- Les entrées `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` et `reference_audios` font partie du groupe d'options `model`.
- Les entrées `first_frame` et `last_frame` ne peuvent pas être combinées avec un média de référence.
- `reference_audios` ne peut pas être utilisé sauf si au moins une `reference_image` ou `reference_video` est également connectée.
- Lorsqu'aucune image et aucun média de référence ne sont connectés, `ratio` ne peut pas être défini sur `"adaptive"`.
- Les vidéos de référence doivent durer environ 2 à 15 secondes chacune, avec une durée totale ne dépassant pas 15 secondes. Leur fréquence d'images doit être comprise entre 23,9 et 60,5 FPS.
- Les références audio doivent durer environ 2 à 15 secondes chacune, avec une durée totale ne dépassant pas 15 secondes.
- `first_frame`, `last_frame` et chaque image de référence doivent mesurer au moins 256x256 pixels et avoir un ratio d'aspect compris entre 0,4 et 2,5.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `STRING` | L'invite vidéo structurée et améliorée générée par MiniMax H3 Context IR. Elle peut être connectée à l'entrée `prompt` d'un nœud de génération vidéo MiniMax H3. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/fr.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
