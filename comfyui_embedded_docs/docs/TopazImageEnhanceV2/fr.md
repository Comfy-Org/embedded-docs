# Topaz Amélioration d’Image

Topaz Image Enhance applique une mise à l'échelle et une amélioration d'image aux standards de l'industrie à une seule image d'entrée à l'aide des modèles Topaz. Il envoie l'image à l'API Topaz, la traite avec le modèle sélectionné et renvoie le résultat amélioré. Vous pouvez choisir parmi trois modèles : Reimagine, Bloom 2 et Wonder 3.5.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à améliorer. Une seule image d'entrée est prise en charge. | IMAGE | Oui | Image unique |
| `modèle` | Le modèle d'amélioration Topaz à utiliser. Le modèle sélectionné détermine les paramètres spécifiques au modèle qui apparaissent. | DYNAMIC_COMBO | Oui | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `largeur de sortie` | Une valeur nulle signifie un calcul automatique (généralement la taille d'origine ou une mise à l'échelle proportionnelle à `output_height` si spécifiée). Wonder 3.5 ne prend en charge que des facteurs d'agrandissement de 1x à 6x. Bloom 2 et Wonder 3.5 préservent le rapport hauteur/largeur de l'image d'entrée et traitent la taille demandée comme une cible. (par défaut : 0) | INT | Non | 0 à 32000 |
| `hauteur de sortie` | Une valeur nulle signifie que la hauteur de sortie est la même que celle d'origine ou mise à l'échelle proportionnellement à `output_width` si spécifiée. Wonder 3.5 ne prend en charge que des facteurs d'agrandissement de 1x à 6x. Bloom 2 et Wonder 3.5 préservent le rapport hauteur/largeur de l'image d'entrée et traitent la taille demandée comme une cible. (par défaut : 0) | INT | Non | 0 à 32000 |

### Entrées Reimagine

Ces paramètres s'appliquent lorsque `model` est défini sur `"Reimagine"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite de texte facultative pour guider l'amélioration créative. (par défaut : "") | STRING | Oui | Texte libre |
| `creativity` | Niveau de créativité pour l'amélioration. (par défaut : 3) | INT | Oui | 1 à 9 |
| `subject_detection` | Mode de détection du sujet. | COMBO | Oui | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Améliorer les visages (s'ils sont présents) pendant le traitement. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `face_enhancement_creativity` | Définit le niveau de créativité pour l'amélioration des visages. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `face_enhancement_strength` | Contrôle la netteté des visages améliorés par rapport à l'arrière-plan. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `face_preservation` | Préserver l'identité faciale des sujets. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `color_preservation` | Préserver les couleurs d'origine. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `crop_to_fill` | Par défaut, l'image est letterboxée lorsque le rapport hauteur/largeur de sortie diffère. Activer pour recadrer l'image afin de remplir les dimensions de sortie. (par défaut : False) | BOOLEAN | Oui | true<br>false |

### Entrées Bloom 2

Ces paramètres s'appliquent lorsque `model` est défini sur `"Bloom 2"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite de texte facultative pour la génération. Laissez vide pour générer automatiquement une invite à partir de l'image d'entrée. (par défaut : "") | STRING | Oui | Texte libre |
| `creativity` | 1 est une amélioration modérée, 9 est une réinterprétation prononcée avec des détails nouvellement générés. (par défaut : 3) | INT | Oui | 1 à 9 |
| `seed` | Graine pour une génération reproductible. (par défaut : 2) | INT | Oui | 1 à 2000 |
| `color_preservation` | Préserver les couleurs d'origine. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `grain` | Ajouter du grain à l'image de sortie. (par défaut : False) | BOOLEAN | Oui | true<br>false |
| `grain_model` | Modèle de grain à utiliser. Est ignoré si le grain est désactivé. | COMBO | Oui | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Force de l'effet de grain. Est ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |
| `grain_size` | Taille des particules de grain. Est ignoré si le grain est désactivé. (par défaut : 1.0) | FLOAT | Oui | 1.0 à 5.0 |
| `grain_density` | Intensité de l'effet de grain. Est ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |

### Entrées Wonder 3.5

Ces paramètres s'appliquent lorsque `model` est défini sur `"Wonder 3.5"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `enhancement_strength` | Niveau d'amélioration pour différentes conditions d'entrée. (par défaut : "high") | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Ajouter du grain à l'image de sortie. (par défaut : False) | BOOLEAN | Oui | true<br>false |
| `grain_model` | Modèle de grain à utiliser. Est ignoré si le grain est désactivé. | COMBO | Oui | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Force de l'effet de grain. Est ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |
| `grain_size` | Taille des particules de grain. Est ignoré si le grain est désactivé. (par défaut : 1.0) | FLOAT | Oui | 1.0 à 5.0 |
| `grain_density` | Intensité de l'effet de grain. Est ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Une seule image d'entrée est prise en charge. Les paramètres de grain (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) sont ignorés sauf si `grain` est activé. Pour Bloom 2, laisser `prompt` vide génère automatiquement une invite à partir de l'image d'entrée. Wonder 3.5 ne prend en charge que des facteurs d'agrandissement de 1x à 6x ; Bloom 2 et Wonder 3.5 préservent le rapport hauteur/largeur de l'image d'entrée et traitent la taille demandée comme une cible.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image améliorée et agrandie renvoyée par l'API Topaz. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/fr.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
