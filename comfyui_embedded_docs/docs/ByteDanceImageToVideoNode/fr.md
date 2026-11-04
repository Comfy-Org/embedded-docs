# ByteDance Image en vidéo

Le nœud ByteDance Image to Video génère des vidéos à l'aide des modèles ByteDance via une API à partir d'une image d'entrée et d'une invite textuelle. Il prend une image initiale comme première image et crée une séquence vidéo qui suit la description fournie. Le nœud offre diverses options de personnalisation pour la résolution vidéo, le format d'image, la durée et d'autres paramètres de génération.

**Remarque :** Ce nœud est marqué comme obsolète dans le code source.

**Remarque:** BytePlus arrête le modèle Seedance 1.5 Pro le 11 novembre 2026 : ce nœud ne le propose donc plus et les workflows enregistrés avec lui cessent de fonctionner. Utilisez plutôt `seedance-1-0-pro-250528`, `seedance-1-0-pro-fast-251015` ou le [nœud partenaire Seedance 2.5](https://docs.comfy.org/fr/tutorials/partner-nodes/bytedance/seedance-2-5).

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `modèle` | Le modèle ByteDance à utiliser pour la génération vidéo (par défaut : `"seedance-1-0-pro-fast-251015"`). | COMBO | Oui | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | L'invite textuelle utilisée pour générer la vidéo. Doit contenir au moins 1 caractère après suppression des espaces. | STRING | Oui | - |
| `image` | Première image à utiliser pour la vidéo. Doit être comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur entre 0.4 et 2.5. | IMAGE | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `ratio_d'aspect` | Le rapport hauteur/largeur de la vidéo de sortie. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 3 - 12 |
| `graine` | Graine à utiliser pour la génération (par défaut : 0). | INT | Non | 0 - 2147483647 |
| `caméra_fixe` | Spécifie si la caméra doit être fixe. La plateforme ajoute une instruction de fixation de la caméra à votre invite, mais ne garantit pas l'effet réel (par défaut : False). | BOOLEAN | Non | `False`<br>`True` |
| `filigrane` | Indique s'il faut ajouter un filigrane « généré par IA » à la vidéo (par défaut : False). | BOOLEAN | Non | `False`<br>`True` |
| `générer_audio` | Ajoute une piste audio générée par IA. Les modèles restants ignorent cette entrée (par défaut : False). | BOOLEAN | Non | `False`<br>`True` |

**Remarque :** L'invite ne doit pas contenir les mots suivants (insensibles à la casse) : `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Ces paramètres sont définis via leurs entrées dédiées.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `output` | Le fichier vidéo généré à partir de l'image d'entrée et des paramètres de l'invite. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `a1841a368e625bd90583e0f0dbdc32369e6701a44cf985f01de8faa3d999b224`
