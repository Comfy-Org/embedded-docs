> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `audio_*` | AUDIO | Oui | 1 à 8 fichiers | Enregistrements audio pour le clonage vocal. Vous devez fournir entre 1 et 8 fichiers audio. |
| `remove_background_noise` | BOOLEAN | Non | Vrai / Faux | Supprime le bruit de fond des échantillons vocaux en utilisant l'isolation audio. (par défaut : Faux) |

**Note :** Vous devez fournir au moins un fichier audio, et vous pouvez en fournir jusqu'à huit. Le nœud créera automatiquement des emplacements d'entrée pour les fichiers audio que vous ajoutez.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `voice` | ELEVENLABS_VOICE | L'identifiant unique du nouveau modèle vocal cloné créé. Cette sortie peut être connectée à d'autres nœuds de synthèse vocale ElevenLabs. |