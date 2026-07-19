# ElevenLabs Clonage Instantané de Voix

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/en.md)

Le nœud ElevenLabs Instant Voice Clone crée un nouveau modèle vocal unique en analysant de 1 à 8 enregistrements audio de la voix d'une personne. Il envoie ces échantillons à l'API ElevenLabs, qui les traite pour générer un clone vocal pouvant être utilisé pour la synthèse vocale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `audio_*` | Enregistrements audio pour le clonage vocal. Vous devez fournir entre 1 et 8 fichiers audio. | AUDIO | Oui | 1 à 8 fichiers |
| `supprimer_bruit_de_fond` | Supprime le bruit de fond des échantillons vocaux à l'aide de l'isolation audio. (par défaut : Faux) | BOOLEAN | Non | Vrai / Faux |

**Remarque :** Vous devez fournir au moins un fichier audio, et vous pouvez en fournir jusqu'à huit. Le nœud créera automatiquement des emplacements d'entrée pour les fichiers audio que vous ajoutez.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `voix` | L'identifiant unique du modèle vocal cloné nouvellement créé. Cette sortie peut être connectée à d'autres nœuds de synthèse vocale ElevenLabs. | ELEVENLABS_VOICE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsInstantVoiceClone/fr.md)

---
**Source fingerprint (SHA-256):** `297598e183df3ccddabc75d6903c5c69f10648adeea430e546f9c5f6df49bdb2`
