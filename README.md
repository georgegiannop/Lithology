# Dataset Preprocessing

The preprocessing of the dataset was executed using a combination of SNAP, QGIS and ENVI tools. 

## Preprocessing steps:
- Defining areas
- Zero cloud and snow coverage
- No water bodies
- Minimum vegetation

### Aster:
- Subset on defined areas
- Mosaic images when needed
- Digitising clouds

### Labels:
- Soil map from YPEN
- Subset on defined areas
- All categories are represented with good analogies
- Clip label files with digitised clouds
- Rasterize

Labels have the following coding:

 Category | Label
:---: | :---:
Alluvial deposits | 0
Limestone colluvial deposits | 1
Limestones | 2
Schists | 3
Quaternary sediments |4
Gneiss | 5
Slope fan debris | 6
Mixed flysch | 7
Flysch shale and cherts | 8
Dolomites | 9
Granite |10
Sandstone flysch | 11
Flysch colluvial deposits | 12
Peridotite and Gabbro | 13
River bed deposits | 14
Gneiss colluvial deposits |15
Not available |-100
cloud coverage |-999

The following table lists the available areas and the categories that each contain.
|                | Alluvial deposits | Limestone colluvial deposits | Limestones | Schists | Quaternary sediments | Gneiss | Slope fan debris | Mixed flysch | Flysch shale and cherts | Dolomites | Granite | Sandstone flysch | Flysch colluvial deposits | Peridotite and Gabbro | River bed deposits | Gneiss colluvial deposits |
|----------------|-------------------|------------------------------|------------|---------|----------------------|--------|------------------|--------------|-------------------------|-----------|---------|------------------|---------------------------|-----------------------|--------------------|---------------------------|
| Agios_Georgios | ●                 | ●                            | ●          | ●       | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Amfilochia     |                   | ●                            | ●          | ●       |                      |        |                  |              |                         | ●         |         |                  |                           |                       |                    |                           |
| Anafi          |                   |                              |            | ●       | ●                    |        | ●                |              |                         |           | ●       |                  |                           |                       |                    |                           |
| Crete_A        | ●                 |                              | ●          | ●       | ●                    |        |                  | ●            |                         |           |         |                  |                           |                       |                    |                           |
| Crete_B        |                   |                              | ●          | ●       | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Desfina        | ●                 |                              | ●          |         |                      |        |                  |              |                         |           |         | ●                |                           |                       |                    |                           |
| Desfina_B      | ●                 |                              | ●          |         |                      |        |                  |              |                         |           |         |                  | ●                         |                       |                    |                           |
| Ermoupoli      |                   |                              | ●          | ●       |                      |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Exarchos       | ●                 | ●                            | ●          |         | ●                    |        |                  |              |                         |           |         |                  |                           | ●                     |                    |                           |
| Grevena        | ●                 |                              |            |         | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Kastro         | ●                 |                              | ●          |         | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Kirko_Bunaras  |                   |                              |            |         | ●                    | ●      |                  |              |                         |           | ●       |                  |                           |                       |                    |                           |
| Kithnos_A      | ●                 |                              | ●          | ●       |                      |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Kithnos_B      | ●                 |                              |            | ●       |                      |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Kyprios        | ●                 |                              |            | ●       | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Lighurio       | ●                 | ●                            | ●          |         | ●                    |        |                  |              |                         |           |         |                  |                           | ●                     |                    |                           |
| Limenaria      | ●                 | ●                            | ●          |         | ●                    | ●      |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Megara         |                   | ●                            | ●          | ●       |                      |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Mesorrahi      |                   | ●                            | ●          | ●       | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Metsitia_Arta  | ●                 | ●                            | ●          |         |                      |        | ●                | ●            | ●                       |           |         |                  |                           |                       |                    |                           |
| Monopigado     |                   |                              | ●          | ●       | ●                    |        |                  |              |                         |           | ●       |                  |                           |                       |                    |                           |
| Neraidoxori    | ●                 |                              | ●          | ●       |                      |        |                  | ●            | ●                       |           |         |                  |                           |                       | ●                  |                           |
| Petroto        | ●                 | ●                            | ●          | ●       |                      | ●      |                  |              |                         |           | ●       |                  |                           |                       |                    | ●                         |
| Skandalo       | ●                 |                              | ●          | ●       |                      |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Tirnavos       | ●                 | ●                            | ●          |         |                      |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Velia          |                   | ●                            | ●          |         | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Voras          |                   |                              | ●          |         |                      | ●      |                  |              |                         |           |         |                  |                           |                       |                    |                           |
| Xios           | ●                 | ●                            | ●          | ●       | ●                    |        |                  |              |                         |           |         |                  |                           |                       |                    |                           |


## Sentinel 2 Images:
- Resampling 10m
- Subset on defined areas

Here is an example of the data and their origin from different areas in Greece:

![Data Example](/images/EGU_S2.png "Here we can see the data and their origin from different areas in Greece")

Sentinel 2 map: Sentinel 2 false colour composite 11/8/4 with OSM background
