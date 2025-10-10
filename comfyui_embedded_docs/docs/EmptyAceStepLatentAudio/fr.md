> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/fr.md)

Le nœud EmptyAceStepLatentAudio crée des échantillons audio latents vides d'une durée spécifiée. Il génère un lot d'audio latent silencieux avec des zéros, où la longueur est calculée en fonction des secondes d'entrée et des paramètres de traitement audio. Ce nœud est utile pour initialiser les workflows de traitement audio qui nécessitent des représentations latentes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | Non | 1.0 - 1000.0 | La durée de l'audio en secondes (par défaut : 120.0) |
| `batch_size` | INT | Non | 1 - 4096 | Le nombre d'images latentes dans le lot (par défaut : 1) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | LATENT | Retourne des échantillons audio latents vides avec des zéros |