# ByteDance Images de référence en vidéo

Le nœud Image de Référence ByteDance génère des vidéos à partir d’une invite textuelle et d’une à quatre images de référence. Il envoie les images et l’invite à un service API externe qui crée une vidéo correspondant à votre description tout en intégrant le style visuel et le contenu de vos images de référence. Ce nœud offre divers contrôles pour la résolution vidéo, le rapport hauteur/largeur, la durée et d’autres paramètres de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle IA à utiliser pour la génération vidéo (par défaut : `"seedance-1-0-lite-i2v-250428"`). | STRING | Oui | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` |
| `prompt` | L’invite textuelle utilisée pour générer la vidéo. | STRING | Oui | - |
| `images` | Une à quatre images. Chaque image doit avoir une taille comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0,4 et 2,5. | IMAGE | Oui | - |
| `résolution` | La résolution de la vidéo de sortie. | STRING | Oui | `"480p"`<br>`"720p"` |
| `ratio_d'aspect` | Le rapport hauteur/largeur de la vidéo de sortie (par défaut : `"adaptive"`). | STRING | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `durée` | La durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 3 - 12 |
| `graine` | La graine à utiliser pour la génération (par défaut : 0). | INT | Non | 0 - 2147483647 |
| `filigrane` | Indique s’il faut ajouter un filigrane « Généré par IA » à la vidéo (par défaut : False). | BOOLEAN | Non | - |

**Remarque :** Le texte de l’invite ne doit pas contenir les chaînes de paramètres suivantes : `--resolution`, `--ratio`, `--duration`, `--seed` ou `--watermark`. Ces valeurs sont contrôlées exclusivement via leurs widgets d’entrée dédiés.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré en fonction de l’invite d’entrée et des images de référence. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/fr.md)

---
**Source fingerprint (SHA-256):** `d5d1292d6af2fe24dc5c8a10174204546a5a6054ea1f43db44a45ce1017957d6`
