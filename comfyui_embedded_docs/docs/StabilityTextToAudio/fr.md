> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/fr.md)

Génère de la musique et des effets sonores de haute qualité à partir de descriptions textuelles. Ce nœud utilise la technologie de génération audio de Stability AI pour créer du contenu audio basé sur vos invites textuelles.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"stable-audio-2.5"` | Le modèle de génération audio à utiliser (par défaut : "stable-audio-2.5") |
| `prompt` | STRING | Oui | - | La description textuelle utilisée pour générer le contenu audio (par défaut : chaîne vide) |
| `duration` | INT | Non | 1-190 | Contrôle la durée en secondes de l'audio généré (par défaut : 190) |
| `seed` | INT | Non | 0-4294967294 | La graine aléatoire utilisée pour la génération (par défaut : 0) |
| `steps` | INT | Non | 4-8 | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | Le fichier audio généré basé sur l'invite textuelle |