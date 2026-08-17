# LTXV Reference Audio (ID-LoRA)

Le nœud LTXV Reference Audio définit un clip audio de référence pour le transfert d'identité du locuteur ID-LoRA dans la génération audio. Il encode le clip dans le conditionnement afin que l’audio généré adopte les caractéristiques vocales du locuteur, et modifie éventuellement le modèle avec un guidage d’identité, ce qui exécute une passe avant supplémentaire sans la référence pour amplifier l’effet d’identité du locuteur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle à modifier avec le guidage d’identité. | MODEL | Oui | - |
| `positive` | L’entrée de conditionnement positive. | CONDITIONING | Oui | - |
| `negative` | L’entrée de conditionnement négative. | CONDITIONING | Oui | - |
| `reference_audio` | Clip audio de référence dont l’identité du locuteur doit être transférée. ~5 secondes recommandées (durée d’entraînement). Des clips plus courts ou plus longs peuvent dégrader le transfert d’identité vocale. | AUDIO | Oui | - |
| `audio_vae` | VAE audio LTXV pour l’encodage. | VAE | Oui | - |
| `identity_guidance_scale` | Intensité du guidage d’identité. Exécute une passe avant supplémentaire sans référence à chaque étape pour amplifier l’identité du locuteur. Mettre à 0 pour désactiver (aucune passe supplémentaire). (par défaut : 3.0) | FLOAT | Non | 0.0 - 100.0 |
| `start_percent` | Début de la plage sigma où le guidage d’identité est actif. (par défaut : 0.0) | FLOAT | Non | 0.0 - 1.0 |
| `end_percent` | Fin de la plage sigma où le guidage d’identité est actif. (par défaut : 1.0) | FLOAT | Non | 0.0 - 1.0 |

Note : Le guidage d’identité n’est actif que pour les valeurs de sigma comprises dans la plage définie par `start_percent` et `end_percent` ; en dehors de cette plage, la sortie débruitée reste inchangée. L’audio de référence est ajouté à la fois au conditionnement positif et au conditionnement négatif. Si la fréquence d’échantillonnage de l’audio de référence diffère de celle du VAE audio, l’audio est rééchantillonné automatiquement pour correspondre au VAE.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec la fonction de guidage d’identité. | MODEL |
| `positive` | Le conditionnement positif, contenant désormais les données audio de référence encodées. | CONDITIONING |
| `negative` | Le conditionnement négatif, contenant désormais les données audio de référence encodées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
