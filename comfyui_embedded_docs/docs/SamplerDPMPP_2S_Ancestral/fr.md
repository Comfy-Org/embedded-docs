# SamplerDPMPP_2S_Ancestral

Le nœud SamplerDPMPP_2S_Ancestral crée un échantillonneur qui utilise la méthode d'échantillonnage ancêtre DPM++ 2S pour générer des images. Cet échantillonneur combine des éléments déterministes et stochastiques pour produire des résultats variés tout en maintenant une certaine cohérence. Il vous permet de contrôler le caractère aléatoire et les niveaux de bruit pendant le processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `eta` | Contrôle la quantité de bruit stochastique ajouté pendant l'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |
| `s_bruit` | Contrôle l'échelle du bruit appliqué pendant le processus d'échantillonnage (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Renvoie un objet échantillonneur configuré qui peut être utilisé dans le pipeline d'échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/fr.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`
