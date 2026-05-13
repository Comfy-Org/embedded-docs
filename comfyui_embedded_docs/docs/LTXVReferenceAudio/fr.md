> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/fr.md)

Voici la traduction en français de la documentation du nœud LTXVReferenceAudio :

Le nœud LTXV Reference Audio est utilisé pour le transfert d'identité du locuteur dans la génération audio. Il encode un clip audio de référence dans le conditionnement d'un modèle, permettant à l'audio généré d'adopter les caractéristiques vocales du locuteur. Il peut également appliquer un guidage d'identité, qui exécute une étape de traitement supplémentaire pour amplifier l'effet d'identité du locuteur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle à patcher avec le guidage d'identité. |
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positive. |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négative. |
| `reference_audio` | AUDIO | Oui | - | Clip audio de référence dont l'identité du locuteur doit être transférée. ~5 secondes recommandées (durée d'entraînement). Des clips plus courts ou plus longs peuvent dégrader le transfert d'identité vocale. |
| `audio_vae` | VAE | Oui | - | VAE audio LTXV pour encoder l'audio de référence. |
| `identity_guidance_scale` | FLOAT | Non | 0.0 - 100.0 | Force du guidage d'identité. Exécute une passe avant supplémentaire sans référence à chaque étape pour amplifier l'identité du locuteur. Mettre à 0 pour désactiver (pas de passe supplémentaire). (par défaut : 3.0) |
| `start_percent` | FLOAT | Non | 0.0 - 1.0 | Début de la plage sigma où le guidage d'identité est actif. (par défaut : 0.0) |
| `end_percent` | FLOAT | Non | 0.0 - 1.0 | Fin de la plage sigma où le guidage d'identité est actif. (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `model` | MODEL | Le modèle patché avec la fonction de guidage d'identité. |
| `positive` | CONDITIONING | Le conditionnement positif, contenant désormais les données audio de référence encodées. |
| `negative` | CONDITIONING | Le conditionnement négatif, contenant désormais les données audio de référence encodées. |

---
**Source fingerprint (SHA-256):** `0b87fb135ba8e752f4114cb47152503b0ec548eefcaa03f99f1cbdda6664874c`
