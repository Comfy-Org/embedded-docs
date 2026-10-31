# Pruna P-Video Upscale

Pruna P-Video Upscale agrandit une vidéo en 720p, 1080p, 2K ou 4K tout en conservant son rapport d’aspect et sa piste audio. Le clip est envoyé à Pruna, la prédiction est interrogée par polling, puis la vidéo agrandie est renvoyée. Une source déjà à ou au-dessus de la taille cible conserve ses dimensions et est seulement améliorée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo à agrandir, jusqu’à 512 MiB. Les vidéos de plus de 10 mégapixels ne peuvent être envoyées que vers la cible 2K ou 4K. | VIDEO | Oui | Jusqu’à 512 MiB |
| `target` | Surface en pixels de sortie : 720p correspond à environ 0,9 mégapixel, 1080p à 2,1, 2K à 3,7 et 4K à 8,3. Le clip le plus long est limité par la cible : 2400, 1200, 600 ou 300 images, soit environ 100, 50, 25 ou 12,5 secondes à 24 fps (par défaut : "1080p"). | COMBO | Oui | "720p"<br>"1080p"<br>"2K"<br>"4K" |
| `fps` | Fréquence d’images de sortie (par défaut : "source"). "source" conserve la fréquence de la vidéo, jusqu’à 60 ; une fréquence supérieure est interpolée. Une sortie au-delà de 30 fps coûte deux fois plus cher. | COMBO | Oui | "source"<br>"16"<br>"24"<br>"25"<br>"30"<br>"48"<br>"50"<br>"60" |
| `turbo` | Agrandissement plus rapide avec des détails plus doux, au même prix (par défaut : false). | BOOLEAN | Non | true<br>false |

### Contraintes des paramètres

- Le clip doit faire 512 MiB ou moins, mesuré après son réencodage en H.264 MP4.
- La limite d’images est comptée à un maximum de 30 fps : 2400 images pour 720p, 1200 pour 1080p, 600 pour 2K et 300 pour 4K. Un clip plus long nécessite une cible plus basse, un `fps` plus bas ou un montage plus court.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo agrandie avec son audio d’origine. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaPVideoUpscaleNode/fr.md)

---
**Source fingerprint (SHA-256):** `e8fc88b6177085e0852d17ff92b0a22a26c9914c012a9a244b19da9b2c0e38c2`
