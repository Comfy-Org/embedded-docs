Le nœud ConditioningStableAudio ajoute des informations de synchronisation aux entrées de conditionnement positif et négatif pour la génération audio. Il définit les paramètres de temps de début et de durée totale qui aident à contrôler quand et pendant combien de temps le contenu audio doit être généré. Ce nœud modifie les données de conditionnement existantes en y ajoutant des métadonnées de synchronisation spécifiques à l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positif à modifier avec les informations de synchronisation audio | CONDITIONING | Oui | - |
| `négative` | L'entrée de conditionnement négatif à modifier avec les informations de synchronisation audio | CONDITIONING | Oui | - |
| `secondes_début` | Le temps de début en secondes pour la génération audio (par défaut : 0,0) | FLOAT | Oui | 0,0 à 1000,0 |
| `secondes_total` | La durée totale en secondes pour la génération audio (par défaut : 47,0) | FLOAT | Oui | 0,0 à 1000,0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `négatif` | Le conditionnement positif modifié avec les informations de synchronisation audio appliquées | CONDITIONING |
| `négative` | Le conditionnement négatif modifié avec les informations de synchronisation audio appliquées | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/fr.md)

---
**Source fingerprint (SHA-256):** `ad4fdb2ac536e4f9cc23c044a7a63333e3f3530cc782937eaedc1565cc7c5d0e`
