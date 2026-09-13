# LatentApplyOperationCFG

Le nœud LatentApplyOperationCFG applique une opération latente lors de l’étape classifier-free guidance (CFG) du processus d’échantillonnage d’un modèle. Il intercepte les sorties de conditionnement produites avant la CFG, applique l’opération connectée aux valeurs latentes, et renvoie le modèle avec ce comportement d’échantillonnage modifié.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel l’opération CFG sera appliquée | MODEL | Oui | - |
| `operation` | L’opération latente à appliquer pendant le processus d’échantillonnage CFG | LATENT_OPERATION | Oui | - |

Remarque : ce nœud est marqué comme expérimental. L’opération est appliquée aux sorties de conditionnement du modèle pendant le processus d’échantillonnage CFG. Lorsque deux sorties de conditionnement sont présentes, l’opération est appliquée à la différence entre la première et la seconde sortie, puis la seconde sortie est de nouveau ajoutée au résultat. Lorsqu’une seule sortie de conditionnement est présente, l’opération y est appliquée directement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l’opération CFG appliquée à son processus d’échantillonnage | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/fr.md)

---
**Source fingerprint (SHA-256):** `e383684a785878bfa4004c2fac78ae562d8e035fdfe081f8e4ebbb2c50161987`
