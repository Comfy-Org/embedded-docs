# SamplerEulerAncestralCFG++

Le nœud SamplerEulerAncestralCFG++ crée un échantillonneur qui utilise la méthode Euler Ancestral avec guidage sans classificateur (CFG++) pour la génération d'images. Cet échantillonneur combine les techniques d'échantillonnage ancestral avec le conditionnement de guidage afin de produire des variations d'image diverses tout en maintenant la cohérence, et permet un réglage fin via des paramètres qui contrôlent le bruit et les ajustements de taille de pas.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la taille du pas pendant l'échantillonnage ; des valeurs plus élevées entraînent des mises à jour plus agressives (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `s_bruit` | Ajuste la quantité de bruit ajoutée pendant le processus d'échantillonnage (valeur par défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré pouvant être utilisé dans le pipeline de génération d'images | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/fr.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
