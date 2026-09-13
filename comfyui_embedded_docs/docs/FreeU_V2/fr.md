# FreeU_V2

FreeU_V2 améliore la qualité de génération d’images en appliquant des modifications basées sur les fréquences à l’architecture U-Net d’un modèle de diffusion. Il utilise des facteurs d’échelle configurables pour ajuster les canaux de caractéristiques dans différents blocs, améliorant ainsi la sortie sans nécessiter d’entraînement supplémentaire. Le nœud fonctionne en patchant les blocs de sortie du modèle et en filtrant les composantes haute fréquence des états cachés.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle de diffusion auquel appliquer l’amélioration FreeU | MODEL | Oui | - |
| `b1` | Facteur d’échelle des caractéristiques du backbone pour le premier bloc (par défaut : 1.3) | FLOAT | Oui | 0.0 - 10.0 |
| `b2` | Facteur d’échelle des caractéristiques du backbone pour le second bloc (par défaut : 1.4) | FLOAT | Oui | 0.0 - 10.0 |
| `s1` | Facteur d’échelle des caractéristiques de connexion skip pour le premier bloc (par défaut : 0.9) | FLOAT | Oui | 0.0 - 10.0 |
| `s2` | Facteur d’échelle des caractéristiques de connexion skip pour le second bloc (par défaut : 0.2) | FLOAT | Oui | 0.0 - 10.0 |

Remarque : `b1`, `b2`, `s1` et `s2` sont des paramètres avancés masqués par défaut dans l’interface du nœud. Ils peuvent être définis par pas de 0.01 dans la plage 0.0 - 10.0. `b1` et `s1` contrôlent le bloc U-Net comportant le plus de canaux (quatre fois le nombre de canaux de base du modèle), tandis que `b2` et `s2` contrôlent le bloc comportant deux fois moins de canaux (deux fois le nombre de canaux de base).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle de diffusion amélioré avec les modifications FreeU appliquées | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/fr.md)

---
**Source fingerprint (SHA-256):** `4cef2af9b04164a8ead25bea9c9bb3311be9224f2539a5cc6edbe97ad8465d65`
