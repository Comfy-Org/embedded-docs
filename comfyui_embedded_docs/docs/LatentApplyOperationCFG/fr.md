# LatentApplyOperationCFG

Le nœud LatentApplyOperationCFG applique une opération latente lors de l’étape classifier-free guidance (CFG) du processus d’échantillonnage d’un modèle. Il intercepte les sorties de conditionnement produites avant la CFG, applique l’opération connectée aux valeurs latentes, et renvoie le modèle avec ce comportement d’échantillonnage modifié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel l’opération CFG sera appliquée | MODEL | Oui | - |
| `operation` | L’opération latente à appliquer pendant le processus d’échantillonnage CFG | LATENT_OPERATION | Oui | - |
| `start_percent` | Fraction de la planification de débruitage à laquelle l'opération commence à être appliquée ; 0 correspond au début de la planification (par défaut : 0.0) | FLOAT | Non | 0.0 à 1.0 (pas 0.001) |
| `end_percent` | Fraction de la planification de débruitage à laquelle l'opération cesse d'être appliquée ; 1 correspond à la fin de la planification (par défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 (pas 0.001) |

Remarque : ce nœud est marqué comme expérimental. L’opération est appliquée aux sorties de conditionnement du modèle pendant le processus d’échantillonnage CFG. Lorsque deux sorties de conditionnement sont présentes, l’opération est appliquée à la différence entre la première et la seconde sortie, puis la seconde sortie est de nouveau ajoutée au résultat. Lorsqu’une seule sortie de conditionnement est présente, l’opération y est appliquée directement. L'opération ne s'exécute qu'entre les points `start_percent` et `end_percent` de la planification de débruitage, elle peut donc être limitée à une partie de la planification ; en dehors de cette fenêtre, les sorties de conditionnement sont renvoyées sans modification.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l’opération CFG appliquée à son processus d’échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/fr.md)

---
**Source fingerprint (SHA-256):** `6a5f59f02eaec38334c63d871e48e89aa983a5ac2ca10801161cdc9e13cacdf2`
