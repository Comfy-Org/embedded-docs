# Génération de vidéo Google Veo2

Voici la traduction en français de la documentation technique du nœud ComfyUI :

Génère des vidéos à partir de descriptions textuelles en utilisant l'API Google Veo 2. Ce nœud peut créer des vidéos à partir de descriptions textuelles et d'images d'entrée optionnelles, avec un contrôle sur des paramètres tels que le rapport hauteur/largeur, la durée, et plus encore.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Description textuelle de la vidéo (par défaut : vide) | STRING | Oui | - |
| `aspect_ratio` | Rapport hauteur/largeur de la vidéo de sortie (par défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `negative_prompt` | Invite textuelle négative pour guider ce qu'il faut éviter dans la vidéo (par défaut : vide) | STRING | Non | - |
| `duration_seconds` | Durée de la vidéo de sortie en secondes (par défaut : 5) | INT | Non | 5-8 |
| `enhance_prompt` | Indique s'il faut améliorer l'invite avec l'assistance IA (par défaut : True). Il s'agit d'un paramètre avancé. | BOOLEAN | Non | - |
| `person_generation` | Indique s'il faut autoriser la génération de personnes dans la vidéo (par défaut : "ALLOW"). Il s'agit d'un paramètre avancé. | COMBO | Non | "ALLOW"<br>"BLOCK" |
| `seed` | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0). Il s'agit d'un paramètre avancé. | INT | Non | 0-4294967295 |
| `image` | Image de référence optionnelle pour guider la génération vidéo | IMAGE | Non | - |
| `modèle` | Modèle Veo 2 à utiliser pour la génération vidéo (par défaut : "veo-2.0-generate-001") | COMBO | Non | "veo-2.0-generate-001" |

**Remarque :** Le paramètre `generate_audio` est uniquement disponible pour les modèles Veo 3.0 et est automatiquement géré par le nœud en fonction du modèle sélectionné. Lors de l'utilisation de modèles Veo 3.0, le paramètre `enhance_prompt` est forcé à True.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/fr.md)

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
