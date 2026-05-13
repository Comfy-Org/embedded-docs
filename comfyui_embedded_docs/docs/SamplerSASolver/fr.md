> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/fr.md)

Le nœud SamplerSASolver implémente un algorithme d'échantillonnage personnalisé pour les modèles de diffusion. Il utilise une approche prédicteur-correcteur avec des paramètres d'ordre configurables et des paramètres d'équation différentielle stochastique (SDE) pour générer des échantillons à partir du modèle d'entrée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle de diffusion à utiliser pour l'échantillonnage |
| `eta` | FLOAT | Non | 0,0 - 10,0 | Contrôle le facteur d'échelle de la taille du pas (par défaut : 1,0) |
| `sde_start_percent` | FLOAT | Non | 0,0 - 1,0 | Le pourcentage de départ pour l'échantillonnage SDE (par défaut : 0,2) |
| `sde_end_percent` | FLOAT | Non | 0,0 - 1,0 | Le pourcentage de fin pour l'échantillonnage SDE (par défaut : 0,8) |
| `s_noise` | FLOAT | Non | 0,0 - 100,0 | Contrôle la quantité de bruit ajoutée lors de l'échantillonnage (par défaut : 1,0) |
| `predictor_order` | INT | Non | 1 - 6 | L'ordre du composant prédicteur dans le solveur (par défaut : 3) |
| `corrector_order` | INT | Non | 0 - 6 | L'ordre du composant correcteur dans le solveur (par défaut : 4) |
| `use_pece` | BOOLEAN | Non | - | Active ou désactive la méthode PECE (Prédire-Évaluer-Corriger-Évaluer) |
| `simple_order_2` | BOOLEAN | Non | - | Active ou désactive les calculs simplifiés de second ordre |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `sampler` | SAMPLER | Un objet échantillonneur configuré pouvant être utilisé avec les modèles de diffusion |

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
