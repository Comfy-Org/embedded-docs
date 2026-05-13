> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/fr.md)

Voici la traduction en français de la documentation du nœud Vidu2 Text-to-Video :

Le nœud de génération vidéo Vidu2 à partir de texte crée une vidéo à partir d'une description textuelle. Il se connecte à une API externe pour générer un contenu vidéo basé sur votre invite, vous permettant de contrôler la durée, le style visuel et le format de la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"viduq2"` | Le modèle d'IA à utiliser pour la génération vidéo. Actuellement, un seul modèle est disponible. |
| `prompt` | STRING | Oui | - | Une description textuelle pour la génération vidéo, avec une longueur maximale de 2000 caractères. |
| `duration` | INT | Non | 1 à 10 | La durée de la vidéo générée en secondes. La valeur peut être ajustée à l'aide d'un curseur (par défaut : 5). |
| `seed` | INT | Non | 0 à 2147483647 | Un nombre utilisé pour contrôler l'aléatoire de la génération, permettant d'obtenir des résultats reproductibles. Il peut être contrôlé après la génération (par défaut : 1). |
| `aspect_ratio` | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` | La relation proportionnelle entre la largeur et la hauteur de la vidéo. |
| `resolution` | COMBO | Non | `"720p"`<br>`"1080p"` | Les dimensions en pixels de la vidéo générée. Il s'agit d'un paramètre avancé. |
| `background_music` | BOOLEAN | Non | - | Indique s'il faut ajouter une musique de fond à la vidéo générée (par défaut : False). Il s'agit d'un paramètre avancé. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `1e9e3629806e9b5a66d8f830d8ec33ef208a7a27b53caf43b44f7b746a85014b`
