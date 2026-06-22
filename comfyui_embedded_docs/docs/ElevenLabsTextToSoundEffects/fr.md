# ElevenLabs Text to Sound Effects

Le nœud ElevenLabs Text to Sound Effects génère des effets sonores audio à partir d'une description textuelle. Il utilise l'API ElevenLabs pour créer des effets sonores basés sur votre prompt, vous permettant de contrôler la durée, le comportement de boucle et la fidélité du son au texte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `text` | Description textuelle de l'effet sonore à générer. Ce champ est obligatoire. | STRING | Oui | N/A |
| `model` | Modèle à utiliser pour la génération d'effets sonores. La sélection de ce modèle révèle des paramètres supplémentaires : `duration` (par défaut : 5,0, plage : 0,5 à 30,0 secondes), `loop` (par défaut : False) et `prompt_influence` (par défaut : 0,3, plage : 0,0 à 1,0). | COMBO | Oui | `"eleven_sfx_v2"` |
| `output_format` | Format de sortie audio. | COMBO | Oui | `"mp3_44100_192"`<br>`"opus_48000_192"` |

**Détails des paramètres :**

* **`model["duration"]`** : Durée de l'effet sonore généré en secondes. La valeur par défaut est 5,0, avec un minimum de 0,5 et un maximum de 30,0.
* **`model["loop"]`** : Lorsqu'il est activé, crée un effet sonore en boucle fluide. La valeur par défaut est False.
* **`model["prompt_influence"]`** : Contrôle la fidélité de la génération au prompt textuel. Des valeurs plus élevées font correspondre le son plus étroitement au texte. La valeur par défaut est 0,3, avec une plage de 0,0 à 1,0.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | Le fichier audio de l'effet sonore généré. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/fr.md)

---
**Source fingerprint (SHA-256):** `c23c4dd3c9c12f0e891d40683265c5b74b5c6320601aaadb686489510db9f107`
