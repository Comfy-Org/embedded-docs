> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageReferenceNode/fr.md)

Le nœud Image de Référence ByteDance génère des vidéos à partir d’une invite textuelle et d’une à quatre images de référence. Il envoie les images et l’invite à un service API externe qui crée une vidéo correspondant à votre description tout en intégrant le style visuel et le contenu de vos images de référence. Ce nœud offre divers contrôles pour la résolution vidéo, le rapport hauteur/largeur, la durée et d’autres paramètres de génération.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | STRING | Oui | `"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` | Le modèle IA à utiliser pour la génération vidéo (par défaut : `"seedance-1-0-lite-i2v-250428"`). |
| `prompt` | STRING | Oui | - | L’invite textuelle utilisée pour générer la vidéo. |
| `images` | IMAGE | Oui | - | Une à quatre images. Chaque image doit avoir une taille comprise entre 300x300 et 6000x6000 pixels, avec un rapport hauteur/largeur compris entre 0,4 et 2,5. |
| `resolution` | STRING | Oui | `"480p"`<br>`"720p"` | La résolution de la vidéo de sortie. |
| `aspect_ratio` | STRING | Oui | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | Le rapport hauteur/largeur de la vidéo de sortie (par défaut : `"adaptive"`). |
| `duration` | INT | Oui | 3 - 12 | La durée de la vidéo de sortie en secondes (par défaut : 5). |
| `seed` | INT | Non | 0 - 2147483647 | La graine à utiliser pour la génération (par défaut : 0). |
| `watermark` | BOOLEAN | Non | - | Indique s’il faut ajouter un filigrane « Généré par IA » à la vidéo (par défaut : False). |

**Remarque :** Le texte de l’invite ne doit pas contenir les chaînes de paramètres suivantes : `--resolution`, `--ratio`, `--duration`, `--seed` ou `--watermark`. Ces valeurs sont contrôlées exclusivement via leurs widgets d’entrée dédiés.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré en fonction de l’invite d’entrée et des images de référence. |

---
**Source fingerprint (SHA-256):** `d5d1292d6af2fe24dc5c8a10174204546a5a6054ea1f43db44a45ce1017957d6`
