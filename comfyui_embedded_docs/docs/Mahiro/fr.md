# Mahiro est si mignonne qu'elle mérite une meilleure fonction de guidage!! (。・ω・。)

Le nœud Mahiro modifie la fonction de guidage pour se concentrer davantage sur la direction de la consigne positive plutôt que sur la différence entre les consignes positive et négative. Il crée un modèle patché qui applique une approche de mise à l'échelle du guidage personnalisée, utilisant la similarité cosinus entre les sorties débruitées conditionnelles et inconditionnelles normalisées. Ce nœud expérimental aide à orienter la génération plus fortement vers la direction souhaitée de la consigne positive.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à patcher avec la fonction de guidage modifiée | MODEL | Oui |  |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `modèle_modifié` | Le modèle modifié avec la fonction de guidage Mahiro appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/fr.md)

---
**Source fingerprint (SHA-256):** `8b4a73cfa488f97d87e5a18d5ab30765055b5d5a66c6c2f1a5f016eed2af0300`
