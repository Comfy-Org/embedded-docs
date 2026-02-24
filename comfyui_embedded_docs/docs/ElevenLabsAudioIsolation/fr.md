> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/fr.md)

Le nœud ElevenLabs Voice Isolation supprime le bruit de fond d'un fichier audio, en isolant les voix ou la parole. Il envoie l'audio à l'API ElevenLabs pour traitement et renvoie l'audio nettoyé.

## Entrées

| Paramètre | Type de données | Obligatoire | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Oui | | Audio à traiter pour la suppression du bruit de fond. |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `audio` | AUDIO | L'audio traité avec le bruit de fond supprimé. |
