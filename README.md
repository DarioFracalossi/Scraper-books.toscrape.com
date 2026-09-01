# SCRAPER PARA BOOKS.TOSCRAPE.COM

### Descripción breve

Este script está programado para leer el HTML de la pagina books.toscrape.com para extraer los siguiente datos: nombres de libros y precios de ellos. Este los exporta en un archivo CSV o Excel (a elección del usuario).

### Caracteristicas del programa

El programa toma la URL de BOOKS.TOSCRAPE.COM de manera automatica, extrayendo los datos de ella. Los transforma en un DataFrame, que luego puede ser exportado en un archivo CSV o Excel luego de mostrarlo en consola, donde el usuario quiera. El objetivo de este script es mostrar el manejo de datos extraidos de un HTML, mediante el scraping.

### Limitaciones del programa

Este scraper está programado especificamente para leer los datos de books.toscrape.com, con el objetivo de demostrar una habilidad y una forma de trabajar. No es aplicable a cualquier web ya que esto implicaria adaptar el codigo para leer los datos especificos de ese HTML.

### Requisitos de ejecución

Como requisito primordial, se necesita utilizar Python 3.10+.

### Como usarlo

Al ejecutar, el script tomara la URL de la pagina de manera fija, y hara los procedimientos necesarios de manera automatica. A traves de la consola, el usuario debe elegir si exportar los datos en un archivo CSV o Excel, e ingresar la ruta donde será exportado.

### Ejemplo de salida

```
                                                                                       Titulos Precios
                                                                          A Light in the Attic  £51.77
                                                                            Tipping the Velvet  £53.74
                                                                                    Soumission  £50.10
                                                                                 Sharp Objects  £47.82
                                                         Sapiens: A Brief History of Humankind  £54.23
                                                                               The Requiem Red  £22.65
                                            The Dirty Little Secrets of Getting Your Dream Job  £33.34
       The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull  £17.93
The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics  £22.60
                                                                               The Black Maria  £52.15
                                                Starving Hearts (Triangular Trade Trilogy, #1)  £13.99
                                                                         Shakespeare's Sonnets  £20.66
                                                                                   Set Me Free  £17.46
                                       Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)  £52.29
                                                                     Rip it Up and Start Again  £35.02
            Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991  £57.25
                                                                                          Olio  £23.88
                                         Mesaerion: The Best Science Fiction Stories 1800-1849  £37.59
                                                                  Libertarianism for Beginners  £51.33
                                                                       It's Only the Himalayas  £45.17
Ingrese la letra E si quiere exportar un archivo Excel o la letra C si quiere exportar un archivo CSV: E
Ingrese una ruta para guardar el archivo Excel: C:\Users\Dario\OneDrive\Escritorio\python\ElPlan\Scraper books.toscrape.com
¡Archivo exportado exitosamente!
