# MinimaxHailuo03ReferenceNode

Ce nœud génère une vidéo à l’aide du modèle MiniMax H3, en utilisant des images, des vidéos et de l’audio de référence pour conditionner le résultat. Les références sont désignées dans le prompt par leur ordre de connexion : « Image 1 », « Image 2 », « Video 1 », « Audio 1 », etc.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser pour la génération vidéo (par défaut : « MiniMax H3 »). La sélection de « MiniMax H3 » fournit les paramètres `prompt`, `duration`, `resolution`, `ratio`, `reference_images`, `reference_videos` et `reference_audios` ci-dessous. | STRING | Oui | « MiniMax H3 » |
| `prompt` | Description textuelle de la vidéo à générer. Les médias de référence peuvent être désignés par leur ordre, par exemple « Image 1 », « Image 2 », « Video 1 » ou « Audio 1 ». | STRING | Oui | Longueur minimale : 1 caractère |
| `duration` | Durée de la vidéo générée en secondes. | INT | Oui | Plusieurs options disponibles |
| `resolution` | Résolution de sortie de la vidéo générée. | STRING | Oui | Plusieurs options disponibles |
| `ratio` | Ratio d’aspect de la vidéo générée. | STRING | Oui | Plusieurs options disponibles |
| `reference_images` | Images de référence de sujet ou de style, désignées dans le prompt comme « Image 1 » à « Image 9 » dans l’ordre de connexion. Jusqu’à 9 images. | IMAGE | Non | 0 à 9 images |
| `reference_videos` | Vidéos de référence de mouvement ou de scène, désignées dans le prompt comme « Video 1 » à « Video 3 » dans l’ordre de connexion. Jusqu’à 3 vidéos, de 2 à 15 secondes chacune, 15 secondes au total. | VIDEO | Non | 0 à 3 vidéos |
| `reference_audios` | Références audio, désignées dans le prompt comme « Audio 1 » à « Audio 3 » dans l’ordre de connexion. Jusqu’à 3 clips, de 2 à 15 secondes chacun, 15 secondes au total. Ne peuvent pas être utilisées sans une image ou une vidéo de référence. | AUDIO | Non | 0 à 3 clips |
| `graine` | Seed aléatoire. La même requête avec la même seed donne des résultats similaires, mais pas garantis identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |
| `filigrane` | Indique s’il faut ajouter un filigrane AIGC à la vidéo (par défaut : false). | BOOLEAN | Non | true<br>false |

### Contraintes des paramètres

- Au moins une image de référence ou une vidéo de référence est requise. L’audio de référence seul n’est pas accepté.
- Chaque image de référence doit avoir un ratio d’aspect compris entre environ 0.4 et 2.5 (2:5 à 5:2) et une largeur et une hauteur minimales de 256 pixels.
- Chaque vidéo de référence doit avoir une durée comprise entre 2 et 15 secondes et une cadence comprise entre 23.976 et 60 FPS. La durée totale de toutes les vidéos de référence ne peut pas dépasser 15 secondes.
- Chaque clip audio de référence doit durer entre 2 et 15 secondes. La durée totale de tous les clips audio de référence ne peut pas dépasser 15 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `beca020333a544188e6c21829eb8e63415aa5299efc676438e85662a5f08660d`
