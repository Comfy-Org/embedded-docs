> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/fr.md)

Le nœud ByteDance Image to Video génère des vidéos à l'aide des modèles ByteDance via une API, en se basant sur une image d'entrée et un texte descriptif. Il prend une image de départ comme première frame et crée une séquence vidéo qui suit la description fournie. Le nœud offre diverses options de personnalisation pour la résolution vidéo, le rapport hauteur/largeur, la durée et d'autres paramètres de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | STRING | Oui | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` | Le modèle ByteDance à utiliser pour la génération vidéo (par défaut : `"seedance-1-0-pro-fast-251015"`). |
| `prompt` | STRING | Oui | - | Le texte descriptif utilisé pour générer la vidéo. Doit contenir au moins 1 caractère après suppression des espaces. |
| `image` | IMAGE | Oui | - | Première frame à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0,4 et 2,5. |
| `resolution` | STRING | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` | La résolution de la vidéo de sortie. |
| `aspect_ratio` | STRING | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | Le rapport hauteur/largeur de la vidéo de sortie. |
| `duration` | INT | Oui | 3 - 12 | La durée de la vidéo de sortie en secondes (par défaut : 5). Pour le modèle `seedance-1-5-pro-251215`, la durée minimale prise en charge est de 4 secondes. |
| `seed` | INT | Non | 0 - 2147483647 | Graine à utiliser pour la génération (par défaut : 0). |
| `camera_fixed` | BOOLEAN | Non | - | Spécifie si la caméra doit être fixe. La plateforme ajoute une instruction pour fixer la caméra à votre prompt, mais ne garantit pas l'effet réel (par défaut : False). |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo (par défaut : False). |
| `generate_audio` | BOOLEAN | Non | - | Ce paramètre est ignoré pour tous les modèles sauf `seedance-1-5-pro-251215` (par défaut : False). |

**Remarque :** Le prompt ne doit pas contenir les mots suivants (insensibles à la casse) : `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Ces paramètres sont définis via leurs entrées dédiées.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré en fonction de l'image d'entrée et des paramètres du prompt. |

---
**Source fingerprint (SHA-256):** `e47e14c69f4bdf4921a5a5eaec20fb775473483e80cdd9dd6700d2c7f9219e65`
