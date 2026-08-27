# ElevenLabs Text to Sound Effects

Le nœud ElevenLabs Text to Sound Effects génère des effets sonores audio à partir d'une description textuelle. Il utilise l'API ElevenLabs pour créer des effets sonores en fonction de votre invite, vous permettant de contrôler la durée, le comportement de boucle et la fidélité du son au texte.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération d'effets sonores. Un seul modèle est actuellement disponible : `eleven_sfx_v2`. | DYNAMIC_COMBO | Oui | `"eleven_sfx_v2"` |
| `text` | Description textuelle de l'effet sonore à générer. (par défaut : vide) | STRING | Oui | N/A |
| `output_format` | Format de sortie audio. | COMBO | Oui | `"mp3_44100_192"`<br>`"opus_48000_192"` |

### Entrées eleven_sfx_v2

Ces paramètres sont affichés lorsque le modèle `eleven_sfx_v2` est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `duration` | Durée du son généré en secondes. (par défaut : 5.0) | FLOAT | Oui | 0.5 à 30.0 |
| `loop` | Crée un effet sonore en boucle fluide. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `prompt_influence` | Degré de fidélité de la génération à l'invite. Des valeurs plus élevées rendent le son plus conforme au texte. (par défaut : 0.3) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Le paramètre `text` ne doit pas être vide ; il est validé avant l'envoi de la demande de génération sonore.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | Le fichier audio de l'effet sonore généré. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/fr.md)

---
**Source fingerprint (SHA-256):** `218ff617256cea33f310c1bcfc6407c46aaadc59201a0324b0ec64583166ce58`
