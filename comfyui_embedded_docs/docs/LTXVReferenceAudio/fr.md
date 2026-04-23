> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/fr.md)

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle à modifier avec le guidage d'identité. |
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positive. |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négative. |
| `reference_audio` | AUDIO | Oui | - | Extrait audio de référence dont l'identité du locuteur doit être transférée. Une durée d'environ 5 secondes est recommandée (durée d'entraînement). Des extraits plus courts ou plus longs peuvent dégrader le transfert de l'identité vocale. |
| `audio_vae` | VAE | Oui | - | VAE audio LTXV pour encoder l'audio de référence. |
| `identity_guidance_scale` | FLOAT | Non | 0.0 - 100.0 | Intensité du guidage d'identité. Exécute une passe avant supplémentaire sans référence à chaque étape pour amplifier l'identité du locuteur. Régler à 0 pour désactiver (pas de passe supplémentaire). (par défaut : 3.0) |
| `start_percent` | FLOAT | Non | 0.0 - 1.0 | Début de la plage de sigma où le guidage d'identité est actif. (par défaut : 0.0) |
| `end_percent` | FLOAT | Non | 0.0 - 1.0 | Fin de la plage de sigma où le guidage d'identité est actif. (par défaut : 1.0) |

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `model` | MODEL | Le modèle modifié avec la fonction de guidage d'identité. |
| `positive` | CONDITIONING | Le conditionnement positif, contenant désormais les données audio de référence encodées. |
| `negative` | CONDITIONING | Le conditionnement négatif, contenant désormais les données audio de référence encodées. |