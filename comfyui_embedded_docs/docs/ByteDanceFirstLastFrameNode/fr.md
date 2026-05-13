> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/fr.md)

Ce nœud génère une vidéo à partir d'une invite textuelle ainsi que d'images de première et dernière images. Il prend votre description et les deux images clés pour créer une séquence vidéo complète qui effectue une transition entre elles. Le nœud offre diverses options pour contrôler la résolution, le rapport hauteur/largeur, la durée et d'autres paramètres de génération de la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` | Le modèle à utiliser pour la génération vidéo (par défaut : `"seedance-1-0-lite-i2v-250428"`). |
| `invite` | STRING | Oui | - | L'invite textuelle utilisée pour générer la vidéo. |
| `première_image` | IMAGE | Oui | - | Première image à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0,4 et 2,5. |
| `dernière_image` | IMAGE | Oui | - | Dernière image à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0,4 et 2,5. |
| `résolution` | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` | La résolution de la vidéo de sortie. |
| `ratio_d'aspect` | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | Le rapport hauteur/largeur de la vidéo de sortie (par défaut : `"adaptive"`). |
| `durée` | INT | Oui | 3 - 12 | La durée de la vidéo de sortie en secondes (par défaut : 5). Remarque : Pour le modèle `seedance-1-5-pro-251215`, la durée minimale prise en charge est de 4 secondes. |
| `graine` | INT | Non | 0 - 2147483647 | La graine à utiliser pour la génération (par défaut : 0). |
| `camera_fixed` | BOOLEAN | Non | - | Spécifie s'il faut fixer la caméra. La plateforme ajoute une instruction pour fixer la caméra à votre invite, mais ne garantit pas l'effet réel (par défaut : False). |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo (par défaut : False). |
| `générer_audio` | BOOLEAN | Non | - | Ce paramètre est ignoré pour tous les modèles sauf `seedance-1-5-pro-251215` (par défaut : False). |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |

---
**Source fingerprint (SHA-256):** `2da7b8ad2bc818a21988c028155ba2b466452a1655ac506fcef01c143dda7450`
