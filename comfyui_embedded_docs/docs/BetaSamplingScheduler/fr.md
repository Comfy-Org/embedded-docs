> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/fr.md)

Le nœud BetaSamplingScheduler génère une séquence de niveaux de bruit (sigmas) pour le processus d'échantillonnage à l'aide d'un algorithme de planification bêta. Il prend un modèle et des paramètres de configuration pour créer un plan de bruit personnalisé qui contrôle le processus de débruitage lors de la génération d'images. Ce planificateur permet un réglage fin de la trajectoire de réduction du bruit grâce aux paramètres alpha et bêta.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle utilisé pour l'échantillonnage, qui fournit l'objet d'échantillonnage du modèle |
| `étapes` | INT | Oui | 1 à 10000 | Le nombre d'étapes d'échantillonnage pour générer les sigmas (par défaut : 20) |
| `alpha` | FLOAT | Oui | 0.0 à 50.0 | Paramètre alpha pour le planificateur bêta, contrôlant la courbe de planification (par défaut : 0.6) |
| `beta` | FLOAT | Oui | 0.0 à 50.0 | Paramètre bêta pour le planificateur bêta, contrôlant la courbe de planification (par défaut : 0.6) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `SIGMAS` | SIGMAS | Une séquence de niveaux de bruit (sigmas) utilisée pour le processus d'échantillonnage |

---
**Source fingerprint (SHA-256):** `8b3d17ef737107da3d5cacc84278de8a93f6889e6567619012729b205bbc421e`
