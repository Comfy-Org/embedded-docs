Voici la traduction en français de la documentation du nœud ByteDance Text to Video :

Le nœud ByteDance Text to Video génère des vidéos en utilisant les modèles ByteDance via une API basée sur des invites textuelles. Il prend en entrée une description textuelle et divers paramètres vidéo, puis crée une vidéo correspondant aux spécifications fournies. Le nœud gère la communication avec l'API et renvoie la vidéo générée en sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle ByteDance à utiliser pour la génération (par défaut : `"seedance-1-0-pro-fast-251015"`). | STRING | Oui | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-t2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | L'invite textuelle utilisée pour générer la vidéo. | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. | STRING | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo de sortie. | STRING | Oui | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | La durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 3 à 12 |
| `seed` | La graine à utiliser pour la génération (par défaut : 0). | INT | Non | 0 à 2147483647 |
| `camera_fixed` | Spécifie si la caméra doit être fixe. La plateforme ajoute une instruction pour fixer la caméra à votre invite, mais ne garantit pas l'effet réel (par défaut : False). | BOOLEAN | Non | - |
| `filigrane` | Indique s'il faut ajouter un filigrane "Généré par IA" à la vidéo (par défaut : False). | BOOLEAN | Non | - |
| `générer_audio` | Ce paramètre est ignoré pour tous les modèles sauf `seedance-1-5-pro-251215` (par défaut : False). | BOOLEAN | Non | - |

**Contraintes des paramètres :**

- Le paramètre `prompt` doit contenir au moins 1 caractère après suppression des espaces.
- Le paramètre `prompt` ne peut pas contenir les paramètres textuels suivants : "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- Le paramètre `duration` est limité à des valeurs comprises entre 3 et 12 secondes. Pour le modèle `seedance-1-5-pro-251215`, la durée minimale prise en charge est de 4 secondes.
- Le paramètre `seed` accepte des valeurs de 0 à 2 147 483 647.
- Le paramètre `generate_audio` n'a d'effet que lorsque le `model` est défini sur `seedance-1-5-pro-251215` ; il est ignoré pour tous les autres modèles.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `44ea3e40b99b337340cc39be1c5b6c903680591f1de49b1f2e82f398979355c5`
