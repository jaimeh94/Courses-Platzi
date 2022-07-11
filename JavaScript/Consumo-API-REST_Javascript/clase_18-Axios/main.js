// El mismo proyecto de API Rest pero usando Axios

const API_KEY = 'a431a97d-2ce6-439b-87e3-f1e9a55f318a';

// Creando una instancia de axios para reutilizarla
const api = axios.create({
    baseURL: 'https://api.thecatapi.com/v1/',
    headers: { 'X-API-KEY': API_KEY },
});

const URL_RANDOM_RES = '/images/search?limit=2';
const URL_FAVORITES_RES = '/favourites';

const randomCats = document.querySelector('#random-cats');
const favoritesCats = document.querySelector('#favorites-cats');
const buttonReload = document.querySelector('#reload');
const errorNode = document.querySelector('#error');

// Función para adicionar imagen a una sección
function addImageNode({nodeSection, imageId, imageUrl, attId, buttonText}) {
    const article = document.createElement('article');
    const img = document.createElement('img');
    const button = document.createElement('button');
    img.className = 'random-img';
    img.setAttribute(attId, imageId);
    img.src = imageUrl;
    const btnText = document.createTextNode(buttonText);
    button.appendChild(btnText);
    article.appendChild(img);
    article.appendChild(button);
    nodeSection.appendChild(article);
}

// Cargando imágenes aleatorias
async function loadRandomCats() {
    try {
        const { data, status } = await api.get(URL_RANDOM_RES);
        if (status !== 200) throw new Error(`Error de petición HTTP en Random: ${status}`);
        data.forEach(el => {
            addImageNode({
                nodeSection: randomCats,
                imageId: el.id,
                imageUrl: el.url,
                attId: 'data-imageid',
                buttonText: 'Guardar Favorito',
            });
        });
    } catch (error) {
        errorNode.innerText = `Error: ${error.message}`;
    }
};

// Cargando imágenes de favoritos
async function loadFavoritesCats() {
    try {
        const { data, status } = await api.get(URL_FAVORITES_RES);
        if (status !== 200) throw new Error(`Error de petición HTTP en Favoritos: ${status}`);
        data.forEach(el => {
            addImageNode({
                nodeSection: favoritesCats,
                imageId: el.id, // no es id de la imagen sino id de favorito
                imageUrl: el.image.url,
                attId: 'data-id',
                buttonText: 'Eliminar Favorito',
            });
        });
    } catch (error) {
        errorNode.innerText = `Error: ${error.message}`;
    }
};

// Salvando imagenes a favoritos
async function saveFavoritesCat(id) {
    try {
        // Llamamos al objeto axios con método que necesitamos, en este caso POST
        // response = { data, status }
        const { data, status } = await api.post(URL_FAVORITES_RES, {
            // Pasamos los parámetros o querystring
            image_id: id,
        });
        if (status !== 200) throw new Error(`Error de petición POST HTTP en Favoritos: ${status}`);
        return data.id;
    } catch (error) {
        errorNode.innerText = `Error: ${error.message}`;
    }
};

// Eliminando imágenes de favoritos
async function deleteFavoritesCat(id) {
    try {
        const { status } = await api.delete(`${URL_FAVORITES_RES}/${id}`);
        if (status !== 200) throw new Error(`Error de petición DELETE HTTP en Favoritos: ${status}`);
    } catch (error) {
        errorNode.innerText = `Error: ${error.message}`;
    }
}

// Evento recargar imagenes random
buttonReload.addEventListener('click', () => {
    while (randomCats.lastChild.nodeName === 'ARTICLE') {
        randomCats.lastChild.remove();
    }
    loadRandomCats();
});

// Evento guardar imagen en favorito
randomCats.addEventListener('click', (e) => {
    const target = e.target;
    if (target && target.nodeName === 'BUTTON') {
        const img = target.previousSibling;
        const imageId = img.dataset.imageid;
        saveFavoritesCat(imageId).then((id) => {
            alert('Hemos guardado la imagen a favoritos!');
            addImageNode({
                nodeSection: favoritesCats,
                imageId: id, // no es id de la imagen sino id de favorito
                imageUrl: img.src,
                attId: 'data-id',
                buttonText: 'Eliminar Favorito',
            });
        });
    }
});

// Evento eliminar imágenes de favorito
favoritesCats.addEventListener('click', (e) => {
    const target = e.target;
    if (target && target.nodeName === 'BUTTON') {
        const img = target.previousSibling;
        const id = img.dataset.id;
        deleteFavoritesCat(id);
        alert('Hemos eliminado la imagen a favoritos!');
        const parent = target.parentNode;
        if (parent.nodeName === 'ARTICLE') parent.remove();
    }
});

loadRandomCats();

loadFavoritesCats();