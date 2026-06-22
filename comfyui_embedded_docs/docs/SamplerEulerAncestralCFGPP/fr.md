# SamplerEulerAncestralCFG++

Le nœud `SamplerEulerAncestralCFGPP` crée un échantillonneur utilisant la méthode Euler Ancestrale avec guidage sans classifieur (CFG++) pour la génération d'images. Cet échantillonneur combine des techniques d'échantillonnage ancestrales avec un conditionnement par guidage afin de produire des variations d'images diversifiées tout en maintenant la cohérence, et permet un réglage fin via des paramètres contrôlant le bruit et les ajustements de pas.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la taille du pas lors de l'échantillonnage, des valeurs plus élevées entraînant des mises à jour plus agressives (par défaut : 1.0) | FLOAT | Oui | 0.0 - 1.0 |
| `s_bruit` | Ajuste la quantité de bruit ajoutée pendant le processus d'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 10.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré pouvant être utilisé dans le pipeline de génération d'images | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/fr.md)

---
**Source fingerprint (SHA-256):** `7eceec539a6a045db4d9953214add17011ef9d17e663dbbbbbb2bae0cbe40aa2`
