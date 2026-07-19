# ByteDance Première-Dernière Image vers Vidéo

Ce nœud génère une vidéo à partir d'une invite textuelle ainsi que d'images de première et dernière images. Il prend votre description et les deux images clés pour créer une séquence vidéo complète qui effectue une transition entre elles. Le nœud offre diverses options pour contrôler la résolution, le rapport hauteur/largeur, la durée et d'autres paramètres de génération de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour la génération vidéo (par défaut : `"seedance-1-0-lite-i2v-250428"`). | COMBO | Oui | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` |
| `invite` | L'invite textuelle utilisée pour générer la vidéo. | STRING | Oui | - |
| `première_image` | Première image à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0,4 et 2,5. | IMAGE | Oui | - |
| `dernière_image` | Dernière image à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0,4 et 2,5. | IMAGE | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio_d'aspect` | Le rapport hauteur/largeur de la vidéo de sortie (par défaut : `"adaptive"`). | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut : 5). Remarque : Pour le modèle `seedance-1-5-pro-251215`, la durée minimale prise en charge est de 4 secondes. | INT | Oui | 3 - 12 |
| `graine` | La graine à utiliser pour la génération (par défaut : 0). | INT | Non | 0 - 2147483647 |
| `camera_fixed` | Spécifie s'il faut fixer la caméra. La plateforme ajoute une instruction pour fixer la caméra à votre invite, mais ne garantit pas l'effet réel (par défaut : False). | BOOLEAN | Non | - |
| `watermark` | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo (par défaut : False). | BOOLEAN | Non | - |
| `générer_audio` | Ce paramètre est ignoré pour tous les modèles sauf `seedance-1-5-pro-251215` (par défaut : False). | BOOLEAN | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `2da7b8ad2bc818a21988c028155ba2b466452a1655ac506fcef01c143dda7450`
