# FishAudioInstantVoiceClone

Ce nœud crée une voix clonée privée à partir de vos enregistrements audio via l'API Fish Audio. Vous fournissez un ou plusieurs échantillons audio, et le nœud construit une voix personnalisée qui peut être immédiatement utilisée pour la synthèse vocale. Il accepte de 1 à 20 enregistrements, avec une durée recommandée de 10 à 30 secondes chacun et une limite totale de 270 secondes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `files` | Enregistrements audio pour le clonage de voix. Il s'agit d'une entrée extensible : connectez un ou plusieurs éléments audio (par exemple `audio_1`, `audio_2`, ...) pour fournir les échantillons vocaux. | AUDIO | Oui | 1 à 20 enregistrements |
| `enhance_audio_quality` | Améliorer la qualité de l'audio de référence avant l'entraînement (par défaut : True). | BOOLEAN | Oui | True<br>False |

**Remarque :** La durée totale de tous les audios de référence combinés doit être inférieure à 270 secondes. Si la durée combinée atteint ou dépasse 270 secondes, le nœud renvoie une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `voice` | La voix clonée nouvellement créée, identifiée par un identifiant de voix unique renvoyé par l'API Fish Audio. Cette voix peut être utilisée pour la synthèse vocale. | FISHAUDIO_VOICE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioInstantVoiceClone/fr.md)

---
**Source fingerprint (SHA-256):** `6c4f011a4611a076b2488152591efeb61c029d6dfae2b079ba74689891c84803`
