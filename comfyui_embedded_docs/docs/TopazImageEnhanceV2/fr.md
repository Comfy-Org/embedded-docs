# Topaz Amélioration d’Image

Topaz Image Enhance applique une mise à l'échelle et une amélioration d'image conformes aux standards du secteur à une seule image d'entrée en utilisant les modèles Topaz. Il envoie l'image à l'API Topaz, la traite avec le modèle sélectionné et renvoie le résultat amélioré. Vous pouvez choisir parmi trois modèles : Reimagine, Bloom 2 et Wonder 3.5.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `image` | L'image d'entrée à améliorer. Une seule image d'entrée est prise en charge. | IMAGE | Oui | Image unique |
| `model` | Le modèle d'amélioration Topaz à utiliser. Le modèle sélectionné détermine quels paramètres spécifiques au modèle apparaissent. | DYNAMIC_COMBO | Oui | `"Reimagine"`<br>`"Bloom 2"`<br>`"Wonder 3.5"` |
| `output_width` | Une valeur nulle signifie un calcul automatique (généralement la taille d'origine ou une mise à l'échelle proportionnelle à `output_height` si spécifié). Wonder 3.5 ne prend en charge que les facteurs d'agrandissement de 1x à 6x. Bloom 2 et Wonder 3.5 préservent le rapport d'aspect de l'entrée et traitent la taille demandée comme une cible. (par défaut : 0) | INT | Non | 0 à 32000 |
| `output_height` | Une valeur nulle signifie une sortie à la même hauteur que l'original ou une mise à l'échelle proportionnelle à `output_width` si spécifié. Wonder 3.5 ne prend en charge que les facteurs d'agrandissement de 1x à 6x. Bloom 2 et Wonder 3.5 préservent le rapport d'aspect de l'entrée et traitent la taille demandée comme une cible. (par défaut : 0) | INT | Non | 0 à 32000 |

### Entrées Reimagine

Ces paramètres s'appliquent lorsque `model` est défini sur `"Reimagine"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite textuelle facultative pour guider l'agrandissement créatif. (par défaut : "") | STRING | Oui | Tout texte |
| `creativity` | Niveau de créativité pour l'amélioration. (par défaut : 3) | INT | Oui | 1 à 9 |
| `subject_detection` | Mode de détection du sujet (avancé). | COMBO | Oui | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Améliorer les visages (s'ils sont présents) pendant le traitement. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `face_enhancement_creativity` | Définit le niveau de créativité pour l'amélioration des visages. (par défaut : 0.0) | FLOAT | Oui | 0.0 à 1.0 |
| `face_enhancement_strength` | Contrôle la netteté des visages améliorés par rapport à l'arrière-plan. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 |
| `face_preservation` | Préserver l'identité faciale des sujets. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `color_preservation` | Préserver les couleurs d'origine. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `crop_to_fill` | Par défaut, l'image est mise en boîte aux lettres lorsque le rapport d'aspect de sortie diffère. Activez cette option pour rogner l'image afin de remplir les dimensions de sortie. (par défaut : False) | BOOLEAN | Oui | true<br>false |

### Entrées Bloom 2

Ces paramètres s'appliquent lorsque `model` est défini sur `"Bloom 2"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Invite textuelle facultative pour la génération. Laissez vide pour générer automatiquement une invite à partir de l'image d'entrée. (par défaut : "") | STRING | Oui | Tout texte |
| `creativity` | 1 correspond à une amélioration retenue, 9 à une réinterprétation marquée avec des détails nouvellement générés. (par défaut : 3) | INT | Oui | 1 à 9 |
| `seed` | Graine pour une génération reproductible. (par défaut : 2) | INT | Oui | 1 à 2000 |
| `color_preservation` | Préserver les couleurs d'origine. (par défaut : True) | BOOLEAN | Oui | true<br>false |
| `grain` | Ajouter du grain à l'image de sortie. (par défaut : False) | BOOLEAN | Oui | true<br>false |
| `grain_model` | Modèle de grain à utiliser. Ignoré si le grain est désactivé. | COMBO | Oui | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Intensité de l'effet de grain. Ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |
| `grain_size` | Taille des particules de grain. Ignoré si le grain est désactivé. (par défaut : 1.0) | FLOAT | Oui | 1.0 à 5.0 |
| `grain_density` | Densité de l'effet de grain. Ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |

### Entrées Wonder 3.5

Ces paramètres s'appliquent lorsque `model` est défini sur `"Wonder 3.5"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `enhancement_strength` | Niveau d'amélioration pour diverses conditions d'entrée. (par défaut : "high") | COMBO | Oui | `"low"`<br>`"medium"`<br>`"high"` |
| `grain` | Ajouter du grain à l'image de sortie. (par défaut : False) | BOOLEAN | Oui | true<br>false |
| `grain_model` | Modèle de grain à utiliser. Ignoré si le grain est désactivé. | COMBO | Oui | `"silver"`<br>`"gaussian"`<br>`"grey"` |
| `grain_strength` | Intensité de l'effet de grain. Ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |
| `grain_size` | Taille des particules de grain. Ignoré si le grain est désactivé. (par défaut : 1.0) | FLOAT | Oui | 1.0 à 5.0 |
| `grain_density` | Densité de l'effet de grain. Ignoré si le grain est désactivé. (par défaut : 0.5) | FLOAT | Oui | 0.0 à 1.0 |

**Remarque :** Une seule image d'entrée est prise en charge ; le nœud génère une erreur si le lot d'entrée contient plus d'une image. Les paramètres de grain (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) sont ignorés sauf si `grain` est activé. Pour Bloom 2, laisser `prompt` vide génère automatiquement une invite à partir de l'image d'entrée. Wonder 3.5 ne prend en charge que les facteurs d'agrandissement de 1x à 6x ; Bloom 2 et Wonder 3.5 préservent le rapport d'aspect de l'entrée et traitent la taille demandée comme une cible.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `IMAGE` | L'image améliorée et agrandie renvoyée par l'API Topaz. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/fr.md)

---
**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`
