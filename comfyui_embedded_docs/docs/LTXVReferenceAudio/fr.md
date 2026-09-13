# LTXV Reference Audio (ID-LoRA)

LTXV Reference Audio transfère l'identité vocale d'un locuteur depuis un clip audio de référence vers l'audio généré. Il encode l'audio de référence dans le conditionnement et applique éventuellement un patch au modèle avec le guidage d'identité, ce qui exécute une passe avant supplémentaire sans la référence à chaque étape afin d'amplifier l'effet d'identité du locuteur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer le patch avec le guidage d'identité. | MODEL | Oui | - |
| `positif` | L'entrée de conditionnement positive. | CONDITIONING | Oui | - |
| `négatif` | L'entrée de conditionnement négative. | CONDITIONING | Oui | - |
| `audio_de_référence` | Clip audio de référence dont l'identité du locuteur doit être transférée. ~5 secondes recommandées (durée d'entraînement). Des clips plus courts ou plus longs peuvent dégrader le transfert de l'identité vocale. | AUDIO | Oui | - |
| `audio_vae` | VAE audio LTXV pour l'encodage. | VAE | Oui | - |
| `échelle_guidage_identité` | Force du guidage d'identité. Exécute une passe avant supplémentaire sans la référence à chaque étape pour amplifier l'identité du locuteur. Réglez sur 0 pour désactiver (aucune passe supplémentaire). (par défaut : 3.0) | FLOAT | Oui | 0.0 - 100.0 |
| `pourcentage_début` | Début de la plage sigma où le guidage d'identité est actif. (par défaut : 0.0) | FLOAT | Oui | 0.0 - 1.0 |
| `pourcentage_fin` | Fin de la plage sigma où le guidage d'identité est actif. (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |

Remarque : Le guidage d'identité n'est appliqué que lorsque `identity_guidance_scale` est supérieur à 0 et que l'étape d'échantillonnage actuelle se situe dans la plage définie par `start_percent` et `end_percent`. L'audio de référence est rééchantillonné au taux d'échantillonnage du VAE audio si les deux diffèrent.

Remarque : `start_percent` et `end_percent` sont des paramètres avancés, affichés uniquement lorsque les options avancées sont activées dans l'interface.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle patché avec la fonction de guidage d'identité. | MODEL |
| `positive` | Le conditionnement positif, contenant désormais les données audio de référence encodées. | CONDITIONING |
| `negative` | Le conditionnement négatif, contenant désormais les données audio de référence encodées. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
