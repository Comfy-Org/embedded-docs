# ChargerAudio

Voici la traduction de la documentation du nœud LoadAudio, conforme à vos règles :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/en.md)

Le nœud LoadAudio charge des fichiers audio depuis le répertoire d'entrée et les convertit dans un format pouvant être traité par d'autres nœuds audio dans ComfyUI. Il lit les fichiers audio et extrait à la fois les données de forme d'onde et la fréquence d'échantillonnage, les rendant disponibles pour les tâches de traitement audio en aval.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio` | Le fichier audio à charger depuis le répertoire d'entrée | AUDIO | Oui | Tous les fichiers audio et vidéo pris en charge dans le répertoire d'entrée |

**Remarque :** Le nœud accepte uniquement les fichiers audio et vidéo présents dans le répertoire d'entrée de ComfyUI. Le fichier doit exister et être accessible pour un chargement réussi.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `AUDIO` | Données audio contenant les informations de forme d'onde et de fréquence d'échantillonnage | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/fr.md)

---
**Source fingerprint (SHA-256):** `a7fe63cbbb3a854359189e8685936a2b8b855e22c3c282fc77affacf640af010`
