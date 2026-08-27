# TopazImageEnhanceV2

Topaz Image Enhance applique une mise à l’échelle et une amélioration d’image standard de l’industrie à une seule image d’entrée à l’aide des modèles Topaz. Il envoie l’image à l’API Topaz, la traite avec le modèle sélectionné et renvoie le résultat amélioré. Vous pouvez choisir parmi trois modèles : Reimagine, Bloom 2 et Wonder 3.5.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L’image d’entrée à améliorer. Une seule image d’entrée est prise en charge. | IMAGE | Oui | Image unique |
| `modèle` | Le modèle d’amélioration Topaz à utiliser. Le modèle sélectionné détermine les paramètres spécifiques au modèle qui apparaissent. | STRING | Oui | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `largeur de sortie` | Une valeur nulle signifie que le calcul est automatique (généralement la taille d’origine ou une mise à l’échelle proportionnelle à `output_height` si spécifié). Wonder 3.5 ne prend en charge que des facteurs d’agrandissement de 1x à 6x. Bloom 2 et Wonder 3.5 préservent le rapport hauteur/largeur de l’entrée et traitent la taille demandée comme une cible. (défaut : 0) | INT | Non | 0 à 32000 |
| `hauteur de sortie` | Une valeur nulle signifie que la hauteur de sortie est identique à celle de l’originale ou mise à l’échelle proportionnellement à `output_width` si spécifié. Wonder 3.5 ne prend en charge que des facteurs d’agrandissement de 1x à 6x. Bloom 2 et Wonder 3.5 préservent le rapport hauteur/largeur de l’entrée et traitent la taille demandée comme une cible. (défaut : 0) | INT | Non | 0 à 32000 |

### Paramètres de Reimagine

Ces paramètres s’appliquent lorsque `model` est défini sur `"Reimagine"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel optionnel pour guider l’agrandissement créatif. (défaut : "") | STRING | Oui | Texte libre |
| `creativity` | Niveau de créativité pour l’amélioration. (défaut : 3) | INT | Oui | 1 à 9 |
| `subject_detection` | Mode de détection du sujet. | STRING | Oui | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Améliorer les visages (s’ils sont présents) pendant le traitement. (défaut : True) | BOOLEAN | Oui | true<br>false |
| `face_enhancement_creativity` | Définir le niveau de créativité pour l’amélioration des visages. (défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `face_enhancement_strength` | Contrôle la netteté des visages améliorés par rapport à l’arrière-plan. (défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `face_preservation` | Préserver l’identité faciale des sujets. (défaut : True) | BOOLEAN | Oui | true<br>false |
| `color_preservation` | Préserver les couleurs d’origine. (défaut : True) | BOOLEAN | Oui | true<br>false |
| `crop_to_fill` | Par défaut, l’image est letterboxée lorsque le rapport hauteur/largeur de sortie diffère. Activer pour recadrer l’image afin de remplir les dimensions de sortie. (défaut : False) | BOOLEAN | Oui | true<br>false |

### Paramètres de Bloom 2

Ces paramètres s’appliquent lorsque `model` est défini sur `"Bloom 2"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel optionnel pour la génération. Laissez vide pour générer automatiquement un prompt à partir de l’image d’entrée. (défaut : "") | STRING | Oui | Texte libre |
| `creativity` | 1 correspond à une amélioration modérée, 9 à une réinterprétation prononcée avec des détails nouvellement générés. (défaut : 3) | INT | Oui | 1 à 9 |
| `seed` | Graine pour une génération reproductible. (défaut : 2) | INT | Oui | 1 à 2000 |
| `color_preservation` | Préserver les couleurs d’origine. (défaut : True) | BOOLEAN | Oui | true<br>false |
| `grain` | Ajouter du grain à l’image de sortie. (défaut : False) | BOOLEAN | Oui | true<br>false |
| `grain_model` | Modèle de grain à utiliser. Est ignoré si le grain est désactivé. | STRING | Oui | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Force de l’effet de grain. Est ignoré si le grain est désactivé. (défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |
| `grain_size` | Taille des particules de grain. Est ignoré si le grain est désactivé. (défaut : 1.0) | FLOAT | Oui | 1.0 à 5.0 |
| `grain_density` | Intensité de l’effet de grain. Est ignoré si le grain est désactivé. (défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |

### Paramètres de Wonder 3.5

Ces paramètres s’appliquent lorsque `model` est défini sur `"Wonder 3.5"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `enhancement_strength` | Niveau d’amélioration pour différentes conditions d’entrée. (défaut : "high") | STRING | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Ajouter du grain à l’image de sortie. (défaut : False) | BOOLEAN | Oui | true<br>false |
| `grain_model` | Modèle de grain à utiliser. Est ignoré si le grain est désactivé. | STRING | Oui | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Force de l’effet de grain. Est ignoré si le grain est désactivé. (défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |
| `grain_size` | Taille des particules de grain. Est ignoré si le grain est désactivé. (défaut : 1.0) | FLOAT | Oui | 1.0 à 5.0 |
| `grain_density` | Intensité de l’effet de grain. Est ignoré si le grain est désactivé. (défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image améliorée et agrandie renvoyée par l’API Topaz. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/fr.md)

---
**Source fingerprint (SHA-256):** `4301abb7cbab5122490b2ed3b328b199a29409da0dcc5ea5201570c2acbc2a58`
