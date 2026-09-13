# ÉchantillonneurSASolveur

Le nœud SamplerSASolver crée et configure un sampler personnalisé pour les modèles de diffusion. Il utilise l’algorithme d’échantillonnage `sa_solver` avec un schéma prédicteur-correcteur configurable et des paramètres d’équation différentielle stochastique (SDE), et renvoie un objet sampler pouvant être branché dans un nœud d’échantillonnage. Les valeurs `sde_start_percent` et `sde_end_percent` sont converties en valeurs sigma à l’aide du calendrier d’échantillonnage du modèle connecté afin de définir l’intervalle dans lequel la composante stochastique est appliquée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion dont le calendrier d’échantillonnage est utilisé pour construire le sampler | MODEL | Oui | - |
| `eta` | Contrôle le facteur d’échelle de la taille de pas du solveur SDE (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |
| `pourcent_début_sde` | Pourcentage de début du processus d’échantillonnage où commence la composante stochastique (SDE) ; converti en valeur sigma à l’aide du calendrier du modèle (par défaut : 0.2) | FLOAT | Non | 0.0 - 1.0 |
| `pourcent_fin_sde` | Pourcentage de fin du processus d’échantillonnage où s’arrête la composante stochastique (SDE) ; converti en valeur sigma à l’aide du calendrier du modèle (par défaut : 0.8) | FLOAT | Non | 0.0 - 1.0 |
| `s_bruit` | Contrôle la quantité de bruit ajoutée pendant l’échantillonnage (par défaut : 1.0) | FLOAT | Non | 0.0 - 100.0 |
| `ordre_prédicteur` | Ordre de la composante prédicteur dans le solveur (par défaut : 3) | INT | Non | 1 - 6 |
| `ordre_correcteur` | Ordre de la composante correcteur dans le solveur (par défaut : 4) | INT | Non | 0 - 6 |
| `utiliser_pece` | Active la méthode PECE (Predict-Evaluate-Correct-Evaluate) (par défaut : désactivé) | BOOLEAN | Non | - |
| `ordre_simple_2` | Active les calculs simplifiés du second ordre (par défaut : désactivé) | BOOLEAN | Non | - |

Toutes les entrées optionnelles sont marquées comme avancées dans l’interface.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet sampler configuré (utilisant l’algorithme `sa_solver`) pouvant être utilisé par les nœuds d’échantillonnage | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/fr.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
