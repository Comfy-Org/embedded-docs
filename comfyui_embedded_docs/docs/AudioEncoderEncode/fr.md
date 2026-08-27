# EncodeurAudioEncoder

Le nœud AudioEncoderEncode convertit des données audio en une représentation encodée à l'aide d'un modèle d'encodeur audio. Il prend un encodeur audio et une entrée audio brute, puis extrait la forme d'onde et la fréquence d'échantillonnage de l'audio pour produire une sortie encodée adaptée à un traitement ultérieur dans le pipeline de conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `encodeur_audio` | Le modèle d'encodeur audio utilisé pour traiter l'entrée audio | AUDIO_ENCODER | Oui | - |
| `audio` | Les données audio contenant les informations de forme d'onde et de fréquence d'échantillonnage | AUDIO | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La représentation audio encodée générée par l'encodeur audio | AUDIO_ENCODER_OUTPUT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/fr.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
