> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/fr.md)

Le nœud TextEncodeAceStepAudio1.5 prépare les métadonnées textuelles et audio pour le modèle AceStepAudio 1.5. Il prend des balises descriptives, des paroles et des paramètres musicaux, puis utilise un modèle CLIP pour les convertir en un format de conditionnement adapté à la génération audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | N/A | Le modèle CLIP utilisé pour tokeniser et encoder le texte d'entrée. |
| `tags` | STRING | Oui | N/A | Balises descriptives pour l'audio, telles que le genre, l'ambiance ou les instruments. Prend en charge les entrées multilignes et les invites dynamiques. |
| `lyrics` | STRING | Oui | N/A | Les paroles de la piste audio. Prend en charge les entrées multilignes et les invites dynamiques. |
| `seed` | INT | Non | 0 à 18446744073709551615 | Une valeur de graine aléatoire pour une génération reproductible. Dispose d'un widget control_after_generate. Par défaut : 0. |
| `bpm` | INT | Non | 10 à 300 | Le nombre de battements par minute (BPM) pour l'audio généré. Par défaut : 120. |
| `duration` | FLOAT | Non | 0,0 à 2000,0 | La durée souhaitée de l'audio en secondes. Par défaut : 120,0. |
| `timesignature` | COMBO | Non | `"2"`<br>`"3"`<br>`"4"`<br>`"6"` | La signature rythmique musicale. |
| `language` | COMBO | Non | `"ar"`<br>`"az"`<br>`"bg"`<br>`"bn"`<br>`"ca"`<br>`"cs"`<br>`"da"`<br>`"de"`<br>`"el"`<br>`"en"`<br>`"es"`<br>`"fa"`<br>`"fi"`<br>`"fr"`<br>`"he"`<br>`"hi"`<br>`"hr"`<br>`"ht"`<br>`"hu"`<br>`"id"`<br>`"is"`<br>`"it"`<br>`"ja"`<br>`"ko"`<br>`"la"`<br>`"lt"`<br>`"ms"`<br>`"ne"`<br>`"nl"`<br>`"no"`<br>`"pa"`<br>`"pl"`<br>`"pt"`<br>`"ro"`<br>`"ru"`<br>`"sa"`<br>`"sk"`<br>`"sr"`<br>`"sv"`<br>`"sw"`<br>`"ta"`<br>`"te"`<br>`"th"`<br>`"tl"`<br>`"tr"`<br>`"uk"`<br>`"ur"`<br>`"vi"`<br>`"yue"`<br>`"zh"`<br>`"unknown"` | La langue du texte d'entrée. Par défaut : "en". |
| `keyscale` | COMBO | Non | `"C major"`<br>`"C minor"`<br>`"C# major"`<br>`"C# minor"`<br>`"Db major"`<br>`"Db minor"`<br>`"D major"`<br>`"D minor"`<br>`"D# major"`<br>`"D# minor"`<br>`"Eb major"`<br>`"Eb minor"`<br>`"E major"`<br>`"E minor"`<br>`"F major"`<br>`"F minor"`<br>`"F# major"`<br>`"F# minor"`<br>`"Gb major"`<br>`"Gb minor"`<br>`"G major"`<br>`"G minor"`<br>`"G# major"`<br>`"G# minor"`<br>`"Ab major"`<br>`"Ab minor"`<br>`"A major"`<br>`"A minor"`<br>`"A# major"`<br>`"A# minor"`<br>`"Bb major"`<br>`"Bb minor"`<br>`"B major"`<br>`"B minor"` | La tonalité et la gamme musicales (majeur ou mineur). |
| `generate_audio_codes` | BOOLEAN | Non | N/A | Active le LLM qui génère les codes audio. Cela peut être lent mais améliorera la qualité de l'audio généré. Désactivez cette option si vous fournissez une référence audio au modèle. Par défaut : Vrai. |
| `cfg_scale` | FLOAT | Non | 0,0 à 100,0 | L'échelle de guidage sans classifieur. Des valeurs plus élevées font que la sortie suit plus fidèlement l'invite. Par défaut : 2,0. |
| `temperature` | FLOAT | Non | 0,0 à 2,0 | Une température d'échantillonnage. Des valeurs plus basses rendent la sortie plus déterministe. Par défaut : 0,85. |
| `top_p` | FLOAT | Non | 0,0 à 2000,0 | La probabilité d'échantillonnage nucléaire (top-p). Par défaut : 0,9. |
| `top_k` | INT | Non | 0 à 100 | Le nombre de jetons avec la probabilité la plus élevée à considérer (top-k). Par défaut : 0. |
| `min_p` | FLOAT | Non | 0,0 à 1,0 | Le seuil de probabilité minimum pour l'échantillonnage des jetons (min-p). Par défaut : 0,000. |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Les données de conditionnement, qui contiennent le texte encodé et les paramètres audio pour le modèle AceStepAudio 1.5. |

---
**Source fingerprint (SHA-256):** `df70a55024812d8c77a3b618cbff6d3148a3f3f5fc4d17dd3c4282ce7f3cbc2c`
