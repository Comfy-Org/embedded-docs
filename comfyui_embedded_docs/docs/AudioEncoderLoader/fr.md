# ChargeurEncodeurAudio

Le nœud `AudioEncoderLoader` charge un modèle d'encodeur audio à partir d'un fichier dans votre dossier d'encodeurs audio. Il prend le nom de fichier d'un modèle d'encodeur audio comme entrée et retourne le modèle chargé, qui peut ensuite être utilisé pour des tâches de traitement audio dans votre flux de travail.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio_encoder_name` | Sélectionne le fichier de modèle d'encodeur audio à charger | COMBO | Oui | Liste des fichiers d'encodeur audio disponibles dans le dossier audio_encoders |

Note : Le fichier sélectionné doit contenir un modèle d'encodeur audio valide. Si le fichier est invalide et ne contient pas un modèle valide, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio_encoder` | Le modèle d'encodeur audio chargé, prêt à être utilisé dans des flux de travail de traitement audio | AUDIO_ENCODER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/fr.md)

---
**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`
