# Curso de Consumo de API REST con JavaScript

Resumen del curso: 

Consumir una API REST con JavaScript. 

Descubre el flujo de comunicación entre Frontend y Backend

 Primeras solicitudes asíncronas usando fetch. 

Comprende los fundamentos del consumo de APIs

Profesor: Juan DC

## Clase 1 - ****¿Qué es una API REST?****

JS - frontend: 

Responsabilidades; interactuar con los usuarios

Comunicarnos con el backend para que nos de las respuestas a la mayoría de preguntas que nos hacen los usuarios 

JS: puente entre los usuarios y el backend: vamos aprender hacer esa intercepción 

Qué es una API: Application Program Interfaz 

Las interfaces son el mecanismo en que un robot le permite a los usuarios comunicarse e interactuar con el robot como un app 

API REST: Es una interfaz pero no para comunicar user con robots, sino robots con otros robots, backend o con frontend o backend con otros backends 

REST: *Representational State Transfer*

En resumen si las API´s REST interfaces que comunican robots con robots por medio de HTTP, por medio de internet, ejemplo:

Cuando entras a una pagina  ves en la barra: https//:platzi.com

Con las API entramos a [https://api.platzi.com](https://api.platzi.com) donde este el API,  no nos van a responder con html directamente, sino con JSON, en ese formato vamos a recibir todos los datos, en ese formato el backend nos va dar la información para que en el frontend obtenenga esos datos y se los mostremos a los usuarios ahora si con html, imagenes botones, videos 

API REST: Interfaces que se comunican por medio de HTTP 

Aun hay algunas aplicaciones viejitas  que siguen usando SOAP para mandar información entre computadoras. Sin embargo, actualmente REST está dominando su aplicación.

## Clase 2 - ****Flujo de comunicación entre usuarios, frontend y backend****

Todas la paginas web tiene Frontend y Backend y los usuarios  interactuan con nuestra página web para conseguir la información que estén buscando, pero los usuarios no interactúan ni reciben directamente  esa información, si no que nosotros en el frontend recibimos las interacciones de los usuarios y eso lo traducimos a consultas al backend, para que el backend que si tiene esa información  nos la devuelva al frontend y este pueda dársela a los users 

**Server Side Rendering - SSR - flujo 1**

Las SSRs son páginas que necesitan traer diferentes archivos HTML del servidor cada vez que el usuario navega por nuestra aplicación, es decir, casi todas las veces que damos click en un link o botón. Aunque estas páginas tienen un tiempo de carga muy corto, la carga debe repetirse.

**Single Page Applications - SPA -flujo 2**

 Gracias a JS nosotros no solo vamos a tener 1 html estático, dar consulta al servidor y tener otro html, manipulación del DOM con JS, ya no va a traer varios html, este puede hacer solicitudes a una API.

 Gracias a JS también podemos escribir desde JS al html (manipulación del DOM: leer el html y actualizarlo), cuando el user interactue con **la página JS va a escuchar esos eventos**  y va a poder hacer lo que quiera con esos eventos, **manipular el DOM** o hacer una **solicitud a una API** 

Por medio de esta comunicación sucede por medio de una API REST y por medio de esta vamos a poder comunicar con el backend, **no regrese otro html** sino para que **retorne en formato JSON  una respuesta y recibirla desde JS**

En resumen:

usuario consulta al  frontend → backend(servidor) regresa → HTML → JS(manipulación del DOM) →  API REST → consulta al Backend → retorna información a la API → JS → HTML actualizado 

En el backend tenemos **las bases de datos** MySQL, Mongol DB , etc, nos ayudan a persistir información: si los users crearon un producto o comentario, **JS va mandar está información a la API al backend y esta API va a responder si todo salió bien** y **retorna es información**, pero, para guardar ese comentario y que otros user puedan ver ese comentario en el futuro se debe de **guardar ese comentario en una base de datos** 

Cuando los **user piden información** de un curso, **se convierte en JS**, **escuchamos esa consult**a de los users **por medio de la API REST** pedirle es **info al backend**, esta hace una **consulta a la base de datos** y se regresan todos **la información solicitada** 

![Untitled](images/Untitled.png)

## Clase 3 - Consume tu primera API REST

Google: https://github.com/public-apis/public-apis [https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)

lista APIs públicas que podemos usar sin pagar

![Untitled](images/Untitled%201.png)

Si va iniciando no uses CORS, 

HTTPS: seguro

Auth: método de autenticación, que requiere el API para poderla usar, las que tienen NO, nos dicen que no requieren método de autenticación o apikey, estas 2 si estas iniciando puedes escogerlos pero si vas iniciando NO escojas 0Auth es muy complejo 

La que se escogió fue:

![Untitled](images/Untitled%202.png)

CLICK en ABOUT

![Untitled](images/Untitled%203.png)

Click en Documentation: vemos que tendremos fotos de gatos aleatorias:

tutorial rápido

1- cargar la url 

2-tener una respuesta de tipo JSON 

3- Dentro tiene una propiedad .url que tiene la imagen aleatoria de los 🐱  

![Untitled](images/Untitled%204.png)

Abrimos nuestro editor de código

Creamos un index.html y un main.js

![Untitled](images/Untitled%205.png)

E*n tu navegador busca: json viewer e instala esta herramienta*

*[https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh](https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh)*

*ya puedes ver la estructura de la api: ahora pega el URL:  [https://api.thecatapi.com/v1/images/search](https://api.thecatapi.com/v1/images/search)*

*Ya puedes ver la estructura de la API*

![Untitled](images/Untitled%206.png)

La estructura que ves en la anterior imagen es lo que estamos recibiendo en **data**, donde sacaremos a continuación su elemento 0 y su atributo **url** (imagen aleatoria que nos esta dando nuestra API)

`Para respuesta.json` la estamos transformando en json 

![Untitled](images/Untitled%207.png)

Tenemos que ponerle la url a nuestra img en html, para eso haremos una manipulación del DOM 

![Untitled](images/Untitled%208.png)

ya podríamos ver las fotos random de los michis en tu html, abre el live server con  Alt + L + O

- *Reto crear un boton donde puedas dar click y se recarge la imagen (evento, llame a la funcion que llame a nuestro fetch )*
- *Usar async y await*

![Untitled](images/Untitled%209.png)

![Untitled](images/Untitled%2010.png)

## Clase 4 - ****Endpoints y query parameters****

Son una de las formas en que podemos modificar el resultado de nuestra API REST

**Endpoints: rutas**

Distintas rutas para solicitar distinto contenido,  solo necesitamos filtrar alguna información que necesitemos no toda la base de Datos

Po r ese motivo las API se organizan su información para evitar hacer solicitudes a toda la base de datos en cada solicitud, solo pedirlo por pequeños módulos

Por ejemplo:

 

![Untitled](images/Untitled%2011.png)

 Distintos endpoints para las categorías de 😺 

- razas
- Imágenes
- imágenes de un 🐱 en particular

Es necesario ver la documentación de la API para saber las rutas que tendrás disponibles para usar 

### **Query parameters:**

son **información extra a las rutas para poder limitar o especificar el contenido que queremos pedirle a nuestra API, al backend**

si ya en la ruta dijimos que queremos cargar las categorías, **especificamos con un query parameter que nos retorne** 

- las categorías que tengan  fun en el titulo
- breeds/razas: tráenos 5 tipos de razas, pero no de la página 1, sino que la página 2
- imágenes de categoría 3
- la imagen del michi 34 con formato png

![Untitled](images/Untitled%2012.png)

 Esto solo funciona si nuestra API está preparada para recibir estos query parameters 

Revisa la documentación 

Resolvamos el reto del botón 

HTML

![Untitled](images/Untitled%2013.png)

![Untitled](images/Untitled%2014.png)

V*amos a llamar a la función 2 veces para que al entrar no aparezca la página sin imagen*

E*stamos llamando a la función 2 veces una cuando cargamos nuestro código y otra cuando le damos click al botón*

Vamos a implamentar los ****Endpoints y query parameters en nuestra funcion****

- Primero tenemos que ver los ****Endpoints y query parameters,**** que tenemos disponibles
- Vamos a la documentación [https://docs.thecatapi.com/](https://docs.thecatapi.com/)

![Untitled](images/Untitled%2015.png)

![Untitled](images/Untitled%2016.png)

- vemos nuestro **Endpoint: /images/search** que nos da las imágenes random
- el endpoint tiene 2 query parameters que podemos usar: **limit y page**
- limit: cuantas imagenes quieres que te retorne: 1, 2 o 3, las que tu quieras
- page: el numero de página, nos ayuda a seleccionar la página que queremos cargar

Para este ejercicio solo necesitamos el limit, ya que queremos que nos retorne 3 imágenes random

sintaxis 

? | query parameter = numero de imagenes & otro query parameter = número de página

?limit=3&page=2

![Untitled](images/Untitled%2017.png)

en este caso solo queremos una query: **?limit=3**

![Untitled](images/Untitled%2018.png)

agregamos el console.log(data); para ver que sucede

![Untitled](images/Untitled%2019.png)

vemos que ya no tenemos el elemento [0], sino [{0}, {1}, {2}], tenemos 3 elementos porque, ese fue el limite de nuestro query parameter, ahora tenemos un array de 3 elementos que por dentro son un objeto y que por dentro tienen la propiedad url: imagen-random

![Untitled](images/Untitled%2020.png)

para poder presentar las 3 imágenes, triplicamos la etiqueta de img y le agregamos un id=”” distinto a cada imagen 

 

![Untitled](images/Untitled%2021.png)

Ahora debemos modificar el código en JS

![Untitled](images/Untitled%2022.png)

Nota: para múltiples cursores usa 

![Untitled](images/Untitled%2023.png)

## Clase 5 -****¿Qué son los HTTP Status Codes?****

son la forma que el protocolo HTTP nos da un spoiler del estado de nuestra solicitud, si todo va bien o todo se rompió, se puede presentar una falla en cualquier momento y hay que estar preparado para decirle a los usuarios el fallo ya sea nuestro o de la API

Aprender a reaccionar a los errores: para existen los HTTP Status Code

HTTP Status Code: 100 hasta +500

- La centena de los **200**: significa que frontend y backend están bien 🙂
    - 201: el API es más especifico del tipo de éxito
    - 202: todo va bien pero no se ha terminado de crear lo que mandaste a crear
    
- La centena de los **300:** redirecciones, la solicitud, la ruta en la que entramos no es la ruta final, sino que el backend hace una redirección hacia alguna otra ruta, es decir le haces una solicitud y te manda a otro sitio
    - **307**: la redirección es temporal, no sabemos si en el futuro seguira siendo la misma ruta a donde nos mande
    - **308:** siempre nos va a mandar a la misma ruta
- La centena de los **400:** nos equivocamos, el frontend hizo una solicitud incorrecta
    - **400** puro: error de sintaxis, typo, la ruta, etc
    - **401**: la ruta no funciona, sino que debemos darle algun metodo de autenticación  y no estamos autorizados para recibir esa información que viene en esa ruta.
    - **402**: necesitamos pagar poder entrar a esa ruta y recibir la información que requerimos
    - **404** not found: lo que estamos solicitando no fue encontrado ☹️
    
- La centena de los **500**: no sabemos si el frontend está bien o mal, pero el backend falló 😫
    - hubo tantas solicitudes que el backend son alcanzo a responderlas todas a tiempo y el frontend se cansó de esperar
    - Tal vez murió ☠, no hay nada que hacer bro, es un error del servidor, el servidor lo tiene que arreglar

Es importante saber de Fronted y backend 

**Frontend** debes saber **Backend** para que las solicitudes o cosas que hables con las personas de Backend no van a tener sentido, no van a tener una **buena comunicación**, mínimo entiende los **fundamentos de backend**, si sucede un error como el 500 vas a poder **ayudar y comunicárselo a los users**

**Backend** debes saber **frontend** para entender como se **interactúa con los usuarios**, como el frontend necesita que le **entregues la información para dárselo correctamente a los usuarios.**

Reto: que significa y de donde salió el código de estado HTTP 418: tetera

Recurso de la clase 👉[https://httpstatusdogs.com/](https://httpstatusdogs.com/)

## Clase 6 - ****¿Qué es una API KEY?****

Es una de las formas en que el backend puede identificar quien está haciendo cada solicitud 

Palabras clave: **Autenticación y Autorización**

**Autenticación:** identificar quien es cada quien, quien eres tu? 

**Autorización:** nos dice que permisos tiene cada quien, para que puedan realizar una acción.

Ejemplo: persona “y” quiere ver las fotos de persona “z”, la autorización va a decir “quien eres?”,

ok eres persona “y”, pásame un token y luego empieza a revisar los permisos “persona “y” trata de ver las fotos privadas  de persona “z”,  sin embargo no tiene permiso de ver esas fotos entonces se lo va a 🚷 

![Untitled](images/Untitled%2024.png)

Estos trabajan en conjunto para prohibir o permitir el acceso en toda la información que tenemos en nuestra aplicación y ahí entran nuestra API KEYS

**API KEYS:** son una de las formas en que el backend puede identificar quien es cada quien, quien hace cada solicitud para proteger la información privada de las personas y para limitar la cantidad o las solicitudes que hacemos a la aplicación:

Por ejemplo en nuestra API de 😺 tenemos un limite de 10,000 solicitudes al mes, si nos pasamos, nos prohíbe hacer la solicitud 10,001 para pagar los 10 dólares al mes y poder hacer 100,000.

Muchas rutas serán 🚷, no podrás acceder a ellos sino hasta que le enviemos una API KEY 🗝, que identifique quien es cada quien.

Para que nosotro le podamos enviar esta API 🗝 en cada solicitud que le hagamos al backend podemos usar varias formas: 

- Usar un Query parameter:
    - ?api_key=tu_api_🗝,  para cada solicitud
- Authorization Header: una forma más comoda de enviar tu API Key
    - X-API-Key: tu_api_key

Las API KEY no son la única forma de que el backend identifique quien es cada quien:

![Untitled](images/Untitled%2025.png)

0Auth 2.0: es de las mejores y más complejas de autenticar:

- este curso te ayudara con este método [https://platzi.com/cursos/autenticacion-oauth/](https://platzi.com/cursos/autenticacion-oauth/)

![Untitled](images/Untitled%2026.png)

Estamos usando un **Application-based authentication**: estamos autenticando nuestra aplicación , estamos autenticando a nuestro frontend  para hacer solicitudes al backend 

Pero hay aplicaciones que necesitan combinar  **Application-based authentication y User-based authentication.**

 Por ejemplo: el backend necesita saber quien es el dueño de la aplicación que esta haciendo las solicitudes, a veces también necesita dar información privada a usuarios y nosotros en el frontend, manejamos distintos usuarios y tenemos que mostrarles distinta información a cada usuario, no es suficiente con un API KEY también se necesita una User-based authentication, a esto se le llama **trabajar con autenticación.** 

- si quieres profundizar INVESTIGA sobre las User-based authentication, en el curso solo veremos Application-based authentication

Vamos a sacar nuestra  API KEY para autenticar a nuestro fronted y nos cuente la limitación de las 10,000 solicitudes al mes 

click: [https://docs.thecatapi.com/authentication](https://docs.thecatapi.com/authentication)

![Untitled](images/Untitled%2027.png)

If you don’t have an API Key, just head over to [https://thecatapi.com](https://thecatapi.com/)
 and get one for free

![Untitled](images/Untitled%2028.png)

![Untitled](images/Untitled%2029.png)

![Untitled](images/Untitled%2030.png)

Ya tienes tu API KEY, ahora agrégala al link

![Untitled](images/Untitled%2031.png)

lo agregas con un &api_key=tu-api

Ahora nuestro backend sabe que nosotros con nuestra API KEY,  el dueñ@ de la API ya hizo una solicitud y la va a empezar a contar. Ya podremos hacer solicitudes a cualquier ruta de nuestra API

## Clase 7 - ****Maquetación del proyecto****

Vamos a preparar todo nuestro HTML para que en las próximas clases podamos concentrarnos los métodos HTTP para guardar favoritos, cargar gatitos, borrarlos y subir nuestras propias fotos de gatitos, subirlas a nuestra API 

- Vamos a necesitar una sección para guardar nuestra fotos favoritas, que se puedan agregar y eliminar
- Otra sección para subir nuestras propias fotos

Maqueta en tu HTML campeón@ >_

## Clase 8 - ****¿Qué son los Métodos HTTP?****

Los métodos HTTP son la forma en que el frontend le puede dar un spoiler al backend del tipo de solicitud que vamos hacer

5 métodos más importantes:

![Untitled](images/Untitled%2032.png)

 

- **GET:** por defecto siempre hemos utilizado, **FETCH lo pone automáticamente** al hacer una solicitud, este tipo de método son las **normal**es, **para consumir información, para leer**, no estamos modificando, creando, borrando.
- **POST**:  Nos sirve para darle nacimiento a nuevas cosas, **para crear nueva información,** crear nuevos usuarios, crear nuevos gatitos, crear algo especifico para cada 😺
- **PUT y PATCH**: Ambos son para **editar la información que hemos creado**, NO para crear nueva sino para editar la que ya hallamos creado.
    - PUT: vamos a **editar** toda la información, **todo** **el elemento**
    - PATCH: solo vamos a **modificar una parte pequeña del elemento**, un atributo NO todo.
- DELETE: **borrar información,** si nosotros y los usuarios nos piden borrar información de la aplicación el frontend tiene que traducir eso a una solicitud de tipo delete para avisar al backend

documentación 👉[https://developer.mozilla.org/es/docs/Web/HTTP/Methods](https://developer.mozilla.org/es/docs/Web/HTTP/Methods)

[https://www.notion.so](https://www.notion.so)

## **Clase 9 - GET: leyendo michis favoritos**

Vamos a crear la sección de favoritos

- Definir específicamente el nombre de las funciones
- 

![Untitled](images/Untitled%2033.png)

- le creamos su función a la sección de favoritos

![Untitled](images/Untitled%2034.png)

- Tenemos un problema: solo tenemos un API URL y esa nos lleva a la ruta donde cargamos imágenes aleatorias y eso nos nos sirve para nuestra nueva función
- Requerimos una API KEY

![Untitled](images/Untitled%2035.png)

![Untitled](images/Untitled%2036.png)

Veamos más información de referencia para cargar información de los michis marcados como favoritos

![Untitled](images/Untitled%2037.png)

Tenemos rutas para: cargar todos los 🐱 favoritos, cargar 1 🐱 en especifico, otro para borrar y uno para subir una imagen a nuestros favoritos 

Dividamos un problema grande en trozos pequeños: empecemos con cargar todos los favoritos

![Untitled](images/Untitled%2038.png)

![Untitled](images/Untitled%2039.png)

![Untitled](images/Untitled%2040.png)

![Untitled](images/Untitled%2041.png)

Vamos a tener 2 constantes distintas y especificamos nombres, pero en API_URL_FAVORITES vamos a cambiar la ruta de /images/search  a  →  /favourites

IMAGEN DE LA CONST API_URL_RANDOM y API_URL_FAVORITES

Sin embargo la función de favoritos tiene que cambiar, en el HTML de igual forma debemos de agregar nuevos articles, nuevas imágenes por cada elemento que venga en el array de información que nos va a retornar la API

Pero antes probemos algunas cosas interesantes

![Untitled](images/Untitled%2042.png)

- Si borramos nuestra API, vemos que pasara, recuerda que en la documentación nos indica que la necesitamos (API KEY Required):

![Untitled](images/Untitled%2043.png)

![Untitled](images/Untitled%2044.png)

Error en hacer una solicitud de tipo GET a esta ruta  y nos dice que el error es 401

Recuerda error 400: nosotros cometimos un error desde el Fronted 

El backend especificando nos dice que nos hace falta autenticación, no podemos entrar a la ruta si no tenemos una API 🗝 

Pero si nos topamos con un error 500 debemos de avisarle a los usuarios y avisar que lo intenten más tarde

Cada vez que llame a fetch me diga que el status code fallo, o sea cualquier cosa que no sea 200, vamos a mostrar el error para que los usuarios sepan que está pasando y para eso creamos una condicional  

Antes de mostrar el código checa esto en la consola

![Untitled](images/Untitled%2045.png)

![Untitled](images/Untitled%2046.png)

para crear el error borra la api 

![Untitled](images/Untitled%2043.png)

![Untitled](images/Untitled%2047.png)

![Untitled](images/Untitled%2048.png)

Esto lo podemos aprovechar de agregar el mensaje

con `data. message`

hubo un error 401 AUTHENTICATION_ERROR - you need to send your API Key as the 'x-api-key' header

Este mensaje los usuarios no lo van a entender, asi que puedes hacer un objeto con los distintos status code de posibles errores que puedas tener para hacer una comparación con cada uno de erros y mostrando el error que obtuviste 

## Clase 10 - ****POST: guardando michis favoritos****

Vamos a ver como marcar un 😺 como favorito 

Vamos a ver como se utiliza el metodo POST y GET 

- Primero tenemos que hacer es crear una nueva función asíncrona para guardar a nuestros 😺en favoritos
- *necesitamos la URL de la ruta del API donde tenemos que enviar está información, nos dirigimos a la documentación para guardar a un 😺 en favoritos*

![Untitled](images/Untitled%2049.png)

![Untitled](images/Untitled%2050.png)

Nos ayuda a especificar una imagen con su ID  debe aparecer en favoritos 

Debemos enviarle nuestra API KEY 

![Untitled](images/Untitled%2051.png)

Tenemos que enviarle un body 

![Untitled](images/Untitled%2052.png)

Nos retornará una respuesta y un 🆔 

![Untitled](images/Untitled%2053.png)

Vemos que debemos entrar a está ruta con la diferencia de que la solicitud es de tipo POST

![Untitled](images/Untitled%2054.png)

 Creamos nuestra función, lo llamamos con el HTML y lo llamamos para ver si funciona

![Untitled](images/Untitled%2055.png)

![Untitled](images/Untitled%2056.png)

Abrimos la consola damos click en favoritos y vemos un error de **tipo 400** 

![Untitled](images/Untitled%2057.png)

La solicitud de tipo POST tienen un fallo y tiene un error 

Lo que pasa es que cuando hacemos una solicitud de tipo **POST**, cuando no le decimos a **FETCH** que haga todo por defecto, **métodos headers y body** , cuando **no se lo especificamos tenemos que definirlos manualmente.**

**headers:** información que le diga **cual es el lenguaje** o tipo de contenido o tipo **de respuesta que estamos esperando,** como queremos comunicarnos con el backend 

`´Content-Type’: ‘application/json’`   estamos trabajando en json, mandamelo en json

**body**: tenemos que decirle a la API cual es el 😺, imagen que queremos guardar en favoritos, este body ya no solo son los headers de la solicitud, la meta-información, es como en el HTML es la **información que ya vamos a enviar al backend**, guárdame está imagen en favoritos, por ejemplo  `img_id: 12`

Está vez tenemos que **enviarlo** como un **string**, como este body lo va leer tal cual nuestro backend, no estamos seguros de que el lenguaje en el que está escrito nuestra API, también sea JS y entienda está sintaxis de objetos en JS podría estar escrito en otro lenguaje (para entender mejor lo que dice checa el ****Curso de JavaScript Engine (V8) y el Navegador**** [https://platzi.com/cursos/javascript-navegador/](https://platzi.com/cursos/javascript-navegador/)).

Para estar seguros de que estamos entendiendo entre todos los lenguajes, tenemos que enviar un texto que tenga dentro la información a modo de objeto de JS con la información del 😺 que queremos guardar en favoritos 

`body:JSON.stringify({`

`image_id: 12`

`}),`

![Untitled](images/Untitled%2058.png)

Recapitulando: cuando llamamos a `fetch` y queremos especificarle un metodo diferente al por defecto que es GET, en este caso un POST tenemos que especificarlo con un segundo argumento   de nuestra función, en este caso puede ser un objeto que tenga toda la información que tengamos que enviarle a nuestra API 

`fetch(API_URL_FAVORITES, {
method: 'POST',
header:{
'Content-Type': 'application/json',
},
body: JSON.stringify({
image_id:12
}),`

Por defecto siempre será header y body, si no tiene los 2 o uno de los 2 te retorna un error de tipo 400

Una vez ya lo tengas checa la consola, da click a favoritos y ve que pasa guap@

![Untitled](images/Untitled%2059.png)

Pórque pasa? 🤔

 Pero antes hagamos el mecanismo que ya habíamos hecho, para mostrar el error a los users 👥 y se lo agregamos a la funcion de favoritos

`const data = await res.json();`

`if(res.status !==200){
spanError.innerHTML = "Hubo un error " + res.status + " " +  data.message + ' si quieres saber más, da click aquí 👉 <a href="[https://httpstatusdogs.com/](https://httpstatusdogs.com/)">errors</a>';
}`

vamos a la página y click en el botón de favoritos

![Untitled](images/Untitled%2060.png)

si te das cuenta hay un **image_id" is required**

Pues es sintaxis no es ~~**header**~~ es `headers` con “s”

![Untitled](images/Untitled%2061.png)

vuelve a recargar y dar click en favoritos ( lo se bro, es repetitivo, pero son bugs 🤘🏾)

![Untitled](images/Untitled%2062.png)

Ahora hay otro mensaje: **el id debe ser un string NO un número**

para agregarselo primero ve a consola de 😺 random y checa que en cada objeto tiene una propiedad id 

![Untitled](images/Untitled%2063.png)

**`id: “au”` en mi caso fue este** 

copy and paste in your function

`body: JSON.stringify({
image_id:'au'
}),`

Bum! ya no hay error, al menos para mi, si a ti te salió un error puede ser la sintaxis y si no es eso, puedes reclamarme por Twitter te lo dejo al final de este documento`>_`

Pero sigamos en lo que estábamos haciendo, F5, click en favoritos y checamos la consola ya te la sabes 😉 

Vemos que ya no hay error ya tenemos status 200

![Untitled](images/Untitled%2064.png)

Nuestro 😺 se guardo en favoritos

Ahora como vemos que esta en favoritos 

El dilema está en que siempre guardamos el mismo 🆔 

**`id: “au”`**

si quieres experimentar como ya se estan guardando en favoritos el mismo id varias veces, refresca la página y vuelve a dar click en favoritos y checa la consola, veras como se va agregando el mismo 

![Untitled](images/Untitled%2065.png)

Y como podemos ver, el id es el mismo 😮, pero ya podemos guardar a los 😺 como favoritos

lo que sigue es agregar los 🐱 a la sección de favoritos. Por el momento YA sabes como enviar una solicitud de tipo POST, 

## Clase 11 - ****Consultas a la API para escribir HTML dinámico****

- Ya sabes que es una API
- API REST
- Y a consumimos nuestra 1° API REST
- Sabes sobre el método HTTP GET, es el que usa fetch por defecto
- Sabes como usar el POST
- Header y body

Vamos a manipular el DOM pero dependiendo de la información que nos de nuestra API, es decir no siempre vamos a cargar la misma información en nuestro HTML sino que dependiendo de lo que nos retorne la API, eso es lo que cargaremos en el DOM 

Vamos a cargar la fotos que hemos marcado como favoritos, diferentes fotos.

Expliquemos cada línea de código

- Tenemos nuestras API URLS

![Untitled](images/Untitled%2066.png)

Tenemos nuestro ♨ getElementById de nuestro error, por si aparece un error

`const spanError = document.getElementById('error');`

Tenemos nuestra función

`async function loadRandomMichis() {`

cargamos con fetch que automáticamente ya tiene **GET** ya tiene todo preparado y nos permite hacer la solicitud sin problemas 

`const res = await fetch(API_URL_RANDOM);`

Eso tenemos que pasearlo a json  que tambien es asincrona, nos devuelve una promesa por eso usamos el await

`const data = await res.json();` 

hacemos el span error, que es insertar en el HTML el error que nos este retornando, nuestro llamado al API en caso de que res.status no sea 200 

`if(res.status !==200){
spanError.innerHTML = "Hubo un error " + res.status;
}`

si todo carga bien vamos a buscar con un getElementById nuestras 2 imagenes de 🐱 random y le insertamos el src con la url de la imagen que nos haya cargado la API 

`else{`

`const img1 = document.getElementById('img1');`

`const img2 = document.getElementById('img2');`

`img1.src = data[0].url;`

`img2.src = data[1].url;`

`}`

`}`

Ahora con nuestra otra función, hacemos lo mismo pero con una url diferente, la API_URL_FAVORITES

`async function loadFavouriteMichis() {`

`const res = await fetch(API_URL_FAVORITES);`

`const data = await res.json();`

*`console*.log('FAVORITES', data);`

De igual forma si hay un error que muestre el error, pero si no hay error aún no estamos mostrando nada

`if(res.status !==200) {
spanError.innerHTML = "Hubo un error " + res.status + " " +  data.message + ' si quieres saber más, da click aquí 👉 <a href="[https://httpstatusdogs.com/](https://httpstatusdogs.com/)">errors</a>';
}`

También tenemos otra función de savefavoriteMichis que hace lo mismo que las anteriores solo que no hace un Fetch de tipo GET sino que de tipo POST 

`async function saveFavouriteMichis(){
const res = await fetch(API_URL_FAVORITES, {`

`method: 'POST',`

 en los headers le enviamos un tipo json, que es el lenguaje que vamos hablar entre frontend y backend 

`'Content-Type': 'application/json',`

Además en el body, estoy enviando un JSON.stringify, no es un json tal cual sino que un string que por dentro tiene un json que el backend se encargara de [parsiar](https://developer.mozilla.org/en-US/docs/Glossary/Parse), así como nosotros hicimos nuestro res.json, ahí lo que le estamos enviando es lo que necesita el API, el image_id de la imagen que querramos guardar en favoritos 

`body: *JSON*.stringify({`

`image_id: 'au'`

`}),`

luego volvemos a convertir a res en res.json lo imprimimos y vemos si el estatus es 200, si hay un error lo mostramos si no aún no estamos haciendo nada

`const data = await res.json();`

*`console*.log('Save');`

*`console*.log(res);`

`if(res.status !==200) {`

`spanError.innerHTML = "Hubo un error " + res.status + " " +  data.message + ' si quieres saber más, da click aquí 👉 <a href="[https://httpstatusdogs.com/](https://httpstatusdogs.com/)">errors</a>';`

`}`

Empecemos por la función loadFavoriteMichis( )

 Checa la consola 

![Untitled](images/Untitled%2067.png)

cuando cargamos nuestros 🐱 favoritos recibimos un array y dentro de ese array recibimos distintos objetos y cada uno de estos objetos nos trae el image_id y nos trae otro objeto por dentro que se llama image: que por dentro trae el mismo id y la **url,** y está url es la que necesitamos 

entonces lo que vamos hacer si no hubo errores, es recorrer ese array que es data, asi que podemos recorrer cada uno de sus elementos par hacerl algo con el objeto que tengamos ahi, sacarle esa url para ponercela a nuestras imagenes que están en el HTML en la section de 🐱 favorito 

Lo que vamos hacer es un `data.forEach()` para recorrer, y por cada elemento que estamos recorriendo vamos a sacar a la información de un 🐱 

Cada 🐱 es un objeto y cada uno tiene la propiedad de la url 

![Untitled](images/Untitled%2068.png)

`else{`

`data.forEach( michi => {`

`michi.image.url`

`})` 

`}`

está es la imagen que tenemos que darle a nuestros article>img en el HTML 

Tenemos que agregar un articule que por dentro tenga una imagen y un boton, y eso insertarselo a nuestro contenedor del favorite 🐱 

![Untitled](images/Untitled%2069.png)

Por lo mientras comentamos el  //`michi.image.url` ya que lo vamos a necesitar más adelante para el src de la imagen

`const section = *document*.getElementById('favoriteMichis')`

`const article = *document*.createElement('article');`

`const img = *document*.createElement('img');`

`const btn = *document*.createElement('button');`

Pero si checas nuestro botón tiene texto “Sacar de favoritos” para eso hacemos lo siguiente:

`const btnText = *document*.createTextNode('Sacar de favoritos');`

Así se llama la función que nos ayuda a crear textos para nuestros nodos de HTML

Ahora vamos a unirlos y devolverlos:

- vamos a llamar a button y le vamos a meter el texto

`btn.appendChild(btnText);`

- A nuestra imagen tenemos que agregarle el src, la url de la imagen

`img.src = michi.image.url`

Ya tenemos nuestro boton e imagen listos, ahora debemos meterlo dentro del article

`article.appendChild(img);
article.appendChild(btn);`

Ahora llamamos al section 

`section.appendChild(article);`

Veamos la página, y ya aparece nuestras fotos agregadas a favoritos

![Untitled](images/Untitled%2070.png)

controlemos su tamaño con la siguiente linea de código

`img.width = 150;`

como vemos en la imagen solo nos guarda 1 foto del mismo 😺 porque estamos guardando el mismo id del mismo 😺 

- Primero cambiamos el nombre de la función, porque no guarda varias fotos, solo 1

`saveFavouriteMichis()`   —→ `saveFavouriteMichi()`

además debemos recibir un id, el cual nos va a servir para no escribir a mano el id del 😺 que queremos guardar en favoritos, sino que enviamos ahí lo que nos envien como argumento en está función 

`saveFavouriteMichi(id)` ←—-

`body: *JSON*.stringify({`

`image_id: id`  ←——-

`}),`

Si recargas la página ya no funciona tu botón de guardar en favoritos porque   cambiamos el nombre de la función y debemos enviarle un argumento, en el HTML está así

`<button *id*="btn1" *onclick*="saveFavouriteMichis()">`

pero en este caso como hacemos para que este botón ahora sepa cual es el id de cada 😺 random que aparezca en el HTML, necesitamos a JS

`<button *id*="btn1" >` 

`<button *id*="btn2" >` 

borramos el onclick y debemos hacerlo con JS  

Lo que vamos hacer es que cuando carguemos a los 🐱 random, no solo llamemos a las imagenes, tambien llamar a los botones y para eso nos va a servir tener el `id = “btn1”` 

Carguemos los botones en JS 

esto en la función de `loadRandomMichis( )`

 

`const btn1 = *document*.getElementById('btn1');`

`const btn2 = *document*.getElementById('btn2');`

Ahora cada uno de los botones debe tener su atributo onclick distinto 

`btn1.onclick = saveFavouriteMichi();`

Pero tenemos que enviarle al id como parámetro, como lo hacemos? Recarguemos la página y chequemos la consola

![Untitled](images/Untitled%2071.png)

estamos sacando la url y la propiedad id, eso es lo que tenemos que enviar en el argumento de esta función 

`btn1.onclick = saveFavouriteMichi(data[0].id);
btn2.onclick = saveFavouriteMichi(data[1].id);`

Vas a tu página das click en guardar en favoritos y veras esto

![Untitled](images/Untitled%2072.png)

 no te me desesperes, vuelve a refrescar la página

![Untitled](images/Untitled%2073.png)

Ya cargaron nuestros 😺 🐱 , pero nos aparecen 2 x 1, tenemos un bug 🐛 porque el onclick llama a las 2 imagenes aleatorias que estamos cargando 

El problema es que al cargar la página se agregan otros 2 🐱 random sin siquiera agregarlos a favoritos , el error esta aquí

`btn1.onclick = saveFavouriteMichi(data[0].id);
btn2.onclick = saveFavouriteMichi(data[1].id);`

al llamar al onclick estamos llamando directamente a la función de  `saveFavouriteMichi(data[0].id);` y se está ejecutando antes de darle click por el hecho de definirla la estamos llamando, lo que tenemos que hacer es llamar esta función dentro de otra función.

`btn1.onclick = () => saveFavouriteMichi(data[0].id);`

`btn2.onclick = () => saveFavouriteMichi(data[1].id);`

con una arrow function, al hacer esto ahora la función que estamos declarando es la arrow function y hasta que le demos click es cuando se va a ejecutar la función.

Uff hay otro bug, cual es? Pues te lo muestro a continuación

 

![Untitled](images/Untitled%2074.png)

Es el que nuestra comunidad en la sección de aportes nos advierte ⚠ 

el `limit=22&` lo debemos eliminar de nuestra url

debe quedar así

![Untitled](images/Untitled%2075.png)

Checa la del profesor 

![Untitled](images/Untitled%2076.png)

`const API_URL_FAVOTITES = '[https://api.thecatapi.com/v1/favourites?api_key=c08d415f-dea7-4a38-bb28-7b2188202e46](https://api.thecatapi.com/v1/favourites?api_key=c08d415f-dea7-4a38-bb28-7b2188202e46)';`

el la borro, este nos limita a solo tener 22 imágenes

Y ya te debería de funcionar, si no te funciona tendrías un typo y si tampoco recuerda reclamarme en Twitter 

Bien ahora todo  marcha perfecto  👌 

![Untitled](images/Untitled%2077.png)

## Clase 12 - ****DELETE: borrando michis favoritos****

- Ya sabes como guardar las fotos en favoritos 🔣 y como agregarlas en una sección en nuestra página y que los botones funciones
- Ahora vamos a aprender como eliminarlos de la sección de favoritos, no solo eliminar el nodo en el HTML sino que de verdad hagamos un llamado al API con el método delete para eliminar los 🙀  de favoritos
- PUT, PATCH y DELETE

Vamos a la documentación  —> [https://docs.thecatapi.com/](https://docs.thecatapi.com/)

![Untitled](images/Untitled%2078.png)

![Untitled](images/Untitled%2079.png)

La url, es distinto:

**DELETE `/favourites/{favourite_id}`**

tenemos que decirle cual es el id del gatito guardado en favoritos que queremos eliminar, así que debemos crear otra variable que nos guarde un arrow function que reciba un id y concatenar el id: 

que no se te olvide seleccionar el link y hacer la combinación de comillas invertidas con Alt + 96, para hacerlo correctamente

![Untitled](images/Untitled%2080.png)

Ya quedo el string, pero en realidad es una función 

Tenemos que crear otra función asíncrona 

Necesitamos un parametro de id para saber que 🐱 queremos delete

`async function deleteFavouriteMichi(id){`

llamamos a `API_URL_FAVOTITES_DELETE(id)` y le metemos el id que recibimos en nuestra función 

`const res = await fetch(API_URL_FAVOTITES_DELETE(id), {` 

`method: 'DELETE',`  ← cambiamos de método 

Regresemos a ver nuestra documentación y vemos que necesitamos autorización 

![Untitled](images/Untitled%2081.png)

tenemos que enviar  nuestra API_KEY pero ya lo estamos haciendo 

![Untitled](images/Untitled%2082.png)

Ya no tenemos que hacer nada más solo nos está diciendo que tenemos que mandar nuestro favorite_id  pero no es un query parameter como tal viene en la url **`/favourites/{favourite_id}`**

No hace falta un query parameter

Nota 📝  👁 ————————————————————————————————————————

**Normalmente en otras API l**o que habría pasado es que la URL HABRIA SIDO LA MISMA  que la del POST 

solo habría cambiado el método a DELET y enviar un body con la sintaxis de JSON con el id de la imagen que quisiéramos eliminar

![Untitled](images/Untitled%2083.png)

![Untitled](images/Untitled%2084.png)

---

---

---

---

---

Pero en este caso las personas del backend que hicieron esta API, lo estructuraron de forma que NO lo envies en un body , sino directamente en la url entonces el header y body no hacen falta, como no vamos a enviar ningun body, no tenemos que decirle al backend en que lenguaje estamos hablando, es suficiente con el método DELETE

![Untitled](images/Untitled%2085.png)

Sin embargo aun falta llamar a la función con el botón que saque al 🐱 de favoritos con un evento onclick  

`btn.onclick = () => deleteFavouriteMichi();`

Aún le falta que le agreguemos un id, pero de donde lo sacamos, pues veamos la consola

![Untitled](images/Untitled%2086.png)

vemos que tenemos 2 id, ¿Cuál ponemos? Intentemos con img_id

`btn.onclick = () => deleteFavouriteMichi(michi.image_id);`

Vamos a la página y le damos click a sacar de favoritos

![Untitled](images/Untitled%2087.png)

Nos arroja un error 400 con deleteFavouriteMichi( ) y btn.onclick

![Untitled](images/Untitled%2088.png)

Además de que vemos el mensaje de error 

Claro estamos enviando información incorrecta, solo vamos a enviar el id solito  

`btn.onclick = () => deleteFavouriteMichi(michi.id);`

Checamos la página, recargamos y click en el boton de sacar de favoritos

![Untitled](images/Untitled%2089.png)

Vemos que ya nos carga nuestro else, ahora para que desaparezca la imagen debes de recargar la página y 🤯, ya está 

![Untitled](images/Untitled%2090.png)

 

![Untitled](images/Untitled%2091.png)

Ya me canse de estar recargando para que suceda, así que lo arreglaremos

llamamos la función `loadFavouriteMichis();` dentro de nuestro else 

`else{`

*`console*.log('Cat save in favourites')`

`loadFavouriteMichis();`

`}`

recarguemos la pagina click en agregar en favoritos

y nos damos cuenta de algo 🤯 💣 💥  y es que se nos duplican las fotos que guardamos.

original

![Untitled](images/Untitled%2092.png)

duplicado

![Untitled](images/Untitled%2093.png)

Lo que sucede en realidad es que no limpiamos nuestro HTML, al verlo en consola que todos nuestros articles vuelven aparecer al llamar a la función

![Untitled](images/Untitled%2094.png)

Lo que tenemos que hacer es en la función loadFavoriteMichis() 

antes de hacer el data.forEach(), debemos limpiar nuestra sección

Esto borrara hasta al titulo, pero podemos recrearlo desde JS

 

![Untitled](images/Untitled%2095.png)

Recargamos la página 

![Untitled](images/Untitled%2096.png)

Vemos que ya no hay nada, pero click en guardar en favoritos 

Ufff, tenemos un error 🙁 

![Untitled](images/Untitled%2097.png)

section is not defined  y cierto section lo definimos por fuera

![Untitled](images/Untitled%2098.png)

Así que lo subimos 

![Untitled](images/Untitled%2099.png)

![Untitled](images/Untitled%20100.png)

Volvemos a recargar la pagina y checar la consola, click en guardar en favoritos

![Untitled](images/Untitled%20101.png)

ya se agrego a favoritos sin tener que refrescar la página

![Untitled](images/Untitled%20102.png)

Ya no se duplican las fotos 

Vamos hacer lo mismo cuando borramos una foto, llamando la función 

`else{`

*`console*.log('Cat delete of favourites')`

`loadFavouriteMichis();`

`}`

![Untitled](images/Untitled%20103.png)

Ahora volvemos a la página  a borrar  una foto, ya vemos que se elimina inmediatamente sin recargar la página 

Ya está, ya eliminamos fotos de la sección de favoritos, y podemos hacer que se recargue la sección de favoritos cada vez que guardamos o eliminamos una foto 

## Clase 13 - ****¿Qué son los Headers HTTP?****

En clases anteriores hicimos distintas solicitudes HTTP y muchas veces no solo necesitamos la ruta, la url, sino que podemos agregarle query parameters, incluso headers y body, cuando hicimos la solicitud de tipo POST  

Qué son los **headers**: como podemos usarlos para modificar la información, la mejor forma de entenderlo es **compraralo con HTML,** en HTML tenemos un head y un body 

- El **head:** tiene la metainformación, la metadata
- El **body:** ya tenemos el contenido tal cual que van a ver los usuarios

Pero recuerda que en el HTML  si pones “ñ”, tildes o caracteres raros en tu body no los va a leer a menos que pongas una meta-etiqueta UTF-8, eso es porque aunque el body sea el mismo el head puede cambiar la forma en que se logra leer e interpretar  el body, es comunicación con los navegadores para que los usuarios puedan ver todo de la mejor forma posible  

Lo mismo pasa cuando consumimos API, por ejemplo podríamos decir que en el body es donde nosotros enviamos la información, ya no la que van a leer los usuarios, sino la que vamos a comunicar al backend.

 Muchas veces cuando hacemos solicitudes de tipo GET, no tenemos que mandarle ninguna información, con que el backend sepa que hicimos una solicitud a está ruta en particular ya es más que suficiente 

Pero hay otras, por ejemplo si queremos crear un producto, guardar un 🐱 en favoritos, cuando queremos crear o modificar algo, tenemos que enviarle esa información al backend, no es suficiente  con hacer una solicitud. Entonces para eso nos sirve el body para enviarle esa información al backend y pueda recibirla y hacer lo que tenga que hacer 

Headers: nos ayudan es a que el backend sepa como le estamos enviando esa información de nuestro body, en los headers tenemos que decir cual es el tipo de contenido que estamos enviando en el body, cual es el formato, como está ese tipo de meta información para que el backend pueda recibirla para que sepa como leerla  y sepa como retornarla a nosotros y la podamos leer y recibir y trabajar con ella. 

Ejemplo: imagina que tenemos una carta, el **body** sería la carta y los **headers** seria la información a la oficina postal por ejemplo de como enviarle esa carta a la persona que lo vaya a recibir, al oficina postal, el aviso de fragil, por ejemplo, el fragil serian los headers y el contenido ya sería el vaso de vidrio 

Hay varios tipos de headers

![Untitled](images/Untitled%20104.png)

Documentación: [https://apipheny.io/api-headers/](https://apipheny.io/api-headers/)

Documentación: [https://apipheny.io/api-headers/](https://apipheny.io/api-headers/)

Documentación: [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

Nosotros ya usamos el header de Content Type por que era obligatorio  para poder hacer una solicitud de tipo POST

Proximamente usaremos otro header, el de Authorization para poder enviar API KEYS a modo de query parameter sin usar un header de Authorization para que sea más facil hacer este tipo de solicitudes 

## Clase 14 - ****Header de autorización****

![Untitled](images/Untitled%20105.png)

Un API KEY  podemos usarla para query parameters y authorization header: No hay ninguna diferencia, va a seguir siendo el mismo resultado, lo unico que cambia es que el código se verá más limpio, ya no nos va a tocar enviar ese token en nuestra API KEY al final de cada url, sino en cada solicitud vamos a poder entrar al objeto, al segundo argumento que le enviamos a fetch para decirle en authorization header es tal y el token la API KEY es tal

Solo es estético

Borramos nuestras API KEY 

 

![Untitled](images/Untitled%20106.png)

Vemos que en loadFavoriteMichis() tenemos una solicitud de tipo GET, pero aún así podemos enviarle headers, un Authorization header

vemos como lo pondremos, vamos a la documentación 

[https://docs.thecatapi.com/api-reference/favourites/favourites-post](https://docs.thecatapi.com/api-reference/favourites/favourites-post)

![Untitled](images/Untitled%20107.png)

x-api-key

![Untitled](images/Untitled%20108.png)

si vamos a la sección de autenticación nos dice que si podemos usar un query parameter 

![Untitled](images/Untitled%20109.png)

Pasamos de esto 👆 a esto 👇

![Untitled](images/Untitled%20110.png)

checa tu página, y parece que se logro

Pero no podemos guardar michi en favoritos porque la misma url de antes a la que le quitamos el query parameter nos hace falta otro header 

![Untitled](images/Untitled%20111.png)

Recargamos la página,a hora si puedes guardar fotos en favoritos, por si las dudas tambien hacemos lo mismo en la funcion de eliminar michis 

![Untitled](images/Untitled%20112.png)

![Untitled](images/Untitled%20113.png)

Vemos que todo salió bien 

Una aclaración antes de finalizar 😃

Es un error común pensar que es más seguro enviar un header que enviar un query parameter para cosas privadas como el API KEY por ejemplo, y la verdad es que SI es un poco más seguro, no vamos a estar haciendo solicitudes y no vamos a estar en el historial de nuestroo navegador el API KEY porque la vamos a tener en realidad es en un header, pero siendo realistas, los headers si pueden ser visibles, no es más seguro  seguro realmente, para un hacker, así que sigue siendo igual de inseguro, por eso existen muchos metodos de autenticación y autorización.

Pero hay cursos completos sobre eso, te dejo el link del curso

[https://platzi.com/cursos/autenticacion-oauth/](https://platzi.com/cursos/autenticacion-oauth/)

 [**Curso de Autenticación con OAuth**](https://platzi.com/cursos/autenticacion-oauth/)

Hay API KEY publicas que tienen y no tienen autenticación o su método de autenticación es una API-KEY 

## Clase 15 - ****Header de Content-Type****

El content type es para que el frontend y el backend se pongan de acuerdo y sepamos en que idioma en el que nos vamos a comunicar, tanto para que el frontend envié información al backend en el body, o tambien para el tipo de información que el backend nos va a responder a nosotros, si el backend no lo soporta nos va a retornar un error, para eso debemos ver la documentación o preguntarle al equipo de backend, cual es el tipo de content type que usamos, pero nosotros estamos usando el `application/json`  pero hay muchos más

![Untitled](images/Untitled%20114.png)

![Untitled](images/Untitled%20115.png)

el **form-urlencoded** es para trabajar con formularios de HTML, la forma en que traducimos esto a una url y esa url como la traducimos a una solicitud HTTP,  lo más seguro te lo vayas a tomar y lo uses 

Pero imaginate que nosotros no necesitemos enviar la url de un archivo de audio, un mp3 por ejemplo, muchas veces puede ser que no tengamos la url del archivo, sino que tengamos que subir el archivo para generar esa url y usarla donde sea que lo necesitemos, podemos enviar texto en nuestras peticiones, archivos  de audio, img, videos, excel, power point, word 

![Untitled](images/Untitled%20116.png)

![Untitled](images/Untitled%20117.png)

![Untitled](images/Untitled%20118.png)

![Untitled](images/Untitled%20119.png)

Hay otros tipos de content types como: multipart, es para cosas raras 

![Untitled](images/Untitled%20120.png)

el de form-data lo vamos a usar, cuando nosotros trabajamos con formularios, esos formularios con manipulación y lectura del DOM,  agarrar input por input, tomar el value de todos ellos, meterlo en un objeto y este objeto enviarlo por un body strinfygiado en nuestra función fetch para enviar toda esa información de formularios a nuestra API, pero con un **form-data** para hacerlo mucho más fácil para que todo esto se agrupe automaticamente y puedamos enviar la solicitud sin tanto trabajo 

Hay otro tipo de content Type

![Untitled](images/Untitled%20121.png)

hay uno de texto plano 

¿Cuál es la diferencia entre `tex/txml` y `application/xml` ?

 Lo que vamos hacer es ver como fallamos try to use el content type de texto plano text /play porque nuestra API solo soporta application json 

![Untitled](images/Untitled%20122.png)

Vamos a cambiar el content-type 

![Untitled](images/Untitled%20123.png)

Vamos a guardarlos en favoritos y veremos que hay un error 

![Untitled](images/Untitled%20124.png)

no nos va a entender el backend 

Ahora regresémoslo a como estaba 

![Untitled](images/Untitled%20125.png)

Veamos otra cosa que podríamos profundizar más 

![Untitled](images/Untitled%20126.png)

si esto es JSON porque hay que stringify esto, vemos que pasa si lo borramos 

![Untitled](images/Untitled%20127.png)

lo que sucede al tratar de guardar una foto en favoritos, pasara un error 400

![Untitled](images/Untitled%20128.png)

![Untitled](images/Untitled%20129.png)

Lo que nos dice es que no entiende el body, no se estan entendiendo entre frontend y backend, asi que tenemos que pasar todo lo que nos envien a json, asi sea en formato json 

![Untitled](images/Untitled%20130.png)

No lo estan enviando en formato json pero aun no está parceado en json, JavaScript aún no lo entiende, por eso debemos traducirlo a json para que los datos se puedan entender como objetos de JS, lo mismo pasa con los lenguajes de programación de backend, si le enviamos un objeto de JS, incluso si es JS, pero imaginate un backend con PHP, phyton, go, pues está sintaxis de objetos, así se a “””JSON”””, en realidad es un objeto de JS, pues no lo van a entender,

![Untitled](images/Untitled%20127.png)

Para que todos hablemos el mismo idioma debemos hacer esto 

![Untitled](images/Untitled%20131.png)

Ahora el backend ya la va a poder parcear y entender 

Documentación de todos los content-types que existen [https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types)

## Clase 16 -  ****FormData: publicando imágenes de michis****

Investiga la diferencia entre contente type y mime type 

FormData: usar una instancia del prototipo formData de JS que vienen en nuestros navegadores y como podemos usarlo para agarrar por defecto todos los valores de nuestros inputs que hayan llenado los usuarios en un HTML y además y como podemos agregar información por nuestra cuenta con los métodos SET y GET del formdata 

- Hagamos un formulario en HTML que se conecte a JS  para que los usuarios puedan subir fotos

![Untitled](images/Untitled%20132.png)

Nota <button>: existen diferentes tipos de botones, reset, submit, para que nuestro formulario no se envié automáticamente sino podamos controlar ese envió desde JS

Nota <button>: función onclick porque necesitamos darle al boton y con ayuda de FormData vamos a recibir toda la información todos los valores de nuestros inputs en nuestro formulario

Nota <form>: action="" es una url donde podemos enviar la información de nuestro formulario por medio de enviar todos los valores en la url como query parameters

Nota <input>: name nos ayuda para que formdata pueda saber cual es ese archivo o ese valor que esta guardando, lo guarda en forma de objeto valor, necesitamos un nombre para ese valor de ese file

- Vamos a crear la función que vamos a necesitar en JS

![Untitled](images/Untitled%20133.png)

![Untitled](images/Untitled%20134.png)

![Untitled](images/Untitled%20135.png)

 form.getAll

![Untitled](images/Untitled%20136.png)

![Untitled](images/Untitled%20137.png)

Regresemos a nuestro código

![Untitled](images/Untitled%20132.png)

![Untitled](images/Untitled%20138.png)

Nota : al constructor de esta instancia vamos a enviarle como argumento a form, así que tomará todos los valores que nosotros hayamos agarrado en nuestros inputs                `<input id="file" type="file" name="file">` y los va agregar a formData, nuestra instancia, y ya los vamos a tener listos para usar

Nota 2: recuerda que ya le dimos nombre a nuestros inputs `name='file'` y ese será el nombre de la llave donde va a estar guardado nuestro archivo

Ahora vamos a nuestra página y demos click en Subir foto

y aparece esto: 

![Untitled](images/Untitled%20139.png)

Ahora subiremos una foto

![Untitled](images/Untitled%20140.png)

Al darle click a elegir foto y subir foto en consola vuelve a salir lo mismo, pero con información de la foto

![Untitled](images/Untitled%20141.png)

Ahora vamos a subir la foto a nuestra API, pero veamos la documentación: [https://docs.thecatapi.com/api-reference/favourites/favourites-post](https://docs.thecatapi.com/api-reference/favourites/favourites-post)

![Untitled](images/Untitled%20142.png)

![Untitled](images/Untitled%20143.png)

Vemos en la documentación que podemos subir cualquier jpg o png y la regla es que tenga la foto de un 😼, si no es un gato hay sanciones 😮

debemos entrar a **/images/upload** 

Ahora nos vamos a /images

![Untitled](images/Untitled%20144.png)

Vamos a subir una foto que quede en una url y poderla usar para mostrar la imagen a nuestros usuarios, tenemos que enviarle algo que se llame file (`name='file'`) tenemos que enviarle a nuestro body un file un objeto que diga file y debe ser un archiv, imagen 

![Untitled](images/Untitled%20145.png)

Vamos a copiar la ruta `/image/upload`

![Untitled](images/Untitled%20146.png)

Vamos a crear una nueva API URL, vamos al código

![Untitled](images/Untitled%20147.png)

![Untitled](images/Untitled%20148.png)

 Está vez no estamos solicitando una información normal, sino un FormData, NO tenemos que usar `body{JSON.stringify}`, solo tenemos que guardar nuestro formData

 `const formData = new FormData(form);` decirle que todo lo que venga de nuestro formulario y tenemos algo con nombre file `console.log(formData.get('file'))` que es lo que requiere nuestra documentación.

Vamos a recargar la página, dar click a elegir foto y subir foto

vemos la consola y tenemos un error

![Untitled](images/Untitled%20149.png)

Error 500: error del servidor  https://github.com/github/fetch/issues/505

![Untitled](images/Untitled%20150.png)

![Untitled](images/Untitled%20151.png)

reporte de error 

![Untitled](images/Untitled%20152.png)

![Untitled](images/Untitled%20153.png)

Cuando manualmente asignamos el header de Content-Type   

![Untitled](images/Untitled%20154.png)

Pero nuestro backend necesita más información en nuestro Content-Type 

`Content-Type: multipart/form-data**;boundary=----WebKitFormBoundaryyrV7KO0BoCBuDbTL**`

fijate que eso de boundary es lo que nos muestra el error

![Untitled](images/Untitled%20155.png)

Entonces como le hacemos, fetch es tan inteligente que si le enviamos un formData

![Untitled](images/Untitled%20156.png)

Una instancia del prototipo formData, automaticamente va a poner el content type  y no solo va a decir que es de `Content-Type: multipart/form-data`, sino que va agregar el `boundary` que le hace falta 

entonces comentamos lo siguiente 

![Untitled](images/Untitled%20157.png)

Código completo

![Untitled](images/Untitled%20158.png)

Dirígete a la página y ya puedes subir fotos que aparezcan en favoritos

reto: agregar una miniatura de la foto antes de que los usuarios le den al boton de subir, puedan confirmar la foto que subieron 

boundary: es un separador algo así como esto & pero para los content types 

recursos

[https://github.com/platzi/consumo-api-rest-javascript/blob/master/main.js](https://github.com/platzi/consumo-api-rest-javascript/blob/master/main.js)

[https://developer.mozilla.org/es/docs/Web/API/FormData](https://developer.mozilla.org/es/docs/Web/API/FormData)

[https://muffinman.io/blog/uploading-files-using-fetch-multipart-form-data/](https://muffinman.io/blog/uploading-files-using-fetch-multipart-form-data/)

## Clase 17 - ****Axios: librerías de JavaScript para consumir APIs****

En el curso hemos estado usando fetch para hacer nuestras peticiones http y consumir nuestra API REST 

Antes usábamos XML HHTP REQUEST 

En la era de JQuery usábamos AJAX 

Existen más herramientas 

![Untitled](images/Untitled%20159.png)

  que la mayoria usan fetch por dentro y nos ayudan a usar fetch en el entorno donde no se soporta fetch e incluso nos dan ayudas para que nuestro developer expirence haciendo solicitudes http sea más cómoda que usando fetch la más popular es AXIOS 

 Te vas a topar con fetch y AXIOS muy frecuentemente 

- Axios: nos ahorra tantas cosas, da una forma minimalista de usarla
- Trae.js:  traer, forma minimalista de hacer solicitudes http, muy parecido a fetch pero tiene algunas ayuditas que funciona bastante bien
- node-fetch o request: que nos ayudan a usar fetch, con la misma sintaxis de fetch pero en node.js, porque  node.js no soporta fetch. Pero Node.js ya anuncio que va a soportar fetch de forma nativa, así que todas estás herramientas pasan a ser innecesarias

Vamos a ver como funciona Axios y para que lo vamos a estar utilizando en los proximos cursos 

![Untitled](images/Untitled%20160.png)

[https://axios-http.com/](https://axios-http.com/)

![Untitled](images/Untitled%20161.png)

 cliente HTTP basado en promesas tanto para el navegador como para node.js 

Get Started: documentación 

![Untitled](images/Untitled%20162.png)

Te da diferentes opciones de instalación o de llamado 

![Untitled](images/Untitled%20163.png)

![Untitled](images/Untitled%20164.png)

![Untitled](images/Untitled%20165.png)

La API de Axios es espectacular, tenemos que llamar tal cual a axios, funcion llamada axios y decirle cuales son los elementos de la solicitud que vamos a hacer la configuración, el tipo de solicitud que vamos hacer  

![Untitled](images/Untitled%20166.png)

No tenemos 2 argumentos separados, la url esta dentro, en vez de enviar un body tenemos data, ya no parceamos nada 

![Untitled](images/Untitled%20167.png)

tambien funciona como promesa y podemos usarlo con async y await 

![Untitled](images/Untitled%20168.png)

además podemos crear instancias de axios, podemos llamar a axios.create para guardar información en una variable, darle una base, darle alguna configuración que vamos a compartir entre todas nuestra solicitudes, 

![Untitled](images/Untitled%20169.png)

por ejemplo el authorization header para que esa API puedamos darle despues el resto de configuración que necesitemos con todos estos metodos

![Untitled](images/Untitled%20170.png)

podemos después llamar a API decirle cuál es la URL, cual es método, pero ya no vamos a tener que ir uno por uno, especificando cual es authorization header, ya todos lo van a tener automáticamente

Vamos a ver una probadita de axios 

![Untitled](images/Untitled%20171.png)

Vamos a llamarlo con un `<script>`

![Untitled](images/Untitled%20172.png)

`<script**src**="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>`

lo pegamos en el html antes del archivo main.js

![Untitled](images/Untitled%20173.png)

![Untitled](images/Untitled%20174.png)

axios es una función pero tambien permite crear distintos métodos para crear instancias 

La mejor funcionalidad de axios es crear instancias deaxios con la configuración base que vamos a usar en todas nuestras solicitudes 

vamos a la documentación [https://axios-http.com/docs/config_defaults](https://axios-http.com/docs/config_defaults)

![Untitled](images/Untitled%20175.png)

![Untitled](images/Untitled%20176.png)

cuando creamos una instancia, podemos decirle varias cosas por ejemplo:  baseURL: '[https://api.example.com](https://api.example.com/)' que cuando llamemos a axios no tengamos que decirle siempre cual es el inicio de nuestra url, solo eso lo asuma y lo que nosotros usemos cada vez que llamemos a está instancia a API, solo tengamos que decirle la ultima parte de la url 

![Untitled](images/Untitled%20177.png)

Tambien podemos modificar la instancia, las cosas que va a tener por defecto como por ejemplo un header, para que no tengamos que repetir nuestro API KEY, nuestros token cada vez que llamemos a está instancia de axios, sino que podamos agregar una vez y tenerla para siempre en nuestra API 

![Untitled](images/Untitled%20178.png)

Lo agregamos a nuestro código

![Untitled](images/Untitled%20179.png)

Ya tenemos en teoría nuestra instancia lista y funcionando para que podamos usarla en cualquier otra función, la aplicaremos en nuestra función saveFavouriteMichis(id)

![Untitled](images/Untitled%20180.png)

Solo mira la ruta que tenemos que hacer para tener la información 

En el caso de axios hacemos lo siguiente

![Untitled](images/Untitled%20181.png)

ya podemos enviarle el objeto de configuración y las especificaciones de la consulta que queremos hacer, vamos a la documentación: [https://axios-http.com/docs/post_example](https://axios-http.com/docs/post_example)

![Untitled](images/Untitled%20182.png)

![Untitled](images/Untitled%20183.png)

podemos llamar a [axios.post](http://axio.post) o la innstancia que hemos creado y le podemos decir a donde queremos hacer la solicitud 

nosotros  ya tenemos una baseURL

![Untitled](images/Untitled%20184.png)

Solo tenemos que especificar lo que sigue, nosotros antes estabamos llamando a nuestra `API_URL_FAVOTITES` pero en este caso solo debemos de copiar lo que nos falta

![Untitled](images/Untitled%20185.png)

![Untitled](images/Untitled%20186.png)

Ahora ya lo va a concatenar con la url, ya podemos enviar el resto de nuestra configuración, axios por nosotros ya pone todo en content type, application JSON 

Ya le dijimos a axios que siempre ponga nuiesta API KEY 

![Untitled](images/Untitled%20187.png)

Ya no hace falta enviar un header, y en el segundo objeto de configuración le debemos enviar lo que enviábamos a body  

![Untitled](images/Untitled%20188.png)

fijate que no estamos haciendo todo el proceso que haciamos con JSON.stringyfy, axios ya lo hace por nosotros, ya no tenemos que llamar a res.json()

![Untitled](images/Untitled%20189.png)

este objeto res automaticamente  ya trae a data por dentro 

![Untitled](images/Untitled%20190.png)

Ese objeto res como podemos llamar a nuestras solicitudes ya no debemos de parcearlo y ese parceo que sea =  nuestros datos, data, ahora res ya trae automaticamente y a estatus , asi que ya no hace falta que en la condicional pongamos res.status, solo status 

![Untitled](images/Untitled%20191.png)

![Untitled](images/Untitled%20192.png)

Ahora recarga tu página y guarda al michi en favoritos, y ya debería funcionar,

ya viste todo lo que te ahorra axios

![Untitled](images/Untitled%20193.png)

recursos: [https://github.com/platzi/consumo-api-rest-javascript/tree/93e7314bec42af1df8f27c88a7bfae28a41c3b26](https://github.com/platzi/consumo-api-rest-javascript/tree/93e7314bec42af1df8f27c88a7bfae28a41c3b26)

## Clase 18 - ****CORS, caché, redirect y tu propio clon de fetch****

![Untitled](images/Untitled%20194.png)

Las propiedades que hemos usado en el objeto de configuración de fetch cada vez que hacemos solicitudes http para nuestra API, hemos usado: el metodo, los headers, el body, y esas son las más importantes, las cuales vamos a usar, pero veremos otras 3 que son populares, que te pueden ahorrar muchos dolores de cabeza

La primera es **mode**

![Untitled](images/Untitled%20195.png)

- cors: si has consumido API REST en el pasado sabrás que es un dolor de cabeza, el backend, el servidor, el API, muchas veces quieren limitar con quien intercambia o no cierta información, y dependiendo, de quien sea, que este pidiendo la información, quien sea el frontend o la herramienta intentando enviar la solicitud va a bloquearla o permitirla
- same-origin:  significa que solo va a permitir que su propio frontend en su mismo servidor, en la misma url, solo el mismo origen va a poder hacer solicitudes a la API, es decir el backend solo comparte información consigo mismo y el frontend y el mismo backend este sirviendo, esto en una API pública no funciona tan bien, el backend puede limitar por medio de **cors**  con quien comparte y no información

Pero la parte buena es que tenemos la opción de mode, porque nosotros tambien podemos limitar información, pero si el backend no quiere  darnos información, no va a darnos información , no hay nada que hacer, pero nosotros podemos ser estrictos y decirle a fetch con quien y no queremos compartir información, tambien podemos decirle que  **same-origin,** solamente funciona tu fetch si estoy haciendo solicitudes a mi mismo, mi origen, si me voy a otro backend, url o servidor, porvafor bloqueate y no permitas la solicitud 

- no-cors: por defecto la opcion es no-corse, que permite hacer peticiones y solicitudes a donde yo quiera

Pero es importante que esto existe por si te sale algún error 

![Untitled](images/Untitled%20196.png)

Caché: capacidad que tenemos de recordar la información que ya hemos traído en una solicitud anterior, nosotros podemos guardar los datos que nos hayan traído nuestra API, 

- Podemos guardarlo en el navegador, en nuestra aplicación, en donde sea, para que en el futuro, si necesitamos hacer otra solicitud, no tengamos que hacerla porque ya tenemos los datos ahí guardados,
- Si nos quedamos sin internet podemos usar la información que está en caché para que la aplicación siga funcionando pero explicándole al usuario que no podemos guardar nueva información porque no hay interne solo tenemos lo que esta en cache y ya.
- El backend también tiene su cache para que nos de las respuestas de las solicitudes más rápido, cuidado con esto porque si no lo cuidamos bien vamos a mostrar información a los usuarios que no corresponde a la verdad.
- Pero nosotros desde el frontend podemos especificar si nunca queremos cache, siempre queremos una nueva solicitud  o si siempre queremos cache y si hay algo en cache poderlo agarrar
- Pero tambien hay otras posibilidades como forzar cache, es decir que no revise si hay cache y si hay cache retornarlo pero si no hay, traerlo de la API, es decir, forzar lo que haya en cache, si no hay nada, crashear la información o solo poder hacer la solicitud
- **La recomendación final es que no las uses,** resulta que el condicional, todas las validaciones de si hay información en cache pero cuanto tiempo lleva esa información en cache, realmente nos sirva, ufff, es difícil hasta escribirlo, no lo haré, eso te lo dejo a ti   platzi-compa

**Todo eso ya viene por defecto y fetch ya lo hace, entonces NO es necesario usarlos** 🙂

Esto es una respuesta de entrevistas de trabajo  ; ) 

![Untitled](images/Untitled%20197.png)

Nosotros también podemos decir que hacer cuando nos encontremos con un status code de 300, 307, 308 …. 

- Follow: podemos decirle a fetch donde te manden tu ve, yo te pongo el atajo y tu corre bro.
- Error: podemos decirle, tu eres un fetch de casa de frontend, si te mandan a algún lugar desconocido NO vayas te pueden hacer daño, te bloqueas y devuelves a la casa y evitamos que extraños te den información que no queremos que tu tengas
- Manual: hay casos específicos cuando trabajamos con service workers donde manualmente revisamos cada uno de los redirects para ver si nos sirve o no

Solo hay un caso de uso realmente práctico que es de los service workers, aun así habrá documentación que te compartiré al final 

![Untitled](images/Untitled%20198.png)

![Untitled](images/Untitled%20199.png)

Hay muchas cosas dentro de fetch, como tal no es un prototipo con todo el código con la logica para hacer solicitudes HTTP sino que por dentro fetch usa distintos otros prototipos como el de:

![Untitled](images/Untitled%20200.png)

para trabajar y lo único que ha es consumir estos prototipos, entonces estos prototipos son los que realmente tienen el código de fetch 

El reto es:

1 Analices el código: sección de recursos, lo analices lo máximo que puedas, profundiza y veas como está escrito el código de fetch 

2- Construye tu propio fetch, hay librerias de JS, como Axios, y trae, que nos ayudan a consumir solicitudes HTTP, pero es más comodo, antes pasaba con fetch, era con XMLHTTPRequest y era muy complicado usarlo, gracias a fetch  ahora solo tenemos una función, un objeto con configuración y promesas 

Tu tarea es tratar de mejora a fetch, hazlo a tu propia forma, viendo como funciona request, headers, response y reescribiendo y agreagarle alguna característica como por ejemplo las instancias de axios a tu custom fetch 

Recursos

request.cache

[https://developer.mozilla.org/en-US/docs/Web/API/Request/cache](https://developer.mozilla.org/en-US/docs/Web/API/Request/cache)

fetch()

[https://developer.mozilla.org/en-US/docs/Web/API/fetch](https://developer.mozilla.org/en-US/docs/Web/API/fetch)

request

[https://developer.mozilla.org/en-US/docs/Web/API/Request](https://developer.mozilla.org/en-US/docs/Web/API/Request)

HTTP caching

[https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching#freshness](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching#freshness)

Headers

[https://developer.mozilla.org/en-US/docs/Web/API/Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers)

HTTP caching actaulización

[https://developer.mozilla.org/es/docs/Web/HTTP/Caching#actualización](https://developer.mozilla.org/es/docs/Web/HTTP/Caching#actualizaci%C3%B3n)

Response

[https://developer.mozilla.org/en-US/docs/Web/API/Response](https://developer.mozilla.org/en-US/docs/Web/API/Response)

## Clase 19 - ****GraphQL, Web Sockets y Web 3.0: el mundo más allá de REST****

El mundo más allá de REST 

Rest no es el único protocolo de transferencia de datos por HTTP que podemos usar para crear aplicaciones webn hay más herramientas que nos pueden ayudar:

![Untitled](images/Untitled%20201.png)

Este es como un remplazo a fetch, es una relativamente nueva herramienta que podemos usar en distintos navegadores para hacer una consulta HTTP, pero más que una consulta, lo interesante de está herramienta es que no espera una respuesta, no espera que el servidor le diga fallaste o todo  ok👌 o redirect, el solo manda la solicitud y ya, es muy favorable como para google analytics, como para ver cuantas personas entraron a nuestro sitio 

Como es algo poco crucial para la experiencia de nuestros usuarios, es muy buena idea que no tenga que esperar una respuesta, lo cual realentiza la experiencia de usuario, solo enviamos y que el servidor haga lo que tenga que hacer, si no llego tu tranquil@ se perdio se metrica, pero funciona bien en la mayoria de los casos 

![Untitled](images/Untitled%20202.png)

GraphQL: si es un remplazo a REST, y es una herramienta para que no tengamos distintos **endpoints/ rutas** en nuestra API, tener una ruta para los 😺, otro para las categorías, otro para las razas, etc.

 Sino que tengamos todo en la misma ruta y no sea el backend quien decida como va a clasificar, estructura y ordenar la información en sus propios endpoints, sino que somos nosotros quienes decidimos como queremos la respuesta, como queremos que el backend nos de la respuesta eso le llamamos **empowered clients,** los clientes, el frontend es el que tienen el poder de que va a recibir.

Es muy comun que el backend nos da información que NO necesitamos, debido que diseñaron la API para que nos den toda la información de los 🐱, pero si nosotros no necesitamos las categorías o razas pues igual lo tenemos y ocupa espacio y ralentiza el tiempo que tarda la API en responder 

Si nosotros desde el frontend desde los clientes, podemos elegir cuales son los datos que realmente vamos a usar y esos son los que nos devuelve el backend, tenemos el poder 

![Untitled](images/Untitled%20203.png)

Este  es un ejemplo, tenemos query  and mutation 

![Untitled](images/Untitled%20204.png)

![Untitled](images/Untitled%20205.png)

Las querys: son para leer información, obtener información y como solo tenemos un solo endpoint tenemos que definir con lenguaje de graphQL  GQL, tenemos que definir los esquimas, la información, la estructura de datos que queremos recibir

Ejemplo: quiero recibir un 😺 con id: 325 y no quiero que me des toda la información de ese 😺, solo el 🆔  y la url 

Las mutation: por ejemplo queremos crear un 😺, pero que no lo fabrique y ya, sino que nos devuelva una respuesta, so nolo successful, sino que nos devuelva el id del nuevo 🐱, la imagen y de la imagen la url, en el fronten es muy sencillo de implementar, mientras tengas los conocimientos básicos, el problema es el backend, es muy difícil, lo bueno es que hay herramientas como APOLO SERVER que lo agilizan mucho    

![Untitled](images/Untitled%20206.png)

Un llamado a una API es como una llamada telefónica, cada vez que necesitas algún dato de tu compañero del otro lado de la línea, haces la peticion de la información o dar información pero como los teléfonos  cuelgas y vuelves a marcar, esperar a que te respondan, un ciclo repetitivo

Las Web Sockets es como cuando llamamos dejaramos la llamada abierta, nunca colgar, los mismo el backend, se espera y cada vez que necesitas algo ho hay que hacer todo el proceso de llamado 

![Untitled](images/Untitled%20207.png)

Desde el frontend y backend, con una herramienta llamada socket io, podemos hacer la conexión por medio de web sockets y por medio de eventos, cada vez que por medio de la llamada alguien diga “evento de mensaje”, cuando escuchemos ese mensaje vamos a devolver o reaccionar de distintas formas como el frontend o backend lo requiera 

![Untitled](images/Untitled%20208.png)

Web 1.0: páginas estaticas 

Web 2.0: Google, facebook, Twitter, Instagram; JavaScript moderno que nos permite interacción  

Web 3.0: leer, e interactuar, ser dueñ@s de nuestro contenido, es decir si alguien más lo quiere, se puede vender 

![Untitled](images/Untitled%20209.png)

Cliente -  HTML, CSS, JS

Logica - Lógica de negocios: backend, otorga permisos,  aqui se guardan  imagenes, comentarios, es a donde se conectan los clientes para guardar información y los clientes solo la consuman 

Persistencia: donde se guarda realmente la información , imagenes, bases de datos, archivos o lo que necesitemos 

![Untitled](images/Untitled%20210.png)

![Untitled](images/Untitled%20211.png)

Cliente podemos seguir usan JS, Angular, React, Vue,

 Comunicación con la lógica de negocios usamos WJS, ethers.js, estas son algunas herramientas que usamos ya no tal cual para interacción con los users, sino para conectarnos desde el frontend hacia la lógica de negocios 

Para hacer esa comunicación ya no usamos API REST con json ahora JSON-RPC o en vez de DNS ahora usamos ENS 

Lógica: Solidity, tambien se conectan a lugares de persistencia 

Persistencia: estás herramientas nos ayudan a que realmente seamos dueños de la información que estamos creando, además esto se conecta con el Blockchain 

Diferencia de: web 2.0 vs web 3.0 

DNS - Domain Name System

ENS - Ethereum Naming Service

Similitud: Dominio 

Recursos: 

 graphQL: [https://platzi.com/blog/introduccion-a-graphql/](https://platzi.com/blog/introduccion-a-graphql/)

 REST o GraphQL: [https://platzi.com/blog/rest-o-graphql/](https://platzi.com/blog/rest-o-graphql/)

WebSockets: [https://platzi.com/blog/websockets-en-nodejs/](https://platzi.com/blog/websockets-en-nodejs/)

GraphQL [https://platzi.com/blog/el-rey-ha-muerto-larga-vida-a-graphql/](https://platzi.com/blog/el-rey-ha-muerto-larga-vida-a-graphql/)