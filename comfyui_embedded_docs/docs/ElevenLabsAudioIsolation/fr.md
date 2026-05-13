> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/fr.md)

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/en.md)

Le nœud d'isolation vocale ElevenLabs supprime le bruit de fond d'un fichier audio, en isolant les voix ou la parole. Il envoie l'audio à l'API ElevenLabs pour traitement et renvoie l'audio nettoyé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio` | AUDIO | Oui | | Audio à traiter pour la suppression du bruit de fond. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `audio` | AUDIO | L'audio traité avec le bruit de fond supprimé. |

---
**Source fingerprint (SHA-256):** `eca7919ff853fe48f8419a4135a99589e350d3d113631e27f6e7cb3cbb3faa3b`
