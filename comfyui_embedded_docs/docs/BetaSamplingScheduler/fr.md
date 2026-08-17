# PlanificateurÉchantillonnageBeta

Le nœud BetaSamplingScheduler crée une séquence de niveaux de bruit (sigmas) qui contrôlent la façon dont le bruit est supprimé pendant le processus d'échantillonnage dans la génération d'images. Il utilise un algorithme de planification bêta, et les paramètres `alpha` et `beta` ajustent la forme du programme de bruit. Les sigmas générés sont transmis à un échantillonneur pour guider le processus de débruitage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle utilisé pour l'échantillonnage, qui fournit l'objet d'échantillonnage du modèle. | MODEL | Oui | - |
| `steps` | Le nombre d'étapes d'échantillonnage pour lesquelles générer les sigmas (par défaut : 20). | INT | Oui | 1 à 10000 |
| `alpha` | Paramètre alpha du planificateur bêta, contrôlant la courbe de planification (par défaut : 0.6). Paramètre avancé. | FLOAT | Oui | 0.0 à 50.0 |
| `beta` | Paramètre bêta du planificateur bêta, contrôlant la courbe de planification (par défaut : 0.6). Paramètre avancé. | FLOAT | Oui | 0.0 à 50.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `SIGMAS` | Une séquence de niveaux de bruit (sigmas) utilisée pour le processus d'échantillonnage. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `80adae3cbedff7fe544a1fbcf638af7965f1216e422931063ecf67da53ddff95`
