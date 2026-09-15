# Génération vidéo Vidu2 à partir d'un texte

Le nœud Vidu2 Text-to-Video Generation crée une vidéo à partir d'une description textuelle. Il se connecte à une API externe pour générer du contenu vidéo à partir de votre prompt, ce qui vous permet de contrôler la durée, le style visuel et le format de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour la génération de vidéo. Actuellement, un seul modèle est disponible. | COMBO | Oui | `"viduq2"` |
| `invite` | Une description textuelle pour la génération de vidéo, d'une longueur maximale de 2000 caractères. | STRING | Oui | - |
| `durée` | La durée de la vidéo générée en secondes. La valeur peut être ajustée à l'aide d'un curseur (par défaut : 5). | INT | Non | 1 à 10 |
| `graine` | Un nombre utilisé pour contrôler l'aléatoire de la génération, permettant d'obtenir des résultats reproductibles. Cette valeur peut être contrôlée après la génération (par défaut : 1). | INT | Non | 0 à 2147483647 |
| `rapport d'aspect` | Le rapport proportionnel entre la largeur et la hauteur de la vidéo. | COMBO | Non | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `résolution` | Les dimensions en pixels de la vidéo générée. Il s'agit d'un paramètre avancé. | COMBO | Non | `"720p"`<br>`"1080p"` |
| `musique de fond` | Indique s'il faut ajouter de la musique de fond à la vidéo générée (par défaut : False). Il s'agit d'un paramètre avancé. | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `27b7c05ae1b3b23d07e775f67474ecef1ffc0bd8240f4aa2219e15949d854f27`
