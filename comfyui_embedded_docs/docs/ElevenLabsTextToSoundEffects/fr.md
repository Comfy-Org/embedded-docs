# ElevenLabs Text to Sound Effects

Le nœud ElevenLabs Text to Sound Effects génère un effet sonore à partir d'une description textuelle à l'aide de l'API ElevenLabs. Il envoie votre prompt écrit au service de génération d'effets sonores ElevenLabs et renvoie l'audio résultant, avec des contrôles pour la durée, le comportement de boucle et la fidélité du son au texte.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Modèle à utiliser pour la génération d'effets sonores. Le modèle sélectionné détermine les paramètres de génération disponibles listés ci-dessous. | DYNAMIC_COMBO | Oui | `"eleven_sfx_v2"` |
| `text` | Description textuelle de l'effet sonore à générer. Doit contenir au moins 1 caractère. (par défaut : vide) | STRING | Oui | N/A |
| `output_format` | Format de sortie audio. | COMBO | Oui | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entrées Eleven SFX v2

Sous-paramètres affichés lorsque `model` est défini sur `"eleven_sfx_v2"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `duration` | Durée du son généré en secondes. (par défaut : 5.0) | FLOAT | Oui | 0.5 à 30.0 (pas de 0.1) |
| `loop` | Crée un effet sonore en boucle fluide. (par défaut : False) | BOOLEAN | Non | True ou False |
| `prompt_influence` | Degré de fidélité de la génération au prompt. Des valeurs plus élevées rendent le son plus proche du texte. (par défaut : 0.3) | FLOAT | Oui | 0.0 à 1.0 (pas de 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------|
| `audio` | Le fichier audio de l'effet sonore généré. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/fr.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
