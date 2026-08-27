# Guidage de modalité LTXV (couplage A/V)

Ce nœud applique un guidage intermodal (audio-vidéo) à un modèle LTXV-AV. Pendant l’échantillonnage, il exécute une passe avant supplémentaire à chaque étape avec les connexions d’attention croisée audio-vers-vidéo et vidéo-vers-audio désactivées, puis rapproche le résultat de la prédiction couplée afin de renforcer la synchronisation audiovisuelle, comme la synchro labiale. La valeur par défaut de référence pour `modality_scale` est 3.0 ; la régler à 1.0 désactive la passe supplémentaire, et elle se cumule avec le guider dual-CFG et STG.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle de base auquel le guidage de modalité sera appliqué. Il est cloné en interne, laissant le modèle d’origine inchangé. | MODEL | Oui | - |
| `modality_scale` | Force du guidage de couplage audio-vidéo. La valeur par défaut est 3.0. Régler à 1.0 pour désactiver la passe avant supplémentaire. | FLOAT | Oui | 1.0 à 100.0 (défaut : 3.0) |
| `pourcentage_début` | Le point du processus d’échantillonnage, exprimé en pourcentage de 0.0 à 1.0, auquel le guidage de modalité commence. Ceci est un paramètre avancé. La valeur par défaut est 0.0. | FLOAT | Oui | 0.0 à 1.0 (défaut : 0.0) |
| `pourcentage_fin` | Le point du processus d’échantillonnage, exprimé en pourcentage de 0.0 à 1.0, auquel le guidage de modalité se termine. Ceci est un paramètre avancé. La valeur par défaut est 1.0. | FLOAT | Oui | 0.0 à 1.0 (défaut : 1.0) |

Le guidage n’est appliqué que pour les étapes d’échantillonnage dont les valeurs sigma se situent dans la plage définie par `start_percent` et `end_percent`. En dehors de cette plage, le nœud renvoie le résultat débruité inchangé. Une `modality_scale` de 1.0 désactive également entièrement la passe avant supplémentaire.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Le modèle cloné avec une fonction de guidage post-CFG attachée. Ce modèle modifié applique le guidage de modalité pendant l’échantillonnage. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
