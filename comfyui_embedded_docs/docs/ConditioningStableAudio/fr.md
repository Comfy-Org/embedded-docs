# ConditionnementStableAudio

Le nœud ConditioningStableAudio ajoute des informations de temporisation aux entrées de conditionnement positives et négatives pour la génération audio. Il définit les paramètres de temps de début et de durée totale qui aident à contrôler quand et combien de temps le contenu audio doit être généré. Ce nœud modifie les données de conditionnement existantes en ajoutant des métadonnées de temporisation spécifiques à l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positive à modifier avec les informations de temporisation audio | CONDITIONING | Oui | - |
| `négative` | L'entrée de conditionnement négative à modifier avec les informations de temporisation audio | CONDITIONING | Oui | - |
| `secondes_début` | Le temps de début en secondes pour la génération audio (défaut : 0.0) | FLOAT | Oui | 0.0 à 1000.0 |
| `secondes_total` | La durée totale en secondes pour la génération audio (défaut : 47.0) | FLOAT | Oui | 0.0 à 1000.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positif` | Le conditionnement positif modifié avec les informations de temporisation audio appliquées | CONDITIONING |
| `négatif` | Le conditionnement négatif modifié avec les informations de temporisation audio appliquées | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/fr.md)

---
**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`
