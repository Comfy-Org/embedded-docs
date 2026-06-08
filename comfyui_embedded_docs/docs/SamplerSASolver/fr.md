Le nœud SamplerSASolver implémente un algorithme d'échantillonnage personnalisé pour les modèles de diffusion. Il utilise une approche prédicteur-correcteur avec des paramètres d'ordre configurables et des paramètres d'équation différentielle stochastique (SDE) pour générer des échantillons à partir du modèle d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle de diffusion à utiliser pour l'échantillonnage | MODEL | Oui | - |
| `eta` | Contrôle le facteur d'échelle de la taille du pas (par défaut : 1,0) | FLOAT | Non | 0,0 - 10,0 |
| `pourcent_début_sde` | Le pourcentage de départ pour l'échantillonnage SDE (par défaut : 0,2) | FLOAT | Non | 0,0 - 1,0 |
| `pourcent_fin_sde` | Le pourcentage de fin pour l'échantillonnage SDE (par défaut : 0,8) | FLOAT | Non | 0,0 - 1,0 |
| `s_bruit` | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (par défaut : 1,0) | FLOAT | Non | 0,0 - 100,0 |
| `ordre_prédicteur` | L'ordre du composant prédicteur dans le solveur (par défaut : 3) | INT | Non | 1 - 6 |
| `ordre_correcteur` | L'ordre du composant correcteur dans le solveur (par défaut : 4) | INT | Non | 0 - 6 |
| `utiliser_pece` | Active ou désactive la méthode PECE (Prédire-Évaluer-Corriger-Évaluer) | BOOLEAN | Non | - |
| `ordre_simple_2` | Active ou désactive les calculs simplifiés de second ordre | BOOLEAN | Non | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sampler` | Un objet échantillonneur configuré pouvant être utilisé avec les modèles de diffusion | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/fr.md)

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
