> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

Génère des vidéos à partir de descriptions textuelles en utilisant l'API Google Veo 2. Ce nœud peut créer des vidéos à partir de descriptions textuelles et d'images d'entrée optionnelles, avec un contrôle sur des paramètres tels que le rapport hauteur/largeur, la durée, et plus encore.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Description textuelle de la vidéo (par défaut : vide) |
| `aspect_ratio` | COMBO | Oui | "16:9"<br>"9:16" | Rapport hauteur/largeur de la vidéo de sortie (par défaut : "16:9") |
| `negative_prompt` | STRING | Non | - | Invite textuelle négative pour guider ce qu'il faut éviter dans la vidéo (par défaut : vide) |
| `duration_seconds` | INT | Non | 5-8 | Durée de la vidéo de sortie en secondes (par défaut : 5) |
| `enhance_prompt` | BOOLEAN | Non | - | Indique s'il faut améliorer l'invite avec l'assistance IA (par défaut : True). Il s'agit d'un paramètre avancé. |
| `person_generation` | COMBO | Non | "ALLOW"<br>"BLOCK" | Indique s'il faut autoriser la génération de personnes dans la vidéo (par défaut : "ALLOW"). Il s'agit d'un paramètre avancé. |
| `seed` | INT | Non | 0-4294967295 | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0). Il s'agit d'un paramètre avancé. |
| `image` | IMAGE | Non | - | Image de référence optionnelle pour guider la génération vidéo |
| `modèle` | COMBO | Non | "veo-2.0-generate-001" | Modèle Veo 2 à utiliser pour la génération vidéo (par défaut : "veo-2.0-generate-001") |

**Remarque :** Le paramètre `generate_audio` est uniquement disponible pour les modèles Veo 3.0 et est automatiquement géré par le nœud en fonction du modèle sélectionné. Lors de l'utilisation de modèles Veo 3.0, le paramètre `enhance_prompt` est forcé à True.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |

---
**Source fingerprint (SHA-256):** `1a8b8ffe82fce32566815248f4a2434a1b865b5e5651935ccb3b92c7e38adee9`
