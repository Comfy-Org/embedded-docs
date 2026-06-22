# LTXV Reference Audio (ID-LoRA)

Voici la traduction en français de la documentation du nœud LTXVReferenceAudio :

Le nœud LTXV Reference Audio est utilisé pour le transfert d'identité du locuteur dans la génération audio. Il encode un clip audio de référence dans le conditionnement d'un modèle, permettant à l'audio généré d'adopter les caractéristiques vocales du locuteur. Il peut également appliquer un guidage d'identité, qui exécute une étape de traitement supplémentaire pour amplifier l'effet d'identité du locuteur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à patcher avec le guidage d'identité. | MODEL | Oui | - |
| `positif` | L'entrée de conditionnement positive. | CONDITIONING | Oui | - |
| `négatif` | L'entrée de conditionnement négative. | CONDITIONING | Oui | - |
| `audio_de_référence` | Clip audio de référence dont l'identité du locuteur doit être transférée. ~5 secondes recommandées (durée d'entraînement). Des clips plus courts ou plus longs peuvent dégrader le transfert d'identité vocale. | AUDIO | Oui | - |
| `audio_vae` | VAE audio LTXV pour encoder l'audio de référence. | VAE | Oui | - |
| `échelle_guidage_identité` | Force du guidage d'identité. Exécute une passe avant supplémentaire sans référence à chaque étape pour amplifier l'identité du locuteur. Mettre à 0 pour désactiver (pas de passe supplémentaire). (par défaut : 3.0) | FLOAT | Non | 0.0 - 100.0 |
| `pourcentage_début` | Début de la plage sigma où le guidage d'identité est actif. (par défaut : 0.0) | FLOAT | Non | 0.0 - 1.0 |
| `pourcentage_fin` | Fin de la plage sigma où le guidage d'identité est actif. (par défaut : 1.0) | FLOAT | Non | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le modèle patché avec la fonction de guidage d'identité. | MODEL |
| `négatif` | Le conditionnement positif, contenant désormais les données audio de référence encodées. | CONDITIONING |
| `négatif` | Le conditionnement négatif, contenant désormais les données audio de référence encodées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/fr.md)

---
**Source fingerprint (SHA-256):** `0b87fb135ba8e752f4114cb47152503b0ec548eefcaa03f99f1cbdda6664874c`
