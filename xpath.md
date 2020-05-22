## XPATH TO SCRAPE IN PROJECT RAMAJUDICIAL

Es necesario quitar espacios en todos los campos strip()

### DATOS DEL PROCESO

###### TITULOS GENERALES

(Fecha de Radicación, Despacho, Ponente, Tipo de Proceso, Clase de Proceso, Subclase de Proceso, Recurso, Ubicación del Expediente, Contenido de Radicación)

`//div[@class="panel-title titulo-h4"]//text()`


###### VALORES GENERALES

(Fecha de Radicación, Despacho, Ponente, Tipo de Proceso, Clase de Proceso, Subclase de Proceso, Recurso, Ubicación del Expediente, Contenido de Radicación)

`//div[@class="panel-body"]//text()`

###### TITULOS ONE BY ONE

(Fecha de Radicacion)

`//div[@id="FechaProceso_Label"]//text()`

(Despacho)

`//div[@id="Despacho_Label"]//text()`

(Ponente)

`//div[@id="Ponente_Label"]//text()`

(Tipo de proceso)

`//div[@id="TipoProceso_Label"]//text()`

(Clase de proceso)

`//div[@id="ClaseProceso_Label"]//text()`

(Subclase de proceso)

`//div[@id="SubclaseProceso_Label"]//text()`

(Recurso)

`//div[@id="Recurso_Label"]//text()`

(Ubicacion del expediente)

`//div[@id="Ubicacion_Label"]//text()`

(Contenido de radicacion)

`//div[@id="ContenidoRadicacion_Label"]//text()`

###### VALORES ONE BY ONE

(Valor: fecha de radicacion)

`//div[@id="FechaProceso"]//text()`

(Valor: Despacho)

`//div[@id="Despacho"]//text()`

(Valor: Ponente)

`//div[@id="Ponente"]//text()`

(Valor: Tipo de proceso)

`//div[@id="TipoProceso"]//text()`

(Valor: Clase de proceso)

`//div[@id="ClaseProceso"]//text()`

(Valor: subclase de proceso)

`//div[@id="SubclaseProceso"]//text()`

(Valor: Recurso)

//div[@id="Recurso"]//text()

(Valor: Ubicacion)

`//div[@id="Ubicacion"]//text()`

(Valor: Contenido de radicacion)

`//div[@id="ContenidoRadicacion"]//text()`

### SUJETOS PROCESALES

(Tipo de Sujeto procesal)

`//div[@class="container table-responsive"][1]//table[@class="table table-hover list-styler"][1]//tbody[1]//td[@class=""][1]//text()`

(Nombre o razon social)

`//div[@class="container table-responsive"][1]//table[@class="table table-hover list-styler"][1]//tbody[1]//td[@class=""][3]//text()`

### Actuaciones del Proceso

(Todas las Fechas de actuaciones)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//tbody[1]//td[@class=""][1]//text()`

(Todos los tipos de actuacion)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//tbody[1]//td[@class=""][2]//text()`

(Todas las Anotaciones !ojo no cuenta las anotaciones vacias!)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//tbody[1]//td[@class=""][3]//text()`

(Anotaciones por columna tr)

(Titulos de actuaciones)

(Coje todos los titulos)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//thead[1]//tr[1]//th`

(Coje titulo por titulo moviendose por posicion)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//thead[1]//tr[1]//th`

(Coje titulo por posicion th[1] es fecha de actuacion, 2 actuacion, 3 anotacion, 4 fecha inicia, 5 fecha finaliza, 6 fecha de registro)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//thead[1]//tr[1]//th[1]`

(Coje todos)
`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//thead[1]//tr[1]`

(Coje 12 elementos)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//tbody[1]//tr[1]//text()`

(Coje 1 elemento cada casilla, cambiando el ultimo elemento del tr, #1 siempre va a ser la ultima)

`//div[@class="container table-responsive"][2]//table[@class="table table-hover list-styler"][1]//tbody[1]//tr[1]`
