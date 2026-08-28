# SamplerEulerAncestralCFG++

Le nœud SamplerEulerAncestralCFGPP crée un échantillonneur qui utilise la méthode Euler Ancestral avec guidage sans classificateur (CFG++) pour la génération d'images. Cet échantillonneur combine des techniques d'échantillonnage ancestral avec un conditionnement par guidage pour produire des variations d'images diverses tout en maintenant la cohérence, et permet un réglage fin via des paramètres qui contrôlent le bruit et les ajustements de la taille du pas.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la taille du pas pendant l'échantillonnage, des valeurs plus élevées entraînant des mises à jour plus agressives (défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `s_bruit` | Ajuste la quantité de bruit ajoutée pendant le processus d'échantillonnage (défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré qui peut être utilisé dans le pipeline de génération d'images | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/fr.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
